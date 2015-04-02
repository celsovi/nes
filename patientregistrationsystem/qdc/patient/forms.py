# coding=utf-8
from django.forms import ModelForm, TextInput, DateInput, Select, RadioSelect, TypedChoiceField
from django.forms.widgets import Textarea
from cep.widgets import CEPInput
from django.utils.translation import ugettext_lazy as _

from patient.models import Patient, Telephone, SocialDemographicData, SocialHistoryData, ComplementaryExam, ExamFile
from patient.quiz_widget import SelectBoxCountries, SelectBoxState

# pylint: disable=E1101
# pylint: disable=E1103


class PatientForm(ModelForm):
    class Meta:
        model = Patient

        fields = [
            'name', 'cpf', 'origin', 'medical_record',  'date_birth', 'gender', 'rg', 'marital_status',
            'country', 'zipcode', 'street', 'address_number', 'address_complement', 'district', 'city', 'state', 'email'
        ]

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'autofocus': "true", 'required': "",
                                     'data-error': _('Nome deve ser preenchido')}),
            'cpf': TextInput(attrs={'class': 'form-control',
                                    'placeholder': 'xxx.xxx.xxx-xx'}),
            'origin': TextInput(attrs={'class': 'form-control'}),
            'medical_record': TextInput(attrs={'class': 'form-control'}),
            'date_birth': DateInput(attrs={'class': 'form-control datepicker', 'required': "",
                                           'data-error': _('Data de nascimento deve ser preenchida'),
                                           'placeholder': 'dd/mm/aaaa'}),
            'gender': Select(attrs={'class': 'form-control', 'required': "",
                                    'data-error': _('Sexo deve ser preenchido')}),
            'rg': TextInput(attrs={'class': 'form-control'}),
            'marital_status': Select(attrs={'class': 'form-control'}),

            'country': SelectBoxCountries(attrs={'data-flags': 'true'}),
            'zipcode': CEPInput(address={'street': 'id_street', 'district': 'id_district', 'city': 'id_city',
                                         'state': 'id_state'},
                                attrs={'class': 'form-control', 'pattern': '\d{5}-?\d{3}'}),
            'street': TextInput(attrs={'class': 'form-control'}),
            'address_number': TextInput(attrs={'class': 'form-control'}),
            'address_complement': TextInput(attrs={'class': 'form-control'}),
            'district': TextInput(attrs={'class': 'form-control'}),
            'city': TextInput(attrs={'class': 'form-control'}),
            'state': SelectBoxState(attrs={'data-country': 'id_country'}),
            'email': TextInput(attrs={
                'class': 'form-control', 'type': 'email', 'data-error': _('E-mail incorreto'),
                'pattern': '^[_A-Za-z0-9-\+]+(\.[_A-Za-z0-9-]+)*@[A-Za-z0-9-]+(\.[A-Za-z0-9]+)*(\.[A-Za-z]{2,})$'}),
        }


class TelephoneForm(ModelForm):
    class Meta:
        model = Telephone

        fields = ['number', 'type', 'note']

        widgets = {
            'number': TextInput(attrs={'class': 'form-control telephone_number', 'pattern': '^[- ()0-9]+'}),
            'type': Select(attrs={'class': 'form-control'}),
            'note': TextInput(attrs={'class': 'form-control'})
        }


class SocialDemographicDataForm(ModelForm):
    benefit_government = TypedChoiceField(required=False,
                                          empty_value=None,
                                          choices=((True, 'Sim'), (False, 'Não')),
                                          widget=RadioSelect)

    class Meta:
        model = SocialDemographicData
        fields = ['natural_of', 'citizenship', 'profession', 'occupation', 'tv', 'dvd', 'radio', 'bath',
                  'automobile', 'wash_machine', 'refrigerator', 'freezer', 'house_maid',
                  'religion', 'payment', 'flesh_tone', 'schooling', 'benefit_government',
                  'social_class']
        widgets = {
            'natural_of': TextInput(attrs={'class': 'form-control'}),
            'citizenship': SelectBoxCountries(attrs={'data-flags': 'true'}),
            'schooling': Select(attrs={'class': 'form-control'}),
            'flesh_tone': Select(attrs={'class': 'form-control'}),
            'religion': Select(attrs={'class': 'form-control'}),
            'profession': TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrar profissão'}),
            'occupation': TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrar ocupação'}),
            'payment': Select(attrs={'class': 'form-control'}),
            'tv': RadioSelect(choices=((0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4 ou +'))),
            'dvd': RadioSelect(choices=((0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4 ou +'))),
            'radio': RadioSelect(choices=((0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4 ou +'))),
            'bath': RadioSelect(choices=((0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4 ou +'))),
            'automobile': RadioSelect(choices=((0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4 ou +'))),
            'house_maid': RadioSelect(choices=((0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4 ou +'))),
            'wash_machine': RadioSelect(choices=((0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4 ou +'))),
            'refrigerator': RadioSelect(choices=((0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4 ou +'))),
            'freezer': RadioSelect(choices=((0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4 ou +'))),
            'social_class': TextInput(attrs={'class': 'form-control', 'readonly': ""})
        }


class SocialHistoryDataForm(ModelForm):
    smoker = TypedChoiceField(required=False,
                              empty_value=None,
                              choices=((True, 'Sim'), (False, 'Não')),
                              widget=RadioSelect(attrs={'id': 'id_smoker'}))
    ex_smoker = TypedChoiceField(required=False,
                                 empty_value=None,
                                 choices=((True, 'Sim'), (False, 'Não')),
                                 widget=RadioSelect)
    alcoholic = TypedChoiceField(required=False,
                                 empty_value=None,
                                 choices=((True, 'Sim'), (False, 'Não')),
                                 widget=RadioSelect(attrs={'id': 'id_alcoholic'}))

    class Meta:
        model = SocialHistoryData
        fields = ['smoker', 'amount_cigarettes', 'ex_smoker', 'alcoholic', 'alcohol_frequency',
                  'alcohol_period', 'drugs', ]

        widgets = {
            'amount_cigarettes': Select(attrs={'class': 'form-control'}),
            'alcohol_frequency': Select(attrs={'class': 'form-control'}),
            'alcohol_period': Select(attrs={'class': 'form-control'}),
            'drugs': RadioSelect(choices=(('ja_fez', 'Já fez'), ('faz', 'Faz'), ('nunca_fez', 'Nunca fez'))),
        }


class ComplementaryExamForm(ModelForm):
    class Meta:
        model = ComplementaryExam
        fields = ['date', 'description', 'doctor', 'doctor_register', 'exam_site']

        widgets = {
            'date': DateInput(attrs={'class': 'form-control datepicker', 'placeholder': 'dd/mm/aaaa',
                                     'required': "", 'data-error': "Data deve ser preenchida"}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição', 'rows': '4',
                                           'required': "", 'data-error': "Descrição deve ser preenchida"}),
            'doctor': TextInput(attrs={'class': 'form-control', 'placeholder': 'Médico'}),
            'doctor_register': TextInput(attrs={'class': 'form-control', 'placeholder': 'CRM'}),
            'exam_site': TextInput(attrs={'class': 'form-control', 'placeholder': 'Local de realização'}),
        }


class ExamFileForm(ModelForm):
    class Meta:
        model = ExamFile
        fields = ['content']
