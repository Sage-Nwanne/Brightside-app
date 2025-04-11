from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('entries/', views.entries, name='entries'),
    path('entries/<int:entry_id>/', views.entries_detail, name='entry-detail'),
    path('entries/create/', views.EntriesCreate.as_view(), name='entries-create'),
    path('entries/<int:pk>/update/', views.EntriesUpdate.as_view(), name='entry-update'),
    path('entries/<int:pk>/delete/', views.EntriesDelete.as_view(), name='entry-delete'),
    path('entries/<int:entry_id>/archive/', views.archive_entry, name='entry-archive'),
    path('entries/<int:entry_id>/comment/', views.add_comment, name='add-comment'),
]
