"""
pip install flask, db-sqlite3, stripe

to activate (.venv)
& "c:/Users/Atharva Pawar/Documents/Projects/Python__Notebook/FlaskProjects/AgiMark/.venv/Scripts/Activate.ps1"
"""

from flask import Flask, render_template, request,  redirect, session
import sqlite3
import stripe


app = Flask(__name__)
DATABASE = 'data.db'
app.secret_key = 'your_secret_key'  # Change this to a secure secret key

stripe.api_key = "sk_test_51N8d1mSJLNTNDwCBLrdNNroGB9c49ojEMkgg7xqpce0UuUwMD9aK5yScmOEjANSIWNSHRHXI7phKlGxMOptEaetY00KryWsncZ"

Your_Domain = "http://127.0.0.1:5000/"


# @app.route('/')
# def index():
#   return '<b>Parshu :: Aditya, Riddhi, Atharva '


@app.route('/')
def WelcomePage():
  tempData = ["",""]
  return render_template('welcomeHome.html', data=tempData)


@app.route('/home')
def home():
  conn = sqlite3.connect(DATABASE)
  c = conn.cursor()
  c.execute("SELECT * FROM category_item")
  all_data = c.fetchall()
  conn.close()
  # print("value",all_data)
  tempData = [session['username'],all_data]

  return render_template('home.html',data = tempData)

@app.route('/marketplace')
def marketplace():
  conn = sqlite3.connect(DATABASE)
  c = conn.cursor()

  c.execute("SELECT * FROM category_item WHERE item_category = 'Seeds and Plant Materials'")
  vegetable_seeds = c.fetchall()

  c.execute("SELECT * FROM category_item WHERE item_sub_category = 'Fruit tree saplings'")
  fruit_tree_saplings = c.fetchall()

  c.execute("SELECT * FROM category_item WHERE item_sub_category = 'Flower seeds'")
  flower_seeds = c.fetchall()

  c.execute("SELECT * FROM category_item WHERE item_sub_category = 'Herbs and spices'")
  herbs_and_spices = c.fetchall()

  c.execute("SELECT * FROM category_item WHERE item_sub_category = 'Seedlings and young plants'")
  seedlings_and_young_plants = c.fetchall()

  conn.close()

  path = 'item_img/'
  vegetable_seeds_updated_paths     = [(product[0], product[1], path + product[2], product[3], product[4], product[5])for product in vegetable_seeds]
  fruit_tree_saplings_updated_paths  = [(product[0], product[1], path + product[2], product[3], product[4], product[5])for product in fruit_tree_saplings]
  flower_seeds_updated_paths   = [(product[0], product[1], path + product[2], product[3], product[4], product[5])for product in flower_seeds]
  herbs_and_spices_updated_paths   = [(product[0], product[1], path + product[2], product[3], product[4], product[5])for product in herbs_and_spices]
  seedlings_and_young_plants_updated_paths   = [(product[0], product[1], path + product[2], product[3], product[4], product[5])for product in seedlings_and_young_plants]


  cardelements = [session['username'],
      vegetable_seeds_updated_paths,
      fruit_tree_saplings_updated_paths,
      flower_seeds_updated_paths,
      herbs_and_spices_updated_paths,
      seedlings_and_young_plants_updated_paths
  ]
  for item in cardelements[0]: 
    print(f"item: {item}" )

  return render_template('marketplace.html', data=cardelements)


@app.route('/login_page')
def login_page():
  tempData = ["Login"]
  return render_template('home.html',data = tempData)

