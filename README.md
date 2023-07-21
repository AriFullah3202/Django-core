* [what is Django](#what-is-django)
   * [why Django](#why-django)
   * [how to works](#how-to-works-django)
   * [what is MVT](#why-is-mvt)
   * [difference between MVT vs MVC](#difference-between-mvt-vs-mvc)
* [Extention for Django](#extention-for-django)
* [Install Django](#install-django)
  * [install django globally](#django-install-globally)
  * [install django virtually](#django-install-virtually)
* [Create Django project](#create-django-project-create)
* [explain folder structure and how it work](#project-structure-explain)
* [install python virtually](#django-install-virtually)
* [interpreter setup](#interpreter-setup)


## what is Django
**Django is a web application framework written in Python programming language. Django helps eliminate repetitive tasks making the development process an easy and time saving experience.**


## why Django
* uilt With Python So Easy to Learn
* Cross-Platform
**এটি windows , linux , mac কাজ করে , মানে এখন আমরা windows এ run করর কিছুদিন পর linux , mac রান করাতো পারব**
* Open Source and Huge Community Support
* Security
* Good Documentation

## how to works django
**Django is based on MVT architecture. MVT is a software design pattern for developing a web application.**
**Django MVT pattern ডিজাইন প্যার্টান ফলো করে । মানে Model View Templete**

## why is MVT
**MVT web applicattion জন্য হল সফটওয়ার ডিজাইন প্যাটান ।**
##### MVT হল Model View Templete
* Model
  manuplate data , maintain data এবং database handle করার জন্য মডেল ব্যবহার করা হয় ।
* view 
  যখন user রিকোয়েস্ট করে তখন এখানে আসে এবং return response
* Template 
  একটা website এর ডিজাইন গুলো এই টেম্পে্লেটে ব্যবহার করা হয় ।
## here is diagram
![Alt text](Screenshot%202023-07-21%20123318.png)

## difference between MVT VS MVC
![PICTURE](Screenshot%202023-07-21%20123924.png)
![PICTURE](Screenshot%202023-07-21%20125518.png)




## Extention for Django
আপনি আপনার vscode গিয়ে extention icon ক্লিক করুন । নিচের নাম search করে install দিতে হবে ।

* Auto Rename Tag
* Django
* Pyhton
* SQLite Viewer
* Prettier code formetter
## Install Django 
ইনস্টল দুইভাবে করা যায় ।
1. Globally
2. Virtual envirionment 
নিচে দুইভাবে দেখানো হবে । 
## Django Install Globally
1. windows এ run as Administrator দিয়ে cmd চালু করতে হবে । 
2. প্রথমে python install আছে কিনা চেক করতে হবে । 
চেক করার নিয়ম --- 
```bash
python --version
```
3. python যদি থাকে , তারপর django আছে কিনা চেক করতে হবে । 
শুধু python থাকলে হবে না , Environment path বলে দিতে হবে । 
 
```bash
django-admin --version
```
'django-admin' is not recognized তার মানে বুঝতে হবে , আমাদের django ইনস্টল নেই ।

এবার Globally install করার পালা 

```bash
pip install Django
pip uninstall Django
```
install করার পর চেক করুন 
```bash
django-admin --version
```
ইনস্টল হয়ে গেলে version show করবে ।
## Create Django project create
#### একটা project অনেক app রাখা যায় । এজন্য আমরা প্রথমে project তারপর এর ভিতর অনেক app বানাব ।
এখন আপনি কোন drive এ প্রজেক্ট করতে চান
সে drive গিয়ে প্রজেক্ট করতে হবে ।

command prompt গিয়ে D drive যেতে চাইলে 

d:

ফোল্ডার তৈরি করতে 

mkdir arifullah

ফোল্ডার create হয়ে গেলে , 
এবার dango project করার পালা ।

```bash
django-admin startproject studymart
```
এখন studymart নামে outer folder এবং inner folder studymart এবং manage.py create হবে ।

inner folder এর ভিতরে পাচটা ফাইল create হবে ।

##### মনে রাখতে হবে , inner folder এর ভিতরে গিয়ে  নিচের কমান্ড দিতে হবে ।
### না হয় ইরর দিবে ।

#### এখন app ক্রিয়েট করব 
```bash
python manage.py startapp courses
```
#### এখন আরো কয়েকটি ফাইল ক্রিয়েট হবে ।

```bash
python manage.py runserver
```
এখন http://127.0.0.1:8000/ এটা browser run করতে হবে ।

### এখন কথা হল কিভাবে vscode open করতে হবে । 
উপরে যে ফোল্ডার create কবলাম ওইটা right click করে vs code open করতে হবে ।

## Explain Folder Structur
এখন আমরা কোন কোন ফাইল কি কি কাজ করে এটা দেখব 
##### আমরা প্রথমে inner project এর ভিতরে কি আছে এবং কোনটার কাজ কি এটা দেখব 
 
প্রথমে setting.py এ যেতে হবে । 

এর ভিতরে installed_app নামে একটা লিস্ট আছে , ওটাতে যে courses নামে app create করলাম  , 

ওটা connect করতে হবে । 

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'courses'
]
```
### আমরা এখন utils.py এর মধ্য কি আছে এটা দেখব । 
###### এখানে url connect করা লাগবে ।
###### প্রথমে url গুলো views.py এ যাবে । এখন views.py create করতে , একটা এপ ক্রিয়েট করতে হবে ।
###### তারপর utils.py এ import করতে হবে । 
###### course এ views.py আছে ্

এখটা নতুন function create করলাম cuuses নামে ।
* studyMart
  * courses
    * 
  * studyMart
    * utils.py
    * setting.py
```python
# eta course application er vitore views.py
# views.py
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def courses (request) :
    return HttpResponse("welcome to dajngo")
```
এই ফাংশন ui তে দেখাতে হলে কানেক্ট করতে হবে  । 

কার সাথে কানেক্ট করবো ? views.py কে utils.py এর সাথে ।
* studyMart 
   * studyMart
   * * utils.py

```python
from django.contrib import admin
from django.urls import path
from courses import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.courses)
]
``` 
### now run

```bash
python manage.py runserver
```
এখন print করবে -> welcome to django 


## project structure explain
* studyMart --- এটা outer প্রজেক্ট
  * course  --- এটা application এর ভিতরে অনেক file আছে 
    * -pycache --- এটা cache
    * migration --- এটা পরে দেখব
    * _init_py --- এটা python package
    * admin.py --- আমরা যে model ক্রিয়েট করব । সেটা এখানে রেজিস্টার করব । এটা ডাটাবেজ এ শো হবে ।
    * apps.py  --- এখানে app কে configure করা হয় ।
    * models.py --- আমাদের ডাটাবেজ রিলেটেড কাজ করব । orm রিলেটেড কাজ করব
    * tests.py --- এটা unit test
    * veiws.py  --- এখানে আউটপুটা দেখতে পাই । এটা আমরা connect করছি inner project এ urls.py এর সাথে ।
    পরে আমরা প্রতেকটা application এ আমরা একটা একটা urls.py লিখব  । 
  * studyMart ---- এটা inner প্রজেক্ট
    * _pycache ---- এটা project cache . এটা সার্ভার রান করলে 
    * -init_py --- এটা python প্যাকেজ 
    * asgi.py  --- 
    * setting.py  --- এখানে applicaion কে connect করবো
    * urls.py  --- application এর মধ্যে views থাকে ওটাকে কল দিবো , সাথে path ta বলে দিতে হয় ।
    * wsgi.py  --- web server host করতে কাজে লাগে ।
    * dbsqlite3 --- ডাটাবেজে আমরা কি করছি , এটা আমরা দেখতে পারব
  * manage.py  --- এটা ব্যবহার করে আমরা সার্ভার রান করতেছি
  * Readme.md
 
## Django install virtually
**আগে Django golbally আনইনস্টল করতে হবে । ** `pip uninstall Django` তারপর `terminal` এ `cd ..` দিয়ে এক `folder` পেছনে গিয়ে যেতে হবে 

**তারপর নিচের কমান্ডটা দিতে হবে**
**একটা `env`ইনস্টল হয়ে যাবে ।**
**তারপর ওই folder ‌`Scripts` ফোল্ডারে যেতে হবে ।**
**`env`কে active করতে হবে ।**
**`dir` দিলে দেখা যাবে এখানে `./activate` নামে folder আছে  ওটা `./activate` কমান্ড দিতে হবে । তারপর Django install দিতে হবে**

```bash
python -m venv env
cd env/Scripts
./activate ## output will be --- (env) PS H:\Project\Python\first-django\env\Scripts>
pip install Djangowh
```
```bash
cd ..
cd ..
cd studymart
python manage.py runserver
```
## interpreter setup 
[this is document for interpreter setup](https://www.alphr.com/vs-code-change-python-interpreter/)







