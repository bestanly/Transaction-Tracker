"""django_transaction_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from transactions.views import transactions_view, transaction_delete, transaction_post,  transaction_put, transactions_date, user_login, user_post, user_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/<id>/transactions/', transactions_view),
    path('user/<user_id>/transactions/date/from/<fromDate>/to/<toDate>',
         transactions_date),
    path('user/<user_id>/transaction/<transaction_id>/delete/', transaction_delete),
    path('user/<user_id>/transaction/post/', transaction_post),
    # path('user/<user_id>/transaction/<transaction_id>/details/', transaction_details),
    path('user/<user_id>/transaction/<transaction_id>/put/', transaction_put),
    path('user/login/', user_login),
    path('user/logout/', user_logout),
    path('user/new/', user_post),
]