@app.route('/login', methods=['POST'])
def login_post():
  if request.method == 'POST':
      username = request.form.get('username')
      password = request.form.get('password')

      conn = sqlite3.connect(DATABASE)
      c = conn.cursor()
      c.execute("SELECT * FROM accountlogins WHERE username = ?", (username,))
      row = c.fetchone()

      msg1 = f'Password: {password}, username: {username}'
      # print(msg1,"\n", row)
      if row is not None and str(password) == row[3]:
          session['username'] = username
          # print(username)
          tempData = [username]

          return render_template('home.html', data=tempData)
          # return redirect('/home', data=tempData)
          
      else:
          msg1 = f'Password: {password}, username: {username}'
          
          msg =  'Invalid username or password'
          # print(msg)
          return render_template('login.html', data=msg)

  msg = 'Try Again !!'
  print(msg)
  return render_template('login.html', data = msg)




# ------------------------------------------------------------------

@app.route('/signup_page')
def signup_page():
  return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup_post():
  username = request.form.get('username')
  email = request.form.get('email')
  password = request.form.get('password')
  # Add your login logic here
  # return f'Email: {email}, Password: {password}, username: {username}'

  if request.method == 'POST':
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM accountlogins WHERE username = ?", (username,))
    row = c.fetchone()

    if row is None:
        c.execute("INSERT INTO accountlogins (username, email_id, password) VALUES (?, ?, ?)", (username, email, password))
        conn.commit()
        conn.close()
        return render_template('login.html', data='Signup successful! Please log in.')

    msg = 'Username already exists. Please choose a different username.'
    return render_template('signup.html', data=msg)

  return render_template('signup.html')

@app.route('/logout')
def logout():
  session.pop('username', None)
  tempData = ["Login"]

  return render_template('login.html', data = tempData)
# ------------------------------------------------------------------


# @app.route('/contact')
# def contact():
#   return render_template('contact.html')

# @app.route('/about')
# def about():
#   return render_template('about.html')

# @app.route('/business_plan1')
# def business_plan1():
#   return render_template('business_plan1.html')

# @app.route('/business_plan2')
# def business_plan2():
#   return render_template('business_plan2.html')


@app.route('/productpage')
def productpage():
  conn = sqlite3.connect(DATABASE)
  c = conn.cursor()
  c.execute("SELECT * FROM card_products")  
  all_data = c.fetchall()
  conn.close()
  print(all_data)
  path = 'product_img/'
  all_data_with_cat = [
    (product[0], product[1], path + product[2], 
      'Nutrition' if product[3] == 'Health' else 'Personal Hygiene' if product[3] == 'Cosmetics' else 'Beverages',
       product[4],product[5])for product in all_data]

  return render_template('productlist.html',data = all_data_with_cat)


@app.route('/allproduct')
def allproduct():
  conn = sqlite3.connect(DATABASE)
  print("Opened database successfully")
  c = conn.cursor()     # c.execute("SELECT * FROM card_products")

  c.execute("SELECT * FROM card_products WHERE category = 'Health'")  
  healthCat_data = c.fetchall()

  c.execute("SELECT * FROM card_products WHERE category = 'Cosmetics'")  
  CosmaticsCat_data = c.fetchall()

  c.execute("SELECT * FROM card_products WHERE category = 'Beverages'")  
  BevragesCat_data = c.fetchall()
  conn.close()


  def printAll(data):
    for rowdata in data:
        print(f"{rowdata}\n")

  # Update the image path with full actual path
  path = 'product_img/'
  healthCat_data_with_updated_paths     = [(product[0], product[1], path + product[2], product[3], product[4], product[5])for product in healthCat_data]
  CosmaticsCat_data_with_updated_paths  = [(product[0], product[1], path + product[2], product[3], product[4], product[5])for product in CosmaticsCat_data]
  BevragesCat_data_with_updated_paths   = [(product[0], product[1], path + product[2], product[3], product[4], product[5])for product in BevragesCat_data]
  # OthersCat_data_with_updated_paths     = [(product[0], product[1], path + product[2], product[3], product[4])for product in OthersCat_data]

  # printAll(healthCat_data_with_updated_paths);
  # printAll(CosmaticsCat_data_with_updated_paths)
  # printAll(BevragesCat_data_with_updated_paths)
  # printAll(OthersCat_data_with_updated_paths)

  cardelements = [healthCat_data_with_updated_paths, CosmaticsCat_data_with_updated_paths, BevragesCat_data_with_updated_paths]

  return render_template('allproducts.html', carddata=cardelements)

