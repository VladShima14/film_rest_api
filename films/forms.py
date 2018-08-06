from django import forms
from django.core.exceptions import ValidationError

from .models import Film, Genre


class PlaceholderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PlaceholderForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                if type(field.widget) in (forms.TextInput, ):
                    field.widget.attrs.update(
                        {'placeholder': field.label, 'class': 'span10'}
                    )
                if type(field.widget) in (forms.Select, ):
                    field.widget.attrs.update({'class': 'span10'})
                    field.empty_label = field.label

    def as_p(self):
        return self._html_output(
            normal_row='<p%(html_class_attr)s>%(field)s%(help_text)s</p>',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True
        )


class GenreForm(PlaceholderForm):
    class Meta:
        model = Genre
        fields = ['name']


class FilmForm(PlaceholderForm):
    class Meta:
        model = Film
        fields = ['name', 'genre']
