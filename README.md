# 🛒 Mini Tienda Web con Flask

Proyecto educativo desarrollado con **Flask**, que simula una **mini tienda de productos** con carrito de compras, vista de detalle y filtrado por categorías.  
Ideal para aprendizaje de **backend con Python + Flask**, uso de **plantillas Jinja2**, sesiones y estilos con **CSS**.

---

## 📌 Características

✅ Listado de productos  
✅ Vista de detalle por producto  
✅ Carrito de compras con sesiones  
✅ Miniaturas de productos en el carrito  
✅ Filtro por categorías  
✅ Plantilla base reutilizable (`base.html`)  
✅ Estilos modernos con CSS  
✅ Arquitectura organizada  

---

## 🗂️ Estructura del Proyecto

```

/tu_proyecto
│ app.py
│ products.py
│
├── /static
│     ├── styles.css
│     └── /img
│           audifonos.png
│           mouse.jpg
│           teclado.jpg
│
└── /templates
base.html
index.html
product_detail.html
cart.html
categoria.html

````

---

## ⚙️ Requisitos

- Python 3.8 o superior  
- pip
- Entorno virtual (recomendado)

---

## 🚀 Instalación Paso a Paso

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/mini-tienda-flask.git
cd mini-tienda-flask
````

---

### 2️⃣ Crear entorno virtual

```bash
python -m venv venv
```

Activar entorno:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

---

### 3️⃣ Instalar Flask

```bash
pip install flask
```

---

### 4️⃣ Ejecutar el proyecto

```bash
python app.py
```

Abrir en el navegador:

```
http://127.0.0.1:5000
```

---

## 🧠 Tecnologías Usadas

* Python
* Flask
* HTML5
* CSS3
* Jinja2
* Sesiones con Flask

---

## 🛍️ Funcionamiento del Proyecto

* La página principal muestra los productos.
* Cada producto tiene un botón **"Ver detalle"**.
* Desde el detalle se puede **agregar al carrito**.
* El carrito muestra:

  * Miniatura del producto
  * Nombre
  * Precio
  * Total de la compra
* Se puede vaciar el carrito completamente.
* Las categorías permiten filtrar productos.

---

## 📸 Vista Previa

https://mini-tienda-odpi.onrender.com/ 

---

## 👨‍🏫 Autor

Proyecto desarrollado con fines educativos por **Maria Del Carmen Andrade Gallo**.

---

## 📄 Licencia: Este proyecto es de uso libre para fines educativos.