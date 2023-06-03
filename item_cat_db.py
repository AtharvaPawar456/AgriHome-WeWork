#  tut : https://www.tutorialspoint.com/sqlite/sqlite_python.htm
import sqlite3

DATABASE = 'data.db'


def createDB(DATABASE):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS category_item (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT,
            item_img_name TEXT,
            item_category TEXT,
            item_sub_category TEXT,
            slug TEXT,
            item_sub_header TEXT,
            item_price TEXT,
            item_qty TEXT,
            item_description TEXT,
            item_pay_id TEXT
        )
    """)
    conn.commit()
    conn.close()

"""
            item_name,item_img_name,item_category,item_sub_category,slug
item_name,item_img_name,item_category,item_sub_category,slug,item_sub_header,item_price,item_qty, item_description, item_pay_id
            """

def insertData(DATABASE):
    conn = sqlite3.connect(DATABASE)
    print("Opened database successfully")

    data = [
       ("Tomato seeds","tomato-seeds.jpeg"                  ,"Seeds and Plant Materials","Vegetable seeds","tomato-seeds","1 pack contains 100 seeds","Rs. 100","1","non hybrid","price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        ("Carrot seeds","carrot-seeds.jpeg"                  ,"Seeds and Plant Materials","Vegetable seeds","carrot-seeds","1 pack contains 100 seeds","Rs. 100","1","non hybrid","price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        ("Lettuce seeds","lettuce-seeds.jpeg"                ,"Seeds and Plant Materials","Vegetable seeds","lettuce-seeds","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEz10SJLNTNDwCBAXrxke5i"),      #tomato seeds pay id
        ("Cucumber seeds","cucumber-seeds.jpeg"              ,"Seeds and Plant Materials","Vegetable seeds","cucumber-seeds","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),     #tomato seeds pay id
        ("Bell pepper seeds","bell-pepper-seeds.jpeg"        ,"Seeds and Plant Materials","Vegetable seeds","bell-pepper-seeds","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),      #tomato seeds pay id
        ("Spinach seeds","spinach-seeds.jpeg"                ,"Seeds and Plant Materials","Vegetable seeds","spinach-seeds","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),      #tomato seeds pay id
        ("Zucchini seeds","zucchini-seeds.jpeg"              ,"Seeds and Plant Materials","Vegetable seeds","zucchini-seeds","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),     #tomato seeds pay id
        ("Beetroot seeds","beetroot-seeds.jpeg"              ,"Seeds and Plant Materials","Vegetable seeds","beetroot-seeds","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),     #tomato seeds pay id
        ("Radish seeds","radish-seeds.jpeg"                  ,"Seeds and Plant Materials","Vegetable seeds","radish-seeds","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),     #tomato seeds pay id
        ("Kale seeds","kale-seeds.jpeg"                      ,"Seeds and Plant Materials","Vegetable seeds","kale-seeds","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),     #tomato seeds pay id
        ("Radish seeds","radish-seeds.jpeg"                  ,"Seeds and Plant Materials","Vegetable seeds","radish-seeds","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),     #tomato seeds pay id


        ("Apple tree sapling","apple-tree-sapling.jpeg"      ,"Seeds and Plant Materials","Fruit tree saplings","apple-tree-sapling","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEz41SJLNTNDwCBKgbZG7nr"),
        ("Orange tree sapling","orange-tree-sapling.jpeg"    ,"Seeds and Plant Materials","Fruit tree saplings","orange-tree-sapling","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        ("Mango tree sapling","mango-tree-sapling.jpeg"      ,"Seeds and Plant Materials","Fruit tree saplings","mango-tree-sapling","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        ("Peach tree sapling","peach-tree-sapling.jpeg"      ,"Seeds and Plant Materials","Fruit tree saplings","peach-tree-sapling","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        ("Lemon tree sapling","lemon-tree-sapling.jpeg"      ,"Seeds and Plant Materials","Fruit tree saplings","lemon-tree-sapling","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        ("Avocado tree sapling","avocado-tree-sapling.jpeg"  ,"Seeds and Plant Materials","Fruit tree saplings","avocado-tree-sapling","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        ("Pear tree sapling","pear-tree-sapling.jpeg"        ,"Seeds and Plant Materials","Fruit tree saplings","pear-tree-sapling","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        ("Cherry tree sapling","cherry-tree-sapling.jpeg"    ,"Seeds and Plant Materials","Fruit tree saplings","cherry-tree-sapling","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        ("Plum tree sapling","plum-tree-sapling.jpeg"        ,"Seeds and Plant Materials","Fruit tree saplings","plum-tree-sapling","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        ("Apricot tree sapling","apricot-tree-sapling.jpeg"  ,"Seeds and Plant Materials","Fruit tree saplings","apricot-tree-sapling","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb")


        # ("Sunflower seeds", "sunflower-seeds.jpg", "Seeds and Plant Materials", "Flower seeds", "sunflower-seeds","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        # ("Rose seeds", "rose-seeds.jpg", "Seeds and Plant Materials", "Flower seeds", "rose-seeds","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        # ("Marigold seeds", "marigold-seeds.jpg", "Seeds and Plant Materials", "Flower seeds", "marigold-seeds","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        # ("Lavender seeds", "lavender-seeds.jpg", "Seeds and Plant Materials", "Flower seeds", "lavender-seeds","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        # ("Cosmos seeds", "cosmos-seeds.jpg", "Seeds and Plant Materials", "Flower seeds", "cosmos-seeds","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        # ("Zinnia seeds", "zinnia-seeds.jpg", "Seeds and Plant Materials", "Flower seeds", "zinnia-seeds","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        # ("Petunia seeds", "petunia-seeds.jpg", "Seeds and Plant Materials", "Flower seeds", "petunia-seeds","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        # ("Dahlia seeds", "dahlia-seeds.jpg", "Seeds and Plant Materials", "Flower seeds", "dahlia-seeds","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        # ("Pansy seeds", "pansy-seeds.jpg", "Seeds and Plant Materials", "Flower seeds", "pansy-seeds","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        # ("Sweet pea seeds", "sweet-pea-seeds.jpg", "Seeds and Plant Materials", "Flower seeds", "sweet-pea-seeds","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),

        # ("Basil seeds", "basil-seeds.jpg", "Seeds and Plant Materials", "Herbs and spices", "basil-seeds","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        # ("Mint seeds", "mint-seeds.jpg", "Seeds and Plant Materials", "Herbs and spices", "mint-seeds","1 pack contains 100 seeds","Rs. 100","1","non hybrid"),
        # ("Cilantro seeds", "cilantro-seeds.jpg", "Seeds and Plant Materials", "Herbs and spices", "cilantro-seeds","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        # ("Thyme seeds", "thyme-seeds.jpg", "Seeds and Plant Materials", "Herbs and spices", "thyme-seeds","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        # ("Oregano seeds", "oregano-seeds.jpg", "Seeds and Plant Materials", "Herbs and spices", "oregano-seeds","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        # ("Parsley seeds", "parsley-seeds.jpg", "Seeds and Plant Materials", "Herbs and spices", "parsley-seeds","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        # ("Dill seeds", "dill-seeds.jpg", "Seeds and Plant Materials", "Herbs and spices", "dill-seeds","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        # ("Sage seeds", "sage-seeds.jpg", "Seeds and Plant Materials", "Herbs and spices", "sage-seeds","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        # ("Rosemary seeds", "rosemary-seeds.jpg", "Seeds and Plant Materials", "Herbs and spices", "rosemary-seeds","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        # ("Chives seeds", "chives-seeds.jpg", "Seeds and Plant Materials", "Herbs and spices", "chives-seeds","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),

        # ("Tomato seedlings", "tomato-seedlings.jpg", "Seeds and Plant Materials", "Seedlings and young plants", "tomato-seedlings","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        # ("Pepper seedlings", "pepper-seedlings.jpg", "Seeds and Plant Materials", "Seedlings and young plants", "pepper-seedlings","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        # ("Herb seedlings", "herb-seedlings.jpg", "Seeds and Plant Materials", "Seedlings and young plants", "herb-seedlings","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        # ("Strawberry plants", "strawberry-plants.jpg", "Seeds and Plant Materials", "Seedlings and young plants", "strawberry-plants","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        # ("Cabbage seedlings", "cabbage-seedlings.jpg", "Seeds and Plant Materials", "Seedlings and young plants", "cabbage-seedlings","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        # ("Eggplant seedlings", "eggplant-seedlings.jpg", "Seeds and Plant Materials", "Seedlings and young plants", "eggplant-seedlings","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        # ("Lettuce seedlings", "lettuce-seedlings.jpg", "Seeds and Plant Materials", "Seedlings and young plants", "lettuce-seedlings","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        # ("Kale seedlings", "kale-seedlings.jpg", "Seeds and Plant Materials", "Seedlings and young plants", "kale-seedlings","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        # ("Broccoli seedlings", "broccoli-seedlings.jpg", "Seeds and Plant Materials", "Seedlings and young plants", "broccoli-seedlings","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb"),
        # ("Flower seedlings", "flower-seedlings.jpg", "Seeds and Plant Materials", "Seedlings and young plants", "flower-seedlings","1 pack contains 100 seeds","Rs. 100","1","non hybrid", "price_1NEwk4SJLNTNDwCBYSA0uBMb")



      #  -----------------------------------------
      # old 

        # ("Tomato seeds","tomato-seeds.jpeg"                  ,"Seeds and Plant Materials","Vegetable seeds","tomato-seeds"),
        # ("Carrot seeds","carrot-seeds.jpeg"                  ,"Seeds and Plant Materials","Vegetable seeds","carrot-seeds"),
        # ("Lettuce seeds","lettuce-seeds.jpeg"                ,"Seeds and Plant Materials","Vegetable seeds","lettuce-seeds"),
        # ("Cucumber seeds","cucumber-seeds.jpeg"              ,"Seeds and Plant Materials","Vegetable seeds","cucumber-seeds"),
        # ("Bell pepper seeds","bell-pepper-seeds.jpeg"        ,"Seeds and Plant Materials","Vegetable seeds","bell-pepper-seeds"),
        # ("Spinach seeds","spinach-seeds.jpeg"                ,"Seeds and Plant Materials","Vegetable seeds","spinach-seeds"),
        # ("Zucchini seeds","zucchini-seeds.jpeg"              ,"Seeds and Plant Materials","Vegetable seeds","zucchini-seeds"),
        # ("Beetroot seeds","beetroot-seeds.jpeg"              ,"Seeds and Plant Materials","Vegetable seeds","beetroot-seeds"),
        # ("Radish seeds","radish-seeds.jpeg"                  ,"Seeds and Plant Materials","Vegetable seeds","radish-seeds"),
        # ("Kale seeds","kale-seeds.jpeg"                      ,"Seeds and Plant Materials","Vegetable seeds","kale-seeds"),
        # ("Radish seeds","radish-seeds.jpeg"                  ,"Seeds and Plant Materials","Vegetable seeds","radish-seeds"),


        # ("Apple tree sapling","apple-tree-sapling.jpeg"      ,"Seeds and Plant Materials","Fruit tree saplings","apple-tree-sapling"),
        # ("Orange tree sapling","orange-tree-sapling.jpeg"    ,"Seeds and Plant Materials","Fruit tree saplings","orange-tree-sapling"),
        # ("Mango tree sapling","mango-tree-sapling.jpeg"      ,"Seeds and Plant Materials","Fruit tree saplings","mango-tree-sapling"),
        # ("Peach tree sapling","peach-tree-sapling.jpeg"      ,"Seeds and Plant Materials","Fruit tree saplings","peach-tree-sapling"),
        # ("Lemon tree sapling","lemon-tree-sapling.jpeg"      ,"Seeds and Plant Materials","Fruit tree saplings","lemon-tree-sapling"),
        # ("Avocado tree sapling","avocado-tree-sapling.jpeg"  ,"Seeds and Plant Materials","Fruit tree saplings","avocado-tree-sapling"),
        # ("Pear tree sapling","pear-tree-sapling.jpeg"        ,"Seeds and Plant Materials","Fruit tree saplings","pear-tree-sapling"),
        # ("Cherry tree sapling","cherry-tree-sapling.jpeg"    ,"Seeds and Plant Materials","Fruit tree saplings","cherry-tree-sapling"),
        # ("Plum tree sapling","plum-tree-sapling.jpeg"        ,"Seeds and Plant Materials","Fruit tree saplings","plum-tree-sapling"),
        # ("Apricot tree sapling","apricot-tree-sapling.jpeg"  ,"Seeds and Plant Materials","Fruit tree saplings","apricot-tree-sapling")


        # ("Sunflower seeds", "sunflower-seeds.jpg", "Seeds and Plant Materials", "Flower seeds", "sunflower-seeds"),
        # ("Rose seeds", "rose-seeds.jpg", "Seeds and Plant Materials", "Flower seeds", "rose-seeds"),
        # ("Marigold seeds", "marigold-seeds.jpg", "Seeds and Plant Materials", "Flower seeds", "marigold-seeds"),
        # ("Lavender seeds", "lavender-seeds.jpg", "Seeds and Plant Materials", "Flower seeds", "lavender-seeds"),
        # ("Cosmos seeds", "cosmos-seeds.jpg", "Seeds and Plant Materials", "Flower seeds", "cosmos-seeds"),
        # ("Zinnia seeds", "zinnia-seeds.jpg", "Seeds and Plant Materials", "Flower seeds", "zinnia-seeds"),
        # ("Petunia seeds", "petunia-seeds.jpg", "Seeds and Plant Materials", "Flower seeds", "petunia-seeds"),
        # ("Dahlia seeds", "dahlia-seeds.jpg", "Seeds and Plant Materials", "Flower seeds", "dahlia-seeds"),
        # ("Pansy seeds", "pansy-seeds.jpg", "Seeds and Plant Materials", "Flower seeds", "pansy-seeds"),
        # ("Sweet pea seeds", "sweet-pea-seeds.jpg", "Seeds and Plant Materials", "Flower seeds", "sweet-pea-seeds"),

        # ("Basil seeds", "basil-seeds.jpg", "Seeds and Plant Materials", "Herbs and spices", "basil-seeds"),
        # ("Mint seeds", "mint-seeds.jpg", "Seeds and Plant Materials", "Herbs and spices", "mint-seeds"),
        # ("Cilantro seeds", "cilantro-seeds.jpg", "Seeds and Plant Materials", "Herbs and spices", "cilantro-seeds"),
        # ("Thyme seeds", "thyme-seeds.jpg", "Seeds and Plant Materials", "Herbs and spices", "thyme-seeds"),
        # ("Oregano seeds", "oregano-seeds.jpg", "Seeds and Plant Materials", "Herbs and spices", "oregano-seeds"),
        # ("Parsley seeds", "parsley-seeds.jpg", "Seeds and Plant Materials", "Herbs and spices", "parsley-seeds"),
        # ("Dill seeds", "dill-seeds.jpg", "Seeds and Plant Materials", "Herbs and spices", "dill-seeds"),
        # ("Sage seeds", "sage-seeds.jpg", "Seeds and Plant Materials", "Herbs and spices", "sage-seeds"),
        # ("Rosemary seeds", "rosemary-seeds.jpg", "Seeds and Plant Materials", "Herbs and spices", "rosemary-seeds"),
        # ("Chives seeds", "chives-seeds.jpg", "Seeds and Plant Materials", "Herbs and spices", "chives-seeds"),

        # ("Tomato seedlings", "tomato-seedlings.jpg", "Seeds and Plant Materials", "Seedlings and young plants", "tomato-seedlings"),
        # ("Pepper seedlings", "pepper-seedlings.jpg", "Seeds and Plant Materials", "Seedlings and young plants", "pepper-seedlings"),
        # ("Herb seedlings", "herb-seedlings.jpg", "Seeds and Plant Materials", "Seedlings and young plants", "herb-seedlings"),
        # ("Strawberry plants", "strawberry-plants.jpg", "Seeds and Plant Materials", "Seedlings and young plants", "strawberry-plants"),
        # ("Cabbage seedlings", "cabbage-seedlings.jpg", "Seeds and Plant Materials", "Seedlings and young plants", "cabbage-seedlings"),
        # ("Eggplant seedlings", "eggplant-seedlings.jpg", "Seeds and Plant Materials", "Seedlings and young plants", "eggplant-seedlings"),
        # ("Lettuce seedlings", "lettuce-seedlings.jpg", "Seeds and Plant Materials", "Seedlings and young plants", "lettuce-seedlings"),
        # ("Kale seedlings", "kale-seedlings.jpg", "Seeds and Plant Materials", "Seedlings and young plants", "kale-seedlings"),
        # ("Broccoli seedlings", "broccoli-seedlings.jpg", "Seeds and Plant Materials", "Seedlings and young plants", "broccoli-seedlings"),
        # ("Flower seedlings", "flower-seedlings.jpg", "Seeds and Plant Materials", "Seedlings and young plants", "flower-seedlings")

        # ("Potting soil mix", "potting-soil-mix.jpg", "Gardening Supplies", "Soil and compost", "potting-soil-mix"),
        # ("Organic compost", "organic-compost.jpg", "Gardening Supplies", "Soil and compost", "organic-compost"),
        # ("Seed starting mix", "seed-starting-mix.jpg", "Gardening Supplies", "Soil and compost", "seed-starting-mix"),
        # ("Vermiculite", "vermiculite.jpg", "Gardening Supplies", "Soil and compost", "vermiculite"),
        # ("Perlite", "perlite.jpg", "Gardening Supplies", "Soil and compost", "perlite"),
        # ("Coco coir", "coco-coir.jpg", "Gardening Supplies", "Soil and compost", "coco-coir"),

        # ("Organic vegetable fertilizer", "organic-vegetable-fertilizer.jpg", "Gardening Supplies", "Fertilizers and amendments", "organic-vegetable-fertilizer"),
        # ("Fish emulsion fertilizer", "fish-emulsion-fertilizer.jpg", "Gardening Supplies", "Fertilizers and amendments", "fish-emulsion-fertilizer"),
        # ("Bone meal", "bone-meal.jpg", "Gardening Supplies", "Fertilizers and amendments", "bone-meal"),
        # ("Blood meal", "blood-meal.jpg", "Gardening Supplies", "Fertilizers and amendments", "blood-meal"),
        # ("Epsom salt", "epsom-salt.jpg", "Gardening Supplies", "Fertilizers and amendments", "epsom-salt"),
        # ("Composted manure", "composted-manure.jpg", "Gardening Supplies", "Fertilizers and amendments", "composted-manure"),



        # ("Wood chips", "wood-chips.jpg", "Gardening Supplies", "Mulch and ground cover", "wood-chips"),
        # ("Straw mulch", "straw-mulch.jpg", "Gardening Supplies", "Mulch and ground cover", "straw-mulch"),
        # ("Cocoa bean hulls", "cocoa-bean-hulls.jpg", "Gardening Supplies", "Mulch and ground cover", "cocoa-bean-hulls"),
        # ("Rubber mulch", "rubber-mulch.jpg", "Gardening Supplies", "Mulch and ground cover", "rubber-mulch"),
        # ("Pine needles", "pine-needles.jpg", "Gardening Supplies", "Mulch and ground cover", "pine-needles"),
        # ("Ground cover fabric", "ground-cover-fabric.jpg", "Gardening Supplies", "Mulch and ground cover", "ground-cover-fabric"),

        # ("Plastic nursery pots", "plastic-nursery-pots.jpg", "Gardening Supplies", "Plant pots and containers", "plastic-nursery-pots"),
        # ("Ceramic plant pots", "ceramic-plant-pots.jpg", "Gardening Supplies", "Plant pots and containers", "ceramic-plant-pots"),
        # ("Hanging baskets", "hanging-baskets.jpg", "Gardening Supplies", "Plant pots and containers", "hanging-baskets"),
        # ("Window boxes", "window-boxes.jpg", "Gardening Supplies", "Plant pots and containers", "window-boxes"),
        # ("Grow bags", "grow-bags.jpg", "Gardening Supplies", "Plant pots and containers", "grow-bags"),
        # ("Self-watering planters", "self-watering-planters.jpg", "Gardening Supplies", "Plant pots and containers", "self-watering-planters"),


        # ("Gardening shovel", "gardening-shovel.jpg", "Gardening Supplies", "Garden tools", "gardening-shovel"),
        # ("Garden rake", "garden-rake.jpg", "Gardening Supplies", "Garden tools", "garden-rake"),
        # ("Pruning shears", "pruning-shears.jpg", "Gardening Supplies", "Garden tools", "pruning-shears"),
        # ("Hand trowel", "hand-trowel.jpg", "Gardening Supplies", "Garden tools", "hand-trowel"),
        # ("Garden hoe", "garden-hoe.jpg", "Gardening Supplies", "Garden tools", "garden-hoe"),
        # ("Garden gloves", "garden-gloves.jpg", "Gardening Supplies", "Garden tools", "garden-gloves"),

        # ("Drip irrigation kit", "drip-irrigation-kit.jpg", "Gardening Supplies", "Irrigation systems and supplies", "drip-irrigation-kit"),
        # ("Garden hose", "garden-hose.jpg", "Gardening Supplies", "Irrigation systems and supplies", "garden-hose"),
        # ("Sprinkler system", "sprinkler-system.jpg", "Gardening Supplies", "Irrigation systems and supplies", "sprinkler-system"),
        # ("Irrigation timer/controller", "irrigation-timer-controller.jpg", "Gardening Supplies", "Irrigation systems and supplies", "irrigation-timer-controller"),
        # ("Soaker hoses", "soaker-hoses.jpg", "Gardening Supplies", "Irrigation systems and supplies", "soaker-hoses"),
        # ("Watering cans", "watering-cans.jpg", "Gardening Supplies", "Irrigation systems and supplies", "watering-cans")



    ]

    conn.executemany("INSERT INTO category_item (item_name,item_img_name,item_category,item_sub_category,slug,item_sub_header,item_price,item_qty, item_description, item_pay_id) VALUES (?, ?, ?, ?, ?,?, ?, ?, ?, ?)", data)
    conn.commit()
    print("Records created successfully")
    conn.close()


def Show_Data(DATABASE):
  conn = sqlite3.connect(DATABASE)
  print("Opened database successfully")
  c = conn.cursor()
  c.execute("SELECT * FROM category_item")
#   c.execute("SELECT * FROM category_item WHERE item_sub_category = 'Vegetable seeds'")

#   c.execute("SELECT * FROM products WHERE id = 1")  
  # Modify the WHERE clause to specify the desired ID

  data = c.fetchall()
  for rowdata in data:
    print(f"{rowdata}\n")
  conn.close()


def update_data(DATABASE, name, email):
  conn = sqlite3.connect(DATABASE)
  c = conn.cursor()
  c.execute("UPDATE category_item SET email = ? WHERE name = ?", (email, name))
  conn.commit()
  conn.close()


def delete_data(DATABASE, id):
  conn = sqlite3.connect(DATABASE)
  c = conn.cursor()
  c.execute("DELETE FROM category_item WHERE id = ?", (id, ))
  conn.commit()
  conn.close()


# =============================================================================

# Show_Data(DATABASE)

# createDB(DATABASE)
# insertData(DATABASE)
# update_data(DATABASE, "Paul", "PaulABCmyabc@gmail.com")
# delete_data(DATABASE, "1")

Show_Data(DATABASE)


"""
(1, 
'DXN Reishi Gano Tea', 
'gano-tea.jpg', 
'DXN Reishi Gano Tea is blended with high quality Ganoderma powder. It has no added preservatives, artificial colouring and flavourings. DXN Reishi Gano Tea invigorates your mind and body and delights you with its exceptional flavour and pleasant aroma.', 
'provides refreshment, help to relieve stress, promotes energy & wellness, strengthens immune system, helps in detoxification, supports in maintaining balance of the body', 
'To prepare DXN Reishi Gano Tea, boil water, open a sachet of the tea, pour hot water over the tea powder, and stir. Let it steep for 3-5 minutes before enjoying its exceptional flavor and aroma. No preservatives or artificial additives are included in this tea.', 
'Beverage', 
450, 360, 135, 195)

(1, 
'DXN 2 in 1 Coffee', 
'gano-tea.jpg', 
'DXN Reishi Gano Tea is blended with high quality Ganoderma powder. It has no added preservatives, artificial colouring and flavourings. DXN Reishi Gano Tea invigorates your mind and body and delights you with its exceptional flavour and pleasant aroma.', 
'provides refreshment, help to relieve stress, promotes energy & wellness, strengthens immune system, helps in detoxification, supports in maintaining balance of the body', 
'To prepare DXN Reishi Gano Tea, boil water, open a sachet of the tea, pour hot water over the tea powder, and stir. Let it steep for 3-5 minutes before enjoying its exceptional flavor and aroma. No preservatives or artificial additives are included in this tea.', 
'Beverage', 
450, 360, 135, 195)

"""