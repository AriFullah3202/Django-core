* [Extention for Django](#extention-for-django)
* [Install Django](#install-django)
* [Create Django project](#create-django-project-create)
* []

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
now run

```bash
python manage.py runserver
```
এখন print করবে -> welcome to django 








 




