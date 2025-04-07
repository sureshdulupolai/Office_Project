from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePageFunction, name='home'),
    path('user-table/', views.tablePageFunction, name='table'),
    path('user-signup/', views.signUpPageFunction, name='signup'),
    path('user-login/', views.LoginPageFunction, name='login'),
    path('log-out/', views.logoutPageFunction, name='logout'),
    path('profile/<int:id>/<str:names>/<int:check>/', views.profilePageFunction ,name='profile'),
    path('edit-profile/', views.editProfilePageFunction, name='edit'),
    path('mail/', views.mailPageFunction, name='mail'),
    path('mail-send/', views.mailSendPageFunction, name='send'),
    path('mail-send/direct-profile/<str:obj>/', views.profileEmailPageFunction, name='profileEmail'),
    path('send-mail-to/', views.ownMailSendPageFunction, name='sendUs'),
    path('mail-open/<int:mail_id>/<int:Page_Check>/', views.MailOpenPageFunction, name='MailOpen'),
    path('message-mail/<str:obj>/<str:choice>/', views.DirectMessageFromMail, name='DirectMessage'),
    path('delete-message/<int:msg_id>/', views.DeleteMessagePageFunction, name='DeleteMessage'),
    path('save-mail/<int:mail_id>/', views.saveMailPageFunction, name='SaveMail'),
]