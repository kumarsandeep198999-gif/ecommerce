from flask import Flask, render_template, session, redirect, url_for, request
import sqlite3
import json

app = Flask(__name__)
app.secret_key = "my-ecommerce-secret-key"

DATABASE = "orders.db"


# =========================
# DATABASE
# =========================

def init_db():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            mobile TEXT NOT NULL,
            address TEXT NOT NULL,
            city TEXT NOT NULL,
            state TEXT NOT NULL,
            pincode TEXT NOT NULL,
            items TEXT NOT NULL,
            total INTEGER NOT NULL,
            status TEXT DEFAULT 'Pending'
        )
    """)

    # पुराने database में status column नहीं है तो add करें
    try:
        cursor.execute(
            "ALTER TABLE orders ADD COLUMN status TEXT DEFAULT 'Pending'"
        )
    except sqlite3.OperationalError:
        pass

    conn.commit()
    conn.close()


init_db()


# =========================
# HOME
# =========================

@app.route("/")
def home():
    return render_template("index.html")


# =========================
# DESIGNERS
# =========================

@app.route("/designers")
def designers():
    return render_template("designers.html")


# =========================
# READY TO WEAR
# =========================

@app.route("/ready-to-wear")
def ready_to_wear():
    return render_template("ready-to-wear.html")


# =========================
# SHOES
# =========================

@app.route("/shoes")
def shoes():

    shoe_products = [
        {
            "brand": "Balmain",
            "name": "Designer Sneakers",
            "price": 45000,
            "image": "1.jfif"
        },
        {
            "brand": "Celine",
            "name": "Classic Sneakers",
            "price": 38000,
            "image": "2.jfif"
        },
        {
            "brand": "Loewe",
            "name": "Leather Shoes",
            "price": 55000,
            "image": "3.jfif"
        }
    ]

    return render_template(
        "products.html",
        category="Shoes",
        products=shoe_products
    )


# =========================
# BAGS
# =========================

@app.route("/bags")
def bags():

    bag_products = [
        {
            "brand": "Dior",
            "name": "Classic Handbag",
            "price": 55000
        },
        {
            "brand": "Celine",
            "name": "Leather Bag",
            "price": 65000
        },
        {
            "brand": "Loewe",
            "name": "Designer Bag",
            "price": 75000
        },
        {
            "brand": "Balmain",
            "name": "Luxury Shoulder Bag",
            "price": 85000
        }
    ]

    return render_template(
        "products.html",
        category="Bags",
        products=bag_products
    )


# =========================
# ACCESSORIES
# =========================

@app.route("/accessories")
def accessories():

    accessory_products = [
        {
            "brand": "Dior",
            "name": "Designer Belt",
            "price": 25000
        },
        {
            "brand": "Celine",
            "name": "Fashion Sunglasses",
            "price": 30000
        },
        {
            "brand": "Loewe",
            "name": "Leather Wallet",
            "price": 22000
        },
        {
            "brand": "Balmain",
            "name": "Designer Cap",
            "price": 18000
        }
    ]

    return render_template(
        "products.html",
        category="Accessories",
        products=accessory_products
    )


# =========================
# JEWELRY
# =========================

@app.route("/jewelry")
def jewelry():

    jewelry_products = [
        {
            "brand": "Dior",
            "name": "Gold Necklace",
            "price": 45000
        },
        {
            "brand": "Celine",
            "name": "Designer Earrings",
            "price": 28000
        },
        {
            "brand": "Loewe",
            "name": "Luxury Bracelet",
            "price": 35000
        },
        {
            "brand": "Balmain",
            "name": "Designer Ring",
            "price": 25000
        }
    ]

    return render_template(
        "products.html",
        category="Jewelry",
        products=jewelry_products
    )


# =========================
# BEAUTY
# =========================

@app.route("/beauty")
def beauty():

    beauty_products = [
        {
            "brand": "Dior",
            "name": "Beauty Cream",
            "price": 4500
        },
        {
            "brand": "Celine",
            "name": "Face Serum",
            "price": 3500
        },
        {
            "brand": "Balmain",
            "name": "Lipstick",
            "price": 2500
        },
        {
            "brand": "Loewe",
            "name": "Perfume",
            "price": 6500
        }
    ]

    return render_template(
        "products.html",
        category="Beauty",
        products=beauty_products
    )


# =========================
# SALE
# =========================

@app.route("/sale")
def sale():

    sale_products = [
        {
            "brand": "Ami Paris",
            "name": "Wool Jacket",
            "price": 45000,
            "image": "wool-jacket.jpg"
        },
        {
            "brand": "Lemaire",
            "name": "Relaxed Shirt",
            "price": 28000,
            "image": "relaxed-shirt.jpg"
        }
    ]

    return render_template(
        "products.html",
        category="Sale",
        products=sale_products
    )


# =========================
# READY-TO-WEAR PRODUCTS
# =========================

products = {

    "all-products": [
        {
            "brand": "Ami Paris",
            "name": "Classic Wool Jacket",
            "price": 45000,
            "image": "wool-jacket.jpg"
        },
        {
            "brand": "Balmain",
            "name": "Elegant Black Dress",
            "price": 65000
        },
        {
            "brand": "Lemaire",
            "name": "Relaxed Shirt",
            "price": 28000,
            "image": "relaxed-shirt.jpg"
        }
    ],

    "new-brands": [
        {
            "brand": "Ami Paris",
            "name": "Wool Jacket",
            "price": 45000,
            "image": "wool-jacket.jpg"
        },
        {
            "brand": "Lemaire",
            "name": "Relaxed Shirt",
            "price": 28000,
            "image": "relaxed-shirt.jpg"
        }
    ],

    "jackets": [
        {
            "brand": "Ami Paris",
            "name": "Wool Jacket",
            "price": 45000,
            "image": "wool-jacket.jpg"
        },
        {
            "brand": "Balmain",
            "name": "Black Designer Jacket",
            "price": 65000
        }
    ],

    "dresses": [
        {
            "brand": "Dior",
            "name": "Elegant Evening Dress",
            "price": 95000
        },
        {
            "brand": "Celine",
            "name": "Classic Black Dress",
            "price": 55000
        }
    ],

    "pants": [
        {
            "brand": "The Row",
            "name": "Wide Leg Pants",
            "price": 45000
        },
        {
            "brand": "Loewe",
            "name": "Leather Pants",
            "price": 55000
        }
    ]
}


@app.route("/ready-to-wear/<category>")
def product_category(category):

    category_products = products.get(category, [])

    category_name = category.replace("-", " ").title()

    return render_template(
        "products.html",
        category=category_name,
        products=category_products
    )


# =========================
# DESIGNER BRAND PRODUCTS
# =========================

brand_products = {

    "ami-paris": [
        {
            "brand": "Ami Paris",
            "name": "Ami Paris Wool Jacket",
            "price": 45000,
            "image": "wool-jacket.jpg"
        },
        {
            "brand": "Ami Paris",
            "name": "Ami Paris T-Shirt",
            "price": 18000
        }
    ],

    "balmain": [
        {
            "brand": "Balmain",
            "name": "Balmain Designer Jacket",
            "price": 65000
        },
        {
            "brand": "Balmain",
            "name": "Balmain Black Dress",
            "price": 75000
        }
    ],

    "burberry": [
        {
            "brand": "Burberry",
            "name": "Burberry Classic Coat",
            "price": 85000
        },
        {
            "brand": "Burberry",
            "name": "Burberry Shirt",
            "price": 35000
        }
    ],

    "celine": [
        {
            "brand": "Celine",
            "name": "Celine Classic Bag",
            "price": 65000
        },
        {
            "brand": "Celine",
            "name": "Celine Designer Shoes",
            "price": 55000
        }
    ],

    "chloe": [
        {
            "brand": "Chloé",
            "name": "Chloé Designer Dress",
            "price": 70000
        },
        {
            "brand": "Chloé",
            "name": "Chloé Handbag",
            "price": 60000
        }
    ],

    "dior": [
        {
            "brand": "Dior",
            "name": "Dior Classic Handbag",
            "price": 95000
        },
        {
            "brand": "Dior",
            "name": "Dior Designer Dress",
            "price": 85000
        }
    ],

    "isabel-marant": [
        {
            "brand": "Isabel Marant",
            "name": "Isabel Marant Jacket",
            "price": 55000
        },
        {
            "brand": "Isabel Marant",
            "name": "Isabel Marant Dress",
            "price": 48000
        }
    ],

    "khaite": [
        {
            "brand": "Khaite",
            "name": "Khaite Designer Dress",
            "price": 75000
        },
        {
            "brand": "Khaite",
            "name": "Khaite Leather Bag",
            "price": 85000
        }
    ],

    "lemaire": [
        {
            "brand": "Lemaire",
            "name": "Lemaire Wool Coat",
            "price": 65000
        },
        {
            "brand": "Lemaire",
            "name": "Relaxed Shirt",
            "price": 28000,
            "image": "relaxed-shirt.jpg"
        }
    ],

    "loewe": [
        {
            "brand": "Loewe",
            "name": "Loewe Leather Bag",
            "price": 85000
        },
        {
            "brand": "Loewe",
            "name": "Loewe Designer Shoes",
            "price": 55000
        }
    ],

    "louis-vuitton": [
        {
            "brand": "Louis Vuitton",
            "name": "Louis Vuitton Handbag",
            "price": 120000
        },
        {
            "brand": "Louis Vuitton",
            "name": "Louis Vuitton Shoes",
            "price": 75000
        }
    ],

    "miu-miu": [
        {
            "brand": "Miu Miu",
            "name": "Miu Miu Designer Dress",
            "price": 65000
        },
        {
            "brand": "Miu Miu",
            "name": "Miu Miu Handbag",
            "price": 75000
        }
    ],

    "the-row": [
        {
            "brand": "The Row",
            "name": "The Row Wool Coat",
            "price": 90000
        },
        {
            "brand": "The Row",
            "name": "The Row Designer Pants",
            "price": 55000
        }
    ]
}


# =========================
# BRAND PAGE
# =========================

@app.route("/brand/<brand>")
def brand(brand):

    selected_products = brand_products.get(brand, [])

    brand_names = {
        "ami-paris": "Ami Paris",
        "balmain": "Balmain",
        "burberry": "Burberry",
        "celine": "Celine",
        "chloe": "Chloé",
        "dior": "Dior",
        "isabel-marant": "Isabel Marant",
        "khaite": "Khaite",
        "lemaire": "Lemaire",
        "loewe": "Loewe",
        "louis-vuitton": "Louis Vuitton",
        "miu-miu": "Miu Miu",
        "the-row": "The Row"
    }

    brand_name = brand_names.get(brand, brand)

    return render_template(
        "products.html",
        category=brand_name,
        products=selected_products
    )


# =========================
# CART
# =========================

@app.route("/add-to-cart", methods=["POST"])
def add_to_cart():

    product = {
        "brand": request.form.get("brand"),
        "name": request.form.get("name"),
        "price": int(request.form.get("price")),
        "image": request.form.get("image")
    }

    cart = session.get("cart", [])

    cart.append(product)

    session["cart"] = cart

    return redirect(url_for("cart"))


@app.route("/cart")
def cart():

    cart_items = session.get("cart", [])

    total = sum(item["price"] for item in cart_items)

    return render_template(
        "cart.html",
        cart_items=cart_items,
        total=total
    )


@app.route("/remove-from-cart/<int:index>")
def remove_from_cart(index):

    cart = session.get("cart", [])

    if 0 <= index < len(cart):
        cart.pop(index)

    session["cart"] = cart

    return redirect(url_for("cart"))


@app.route("/clear-cart")
def clear_cart():

    session["cart"] = []

    return redirect(url_for("cart"))


# =========================
# CHECKOUT
# =========================

@app.route("/checkout")
def checkout():

    cart_items = session.get("cart", [])

    if not cart_items:
        return redirect(url_for("cart"))

    total = sum(item["price"] for item in cart_items)

    return render_template(
        "checkout.html",
        cart_items=cart_items,
        total=total
    )


# =========================
# PLACE ORDER
# =========================

@app.route("/place-order", methods=["POST"])
def place_order():

    cart_items = session.get("cart", [])

    if not cart_items:
        return redirect(url_for("cart"))

    customer = {
        "name": request.form.get("name"),
        "mobile": request.form.get("mobile"),
        "address": request.form.get("address"),
        "city": request.form.get("city"),
        "state": request.form.get("state"),
        "pincode": request.form.get("pincode"),
        "items": cart_items,
        "total": sum(item["price"] for item in cart_items)
    }

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO orders
        (name, mobile, address, city, state, pincode, items, total, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        customer["name"],
        customer["mobile"],
        customer["address"],
        customer["city"],
        customer["state"],
        customer["pincode"],
        json.dumps(customer["items"]),
        customer["total"],
        "Pending"
    ))

    conn.commit()
    conn.close()

    session["cart"] = []

    return render_template(
        "order-success.html",
        order=customer
    )


# =========================
# ADMIN LOGIN
# =========================

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "Admin@123"


@app.route("/admin-login", methods=["GET", "POST"])
def admin_login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:

            session["admin_logged_in"] = True

            return redirect(url_for("show_orders"))

        return render_template(
            "admin-login.html",
            error="Wrong username or password"
        )

    return render_template("admin-login.html")


# =========================
# ADMIN ORDERS
# =========================

@app.route("/orders")
def show_orders():

    if not session.get("admin_logged_in"):
        return redirect(url_for("admin_login"))

    conn = sqlite3.connect(DATABASE)

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM orders
        ORDER BY id DESC
    """)

    database_orders = cursor.fetchall()

    conn.close()

    orders = []

    for row in database_orders:

        order = {
            "id": row["id"],
            "name": row["name"],
            "mobile": row["mobile"],
            "address": row["address"],
            "city": row["city"],
            "state": row["state"],
            "pincode": row["pincode"],
            "items": json.loads(row["items"]),
            "total": row["total"],
            "status": row["status"] if "status" in row.keys() else "Pending"
        }

        orders.append(order)

    return render_template(
        "orders.html",
        orders=orders
    )


# =========================
# UPDATE ORDER STATUS
# =========================

@app.route("/update-status/<int:order_id>", methods=["POST"])
def update_status(order_id):

    if not session.get("admin_logged_in"):
        return redirect(url_for("admin_login"))

    status = request.form.get("status")

    allowed_statuses = [
        "Pending",
        "Shipped",
        "Delivered"
    ]

    if status not in allowed_statuses:
        status = "Pending"

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
        UPDATE orders
        SET status = ?
        WHERE id = ?
    """, (status, order_id))

    conn.commit()
    conn.close()

    return redirect(url_for("show_orders"))

# =========================
# DELETE ORDER
# =========================

@app.route("/delete-order/<int:order_id>")
def delete_order(order_id):

    if not session.get("admin_logged_in"):
        return redirect(url_for("admin_login"))

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM orders WHERE id = ?",
        (order_id,)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("show_orders"))


# =========================
# ADMIN LOGOUT
# =========================

@app.route("/admin-logout")
def admin_logout():

    session.pop("admin_logged_in", None)

    return redirect(url_for("admin_login"))


# =========================
# START SERVER
# =========================

if __name__ == "__main__":
    app.run(debug=True)