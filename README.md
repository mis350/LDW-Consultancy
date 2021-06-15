
# Developing Django on Repl.it

- Fork this template to get started
- Simply hit run to start the server
- The server will autoreload as needed. You don't need to restart the server manually.

## Add your first view

1. Create a file under `mysite` named `views.py` with the following contents:

```
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.")
```

2. Add a url pattern under `mysite/urls.py`. It should look like this:

```
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]
```

## Shell

Django utilizes the shell for managing your site. For this click on the `?` in the lower-right corner and click "Workspace shortcuts" from there you can open a new shell pane. 

## Database

By default this template utilizes the sqlite database engine. While this is fine for development it won't work with external users of your app as we don't persist changes to files when they happen outside the development environment. 

We suggest bringing a database using an outside service. 

See Django documentation on how to setup a database: https://docs.djangoproject.com/en/3.0/intro/tutorial02/

based on  amasad/django-template

### Project name: LDW Consultancy
### Group members:
#### 1) Lama AlAjmi 2191115521
#### 2) Dalal ALAjmi 2191112346 (project manager)
#### 3) Abdulwahab Mohammed 2152140715

![WhatsApp Image 2021-06-14 at 11 14 55 PM](https://user-images.githubusercontent.com/82085905/122129710-8c7e0100-ce47-11eb-8c93-db1bc71e2a35.jpeg)

[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=427146&assignment_repo_type=GroupAssignmentRepo)

## Project Requirements:
- Includes models for books, book copies, genre, language, authors, and users. (6 models)
- Users can view, list, and detail information for books and authors. 
- Admin users can create and manage the models.
(view for users 1)
- Users can reserve available books to check out. (views for users 2)
- Librarians and employees(admin) can renew reserved books.
(view for users 3)
- Homepage with the main objects of the library can be viewed.(view to list data 1)
- Create a view to list of all the books available.
- Show a view of the list of authors.
- Create a detailed view for each book.
- Create a detailed view for each author.
- Allow users to leave comments or book reviews under book titles. 
- Allow users to leave comments or reviews under author names.
- Include page of genres available in the library.
- Show the number of available copies of books.
- Show a view page of the number of times the website has been visited. 
