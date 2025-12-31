# ammar-eid / django-projects

this repository includes a few Django projects with simple ideas while i learning django
i have learnt this projects from https://www.geeksforgeeks.org/python/django-projects/

Languages: Python (71.4%), HTML (28.6%)

Table of contents
- About
- Projects
- Features
- Requirements
- Quick start
- Per-project notes
- Running tests
- Docker (optional)
- Contributing
- License
- Contact

About
This repository contains small Django projects and examples intended as learning references and quick starters. Each project demonstrates common Django concepts such as models, views, templates, forms, authentication, CRUD operations, and REST APIs.

Projects
The repository contains the following project directories. Edit the descriptions below if you prefer more detail.

- Weather App / weatherApp — simple weather lookup/demo project
- blog — blog application example (posts, comments)
- blogsite — site template or alternate blog example
- core — shared utilities or a core Django app used by examples
- django course — exercises and examples from a Django course
- djangochat — chat/demo application
- drfproj — Django REST Framework API examples
- imageGallery — image upload and gallery demo
- impactList_site — small site / list-management demo

Features (common)
- User registration, login, logout (where implemented)
- Create / Read / Update / Delete resources
- Templates and responsive HTML
- REST API examples in drfproj
- Simple file/image upload demo in imageGallery
- SQLite by default for easy local setup (projects may support Postgres)

Requirements
- Python 3.8+ (adjust if your projects use a different version)
- Django 3.2+ or 4.x (adjust to the versions used in each project)
- pip and virtualenv/venv recommended
- Optional: Postgres, Redis, Channels, or other dependencies depending on the project

Quick start (local development)
1. Clone the repo
   git clone https://github.com/ammar-eid/django-projects.git

2. Install dependencies
   - pip install django
   - pip install Pillow
   - pip install django-crispy-forms
     
3. Apply migrations and create a superuser
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
6. Run the development server
   python manage.py runserver
   Visit http://127.0.0.1:8000

Per-project notes
- Each project is self-contained in its folder. To work on a specific project:
  cd <project-folder>
  (activate your venv)
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
- If a project uses external services (OpenWeather API, cloud storage, channels), set the required keys/URLs in the environment.

Running tests
- From a project folder run:
  python manage.py test

Contributing
Contributions are welcome.
- Fork the repo
- Create a feature branch
- Open a pull request with a clear description
- Follow PEP8 and add tests for new functionality

Contact
- GitHub: https://github.com/ammar-eid
- Email: ammarelabsawy123@gmail.com

Screenshots / Demos
- Add screenshots or links to live demos per project if you have them.
