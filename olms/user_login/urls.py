from django.conf.urls import url
from . import views,registration

urlpatterns = [
    url(r'^login/',views.user_login.as_view(),name='login'),
    url(r'^register/',registration.register,name='register')
]
