How to install
Download repo,
Initialize virtual environment in it: python -m venv env,
Run that venv: source env/bin/activate,
Install dependencies: pip install -r requirements.txt,
Install frontend dependencies: npm install
Compile frontend assets: npm run dev,
(optional) Change database settings in settings.py if you want to use different (non-sqlite) db backend,
Migrate database: python manage.py migrate,
To run dev server: python manage.py runserver