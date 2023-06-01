"""firstproj URL Configuration

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
from django.urls import path, include

from myapp.views import hello, hello1, hello2, students, free
from students.views import listone, listall, post, post1, postform, delete, edit
from CookieSessionApp import views as csviews
#                                      別名

from flower import views as fviews
from intro import views as iviews
from product import views as pviews
#sfrom contact import views as conviews

from news import views as nviews
from boardapp import views as bviews

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', hello),
  path('hello1/', hello),
  path('hello1/<str:username>', hello1),
  path('hello2/<str:username>', hello2),
  path('stds/', students),
  path('listone/', listone),
  path('listall/', listall),
  path('/post/', post),
  path('post1/', post1),
  path('postform/', postform),
  path('delete/<str:stdID>/', delete),
  path('edit/<str:stdID>/', edit),
  path('edit/<str:stdID>/edit/', edit),
  path('free/', free),

  # cookies
  path('set_cookie/<str:key>/<str:value>/', csviews.set_cookie),
  path('set_cookie2/<str:key>/<str:value>/', csviews.set_cookie2),
  path('get_cookie/<str:key>/', csviews.get_cookie),
  path('get_allcookies/', csviews.get_allcookies),
  path('delete_cookie/<str:key>/', csviews.delete_cookie),
  path('pagecount/', csviews.pagecount),
  # sessions
  path('set_session/<str:key>/<str:value>/', csviews.set_session),
  path('get_session/<str:key>/', csviews.get_session),
  path('get_allsessions/', csviews.get_allsessions),
  # vote
  path('vote/', csviews.vote),
  path('set_session2/<str:key>/<str:value>/', csviews.set_session2),
  path('delete_session/<str:key>/', csviews.delete_session),
  # login
  path('login/', csviews.login),
  path('logout/', csviews.logout),
  path('mypage/', csviews.mypage),
  #path('adduser/', csviews.adduser),
  path('register/', csviews.register),

  # news
  path('newsindex/', nviews.index),
  path('newsindex/<str:pageindex>/', nviews.index),
  path('newsdetail/<int:detailid>/', nviews.detail),
  path('newslogin/', nviews.login),
  path('newslogout/', nviews.logout),
  path('newsadminmain/', nviews.adminmain),
  path('newsadminmain/<str:pageindex>/', nviews.adminmain),
  path('newsadd/', nviews.newsadd),
  path('newsedit/<int:newsid>/', nviews.newsedit),
  path('newsedit/<int:newsid>/<str:edittype>/', nviews.newsedit),
  path('newsdelete/<int:newsid>/', nviews.newsdelete),
  path('newsdelete/<int:newsid>/<str:deletetype>/', nviews.newsdelete),

  #post
  path('showpost/', bviews.showpost),
  path('showpost/<str:pageindex>/', bviews.showpost),
  path('addpost/', bviews.addpost),
  path('captcha/', include('captcha.urls')),

  # allauth
  path('accounts/', include('allauth.urls')),

  # contact
  #path('contact/', conviews.contact),
  #path('contact/create/', conviews.create, name='create'),
  #path('contact/edit/<int:pk>/', conviews.edit, name='edit'),
  #path('contact/delete/<int:pk>/', conviews.delete, name='delete'),
  #path('contact/<slug:slug>/', conviews.detail, name='detail'),

  # flower(放最後面)
  path('flower/', fviews.flowers),
  path('flower/create/', fviews.create, name='create'),
  path('flower/edit/<int:pk>/', fviews.edit, name='edit'),
  path('flower/delete/<int:pk>/', fviews.delete, name='delete'),
  path('flower/<slug:slug>/', fviews.detail, name='detail'),

  # intro
  path('intro/', iviews.intro),
  path('intro/create/', iviews.create, name='create'),
  path('intro/edit/<int:pk>/', iviews.edit, name='edit'),
  path('intro/delete/<int:pk>/', iviews.delete, name='delete'),
  path('intro/<slug:slug>/', iviews.detail, name='detail'),

  # product
  path('product/', pviews.product),
  path('product/create/', pviews.create, name='create'),
  path('product/edit/<int:pk>/', pviews.edit, name='edit'),
  path('product/delete/<int:pk>/', pviews.delete, name='delete'),
  path('product/<slug:slug>/', pviews.detail, name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