# /singleproduct?productslug=johndoe-eysdcv
# @app.route('/singleproduct', methods=['GET'])
# def get_username():
#     item = request.args.get('productslug')
#     return f"<h1>The Product is:<br> {item}</h1>"

# /singleproduct?productslug=tomato-seeds
# @app.route('/products')
@app.route('/singleproduct', methods=['GET'])
def productPage():
  item = request.args.get('productslug')
  # print("item:  ",item)

  conn = sqlite3.connect(DATABASE)
  c = conn.cursor()
  c.execute("SELECT * FROM category_item WHERE slug = ?", (item,))
  item_info = c.fetchone()

  print(item_info)

  cat_name = item_info[4]
  print("cat_name:  ",cat_name)

  # Recommend 3 products cards

  # c.execute(f"SELECT * FROM card_products WHERE description = {cat_name} ORDER BY RANDOM() LIMIT 3;") 
  c.execute("SELECT * FROM category_item WHERE item_sub_category = ? ORDER BY RANDOM() LIMIT 4;", (cat_name,))

  recommend_data = c.fetchall()
  conn.close()
  # print(recommend_data)

  recommend_data = [item for item in recommend_data if item_info not in item]
  # print("filtered_data" , recommend_data)

    

  # all_product_info_with_updated_paths = all_product_info_with_updated_paths + recommend_data
  path = 'item_img/'
  recommend_data_with_updated_paths     = [(product[0], product[1], path + product[2], product[3], product[4], product[5])for product in recommend_data]

  print(recommend_data_with_updated_paths[0])

  # Update the image path with full actual path [10]
  path = 'item_img/'
  all_product_info_with_updated_paths     = [session['username'], item_info[1], path +  item_info[2],item_info[3], item_info[4], item_info[5], item_info[6],item_info[7],item_info[8],item_info[9],item_info[10],recommend_data_with_updated_paths[0],recommend_data_with_updated_paths[1],recommend_data_with_updated_paths[2]]
  # print(all_product_info_with_updated_paths)

  return render_template('product.html', data=all_product_info_with_updated_paths)


# http://localhost:5000/product_id?input=123
# http://localhost:5000/product_id?input=1
@app.route('/product_id')
def show_data():
  input_value = request.args.get('input')
  conn = sqlite3.connect(DATABASE)
  c = conn.cursor()
  c.execute(f"SELECT * FROM products WHERE id = {input_value}")  
  rowdata = c.fetchall()

  return render_template('product.html', data=rowdata)

# ==== Payment Section ============================================================
@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    pay_id_data = request.form.get('data_9')
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items = [
                {
                    'price': pay_id_data,
                    'quantity': 1
                }
            ],
            mode = "subscription",
            success_url = Your_Domain + "success",
            cancel_url  = Your_Domain + "cancel"
        )
    except Exception as e:
        return str(e)
    
    return redirect(checkout_session.url, code=303)

@app.route('/success')
def successPay():
  tempData = [session['username'],"temp"]
  return render_template('success.html',data = tempData)

@app.route('/cancel')
def cancelPay():
  tempData = [session['username'],"temp"]
  return render_template('cancel.html',data = tempData)

if __name__ == '__main__':
  app.run(debug=True)


"""
# def Show_Data(DATABASE):
#   conn = sqlite3.connect(DATABASE)
#   # print("Opened database successfully")
#   c = conn.cursor()
# #   c.execute("SELECT sr FROM products")
#   c.execute("SELECT * FROM products WHERE id = 1")  
#   # Modify the WHERE clause to specify the desired ID

#   data = c.fetchall()
#   for rowdata in data:
#     print(f"{rowdata}\n")
#   conn.close()



"""