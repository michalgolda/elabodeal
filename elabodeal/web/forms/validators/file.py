from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def ebook_file_size(file_object = None):
    if file_object:
        if file_object.size > 1073741824:
            raise ValidationError(_('Plik jest za duży'))

def image_file_size(file_object = None):
    if file_object:
        if file_object.size > 200000000:
            raise ValidationError(_('Plik jest za duży'))