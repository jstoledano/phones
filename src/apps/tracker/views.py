from django.views.generic import FormView
from django import forms
from django.conf import settings
import tabula
import numpy as np
from .forms import TrackerForm


def handle_upload_files(f):
    with open(settings.BASE_DIR.child('temp', 'archivo.pdf'), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
        destination.close()
        df = tabula.convert_into(
            settings.BASE_DIR.child('temp', 'archivo.pdf'),
            settings.BASE_DIR.child('temp', 'archivo.csv'),
            output_format='csv',
            java_options=None,
            pandas_options={
                'header': None,
                'names': ('folio_notificacion', 'clave_elector', 'folio', 'paterno', 'materno', 'nombre', 'telefono'),
                'dtype': {'folio_notificacion': np.str, 'folio': np.str, 'telefono': np.str},
            },
            multiple_tables=False,
            pages='all',
            guess=False,
            lattice=True,
            silent=True,
            area=(152.433, 29.004, 592.532, 917.505),
        )
        return df


class ReporteForm(forms.Form):
    remesa = forms.CharField(max_length=7, help_text='El formato es aaaa-rr')
    mac = forms.CharField(max_length=3, help_text='Los 3 últimos dígitos')
    archivo_pdf = forms.FileField()


class ReporteView(FormView):
    template_name = 'llamadas/index.html'
    form_class = TrackerForm
    success_url = '/'

    def form_valid(self, form):
        archivo_pdf = form.cleaned_data['archivo_pdf']
        handle_upload_files(archivo_pdf)
        return super(ReporteView, self).form_valid(form)
