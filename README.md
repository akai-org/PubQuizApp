# PubQuizApp

## How to install
1. Download repo, 
2. Initialize virtual environment in it: `python -m venv env`,
3. Run that venv: `source env/bin/activate`,
4. Install dependencies: `pip install -r requirements.txt`,
5. Install frontend dependencies: `npm install`
6. Compile frontend assets: `npm run dev`,
7. (optional) Change database settings in settings.py if you want to use different (non-sqlite) db backend, 
8. Migrate database: `python manage.py migrate`,
9. To run dev server: `python manage.py runserver`

## Tips for devs

### Dumping pip installations into the file
If you installed new pip dependency you need to allow others to know about it. To do so it is best to save all requirements
in one file, which in this case in named `requirements.txt`. You can do this by typing following command: 

`pip freeze > requirements.txt`
