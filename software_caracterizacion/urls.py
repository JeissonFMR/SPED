from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #LOGIN
    path('inicio', views.inicio,name='inicio'),

    path('', views.userLogin, name='user-login'),
    path('logout/', views.logout_user, name='logout'),
    #PROCESOS
     path('procesos',views.procesos,name='procesos'),
     path('procesos/crear_proceso', views.crear_proceso,name='crear_proceso'),
     path('detalle_proceso/<int:id>', views.detalle_proceso,name='detalle_proceso'),
     path('editar_proceso/<int:id>',views.editar_proceso,name='editar_proceso'),
     path('eliminar_proceso/<int:id>',views.eliminar_proceso,name='eliminar_proceso'),

    #AUTOMATIZACION PROCESO
    path('automatizacion_proceso/<int:id>', views.automatizacion_proceso,name='automatizacion_proceso'),
    #  ####
     path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
     path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
     path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
     path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

    path('lista/', views.ListaProcesosView.as_view(), name='lista'),
    path('listar-procesos/', views.ListProcesosPdf.as_view(), name='procesos_all'),
    # 
    
    path('ajax/load-responsable/', views.load_responsable, name='ajax_load_responsable'), # AJAX
]