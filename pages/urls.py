from django.urls import path
from . import views
from .views import return_book
from django.conf.urls import handler404
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('error_404', views.error_404, name='404_error'),
    path('add_book', views.add_book, name='add_book'),
    path('admin_book_details/<int:book_id>/', views.admin_book_details, name='admin_book_details'),
    path('admin_profile', views.admin_profile, name='admin_profile'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('edit-book/<int:book_id>/', views.edit_book, name='edit_book'), 
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('library_search', views.library_search, name='library_search'),
    path('login', views.login, name='login'),
    path('logout_confirmation', views.logout_confirmation, name='logout_confirmation'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('user_book_details/<int:user_id>/<int:book_id>/', views.user_book_details, name='user_book_details'),
    path('user_borrowed_books/<int:user_id>/', views.user_borrowed_books, name='user_borrowed_books'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('view_books', views.view_books, name='view_books'),
    path('logout', views.logout, name='logout'),
    path('return_book/', return_book, name='return_book'),
]

