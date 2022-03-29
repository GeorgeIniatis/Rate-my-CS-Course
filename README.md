# Rate My CS Course

The aim of our application is to give new and current students a place to comment, rate and thus help each other choose their computing science courses.

## Running Server Locally

First clone the repository

`$ git clone https://github.com/GeorgeIniatis/Rate-my-CS-Course.git`

Install Dependencies e.g. on Virtual Machine/Server running **Python 3.7**

`$ pip install -r requirements.txt`

When you have the required Dependencies for the environment you can then create the database

`$ python manage.py makemigrations csapp`

`$ python manage.py migrate`

To populate the database with some test data you can use the following (This step can be skipped)

`$ python populate_csapp.py`

Finally run the server

`$ python manage.py runserver`

## Built With

* [Bootstrap](https://getbootstrap.com/) - Extensive list of components and Bundled JavaScript plugins
* [Starfield](https://pypi.org/project/django-starfield/) - Simple widget rendering so-called rating stars as input for an integer field
* [Fontawesome](https://fontawesome.com/) - Use of icons

## Team

* **George Iniatis** 
* **Martina Bilyanska** 
* **Thanh Hieu Nguyen**
* **Stefanos Charalambous** 


## Acknowledgements

* [Zach Reed - Codepen](https://codepen.io/Bluetidepro/pen/GkpEa) - Idea how to display star ratings
* [Vitor Freitas](https://simpleisbetterthancomplex.com/tutorial/2018/01/29/how-to-implement-dependent-or-chained-dropdown-list-with-django.html) - How to implement dependent drop-down lists
* [Vitor Freitas](https://simpleisbetterthancomplex.com/tutorial/2016/07/27/how-to-return-json-encoded-response.html) - How to return JSON responses
* [Drew Ryan](https://www.youtube.com/watch?v=9cKsq14Kfsw) - Responsive Bootstrap Website Tutorial + Idea how the homepage and the navigation bar to look
* [University of Glasgow - Course Catalogue](https://www.gla.ac.uk/coursecatalogue/courselist/?code=REG30200000&name=School+of+Computing+Science) - Used for populating the database with courses
* [University of Glasgow - Open Days Registration Form](https://app.geckoform.com/public/#/modern/FOEU03e6aQmrJHvp) - Linked to from the Open Days page of the application

