from django.urls import path
from .views import CustomPasswordResetView,generar_reporte_pdf,generar_reporte,register_groups,register_user,buscar_usuario, registro_exitoso,modificar_usuario,olvidaste_contrasenia, eliminar_usuario,delete_group,administrar_grupos,update_group,usuarios_view,login_view, logout_view,index
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('administrar_grupos/', administrar_grupos, name='administrar_grupos'),
    path('register_groups/', register_groups, name='register_groups'),
    path('register_user/', register_user, name='register_user'),
    path('registro_exitoso/', registro_exitoso, name='registro_exitoso'),
    path('update_group/<int:group_id>/', update_group, name='update_group'),
    path('delete_group/<int:group_id>/', delete_group, name='delete_group'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('index/',index,name='index'),
    path('buscar_usuario/', buscar_usuario, name='buscar_usuario'),
    path('olvidaste_contrasenia/', olvidaste_contrasenia, name='olvidaste_contrasenia'),
    path('usuarios/', usuarios_view, name='usuarios'),
    path('usuarios/modificar/<int:usuario_id>/', modificar_usuario, name='modificar_usuario'),
    path('usuarios/eliminar/<int:usuario_id>/', eliminar_usuario, name='eliminar_usuario'),
    # path('recuperar-contrasena/', recuperar_contrasena, name='recuperar_contrasena'),
    # path('restablecer-contrasena/<str:token>/', restablecer_contrasena, name='restablecer_contrasena'),
    # Restablecer las passwords
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset_password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    #NUEVAS URLS PARA PRUEBA DE PASSWORD
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('generar_reporte/', generar_reporte, name='generar_reporte'),
    path('generar_reporte_pdf/', generar_reporte_pdf, name='generar_reporte_pdf'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='custom_password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='custom_password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
