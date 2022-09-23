from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import  *
# Register your models here.

# Register your models here.
#PARA EL ADMINISTRADOR
class AutorResource(resources.ModelResource):
  class Meta:
    model = Procesos

class ProcesosAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ("nom_pro", "usuarioid", "user")
    search_fields = ("nom_pro","user__username", "user__id", "fec_pro")
    list_display_links = ('nom_pro',)
    list_per_page = 5
    resource_class = AutorResource
    
    # def save_model(self, request, obj, form, change):
    #     Procesos.objects.all()

admin.site.register(Procesos, ProcesosAdmin)
admin.site.register(TipoProceso)
admin.site.register(Unidades)
admin.site.register(Responsableunidad)
admin.site.register(Usuario)
admin.site.register(Plataforma)

# admin.site.register([Country, City])