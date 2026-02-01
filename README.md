# IMDB Clone – Django REST Framework

A backend API for an IMDB-like application built using **Django** and **Django REST Framework (DRF)**.

This project is created while following the tutorial and reference repository:
https://github.com/ShubhamSarda/IMDB-Clone-DRF

The goal of this repository is **learning Django REST Framework and backend API development**.

---

## Tech Stack

- Python
- Django
- Django REST Framework (DRF)
- SQLite (development)
- Git & GitHub

---

## Project Setup (Step-by-Step)

### Clone the repository
```bash
git clone <your-github-repo-url>
cd <project-folder>
```

### Create & activate virtual environment
bash
Copy code
python -m venv venv
source venv/bin/activate        # macOS / Linux
# venv\Scripts\activate         # Windows
```

### Install dependencies
bash
Copy code
pip install -r requirements.txt
```

### Apply database migrations
bash
Copy code
python manage.py migrate
```

### Create superuser (optional)
bash
Copy code
python manage.py createsuperuser
```

### Run the development server
bash
Copy code
python manage.py runserver
```

Open in browser:
cpp
Copy code
http://127.0.0.1:8000/
```
### Author
Kunal Garg

Feel free to ⭐ the repo if you find it useful!