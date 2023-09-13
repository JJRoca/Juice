from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, Permission
from django.contrib import messages
from .models import Usuario
from django.contrib.auth.models import User, Group
from django.shortcuts import render
from .forms import UserRegistrationForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import GroupForm
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.views import PasswordResetView
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import io
import xlsxwriter

def generar_reporte(request):
    # Obtén los usuarios y grupos de alguna manera (asumo que tienes esta parte implementada)
    usuarios = User.objects.all()  # Supongamos que estás utilizando el modelo User de Django

    # Create a new workbook and add a worksheet
    workbook = xlsxwriter.Workbook('reporte.xlsx')
    worksheet = workbook.add_worksheet()

    # Write the table data to the worksheet
    row = 0
    col = 0
    for header in ['COD', 'Nombre', 'Correo', 'Usuario', 'Rol']:
        worksheet.write(row, col, header)
        col += 1

    row = 1
    col = 0
    for usuario in usuarios:
        worksheet.write(row, col, usuario.id)
        worksheet.write(row, col+1, usuario.first_name)
        worksheet.write(row, col+2, usuario.email)
        worksheet.write(row, col+3, usuario.username)
        grupos_usuario = [grupo.name for grupo in usuario.groups.all()]
        worksheet.write(row, col+4, ', '.join(grupos_usuario))
        row += 1

    # Close the workbook
    workbook.close()

    # Lógica para enviar el archivo Excel como respuesta
    with open('reporte.xlsx', 'rb') as excel_file:
        response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=reporte.xlsx'
        return response

