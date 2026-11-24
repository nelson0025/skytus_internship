
from django.urls import path
from . import views

urlpatterns = [
    path('', views.myapp, name='myapp'),
    path('student/<int:id>/',views.student_detail,name="student_detail"),
    path ('student/',views.student_report,name="student_report"),
    path ('red/',views.student_calculation,name="student_calculation"),
    path ('book/',views.book_detail,name="book_detail"),
    path ('bo_ok/',views.book_list_view.as_view(),name="book_l"),
    path('add_book/',views.add_book.as_view(),name="book_add"),
    path('books/', views.book_list_view.as_view(), name='book_list'),
    path('home/',views.home,name="homes"),
    path('about/',views.about,name="abouts"),
    path('contact/',views.contact,name="contact"),
    path('item/',views.item_list,name="item"),
    path('dashboard/',views.dashboard,name="dashboard"),

]
