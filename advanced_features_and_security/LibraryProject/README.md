# LibraryProject

This Django project demonstrates advanced features and security practices, including:

- Custom user model (`CustomUser`) with extended fields
- Book management with custom permissions (`can_create`, `can_delete`)
- Permission-protected views for listing books

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Apply migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

3. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

4. Run the development server:
   ```
   python manage.py runserver
   ```

## Features

- Custom user authentication
- Permission-based access control
- Book listing view (`book_list`) protected by `can_create` permission

## Security Notes

- Change the `SECRET_KEY` before deploying to production.
- Set `DEBUG = False` and configure `ALLOWED_HOSTS` for production.

##