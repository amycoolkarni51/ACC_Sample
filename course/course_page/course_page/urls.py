"""course_page URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from course_page_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('course.html', views.coursepage, name="coursepage"),
    path('', views.coursepage, name="coursepage"),
    path('course.html',views.ourcourses, name="ourcourses"),

    path('frontend.html',views.frontend, name="frontend.html"),
    path('Html.html',views.html,name="Html.html"),
    path("css.html",views.css, name="css.html"),
    path("javascript.html",views.javascript, name="javascript.html"),
    path("angularjs.html",views.AngularJS, name="angularjs.html"),
    path("reactjs.html",views.ReactJS, name="reactjs.html"),
    path("jquery.html",views.jQuery, name="jquery.html"),

    path('backend.html',views.backend, name="backend.html"),
    path('python.html',views.python, name="python.html"),
    path('java.html',views.java, name="java.html"),
    path("cc++.html",views.cc,name="cc++.html"),
    path("kotlin.html",views.kotlin, name="kotlin.html"),
    path("scale.html",views.scale, name="scale.html"),
    path('php.html',views.php,name="php.html"),

    path('database.html',views.database, name="database"),
    path('oracle.html',views.oracle, name="oracle.html"),
    path('sql.html',views.sql, name='sql.html'),
    path('pssql.html',views.postgresql, name="pssql.html"),
    path('mangodb.html',views.mangodb, name="mangodb.html"),
    path('sqlite.html',views.sqlite, name="sqlite.html"),
    path('sqlserver.html',views.sqlserver, name="sqlserver.html"),

    path('marketing.html',views.marketing, name="marketing"),
    path('digital.html',views.digitalmark, name="digital.html"),
    path('social media.html',views.socialmediamark, name="social media.html"),
    path('content mark.html',views.contentmark, name="content mark.html"),
    path('direct mark.html',views.directmark, name="direct mark.html"),
    path('sales.html',views.salesmark, name="sales.html"),
    path('brand.html',views.brandmark, name="brand.html"),


]
