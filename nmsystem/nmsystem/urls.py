"""nmsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from dashboard.views import home_view, categories_view, \
    updatecategories_view, \
    editcategories_view, \
    deletecategories_view, \
    poroducts_view, \
    editproduct_view, \
    updateproduct_view, \
    deleteproducts_view, \
    bundle_view, \
    register_view, \
    login_view, \
    logout_view, \
    accountsettings_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('categories/', categories_view, name='categories'),
    path('updatecategories/<int:pk>/', updatecategories_view, name='updatecategories'),
    path('editcategories/', editcategories_view, name='editcategories'),
    path('deletecategories/<int:pk>/', deletecategories_view, name='deletecategories'),
    path('products/', poroducts_view, name='products'),
    path('editproducts/', editproduct_view, name='editproducts'),
    path('updateproducts/<int:pk>/', updateproduct_view, name='updateproducts'),
    path('deleteproducts/<int:pk>/', deleteproducts_view, name='deleteproducts'),
    path('bundle/<int:pk>/', bundle_view, name='bundle'),
    path('registration/', register_view, name='registration'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('account/', accountsettings_view, name='account'),
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
         name="password_reset_complete"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
