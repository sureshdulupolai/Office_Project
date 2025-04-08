from django.urls import path
from . import views

urlpatterns = [
    # Home / Auth
    path('', views.homePageFunction, name='home'),
    path('user-login/', views.LoginPageFunction, name='login'),
    path('user-signup/', views.signUpPageFunction, name='signup'),
    path('log-out/', views.logoutPageFunction, name='logout'),

    # Mailbox (Most Used)
    path('mail/', views.mailPageFunction, name='mail'),
    path('mail-send/', views.mailSendPageFunction, name='send'),
    path('send-mail-to/', views.ownMailSendPageFunction, name='sendUs'),
    path('mail-open/<int:mail_id>/<int:Page_Check>/', views.MailOpenPageFunction, name='MailOpen'),
    path('save-mail/', views.saveMailPageFunction, name='SaveMail'),
    path('sucessfull-saved/<int:mail_id>/', views.successfullSaveMailPageFunction, name='successfullSaveMail'),

    # Profile & User
    path('profile/<int:id>/<str:names>/<int:check>/', views.profilePageFunction, name='profile'),
    path('edit-profile/', views.editProfilePageFunction, name='edit'),
    path('user-table/', views.tablePageFunction, name='table'),

    # Direct Communication
    path('mail-send/direct-profile/<str:obj>/', views.profileEmailPageFunction, name='profileEmail'),
    path('message-mail/<str:obj>/<str:choice>/', views.DirectMessageFromMail, name='DirectMessage'),
    path('delete-message/<int:msg_id>/<int:Page>/', views.DeleteMessagePageFunction, name='DeleteMessage'),
]
