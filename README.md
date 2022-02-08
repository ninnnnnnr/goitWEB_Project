# goitWEB_Project
WEB project on course GoIT

CONTENTS
---------------------

 * Introduction
 * Requirements
 * Installation
 * Configuration
 * Troubleshooting
 * FAQ
 * Maintainers

INTRODUCTION
------------

The goitWEB  is a tool with handy features, including the ability 
to make contacts, notes, and lists and search for specific information.


REQUIREMENTS
------------

This module requires the following modules:

 * [Python](https://www.python.org/)

  
 * asgiref==3.5.0
 * backports.zoneinfo==0.2.1
 * certifi==2021.10.8
 * charset-normalizer==2.0.11
 * Django==4.0.1
 * django-crispy-forms==1.14.0
 * django-environ==0.8.1
 * django-filter==21.1
 * idna==3.3
 * psycopg2==2.9.3
 * requests==2.27.1
 * sqlparse==0.4.2
 * tzdata==2021.5
 * urllib3==1.26.8

INSTALLATION
------------

 * Install as you would normally install a contributed Python module. Visit
   https://www.python.org/ for further information. 
```js
 cd personal_assistance
 docker-compose up -d
 docker-compose exec web python manage.py makemigrations --noinput
 docker-compose exec web python manage.py migrate --noinput
```
 * For start app in web browser http://127.0.0.1:8000/


 * You can install the Prerequisites by running the command:
```js
 pip install -r requirements.txt
```

USAGE
-------------
###[Create new account:](http://127.0.0.1:8000/notes/register/)

![img.png](https://github.com/Kantarian/goit-python/blob/main/img/img.png?raw=true)

###Add a contact:
On web-page, open the [Address book](http://127.0.0.1:8000/adress_book/).
At the upper right, tap [Add contact](http://127.0.0.1:8000/adress_book/add_contact/).

![img_3.png](https://github.com/Kantarian/goit-python/blob/main/img/img_3.png?raw=true)

Enter the contact's name, address, phone number, email and birthday. 
When you're finished, tap Submit.

![img_5.png](https://github.com/Kantarian/goit-python/blob/main/img/img_5.png?raw=true)

###Add a Note:
On web-page, open the [Notes](http://127.0.0.1:8000/notes/).
At the upper right, tap [Create a new note](http://127.0.0.1:8000/notes/create/).

![img_6.png](https://github.com/Kantarian/goit-python/blob/main/img/img_6.png?raw=true)

Enter the titel's name, text, and tags. 
When you're finished, tap Submit.

![img_7.png](https://github.com/Kantarian/goit-python/blob/main/img/img_7.png?raw=true)

###Upload file:
On web-page, open the [File manager](http://127.0.0.1:8000/file_manager/).

Enter the File's name, type of file, and comment. Choose file for upload.
When you're finished, tap Upload file.

![img_8.png](https://github.com/Kantarian/goit-python/blob/main/img/img_8.png?raw=true)

CONFIGURATION
-------------

The module has no menu or modifiable settings. There is no configuration. When
enabled, the module will prevent the links from appearing. To get the links
back, disable the module and clear caches.


TROUBLESHOOTING
---------------

---


FAQ
---

-----------

MAINTAINERS
-----------

Current maintainers:
 * [Nikita Nozhenko](mailto:nikitanozhenko@gmail.com) (Team lead)
 * [Oleksandr UTCHENKO](mailto:utenku@gmail.com) (Developer) 
 * [Борис Денисенко](mailto:borysman3@gmail.com) (Developer) 
 * [Yehor Horbatko](mailto:dog380973292312@gmail.com) (Scrum master) 





