from django.views.generic import FormView
from django import forms
from django.conf import settings
import tabula
import numpy as np


def handle_upload_files(f):
    with open(settings.BASE_DIR.child('temp', 'archivo.pdf'), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
        destination.close()
        df = tabula.convert_into(
            settings.BASE_DIR.child('temp', 'archivo.pdf'),
            settings.BASE_DIR.child('temp', 'archivo.csv'),
            output_format='csv',
            pages='all',
            guess=False,
            lattice=True,
            silent=True,
            area=(152.433, 29.004, 592.532, 917.505),
            pandas_options={
                'header': None,
                'names': ('folio_notificacion', 'clave_elector', 'folio', 'paterno', 'materno', 'nombre', 'telefono'),
                'dtype': {'folio_notificacion': np.str, 'folio': np.str, 'telefono': np.str},
            }
        )
        return df


class ReporteForm(forms.Form):
    input_file = forms.FileField()


class ReporteView(FormView):
    template_name = 'llamadas/index.html'
    form_class = ReporteForm
    success_url = '/'

    def form_valid(self, form):
        input_file = form.cleaned_data['input_file']
        handle_upload_files(input_file)
        return super(ReporteView, self).form_valid(form)
