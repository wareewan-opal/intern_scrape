import pandas as pd

data = {'Game_Name': [
    "Mario Kart™ 8 Deluxe",
    "Mario + Rabbids® Kingdom Battle",
    "EA SPORTS FIFA 23 Nintendo Switch™ Legacy Edition",
    "resident evil 4",
    "MARIO + RABBIDS SPARKS OF HOPE",
    "Super Mario Odyssey™",
    "Crash Bandicoot™ - Crashiversary Bundle",
    "Monster Hunter Rise",
    "Have A Nice Death",
    "Mortal Kombat 11",
    "The Legend of Zelda™: Breath of the Wild",
    "The Legend of Zelda™: Tears of the Kingdom",
    "Immortals Fenyx Rising™",
    "Super Mario™ 3D World + Bowser’s Fury",
    "FINAL FANTASY VII",
    "Ni no Kuni: Wrath of the White Witch",
    "Hollow Knight",
    "Nintendo Switch Game Vouchers",
    "DRAGON BALL Xenoverse 2 for Nintendo Switch",
    "Mario Party™ Superstars"
    ],
'Description_Game': [
    "With Nintendo Switch, fans can enjoy the definitive version of Mario Kart 8 anywhere, anytime, even with up to eight friends in local wireless multiplayer.",
    "Embark on an adventure full of unexpected surprises in Mario + Rabbids® Kingdom Battle, an over-the-top turn-based combat game, only on Nintendo Switch.",
    "The World's Game",
    "The original action horror masterpiece.",
    "Team up with Mario, Luigi, Princess Peach, Rabbid Peach, Rabbid Luigi, and their friends on a galactic journey.",
    "Join Mario on a massive, globe-trotting 3D adventure and use his incredible new abilities to rescue Princess Peach from Bowser’s wedding plans!",
    "Celebrate 25 years of marsupial mayhem.",
    "Go on a hunt wherever you want, whenever you want in MONSTER HUNTER RISE for Nintendo Switch!",
    "Have a Nice Death is a 2D action roguelike where you play as an overworked Death, whose employees have run rampant, completely throwing off the balance of souls and his...",
    "Mortal Kombat is back and better than ever in the next evolution of the iconic franchise!",
    "Step into a world of discovery, exploration and adventure in The Legend of Zelda: Breath of the Wild, a boundary-breaking new game in the acclaimed series",
    "An epic adventure across the land and skies of Hyrule awaits in The Legend of Zelda: Tears of the Kingdom for Nintendo Switch.",
    "Play as Fenyx on a quest to save the Greek gods from a dark curse.",
    "Explore a world of Mario fun together!",
    "FINAL FANTASY VII, the timeless classic loved by a legion of fans, comes to Nintendo Switch with a number of helpful extra features!",
    "Follow Oliver’s journey as he embarks to another world in Ni No Kuni Remastered: Wrath of the White Witch on Nintendo Switch.",
    "Descend into darkness and brave the depths of a forgotten kingdom in Hollow Knight, an atmospheric action-adventure for Nintendo eShop on Nintendo Switch.",
    "Users with an active Nintendo Switch Online membership will be able to purchase a set of two vouchers that can be redeemed for a selection of downloadable Nintendo software. Each...",
    "DRAGON BALL XENOVERSE 2 builds upon the highly popular DRAGON BALL XENOVERSE with enhanced graphics that will further immerse players into the largest and most detailed Dragon Ball world ever...",
    "Party like a superstar in this classic collection, Mario Party Superstars for Nintendo Switch!"
],
'Price_Game': [
    "฿1,973.18",
    "฿1,397.83",
    "฿1,124.03",
    "฿522.64",
    "฿1,831.43",
    "฿1,973.18",
    "฿2,952.81",
    "฿1,214.27",
    "฿435.49",
    "฿568.82",
    "฿1,974.19",
    "฿2,065.07",
    "฿1,874.54",
    "฿1,973.18",
    "฿212.56",
    "฿632.05",
    "฿51.77",
    "฿2,608.79",
    "฿910.27",
    "฿1,699.11"
]
}

df = pd.DataFrame(data,columns=['Game_Name',  'Description_Game',  'Price_Game'])
print(df)

df.to_csv('BeautifulSoup_list_games.csv')