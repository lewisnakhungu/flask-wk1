#  Superheroes Flask API

A RESTful API built with Flask and SQLAlchemy that allows users to interact with a database of superheroes, their powers, and the strength of their abilities. This project is built for educational purposes and follows the structure of a typical Phase 4 code challenge.

## 🛠 Tech Stack

* Python 3
* Flask
* Flask SQLAlchemy
* Flask Migrate
* SQLite
* SQLAlchemy Serializer

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/superheroes-flask-api.git
cd superheroes-flask-api
```

### 2. Set Up the Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually install key packages:

```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate sqlalchemy_serializer
```

### 4. Run Database Migrations

```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

### 5. Seed the Database

```bash
python seed.py
```

### 6. Start the Server

```bash
python app.py
```

---

##  API Endpoints

### Heroes

* `GET /heroes`
  Returns a list of all heroes.

* `GET /heroes/<id>`
  Returns a hero by ID, including their powers.

* `DELETE /heroes/<id>`
  Deletes a hero.

* `PUT /heroes/<id>`
  Updates a hero's name or super name.

---

### Powers

* `GET /powers`
  Returns all powers.

* `GET /powers/<id>`
  Returns a single power.

* `PATCH /powers/<id>`
  Updates a power's description (must be ≥ 20 characters).

* `POST /powers`
  Creates a new power.

* `DELETE /powers/<id>`
  Deletes a power.

* `GET /powers/<id>/heroes`
  Returns all heroes that have a given power.

---

### Hero Powers

* `POST /hero_powers`
  Creates a new `HeroPower` link (with strength) between a hero and a power.

* `DELETE /hero_powers/<id>`
  Deletes a `HeroPower` entry.

---

## 🧪 Testing the API

You can use:

* [Postman](https://www.postman.com/)
* [curl](https://curl.se/)
* Any browser (for GET requests)

Example:

```bash
curl http://localhost:5000/heroes
```

---

## 📂 Project Structure

```
.
├── app.py
├── models.py
├── routes.py
├── seed.py
├── migrations/
├── app.db
└── requirements.txt
```

---

## 🧠 Learning Objectives

* Create and relate models using SQLAlchemy
* Build RESTful routes with Flask
* Use serialization to control JSON output
* Validate model data
* Handle errors with appropriate status codes

---

## 📄 License

MIT License. See `LICENSE.md` for details.

---

##
