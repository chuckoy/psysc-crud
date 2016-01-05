from __future__ import unicode_literals

from django.db import models


class Member(models.Model):

    """
    A table containing the list of members of the organisation
    """
    id_number = models.CharField(max_length=10)
    last_name = models.CharField(max_length=50)
    given_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)

class AffiliatedSchool(models.Model):

    """
    A table containing schools affiliated to the organisation
    """
    school_name = models.CharField(max_length=100, unique=True)

def validate_id_number(value):