def generar_reporte_pdf(request):
    # Obtén los usuarios y grupos de alguna manera (asumo que tienes esta parte implementada)
    usuarios = User.objects.all()  # Supongamos que estás utilizando el modelo User de Django

    # Crear un objeto buffer para guardar el PDF generado
    buffer = io.BytesIO()

    # Crear un documento PDF
    doc = SimpleDocTemplate(buffer, pagesize=landscape(letter))

    # Crear una tabla con los datos de los usuarios
    data = [['COD', 'Nombre', 'Correo', 'Usuario', 'Rol']]
    for usuario in usuarios:
        grupos_usuario = ', '.join([grupo.name for grupo in usuario.groups.all()])
        data.append([usuario.id, usuario.first_name, usuario.email, usuario.username, grupos_usuario])

    table = Table(data)
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    table.setStyle(style)

    # Agregar la tabla al documento PDF
    elements = []
    elements.append(table)
    doc.build(elements)

    # Obtener el contenido del buffer y enviarlo como respuesta
    buffer.seek(0)
    response = HttpResponse(buffer.read(), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=reporte.pdf'
    buffer.close()
    return response

# def generar_reporte(request):
#     # Obtén los usuarios y grupos de alguna manera (asumo que tienes esta parte implementada)
#     usuarios = User.objects.all()  # Supongamos que estás utilizando el modelo User de Django

#     # Create a new workbook and add a worksheet
#     workbook = xlsxwriter.Workbook('reporte.xlsx')
#     worksheet = workbook.add_worksheet()

#     # Write the table data to the worksheet
#     row = 0
#     col = 0
#     for header in ['COD', 'Nombre', 'Correo', 'Usuario', 'Rol']:
#         worksheet.write(row, col, header)
#         col += 1

#     row = 1
#     col = 0
#     for usuario in usuarios:
#         worksheet.write(row, col, usuario.id)
#         worksheet.write(row, col+1, usuario.first_name)
#         worksheet.write(row, col+2, usuario.email)
#         worksheet.write(row, col+3, usuario.username)
#         grupos_usuario = [grupo.name for grupo in usuario.groups.all()]
#         worksheet.write(row, col+4, ', '.join(grupos_usuario))
#         row += 1

    # Close the workbook
    workbook.close()

    # Lógica para enviar el archivo Excel como respuesta
    with open('reporte.xlsx', 'rb') as excel_file:
        response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=reporte.xlsx'
        return response




# def recuperar_contrasena(request):
#     if request.method == 'POST':
#         correo = request.POST['correo']
#         try:
#             user = User.objects.get(email=correo)
#             # Generar un token único y almacenarlo en el modelo de usuario
#             # Puedes usar el módulo secrets para generar un token seguro
#             # Además, establecer la fecha y hora de solicitud
#             # Aquí, por simplicidad, simplemente estableceremos una cadena aleatoria como token
#             user.reset_password_token = 'random_token'
#             user.reset_password_requested_at = timezone.now()
#             user.save()

#             # Envía el correo electrónico al usuario con el enlace de recuperación
#             send_mail(
#                 'Restablecer contraseña',
#                 f'Haz clic en este enlace para restablecer tu contraseña: http://tudominio.com/restablecer-contrasena/{user.reset_password_token}',
#                 'hachike67lol@gmail.com',  # Remitente, debe ser el mismo que configuraste en EMAIL_HOST_USER
#                 [correo],
#                 fail_silently=False,
#             )
#             messages.success(request, 'Se ha enviado un correo de recuperación a tu dirección de correo electrónico.')
#             return redirect('nombre_de_la_vista_de_exito')  # Reemplaza esto con el nombre de la vista que mostrará el mensaje de éxito
#         except User.DoesNotExist:
#             messages.error(request, 'Este correo electrónico no está registrado en nuestro sistema.')
#     return render(request, 'recuperar_contrasena.html')


#RECUPERAR PASSWORD DE PRUEBA

class CustomPasswordResetView(PasswordResetView):
    template_name = 'custom_password_reset.html'
    email_template_name = 'custom_password_reset_email.html'
    success_url = '/password_reset/done/'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        if not User.objects.filter(email=email).exists():
            messages.error(self.request, 'El correo electrónico no está registrado.')
            return self.form_invalid(form)
        return super().form_valid(form)

# views.py



# def restablecer_contrasena(request, token):
#     try:
#         user = User.objects.get(reset_password_token=token)
#         # Aquí debes verificar si el token es válido y si la solicitud no ha expirado
#         # Por simplicidad, aquí verificamos solo si el token es igual a 'random_token'
#         if user.reset_password_token == 'random_token':
#             if request.method == 'POST':
#                 nueva_contrasena = request.POST['nueva_contrasena']
#                 confirmar_contrasena = request.POST['confirmar_contrasena']
#                 if nueva_contrasena == confirmar_contrasena:
#                     user.set_password(nueva_contrasena)
#                     user.reset_password_token = None
#                     user.reset_password_requested_at = None
#                     user.save()
#                     messages.success(request, 'Tu contraseña ha sido restablecida exitosamente.')
#                     return redirect('nombre_de_la_vista_de_login')  # Reemplaza esto con el nombre de la vista de inicio de sesión
#                 else:
#                     messages.error(request, 'Las contraseñas no coinciden. Por favor, inténtalo de nuevo.')
#             return render(request, 'restablecer_contrasena.html')
#         else:
#             messages.error(request, 'El enlace de restablecimiento es inválido o ha expirado.')
#             return redirect('nombre_de_la_vista_de_error')  # Reemplaza esto con el nombre de la vista que mostrará el mensaje de error
#     except User.DoesNotExist:
#         messages.error(request, 'El enlace de restablecimiento es inválido o ha expirado.')
#         return redirect('nombre_de_la_vista_de_error')  # Reemplaza esto con el nombre de la vista que mostrará el mensaje de error

#USUARIO OLVIDADO

# MODIFICAR USUARIO
@login_required
@permission_required('usaurios.view_role')
def modificar_usuario(request, usuario_id):
    usuario = get_object_or_404(User, id=usuario_id)

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        grupo_id = request.POST.get('grupo')

        # Actualizar los datos del usuario
        usuario.first_name = nombre
        usuario.email = email
        usuario.username = username

        # Actualizar la contraseña si se proporciona
        if password:
            usuario.set_password(password)

        # Actualizar el grupo del usuario
        grupo = Group.objects.get(id=grupo_id)
        usuario.groups.set([grupo])

        # Guardar los cambios del usuario
        usuario.save()

        return redirect('usuarios')

    grupos = Group.objects.all()
    context = {
        'usuario': usuario,
        'grupos': grupos
    }

    return render(request, 'modificar_usuario.html', context)
#LOGIN
def eliminar_usuario(request, usuario_id):
    if request.method == 'POST':
        usuario = User.objects.get(id=usuario_id)
        usuario.delete()
    return redirect('usuarios')



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

@csrf_exempt
def login_view(request):
    form = LoginForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return HttpResponse('Credenciales incorrectas', status=400)

    return render(request, 'login.html', {'form': form})

@login_required
def index (request):
    return render(request, 'index.html')

def logout_view(request):
    logout(request)
    return redirect('index')  # Cambia 'index' por la URL a la que deseas redirigir después del cierre de sesión

#ADMINISTRACION DE GRUPOS
@login_required
@permission_required('usaurios.view_role')
def update_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('administrar_grupos')
    else:
        form = GroupForm(instance=group)
    return render(request, 'update_group.html', {'form': form, 'group': group})



@login_required
@permission_required('usaurios.view_role')
def administrar_grupos(request):
    groups = Group.objects.all()
    return render(request, 'administrar_grupos.html', {'groups': groups})
@login_required
@permission_required('usaurios.view_role')
def delete_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    if request.method == 'POST':
        group.delete()
        return redirect('administrar_grupos')
    return render(request, 'confirm_delete_group.html', {'group': group})
#REGISTRAR GRUPO
@login_required
@permission_required('usaurios.view_role')
def register_groups(request):
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        permission_ids = request.POST.getlist('permissions')

        # Verificar si el grupo ya existe
        if Group.objects.filter(name=group_name).exists():
            error_message = f"El grupo '{group_name}' ya existe."
            permissions = Permission.objects.all()
            return render(request, 'register_groups.html', {'permissions': permissions, 'error_message': error_message})

        group = Group.objects.create(name=group_name)
        permissions = Permission.objects.filter(id__in=permission_ids)
        group.permissions.set(permissions)

        messages.success(request, f"El grupo '{group_name}' ha sido registrado exitosamente.")
        return redirect('administrar_grupos')

    permissions = Permission.objects.all()
    return render(request, 'register_groups.html', {'permissions': permissions})



# Registro de usuario


# REGISTRO FUNCIONANDO CON ALERTAS y limpiado

def register_user(request):
    success_message = None
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            if User.objects.filter(username=username).exists():
                messages.error(request, 'El nombre de usuario ya está en uso.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'El correo electrónico ya está en uso.')
            else:
                user = form.save()
                group = form.cleaned_data['grupo']
                user.groups.add(group)
                success_message = 'Registro exitoso.'
                # Limpiar los campos del formulario después del registro exitoso
                form = UserRegistrationForm()  # Esto crea un nuevo formulario vacío
                return render(request, 'register_user.html', {'form': form, 'success_message': success_message})
    else:
        form = UserRegistrationForm()

    return render(request, 'register_user.html', {'form': form, 'success_message': success_message})

# REGISTRO CON ALERTAS LOGRADO

# def register_user(request):
#     success_message = None
    
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             email = form.cleaned_data['email']
#             if User.objects.filter(username=username).exists():
#                 messages.error(request, 'El nombre de usuario ya está en uso.')
#             elif User.objects.filter(email=email).exists():
#                 messages.error(request, 'El correo electrónico ya está en uso.')
#             else:
#                 user = form.save()
#                 group = form.cleaned_data['grupo']
#                 user.groups.add(group)
#                 success_message = 'Registro exitoso.'
#     else:
#         form = UserRegistrationForm()

#     return render(request, 'register_user.html', {'form': form, 'success_message': success_message})

#PLANTILLA DE REGISTRO EXITOSO
def registro_exitoso(request):
    return render(request, 'registro_exitoso.html')



def usuarios_view(request):
    usuarios = User.objects.all()
    grupos = Group.objects.all()

    context = {
        'usuarios': usuarios,
        'grupos': grupos,
    }

    return render(request, 'usuarios.html', context)


def olvidaste_contrasenia(request):
    return render(request, 'olvidaste_contrasenia.html')



def buscar_usuario(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        grupo = request.POST.get('grupo')

        try:
            usuario_encontrado = User.objects.get(email=correo, groups__name=grupo)
        except User.DoesNotExist:
            usuario_encontrado = None
    else:
        usuario_encontrado = None

    context = {
        'usuario_encontrado': usuario_encontrado,
    }

    return render(request, 'buscar_usuario.html', context)

#reporte de excel
