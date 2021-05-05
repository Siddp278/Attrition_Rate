from django.urls import path
from django.conf.urls.static import static
from .views import homepage, loginpage, ask_ques, logout_, resu, upload_file, homing
from django.conf import settings

urlpatterns = [
    path('', homepage, name='homepage'),
    path('login_page/', loginpage, name='login_page'),
    path('form_page/', ask_ques, name='ask_page'),
    path('logout_page/', logout_, name='logout_page'),
    path('result/', resu, name='results'),
    path('uploads/', upload_file, name='attrition_file'),
    path('home/', homing, name='home_page')
    ]

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)