from django.urls import path
from web_app import views

urlpatterns = [
    path("", views.home, name="index"),
    path("view_people/", views.view_people, name="view_people"),
    path("create_person/", views.create_person, name="create_person"),
    path("edit_person/<person_id>", views.edit_person, name="edit_person"),
    path("delete_person/<person_id>", views.delete_person, name="delete_person"),
    
    path("view_companies/", views.view_companies, name="view_companies"),
    path("view_company/<company_id>/", views.view_company, name="view_company"),
    path("create_company/", views.create_company, name="create_company"),
    path("edit_company/<company_id>", views.edit_company, name="edit_company"),
    path("delete_company/<company_id>", views.delete_company, name="delete_company"),


]