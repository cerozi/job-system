# django built-in imports;
from django.core.exceptions import ValidationError


def validate_only_number_field(value):
    ''' Validates a model field that is suposed to receive only numbers.
    :param - value: str
    :return - str
    '''
    for n in value:
        if not (str(n).isdigit()):
            raise ValidationError("This field only accepts numbers. ")

    return value