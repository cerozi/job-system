from django.core.exceptions import ValidationError

def validate_only_number_field(value):
    for n in value:
        if not (str(n).isdigit()):
            raise ValidationError("This field only accepts numbers. ")

    return value