Antud paigaldusjuhendis kasutame Python3 ja Visual Studio Code rakendust.


<b>PAIGALDUSJUHEND</b>
1. Kopeeri projekt

```git clone https://github.com/aaavas/test_work.git```


2. Loo virtuaalne keskkond, aktiveeri see ja installi vaja minevad sõltuvused

```python -m venv .venv```

```.venv\Scripts\Activate.ps1```

```(.venv) > pip install -r requirements.txt```
	
virtuaalses keskkonnast väljumiseks on käsklus

```(.venv) > deactivate```
	
2.1 Kui on probleeme andmebaasi migratsioonidega, siis tuleb ära kustutada ```pages/migrations``` kaustast kõik peale ```__pycache__``` ja ```__init__.py``` failide. Lisaks tuleb kustutada ka ```db.sqlite3```
Seejärel laadida ```(.venv) > python manage.py makemigrations``` käsuga migratsioonid ja ```(.venv) > python manage.py migrate``` käsuga migreerida. 
Andmebaasi andmete laadimiseks kasutada käsku ```(.venv) > python manage.py loaddata data_fixture.json```

3. Käivita lokaalne server

```python manage.py runserver```
	
Seejärel mine lehele ```http://127.0.0.1:8000/```, et rakendust kasutada


Serverist väljumiseks kasutada klahvikombinatsiooni CTRL + C


4. Admin vaate avamiseks tuleb luua superuser õigustega kasutaja virtuaalkeskkonnas...

```python manage.py createsuperuser```

...käivitada server...

```python manage.py runserver```

...ja minna veebilehele...

```http://127.0.0.1:8000/admin/```

