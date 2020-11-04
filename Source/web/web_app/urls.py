from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('outlier/', views.outlier, name='outlier'),
    path('data/', views.somedata),
    path('batchanalysis/', views.batch_analysis),
    path('barrelanalysis/', views.barrel_analysis),
    path('managebatches/', views.manage_batches),
    path('account/', views.manage_account),
    path('signin/', views.signin),
    path('signout/', views.signout),
]