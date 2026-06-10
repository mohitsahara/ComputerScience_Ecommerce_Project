# TechMart 

A full-stack e-commerce web application for consumer electronics built with **Django 4.2** and **Bootstrap 5**.

> MSc Computer Science Project — University Assessment Submission by MOHIT KUMAR

---

## Live Site (PythonAnywhere)

| Page | URL |
|------|-----|
| Homepage | https://kumarmohit438.pythonanywhere.com/ |
| Admin Panel | https://kumarmohit438.pythonanywhere.com/admin/ |
| Products | https://kumarmohit438.pythonanywhere.com/products/ |
| Contact Us | https://kumarmohit438.pythonanywhere.com/contact/ |
| Help Centre | https://kumarmohit438.pythonanywhere.com/info/ |


---

## Live Demo Credentials

### Admin Panel
| URL | Username | Password |
|-----|----------|----------|
| `/admin/` | `admin` | `admin123` |

### Customer Accounts
| Username | Password |
|----------|----------|
| `alexander123` | `userabc12345` |
| `chris123` | `userabc54321` |
| `smith123` | `userpqr12345` |
| `amanda123` | `userxyz12345` |

### Discount Codes (enter in cart)
| Code | Discount |
|------|----------|
| `WELCOME20` | 20% off |
| `TECHMART10` | 10% off |
| `SAVE15` | 15% off |

---

## Features

- **User Authentication** — Register, login, logout with PBKDF2 password hashing
- **User Profiles** — Avatar, address, bio, order history
- **Product Catalogue** — 22 products across 5 categories (Smartphones, Smartwatches, Laptops, Tablets, Accessories)
- **Search & Filter** — Full-text search, category/brand/price filters, sort options
- **Shopping Cart** — Session-based cart, works without login
- **Coupon Codes** — Percentage discounts with expiry and usage limits
- **Order Management** — 6-stage order lifecycle with progress tracker
- **Product Reviews** — Star ratings with distribution chart
- **Wishlist** — Save products for later
- **Help Centre** — FAQ, Shipping Policy, and Returns on one page
- **Contact Page** — Enquiry form with subject categorisation
- **Admin Panel** — Full product, order, coupon, and user management

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.10, Django 4.2.7 |
| Database | SQLite 3 |
| Frontend | HTML5, CSS3, Bootstrap 5.3.2, Bootstrap Icons 1.11.3 |
| Forms | django-crispy-forms 2.1, crispy-bootstrap5 0.7, django-widget-tweaks 1.5.0 |
| Images | Pillow 10.1.0 |
| Fonts | Inter (Google Fonts) |

---

## Getting Started

### Prerequisites

- Python 3.10
- pip

### 1. Clone the Repository

```bash
git clone https://github.com/mohitsahara/techmart.git
cd techmart
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Apply Database Migrations

```bash
py -3.10 manage.py migrate
```

### 4. Populate Sample Data *(first time only)*

> ⚠️ Only run this on a **fresh database**. Skip this step if the database already has data — it will not delete existing orders or user accounts but will refresh product records.

```bash
py -3.10 manage.py populate_data
```

### 5. Start the Development Server

```bash
py -3.10 manage.py runserver
```

Visit **http://127.0.0.1:8000** in your browser.

---

## Already Set Up? Just Run the Server

If the database is already populated and you just want to start the project:

```bash
py -3.10 manage.py runserver
```

That's it. No need to re-run migrations or populate_data.

---

## Quick Setup (Automated)

Alternatively, run the provided batch script which handles everything automatically:

```bash
setup_and_run.bat
```

> Note: This runs `populate_data` every time, which refreshes product data. Use this only for a clean first-time setup.

---

## Project Structure

```
techmart_project/         ← Django project settings & main URLs
accounts/                 ← User registration, login, profiles
products/                 ← Product catalogue, search, reviews, wishlist
cart/                     ← Session-based shopping cart
orders/                   ← Checkout, coupons, order management
templates/
│   base.html             ← Site-wide layout (navbar, footer)
│   home.html             ← Homepage
│   accounts/             ← Auth & profile templates
│   products/             ← Product list, detail, wishlist
│   cart/                 ← Cart template
│   orders/               ← Checkout, confirmation, order history
│   pages/                ← Help centre, contact page
static/
│   css/style.css         ← Custom styles (~750 lines)
│   js/main.js            ← Custom JavaScript
requirements.txt
manage.py
```

---

## Key URLs

| Page | URL |
|------|-----|
| Homepage | `http://127.0.0.1:8000/` |
| All Products | `http://127.0.0.1:8000/products/` |
| Shopping Cart | `http://127.0.0.1:8000/cart/` |
| Checkout | `http://127.0.0.1:8000/orders/checkout/` |
| Order History | `http://127.0.0.1:8000/orders/history/` |
| Help Centre | `http://127.0.0.1:8000/info/` |
| Contact Us | `http://127.0.0.1:8000/contact/` |
| My Profile | `http://127.0.0.1:8000/accounts/profile/` |
| Admin Panel | `http://127.0.0.1:8000/admin/` |

---

## Security Features

- PBKDF2-HMAC-SHA256 password hashing (600,000 iterations)
- CSRF protection on all forms
- SQL injection prevention via Django ORM (no raw SQL)
- XSS prevention via Django template auto-escaping
- Session cookie HttpOnly and SameSite flags
- `@login_required` on all user-sensitive views

---

## Dependencies

Install all at once with:

```bash
pip install -r requirements.txt
```

| Package | Version | Purpose |
|---------|---------|---------|
| Django | 4.2.7 | Web framework |
| Pillow | 10.1.0 | Image handling |
| django-crispy-forms | 2.1 | Bootstrap form rendering |
| crispy-bootstrap5 | 0.7 | Bootstrap 5 form pack |
| django-widget-tweaks | 1.5.0 | Template-level form customisation |

---

## License

This project was developed for academic assessment purposes By Mohit Kumar.

---

*Built with Django & Bootstrap 5*
