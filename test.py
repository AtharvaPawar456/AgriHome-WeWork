import sqlite3

DATABASE = 'data.db'

def createDB(DATABASE):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS card_products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_title TEXT,
            product_img_name TEXT,
            category TEXT,
            mrp INTEGER,
            slug TEXT
        )
    """)
    conn.commit()
    conn.close()
    print("DB Table Created !!!")


# def insertData(DATABASE):
#     conn = sqlite3.connect(DATABASE)
#     print("Opened database successfully")
#     conn.execute("INSERT INTO products (product_title, product_img_name, category, mrp)VALUES ('DXN Ashwagandha','di_Ashwagandha.jpg','Health','315')")
#     conn.commit()
#     print("Records created successfully")
#     conn.close()


def insertData(DATABASE):
    conn = sqlite3.connect(DATABASE)
    print("Opened database successfully")

    data = [
        # Beverages
        ('DXN Noni 450ml','di_Noni_450ml.jpg','Beverages','950','dxn-noni-450ml'),
        ('DXN Nonizhi 250ml','di_Nonizhi_250ml.jpg','Beverages','865','dxn-nonizhi-250ml'),
        ('DXN Nonizhi 600ml','di_Nonizhi_600ml.jpg','Beverages','1835','dxn-nonizhi-600ml'),
        ('DXN Roselle Juice 250ml','di_Roselle.jpg','Beverages','585','dxn-roselle-juice-250ml'),

        ('DXN Reishi Gano Tea','di_ReishiTea.jpg','Beverages','450','dxn-reishi-gano-tea'),
        ('DXN Lingzhi Spices','di_LingzhiSpices.jpg','Beverages','465','dxn-lingzhi-spices'),
        ('DXN Dip Green Tea','di_DipGreenTea.jpg','Beverages','245','dxn-dip-green-tea'),
        ('DXN Dip Masala Tea','di_DipMasalaTea.jpg','Beverages','245','dxn-dip-masala-tea'),
        
        ('DXN Lingzhi Coffee 2 in 1','di_2in1.jpg','Beverages','840','dxn-lingzhi-coffee-2-in-1'),
        ('DXN Lingzhi Coffee 3 in 1','di_3in1.jpg','Beverages','910','dxn-lingzhi-coffee-3-in-1'),
        ('DXN Zhi Mocha','di_ZhiMocha.jpg','Beverages','1035','dxn-zhi-mocha'),
        ('DXN Cordyceps Coffee','di_Cordyceps3in1.jpg','Beverages','1075','dxn-cordyceps-coffee'),
        
        ('DXN Cocozhi','di_Cocozhi.jpg','Beverages','890','dxn-cocozhi'),
        ('DXN Lemonzhi','di_Lemonzhi.jpg','Beverages','600','dxn-lemonzhi'),
        ('DXN Spirulina Cereal','di_SpirulinaCereal.jpg','Beverages','1020','dxn-spirulina-cereal'),
        ('DXN Cordyceps Cereal','di_CordycepsCereal.jpg','Beverages','1165','dxn-cordyceps-cereal'),
        
        # Health
        ('DXN Spirulina Tablet 120','di_Spirulina_T120.jpg','Health','575','dxn-spirulina-tablet-120'),
        ('DXN Spirulina Tablet 360','di_Spirulina_T360.jpg','Health','1650','dxn-spirulina-tablet-360'),
        ('DXN Spirulina Capsule 120','di_Spirulina_C120.jpg','Health','575','dxn-spirulina-capsule-120'),
        ('DXN Spirulina Capsule 360','di_Spirulina_C360.jpg','Health','1650','dxn-spirulina-capsule-360'),
         
        ('DXN RG 30','di_RG30.jpg','Health','625','dxn-rg-30'),
        ('DXN GL 30','di_GL30.jpg','Health','475','dxn-gl-30'),
        ('DXN RG 90','di_RG90.jpg','Health','1710','dxn-rg-90'),
        ('DXN GL 90','di_GL90.jpg','Health','1315','dxn-gl-90'),
        
        ('DXN RG 360','di_RG360.jpg','Health','6440','dxn-rg-360'),
        ('DXN GL 360','di_GL360.jpg','Health','5035','dxn-gl-360'),
        ('DXN RG Powder','di_RG_Powder.jpg','Health','965','dxn-rg-powder'),
        ('DXN GL Powder','di_GL_Powder.jpg','Health','885','dxn-gl-powder'),

        ('DXN Spirulina Powder','di_Spirulina_Powder.jpg','Health','770','dxn-spirulina-powder'),
        ('DXN Healthy Bones 30','di_healthy_bones.jpg','Health','315','dxn-healthy-bones-30'),
        ('DXN Panax Ginseng 60','di_panax_ginseng.jpg','Health','625','dxn-panax-ginseng-60'),
        ('DXN Seabuckthorn 60','di_sea_buckthorn.jpg','Health','725','dxn-seabuckthorn-60'),

        ('DXN Ashwagandha','di_Ashwagandha.jpg','Health','315','dxn-ashwagandha'),
        ('DXN Black Cumin','di_black-cumin.jpg','Health','565','dxn-black-cumin'),
        ('DXN Brahmi','di_brahmi.jpg','Health','315','dxn-brahmi'),
        ('DXN Giloy','di_Giloy.jpg','Health','275','dxn-giloy'),
        
        ('DXN Neem','di_Neem.jpg','Health','315','dxn-neem'),
        ('DXN Triphala','di_Triphala.jpg','Health','315','dxn-triphala'),
        ('DXN Himalayan Pink Salt 200g','HimalayanPinkSalt_200g.jpg','Health','120','dxn-himalayan-pink-salt-200g'),
        ('DXN Himalayan Pink Salt 800g','HimalayanPinkSalt_800g.jpg','Health','345','dxn-himalayan-pink-salt-800g'),
        
        ('DXN Jaggery Powder 500grams','di_Jaggery_Powder.jpg','Health','230','dxn-jaggery-powder-500grams'),

        # Cosmetics
        ('DXN Bamboo Toothbrush','Brush_ProductImage.jpg','Cosmetics','105','dxn-bamboo-toothbrush'),
        ('Ganozhi Plus Toothpaste','di_Toothpaste.jpg','Cosmetics','345','ganozhi-plus-toothpaste'),
        ('Ganozhi Plus Toothpaste Small 75g','di_Toothpaste_Small.jpg','Cosmetics','215','ganozhi-plus-toothpaste-small'),
        ('Ganozhi Plus Toothpaste Box (6x)','di_Toothpaste_Box.jpg','Cosmetics','750','ganozhi-plus-toothpaste-box'),
        
        ('DXN Ganozhi Soap','di_Soap.jpg','Cosmetics','145','dxn-ganozhi-soap'),
        ('DXN Aloe. V Cleansing Gel','di_AloeV-CleansingGel.jpg','Cosmetics','375','dxn-aloe-v-cleansing-gel'),
        ('Gano Massage Oil','di_MassageOil.jpg','Cosmetics','485','gano-massage-oil'),
        ('DXN Ganozhi Shampoo','di_Shampoo.jpg','Cosmetics','425','dxn-ganozhi-shampoo'),
        
        ('DXN Chubby Baby Oil','di_ChubbyBabyOil.jpg','Cosmetics','455','dxn-chubby-baby-oil'),
        ('DXN Aloe. V Hand & Body','di_AloeV-H&B-Lotion.jpg','Cosmetics','430','dxn-aloe-v-hand-body'),
        ('Tea Tree Cream','di_TeaTree.jpg','Cosmetics','455','tea-tree-cream'),
        ('DXN Talcum Powder','di_TalcumPowder.jpg','Cosmetics','415','dxn-talcum-powder'),
        
        ('DXN Gano Extra Virgin Coconut Oil 250ml','di_GanoExtraVCO.jpeg','Cosmetics','525','virgin-coconut-oil-250ml'),
        ('DXN Neeli Tailam - Hair Oil','di_NeeliHairOil.jpg','Cosmetics','475','dxn-neeli-tailam'),
        ('DXN Utensil Care 500ml','HP024_UtensilCare_500ml.jpg','Cosmetics','230','dxn-utensil-care-500ml'),
        ('DXN Dyna Wash 1L','HP022G_DXN_Dyna_Wash_1L.jpg','Cosmetics','390','dxn-dyna-wash-1l'),

        # Add more data as needed
    ]

    conn.executemany("INSERT INTO card_products (product_title, product_img_name, category, mrp, slug) VALUES (?, ?, ?, ?, ?)", data)
    conn.commit()
    print("Records created successfully")
    conn.close()

# Call the function with your database name
# insertData('your_database_name.db')


def Show_Data(DATABASE):
    conn = sqlite3.connect(DATABASE)
    print("Opened database successfully")
    c = conn.cursor()
    # c.execute("SELECT * FROM card_products")

    c.execute("SELECT * FROM card_products WHERE category = 'Health'")  
    healthCat_data = c.fetchall()

    c.execute("SELECT * FROM card_products WHERE category = 'Cosmetics'")  
    CosmaticsCat_data = c.fetchall()

    c.execute("SELECT * FROM card_products WHERE category = 'Beverages'")  
    BevragesCat_data = c.fetchall()

    def printALLdata(dataLabel, data):
        print(dataLabel)
        for rowdata in data:
            print(f"{rowdata}\n")

    printALLdata("BevragesCat_data", BevragesCat_data)
    printALLdata("healthCat_data", healthCat_data)
    printALLdata("CosmaticsCat_data", CosmaticsCat_data)
    conn.close()


# createDB(DATABASE)
# insertData(DATABASE)
Show_Data(DATABASE)


"""
INSERT INTO products (product_title, product_img_name, category, mrp)VALUES ('DXN 2 in 1 Coffee','gano-tea.jpg','Beverage','360')


