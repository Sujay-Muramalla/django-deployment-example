from django.conf.urls import url
from password_app import views


#template_urls
app_name = 'password_app'

urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]
