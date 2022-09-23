from distutils.text_file import TextFile
from logging import PlaceHolder
from selectors import SelectSelector
#from tkinter import Widget
#from attr import attr
from django.forms import TextInput, TimeInput, ModelForm, RadioSelect, Textarea, Select

from .models import *

class ProcesosFormulario(ModelForm):
    class Meta:
        model = Procesos
        fields = '__all__'
        widgets = {
            #PREGUNTAR PORQUE NO FUNCIONA EL PLACEHOLDER
            
            'nom_pro':TextInput(attrs={'type': 'text','class' : 'nombre_proceso', 'placeholder':'Ej: Cambio de contraseña de TAU', 'pattern' : '[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]+', 'required' : True }),

            'pre_pro':Textarea(attrs={'type': 'text','class' : 'pregunta_proceso', 'placeholder':'Ej: ¿Comó recuperar mi contraseña de TAU?', 'required' : 'required', 'rows': 3  }),
            
            'res_pro':Textarea(attrs={'type': 'text','class' : 'respuesta_proceso', 'placeholder':'Ej: Para soporte de la plataforma TAU, por favor escribir al siguiente correo tau-ayuda@unicesmag.edu.co, este proceso no corresponde a la Jefatura de Desarrollo de Software', 'required' : 'required', 'rows': 3}),

            'aut_pro':RadioSelect(attrs={'type': 'radio','class' : 'automatizacion_proceso',  }),

            'fec_pro':TimeInput(attrs={'type': 'month','class' : 'fech_creacion_proceso', 'placeholder':'Creacion del proceso', 'required' : 'required' }),

            'hor_pro':TimeInput(attrs={'type': 'time','class' : 'hor_creacion_proceso', 'placeholder':'Creacion Hora del proceso', 'required' : 'required'}),

            'tie_pro':TextInput(attrs={'type': 'number','class' : 'tiem_proceso', 'placeholder':'Ej: 1', 'pattern' : '[0-9]+', 'min':'1', 'max':'59','required' : 'required' }),
        
            'usuarioid':Select(attrs={'required' : 'required' }),
            'plataformaid':Select(attrs={'required' : 'required' }),
            
            'programaid':Select(attrs={'required' : 'required' }),
            'responsableid':Select(attrs={'required' : 'required' }),
            
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['responsableid'].queryset = Responsableunidad.objects.none()

        if 'unidadesid' in self.data:
            try:
                unidades_id = int(self.data.get('unidadesid'))
                self.fields['responsableid'].queryset = Responsableunidad.objects.filter(unidades_id=unidades_id).order_by('nombre')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk and self.instance.unidadesid:
            self.fields['responsableid'].queryset = self.instance.unidadesid.responsableunidad_set.order_by('nombre')

