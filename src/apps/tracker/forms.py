from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, HTML, Field, Button
from crispy_forms.bootstrap import FormActions
from django import forms


class TrackerForm(forms.Form):
    mac = forms.CharField(
        max_length=6,
        help_text='Número de módulo',
        label='MAC',
        required=True
    )
    remesa = forms.CharField(
        max_length=7,
        help_text='Escribe la remesa',
        label='Remesa',
        required=True
    )
    archivo = forms.FileField()

    def __init__(self, *args, **kwargs):
        super(TrackerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'form'
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Field('mac'),
                    Field('remesa'),
                    Field('archivo'),
                    css_class='col-md-4'
                ),
                css_class='row'
            ),
            Div(
                HTML('<hr>'),
                FormActions(
                    Submit('save', 'Guardar cambios'),
                    Button('cancel', 'Cancelar')
                )
            )
        )
