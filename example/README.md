Setup for project's contributors
--------------------------------

1. Create and enable virtualenv
    ```
    virtualenv venv -p python3
    source venv/bin/activate
    ```

2. Update requirements, install this package, apply migrations:
    ```
    pip install -r requirements.txt
    pip install -e ..
    python manage.py migrate
    ```

3. Run the project

    `python manage.py runserver 0:8000`

4. Visit the page:

    `http://127.0.0.1:8000`
