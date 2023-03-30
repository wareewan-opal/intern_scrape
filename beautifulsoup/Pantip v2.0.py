# Databricks notebook source
# !pip install lxml
# !pip install fake-useragent
# !pip install beautifulsoup4
# !pip install aiohttp

# COMMAND ----------
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
from concurrent.futures import wait

# create a thread pool with a large number of worker threads
from time import time
import requests
from pyspark.sql import functions as F
from pyspark.sql import Row
import numpy as np
from pyspark.sql.types import StructType,StructField, StringType,ArrayType
from concurrent.futures import as_completed
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import urllib
import concurrent.futures
import os
import sys

# COMMAND ----------
# ประกาศตัวแปร
all_urls = list()
# list() เก็บข้อมูลในรูปแบบ
global Alldata
global dataArr
# global คือ การประกาศตัวแปรนอก function
dataArr = list()
Alldata = list()

def genrate_url():
    # อ่านคำสั่ง sql
    new_url = spark.sql("""select distinct(url) as url 
    from DELTA.`/mnt/cdpadls2southeast/bronze/insurance/BZ_cxense_traffic` 
    where url like "%pantip.com%"
    and externalUserIds_id is not null""")
    new_url = new_url.withColumn('url',F.split(F.col('url'), '/').getItem(4)).dropDuplicates()
    master_url = spark.sql(""" select topic_id from digide_common.master_pantip_daily """)
    dataframe = new_url.join(master_url,new_url.url == master_url.topic_id,"leftanti")
    # leftanti = ส่งคืนเฉพาะคอลัมน์จาก DataFrame ด้านซ้ายสำหรับบันทึกที่ไม่ตรงกัน
    all_urls.append(dataframe.rdd.flatMap(lambda x: x).collect())
    # append คือการเขียนใหม่

# COMMAND ----------
base_url = ['https://pantip.com/topic/40972866',
'https://pantip.com/topic/36668965',
'https://m.pantip.com/topic/38416486',
'https://m.pantip.com/topic/41587496',
'https://m.pantip.com/topic/32165940',
'https://pantip.com/topic/41319714']


    
def executeRestApi(code):

    try:
      url = f"https://pantip.com/topic/{int(code)}"
      s = requests.Session()
      respones = s.get(url,timeout=60)
      topic_id = respones.url.split("/")[4]
      soup = BeautifulSoup(respones.content, 'html.parser')
    #   Python library for pulling data out of HTML and XML files.
    #   ดูจากสิ่งที่เราต้องการผ่าน devtools
      topic_name = soup.find("h2", {"class": "display-post-title"}).get_text()
    #   find หา
      link_profile = soup.find("a", {"class": "display-post-name owner"}).get('href')
      content_name = soup.find("div", {"class": "display-post-story"}).get_text()
      tag_name = [i.text 
                  for i in soup.find("div", {"class": "display-post-tag-wrapper"}).find_all('a')]
      dataDictionary ={
        'url':respones.url,
        'topic_id':str(topic_id),
        'topic_name':str(topic_name),
        'tag_name':tag_name,
        'content':str(content_name),
        'link_profile':str(link_profile)}
      rowdata = Row(**dataDictionary)
      
      if topic_name and link_profile and content_name and tag_name is not None:        
        Alldata.append(rowdata)
    except  Exception as e:
#         raise e
      print(f"Topic has been remove {url}") 

def start_thread_to_terminate_when_parent_process_dies(ppid):
    pid = os.getpid()
    # getpid() ?-?
    def f():
        while True:
            try:
                os.kill(ppid, 0)
                # kill ไม่เอา
            except OSError:
                os.kill(pid, signal.SIGTERM)
            time.sleep(1)    

if __name__ == '__main__':
    # if __name__ == '__main__' ?-?
    genrate_url()
    dataArr = np.array_split(all_urls[0], 10)
    print(f"Total url diff {len(all_urls[0])}")
    print(f"chunk size {len(dataArr[0])}")
    for i in range(0,9):
      print(f"chunk number {i+1} /10")
    #   แบ่งข้อมูลเป็น 10 ส่วน
      print(f"Total url can collect {len(Alldata)}")
#       with ThreadPoolExecutor(initializer=start_thread_to_terminate_when_parent_process_dies,initargs=(os.getpid(),)) as executor:

# ทำงานแบบ พาราเรียล จะมีแบบ sysc กับ asysc
      with ThreadPoolExecutor() as executor:
        executor.map(executeRestApi,dataArr[i].tolist())
        executor.shutdown()
        

    datframe = spark.createDataFrame(sc.parallelize(Alldata))
    datframe = datframe.dropDuplicates(["topic_id"])
#     datframe.display()   
    datframe.write.partitionBy("link_profile").mode("append").saveAsTable("digide_common.master_pantip_daily")