(product_title, product_img_name, category, mrp)VALUES 

('DXN Ashwagandha','di_Ashwagandha.jpg','Health','315'),
('DXN Black Cumin','di_black-cumin.jpg','Health','565'),
('DXN Brahmi','di_brahmi.jpg','Health','315'),
('DXN Giloy','di_Giloy.jpg','Health','275'),
('DXN Neem','di_Neem.jpg','Health','315'),
('DXN Triphala','di_Triphala.jpg','Health','315'),
('DXN RG 90','di_RG90.jpg','Health','1710'),
('DXN GL 90','di_GL90.jpg','Health','1315'),
('DXN Spirulina Capsule 360','di_Spirulina_C360.jpg','Health','1650'),
('DXN Healthy Bones 30','di_healthy_bones.jpg','Health','315'),
('DXN Panax Ginseng 60','di_panax_ginseng.jpg','Health','625'),
('DXN Seabuckthorn 60','di_sea_buckthorn.jpg','Health','725'),
('DXN Himalayan Pink Salt 200g','HimalayanPinkSalt_200g.jpg','Health','120'),
('DXN Himalayan Pink Salt 800g','HimalayanPinkSalt_800g.jpg','Health','345'),
('DXN Jaggery Powder 500grams','di_Jaggery_Powder.jpg','Health','230'),



