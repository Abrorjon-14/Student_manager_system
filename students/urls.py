from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import student_form, student_list, student_edit, student_delete

urlpatterns = [
    path('', student_form, name='student_form'),
    path('list/', student_list, name='student_list'),
    path('student/<int:pk>/edit/', student_edit, name='student_edit'),
    path('student/<int:pk>/delete/', student_delete, name='student_delete')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)