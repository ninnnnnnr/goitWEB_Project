from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.ContactListView.as_view(), name='contacts'),
    re_path(r'^contact/(?P<pk>\d+)$', views.ContactDetailView.as_view(), name='contact-detail'),
    re_path(r'^add_contact/$', views.AddContact.as_view(), name='add_contact'),
    re_path(r'^contact/(?P<pk>\d+)/update/$', views.UpdateContact.as_view(), name='update_contact'),
    re_path(r'^contact/(?P<pk>\d+)/delete/$', views.DeleteContact.as_view(), name='delete_contact'),
    re_path(r'^search_results/$', views.SearchResultsView.as_view(), name='search_results'),
    re_path(r'^days_to_birthday_results/$', views.DaysToBirthdayResultsView.as_view(), name='days_to_birthday_results'),
]