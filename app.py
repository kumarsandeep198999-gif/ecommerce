from flask import Flask, render_template, request, redirect, session
import sqlite3
import json

app = Flask(__name__)
app.secret_key = "my-secret-key-123"


# =========================
# DATABASE
# =========================

DB_NAME = "orders.db"


def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            items TEXT NOT NULL,
            total REAL NOT NULL,
            status TEXT DEFAULT 'Pending'
        )
    """)

    conn.commit()
    conn.close()


def add_status_column():
    conn = get_db()

    try:
        conn.execute(
            "ALTER TABLE orders ADD COLUMN status TEXT DEFAULT 'Pending'"
        )
        conn.commit()
    except sqlite3.OperationalError:
        pass

    conn.close()


init_db()
add_status_column()


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
# SALE
# =========================

@app.route("/sale")
def sale():

    sale_products = [
        {
            "brand": "Balmain",
            "name": "Designer Jacket",
            "price": 65000
        },
        {
            "brand": "Classic",
            "name": "Handbag",
            "price": 55000
        },
        {
            "brand": "Ami Paris",
            "name": "Wool Jacket",
            "price": 45000
        }
    ]

    return render_template(
        "products.html",
        category="Sale",
        products=sale_products
    )


# =========================
# SHOES
# =========================

@app.route("/shoes")
def shoes():

    products = [
        {
            "brand": "Nike",
            "name": "Air Max Shoes",
            "price": 12000
        },
        {
            "brand": "Adidas",
            "name": "Running Shoes",
            "price": 8500
        },
        {
            "brand": "Puma",
            "name": "Classic Sneakers",
            "price": 6500
        }
    ]

    return render_template(
        "products.html",
        category="Shoes",
        products=products
    )


# =========================
# BAGS
# =========================

@app.route("/bags")
def bags():

    products = [
        {
            "brand": "Classic",
            "name": "Leather Handbag",
            "price": 55000
        },
        {
            "brand": "Luxe",
            "name": "Designer Bag",
            "price": 42000
        },
        {
            "brand": "Urban",
            "name": "Shoulder Bag",
            "price": 18000
        }
    ]

    return render_template(
        "products.html",
        category="Bags",
        products=products
    )


# =========================
# ACCESSORIES
# =========================

@app.route("/accessories")
def accessories():

    products = [
        {
            "brand": "Classic",
            "name": "Leather Belt",
            "price": 4500
        },
        {
            "brand": "Luxury",
            "name": "Designer Sunglasses",
            "price": 8500
        },
        {
            "brand": "Premium",
            "name": "Wallet",
            "price": 6500
        }
    ]

    return render_template(
        "products.html",
        category="Accessories",
        products=products
    )


# =========================
# JEWELRY
# =========================

@app.route("/jewelry")
def jewelry():

    products = [
        {
            "brand": "Luxury",
            "name": "Gold Necklace",
            "price": 75000
        },
        {
            "brand": "Classic",
            "name": "Silver Bracelet",
            "price": 15000
        },
        {
            "brand": "Premium",
            "name": "Designer Ring",
            "price": 25000
        }
    ]

    return render_template(
        "products.html",
        category="Jewelry",
        products=products
    )


# =========================
# BEAUTY
# =========================

@app.route("/beauty")
def beauty():

    products = [
        {
            "brand": "Beauty",
            "name": "Premium Perfume",
            "price": 8500
        },
        {
            "brand": "Luxury",
            "name": "Face Cream",
            "price": 4500
        },
        {
            "brand": "Premium",
            "name": "Beauty Set",
            "price": 6500
        }
    ]

    return render_template(
        "products.html",
        category="Beauty",
        products=products
    )


# =========================
# READY TO WEAR CATEGORIES
# =========================

@app.route("/ready-to-wear/<category>")
def ready_to_wear_category(category):

    products = {

        "all-products": [
            {
                "brand": "Balmain",
                "name": "Designer Jacket",
                "price": 65000
            },
            {
                "brand": "Ami Paris",
                "name": "Wool Jacket",
                "price": 45000
            },
            {
                "brand": "Burberry",
                "name": "Classic Coat",
                "price": 55000
            }
        ],

        "new-brands": [
            {
                "brand": "Ami Paris",
                "name": "Wool Jacket",
                "price": 45000
            },
            {
                "brand": "Lemaire",
                "name": "Relaxed Shirt",
                "price": 28000
            }
        ],

        "jackets": [
            {
                "brand": "Balmain",
                "name": "Designer Jacket",
                "price": 65000
            },
            {
                "brand": "Ami Paris",
                "name": "Wool Jacket",
                "price": 45000
            }
        ],

        "knitwear": [
            {
                "brand": "Loewe",
                "name": "Wool Knitwear",
                "price": 38000
            }
        ],

        "leather": [
            {
                "brand": "Celine",
                "name": "Leather Jacket",
                "price": 72000
            }
        ],

        "tops-shirts": [
            {
                "brand": "Dior",
                "name": "Designer Shirt",
                "price": 32000
            }
        ],

        "sets": [
            {
                "brand": "Miu Miu",
                "name": "Designer Set",
                "price": 48000
            }
        ],

        "skirts": [
            {
                "brand": "Chloé",
                "name": "Designer Skirt",
                "price": 36000
            }
        ],

        "coats": [
            {
                "brand": "Burberry",
                "name": "Classic Coat",
                "price": 55000
            }
        ],

        "dresses": [
            {
                "brand": "The Row",
                "name": "Luxury Dress",
                "price": 60000
            }
        ],

        "denim": [
            {
                "brand": "Isabel Marant",
                "name": "Denim Jeans",
                "price": 22000
            }
        ],

        "pants": [
            {
                "brand": "Lemaire",
                "name": "Designer Pants",
                "price": 26000
            }
        ],

        "suits": [
            {
                "brand": "Balmain",
                "name": "Classic Suit",
                "price": 75000
            }
        ],

        "sweatshirts": [
            {
                "brand": "Ami Paris",
                "name": "Logo Sweatshirt",
                "price": 24000
            }
        ],

        "shorts": [
            {
                "brand": "Louis Vuitton",
                "name": "Designer Shorts",
                "price": 30000
            }
        ],

        "beachwear": [
            {
                "brand": "Khaite",
                "name": "Premium Beachwear",
                "price": 28000
            }
        ]
    }

    selected_products = products.get(category, [])

    return render_template(
        "products.html",
        category=category.replace("-", " ").title(),
        products=selected_products
    )


# =========================
# BRANDS
# =========================

@app.route("/brand/<brand>")
def brand(brand):

    brand_products = {

        "Ami Paris": [
            {
                "brand": "Ami Paris",
                "name": "Wool Jacket",
                "price": 45000
            },
            {
                "brand": "Ami Paris",
                "name": "Logo Sweatshirt",
                "price": 24000
            }
        ],

        "Balmain": [
            {
                "brand": "Balmain",
                "name": "Designer Jacket",
                "price": 65000
            },
            {
                "brand": "Balmain",
                "name": "Classic Suit",
                "price": 75000
            }
        ],

        "Burberry": [
            {
                "brand": "Burberry",
                "name": "Classic Coat",
                "price": 55000
            }
        ],

        "Celine": [
            {
                "brand": "Celine",
                "name": "Leather Jacket",
                "price": 72000
            }
        ],

        "Chloé": [
            {
                "brand": "Chloé",
                "name": "Designer Skirt",
                "price": 36000
            }
        ],

        "Dior": [
            {
                "brand": "Dior",
                "name": "Designer Shirt",
                "price": 32000
            }
        ],

        "Isabel Marant": [
            {
                "brand": "Isabel Marant",
                "name": "Denim Jeans",
                "price": 22000
            }
        ],

        "Khaite": [
            {
                "brand": "Khaite",
                "name": "Premium Beachwear",
                "price": 28000
            }
        ],

        "Lemaire": [
            {
                "brand": "Lemaire",
                "name": "Relaxed Shirt",
                "price": 28000
            },
            {
                "brand": "Lemaire",
                "name": "Designer Pants",
                "price": 26000
            }
        ],

        "Loewe": [
            {
                "brand": "Loewe",
                "name": "Wool Knitwear",
                "price": 38000
            }
        ],

        "Louis Vuitton": [
            {
                "brand": "Louis Vuitton",
                "name": "Designer Shorts",
                "price": 30000
            }
        ],

        "Miu Miu": [
            {
                "brand": "Miu Miu",
                "name": "Designer Set",
                "price": 48000
            }
        ],

        "The Row": [
            {
                "brand": "The Row",
                "name": "Luxury Dress",
                "price": 60000
            }
        ]
    }

    selected_products = brand_products.get(brand, [])

    return render_template(
        "products.html",
        category=brand,
        products=selected_products
    )


# =========================
# ADD TO CART
# =========================

@app.route("/add-to-cart", methods=["POST"])
def add_to_cart():

    product = {
        "brand": request.form.get("brand"),
        "name": request.form.get("name"),
        "price": float(request.form.get("price", 0))
    }

    cart = session.get("cart", [])

    cart.append(product)

    session["cart"] = cart

    return redirect("/cart")


# =========================
# CART
# =========================

@app.route("/cart")
def cart():

    cart_items = session.get("cart", [])

    total = sum(
        float(item.get("price", 0))
        for item in cart_items
    )

    return render_template(
        "cart.html",
        cart=cart_items,
        total=total
    )


# =========================
# REMOVE FROM CART
# =========================

@app.route("/remove-from-cart/<int:index>")
def remove_from_cart(index):

    cart = session.get("cart", [])

    if 0 <= index < len(cart):
        cart.pop(index)

    session["cart"] = cart

    return redirect("/cart")


# =========================
# CLEAR CART
# =========================

@app.route("/clear-cart")
def clear_cart():

    session["cart"] = []

    return redirect("/cart")


# =========================
# CHECKOUT
# =========================

@app.route("/checkout")
def checkout():

    cart_items = session.get("cart", [])

    if not cart_items:
        return redirect("/cart")

    total = sum(
        float(item.get("price", 0))
        for item in cart_items
    )

    return render_template(
        "checkout.html",
        cart=cart_items,
        total=total
    )


# =========================
# PLACE ORDER
# =========================

@app.route("/place-order", methods=["POST"])
def place_order():

    cart_items = session.get("cart", [])

    if not cart_items:
        return redirect("/cart")

    total = sum(
        float(item.get("price", 0))
        for item in cart_items
    )

    conn = get_db()

    conn.execute(
        """
        INSERT INTO orders (items, total, status)
        VALUES (?, ?, ?)
        """,
        (
            json.dumps(cart_items),
            total,
            "Pending"
        )
    )

    conn.commit()
    conn.close()

    session["cart"] = []

    return render_template(
        "order-success.html",
        total=total
    )


# =========================
# ADMIN LOGIN
# =========================

@app.route("/admin-login", methods=["GET", "POST"])
def admin_login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "Admin@123":

            session["admin_logged_in"] = True

            return redirect("/orders")

        return "Invalid username or password"

    return render_template("admin-login.html")


# =========================
# ORDERS
# =========================

@app.route("/orders")
def orders():

    if not session.get("admin_logged_in"):
        return redirect("/admin-login")

    conn = get_db()

    orders_data = conn.execute(
        "SELECT * FROM orders ORDER BY id DESC"
    ).fetchall()

    conn.close()

    orders_list = []

    for order in orders_data:

        orders_list.append({
            "id": order["id"],
            "items": json.loads(order["items"]),
            "total": order["total"],
            "status": order["status"]
        })

    return render_template(
        "orders.html",
        orders=orders_list
    )


# =========================
# UPDATE ORDER STATUS
# =========================

@app.route("/update-status/<int:order_id>", methods=["POST"])
def update_status(order_id):

    if not session.get("admin_logged_in"):
        return redirect("/admin-login")

    status = request.form.get("status")

    allowed_statuses = [
        "Pending",
        "Shipped",
        "Delivered"
    ]

    if status not in allowed_statuses:
        status = "Pending"

    conn = get_db()

    conn.execute(
        """
        UPDATE orders
        SET status = ?
        WHERE id = ?
        """,
        (status, order_id)
    )

    conn.commit()
    conn.close()

    return redirect("/orders")


# =========================
# ADMIN LOGOUT
# =========================

@app.route("/admin-logout")
def admin_logout():

    session.pop("admin_logged_in", None)

    return redirect("/admin-login")


# =========================
# RUN APP
# =========================

if __name__ == "__main__":
    app.run(debug=True)