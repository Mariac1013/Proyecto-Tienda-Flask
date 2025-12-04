# app.py — Archivo principal de la aplicación Flask
# Ruta: app.py

from flask import Flask, render_template, session, redirect, url_for
from products import products
import os

# Crear la aplicación Flask.
# __name__ le indica a Flask dónde está este archivo para ubicar plantillas y rutas.
app = Flask(__name__)

# Clave secreta para manejar sesiones.
# Se intenta leer desde una variable de entorno; si no existe, usa una por defecto.
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "clave_secreta_para_sesiones")

# Función para obtener las categorías únicas de los productos.
def get_categories():
    return sorted(set(p["category"] for p in products))

# Ruta principal (Home).
# Muestra la lista de productos y las categorías disponibles.
@app.route("/")
def index():
    categories = get_categories()
    return render_template("index.html", products=products, categories=categories)

# Aquí irán las demás rutas del proyecto:
# - categoría por nombre
# - detalle de producto
# - agregar al carrito
# - mostrar carrito
# - vaciar carrito

#crear ruta y funcion para acceder  a la pagina de categorias
@app.route("/categoria/<category>")
def categoria(category):
    filtered = [p for p in products if p["category"].lower() == category.lower()]
    categories = get_categories()
    if not filtered:
        return render_template("categoria.html", products=[], category=category, categories=categories, empty=True)
    return render_template("categoria.html", products=filtered, category=category, categories=categories, empty=False)


#crear ruta y funcion para acceder  a la pagina de detalles del producto
@app.route("/producto/<int:producto_id>")
def product_detail(producto_id):
    product = next((p for p in products if p["id"] == producto_id), None)
    categories = get_categories()
    if not product:
        return "Producto no encontrado", 404
    return render_template("product_detail.html", product=product, categories=categories)


#crear ruta y funcion para agregar producto al carrito y vaciar el carrito
@app.route("/agregar/<int:producto_id>")
def add_to_cart(producto_id):
    session.setdefault("cart", [])
    session["cart"].append(producto_id)
    session.modified = True
    return redirect(url_for("cart"))

@app.route("/carrito")
def cart():
    cart_ids = session.get("cart", [])
    categories = get_categories()
    items = [p for p in products if p["id"] in cart_ids]
    return render_template("cart.html", items=items, categories=categories)

@app.route("/vaciar")
def empty_cart():
    session["cart"] = []
    return redirect(url_for("cart"))


#crear ruta y funcion para obtener la opción de eliminar un producto del carrito
@app.route("/eliminar/<int:producto_id>")
def delete_from_cart(producto_id):
    cart = session.get("cart", [])

    if producto_id in cart:
        cart.remove(producto_id)

    session["cart"] = cart
    session.modified = True
    return redirect(url_for("cart"))

#Siempre al final
# Si el archivo se ejecuta directamente, inicia el servidor Flask.
# debug=True activa recarga automática y mensajes de error detallados.
if __name__ == "__main__":
    app.run(debug=True)

