from django import forms



class DateInput(forms.DateInput):
    input_type = 'date'


class Curr(forms.Form):
    date = forms.DateField(label='Виберіть дату курсу', widget = DateInput)