('DXN Aloe. V Cleansing Gel','di_AloeV-CleansingGel.jpg','Cosmatics','375'),
('DXN Aloe. V Hand & Body','di_2in1.jpg','Cosmatics','430'),
('DXN Bamboo Toothbrush','Brush_ProductImage.jpg','Cosmatics','105'),
('DXN Chubby Baby Oil','di_ChubbyBabyOil.jpg','Cosmatics','455'),
('DXN Ganozhi Shampoo','di_Shampoo.jpg','Cosmatics','425'),
('DXN Ganozhi Soap','di_Soap.jpg','Cosmatics','145'),
('DXN Neeli Tailam - Hair Oil','di_NeeliHairOil.jpg','Cosmatics','475'),
('DXN Talcum Powder','di_TalcumPowder.jpg','Cosmatics','415'),
('Gano Massage Oil','di_MassageOil.jpg','Cosmatics','485'),
('Ganozhi Plus Toothpaste','di_Toothpaste.jpg','Cosmatics','345'),
('Tea Tree Cream','di_TeaTree.jpg','Cosmatics','455'),
('DXN Dyna Wash 1L','HP022G_DXN_Dyna_Wash_1L.jpg','Others','390'),
('DXN Mosquito Repellet','HP025_DXN_Mosquito_Repellent_watermark.jpg','Others','115'),
('DXN Utensil Care 500ml','HP024_UtensilCare_500ml.jpg','Others','230'),



('DXN Gano Extra Virgin Coconut Oil 250ml','di_GanoExtraVCO.jpeg','Bevrages','525'),
('DXN Nonizhi 600ml','di_Nonizhi_600ml.jpg','Bevrages','1835'),
('DXN Roselle Juice 250ml','di_Roselle.jpg','Bevrages','585'),
('DXN Lemonzhi','di_Lemonzhi.jpg','Bevrages','600'),
('DXN Lingzhi  Coffee 2 in 1','di_2in1.jpg','Bevrages','840'),
('DXN Lingzhi  Coffee 3 in 1','di_3in1.jpg','Bevrages','910'),
('DXN Cocozhi','di_Cocozhi.jpg','Bevrages','890'),
('DXN Cordyceps Cereal','di_CordycepsCereal.jpg','Bevrages','1165'),
('DXN Cordyceps Coffee','di_Cordyceps3in1.jpg','Bevrages','1075'),
('DXN Reishi Gano Tea','di_ReishiTea.jpg','Bevrages','450'),
('DXN Spirulina Cereal','di_SpirulinaCereal.jpg','Bevrages','1020'),
('DXN White Coffee Zhino','di_WhiteCoffee.jpg','Bevrages','1110'),
('DXN Zhi Mocha','di_ZhiMocha.jpg','Bevrages','1035'),










('Massage','di_2in1','Health','485')")

Health
Cosmatics
Bevrages
# Others
"""