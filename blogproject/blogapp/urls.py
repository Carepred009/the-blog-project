from email.policy import default
from os.path import basename

from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, LogoutView, ProfileViewSet

#for login,logout
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

#Create a router and register our viewset with it
router = DefaultRouter()

#use the posts to list all data
router.register(r'posts', PostViewSet, basename='post') #THe router generates the URLs

#use the /profiles/ access the url
router.register(r'profiles', ProfileViewSet, basename="profile")

urlpatterns = router.urls

# we will us this soon, if we dont use the viewset
urlpatterns = [
    #default url for localhost
    # API routes from ViewSets
    path('api/', include(router.urls)),

    #Use for Login,Logout
    #  path('api/login/', this is wrong!
    # # JWT Authentication
    path('api/token/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),  name='token_refresh' ),

    # JWT Logout
    path('api/logout/', LogoutView.as_view(), name="logout"),
]

'''

/auth/registration/

/auth/login/

/auth/logout/

/auth/password/reset/
'''