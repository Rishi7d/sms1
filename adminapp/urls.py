from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.projecthomepage, name='projecthomepage'),
    path('printpagecall/',views.printpagecall, name='printpagecall'),
    path('printpagelogic/',views.printpagelogic, name='printpagelogic'),
    path('exceptionpagecall/', views.exceptionpagecall, name='exceptionpagecall'),
    path('exceptionpagelogic/', views.exceptionpagelogic, name='exceptionpagelogic'),
    path('randompagecall/', views.randompagecall, name='randompagecall'),
    path('randompagelogic/', views.randompagelogic, name='randompagelogic'),
    path('calculatorpagecall/', views.calculatorpagecall, name='calculatorpagecall'),
    path('calculatorpagelogic/', views.calculatorpagelogic, name='calculatorpagelogic'),
    path('datetimepagecall/', views.datetimepagecall, name='datetimepagecall'),
    path('datetimepagelogic/', views.datetimepagelogic, name='datetimepagelogic'),
    path('add_task/', views.add_task, name='add_task'),
    path('<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('UserRegisterPageCall/', views.UserRegisterPageCall, name='UserRegisterPageCall'),
    path('UserRegisterPageLogic/', views.UserRegisterPageLogic, name='UserRegisterPageLogic'),
    path('UserLoginPageCall/', views.UserLoginPageCall, name='UserLoginPageCall'),
    path('UserLoginPageLogic/', views.UserLoginPageLogic, name='UserLoginPageLogic'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('contact_list/', views.contact_list, name='contact_list'),
    path('add_contact/', views.add_contact, name='add_contact'),
    path('delete/<int:pk>/', views.delete_contact, name='delete_contact')

]