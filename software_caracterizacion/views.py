from django.http import HttpResponse
from django.views.generic import ListView, View
from django.shortcuts import get_object_or_404, redirect, render
from .models import   *
from django.contrib import messages
from .forms import ProcesosFormulario
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from software_caracterizacion.utils import render_to_pdf
from django.core.paginator import Paginator
from django.http import Http404
import datetime
#PDF
class ListaProcesosView(ListView):
    model = Procesos
    template_name = "report/pdf.html"
    context_object_name = 'procesos'

class ListProcesosPdf(View):
    def get(self, request, *args, **kwargs):
        procesos = Procesos.objects.filter(user=request.user).order_by('-fec_pro')
        user = request.user
        day  = datetime.datetime.now()
        formatedDay  = day.strftime("%Y/%m/%d")
        data = {
            'procesos': procesos,
            'user': user,
            'date': formatedDay
        }
        
        pdf = render_to_pdf('report/lista.html', data)
        
        return HttpResponse(pdf, content_type='application/pdf')
#PDF
# Create your views here.
@login_required(login_url="user-login")
def inicio(request):
    return render(request, 'login/inicio.html')

#LOGIN
def index_Login(request):
    return render(request, 'login/index_Login.html')


def userLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            
            login(request, user)
            
            return redirect('inicio')
        else:
            messages.warning(request,'No te has identificado correctamente.')
    return render(request,'login/index_Login.html')

def logout_user(request):
    logout(request)
    return redirect('user-login')

#PROCESOS
@login_required(login_url="user-login")
def procesos(request):
    # BUSCADOR
    if 'q' in request.GET:
        q = request.GET['q']
        no_proceso = Procesos.objects.filter(user=request.user).count()
        busqueda = Procesos.objects.filter(nom_pro__icontains=q)
        contador = busqueda.count()
        #
        page = request.GET.get('page', 1)
        try:
            paginator = Paginator(busqueda, 5)
            busqueda = paginator.page(page)
        except :
            raise Http404
        #
        if contador == 0:
                messages.warning(request, 'No se encontró ningún registro')
                no_proceso = Procesos.objects.filter(user=request.user).count()
                busqueda = Procesos.objects.filter(user=request.user).order_by('-fec_pro').order_by('-hor_pro')
                page = request.GET.get('page', 1)
                try:
                    paginator = Paginator(busqueda, 5)
                    busqueda = paginator.page(page)
                except :
                    raise Http404
                return render(request, 'procesos/index.html', {'no_proceso': no_proceso, 'entity': busqueda, 'paginator':paginator})
    else:
        no_proceso = Procesos.objects.filter(user=request.user).count()
        busqueda = Procesos.objects.filter(user=request.user).order_by('-fec_pro').order_by('-hor_pro')
        page = request.GET.get('page', 1)
        try:
            paginator = Paginator(busqueda, 5)
            busqueda = paginator.page(page)
        except :
            raise Http404
    return render(request, 'procesos/index.html', {'no_proceso': no_proceso, 'entity': busqueda, 'paginator':paginator})
@login_required(login_url="user-login")
def crear_proceso(request):
    if request.method == 'POST':
        form_procesos = ProcesosFormulario(request.POST)
        if form_procesos.is_valid():
            post = form_procesos.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Proceso creado correctamente')
            return redirect('crear_proceso')
        else:
            messages.success(request, 'Este proceso ya existe')
    else:
        # crear nuevoi objeto
        form_procesos = ProcesosFormulario()
    return render(request, 'procesos/crear.html', {'form_procesos': form_procesos})

@login_required(login_url="user-login")
def load_responsable(request):
    unidades_id = request.GET.get('unidades_id')
    responsableunidad = ResponsableUnidad.objects.filter(unidades_id=unidades_id).all()
    return render(request, 'procesos/city_dropdown_list_options.html', {'responsableunidad': responsableunidad})

@login_required(login_url="user-login")
def detalle_proceso(request, id):
    #proceso = Procesos.objects.get(pk=ide_pro)
    proceso = get_object_or_404(Procesos, pk=id)
    return render(request,'procesos/detallemodal.html', {'proceso': proceso})

    
@login_required(login_url="user-login")
def editar_proceso(request, id):
    proceso = get_object_or_404(Procesos, pk=id)
    get_tipo = proceso.user.id #usuario del procesoz
    if request.user.id == get_tipo:
        if request.method == 'POST':
        
            form_procesos = ProcesosFormulario(request.POST, instance=proceso)
            if form_procesos.is_valid():
                form_procesos.save()
                messages.success(request, 'Proceso editado correctamente')
                return redirect('procesos')
        else:
            # crear nuevoi objeto
            form_procesos = ProcesosFormulario(instance=proceso)
        return render(request, 'procesos/editar.html', {'form_procesos': form_procesos})
    else:
        messages.success(request, 'Esta acción no es permitida')
        return render(request, 'login/inicio.html')


@login_required(login_url="user-login")
def eliminar_proceso(request, id):
    proceso = Procesos.objects.get(id=id)
    proceso.delete()
    messages.success(request, 'Proceso eliminado correctamente')
    return redirect('procesos')

# automatizacion proceso
@login_required(login_url="user-login")
def automatizacion_proceso(request, id):
    proceso = get_object_or_404(Procesos, pk=id)
    get_tipo = proceso.tipoprocesoid
    
    
    if request.method == 'POST':
        form_procesos = ProcesosFormulario(request.POST, instance=proceso)
        if form_procesos.is_valid():
            form_procesos.save()
            messages.success(request, 'Proceso ejecutado correctamente')
            return redirect('procesos')
    else:
        # crear nuevoi objeto
        form_procesos = ProcesosFormulario(instance=proceso)
    return render(request, 'procesos/automatizar/detalles_Automatizar.html', {'form_procesos': form_procesos, 'proceso': proceso, 'get_tipo':get_tipo})
    