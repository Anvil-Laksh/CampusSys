"""djcrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from webapp.views import staffView, staffStudentOps, staffParentOps
from webapp.views.staffView import StaffCreateView
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here

urlpatterns = [
    path(r'staffCreate/', StaffCreateView.as_view()),
    #     path(r'staffUpdate/<int:pk>', staffView.StaffUpdate.as_view()),
    #     path(r'newStudent/', staffStudentOps.CreateStudent.as_view()),
    #     path(r'editStudent/', staffStudentOps.AlterDelStudent.as_view()),
    #     path(r'addParent/', staffParentOps.CreateParent.as_view()),
    #     path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here

]
