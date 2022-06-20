from django.contrib import admin
from django.db import router
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

#creating router obj
router=DefaultRouter()

router.register(r'student',views.StudentView, basename='student'),
  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('get-token/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),#for access token and refresh token 
    path('refresh-token/', TokenRefreshView.as_view(), name =' token_refresh'),
    path('verify-token/', TokenVerifyView.as_view(), name =' token_verify'),
]
'''{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU1NjEwMDE3LCJpYXQiOjE2NTU2MDk3MTcsImp0aSI6ImMyZjFhMmM5MjZhYTQ2ZmU4MzY4N2Q3YTExMzg1NThjIiwidXNlcl9pZCI6MX0.oAYXfRFwhDnhK3VIRxHQjIRuL1V4skpmzX0YAdZMamM",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1NTY5NjExNywiaWF0IjoxNjU1NjA5NzE3LCJqdGkiOiI1NzRmMTM5YzYzMDY0ZjdiOWE4YzNiZjBiOTM5MjdmMiIsInVzZXJfaWQiOjF9.9QI2MLy4eIQJmjnAt0LiCrUVSAVfYGzx48sQLYfNaJw"
}
'''