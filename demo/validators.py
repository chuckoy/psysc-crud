import re

from django.core.exceptions import ValidationError


def validate_id_number(value):
    # ID number should follow format: <year><batch>-<applicant no>
    if not re.match(r'\d{4}\w-\d{1,4}', value):
        raise ValidationError('Invalid format for ID %s' % value)
