from __future__ import unicode_literals

from django.db import models

import validators


class Member(models.Model):

    """
    A table containing the list of members of the organisation
    """
    id_number = models.CharField(
        max_length=10, validators=[validators.validate_id_number])
    last_name = models.CharField(max_length=50)
    given_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)


class AffiliatedSchool(models.Model):

    """
    A table containing schools affiliated to the organisation
    """
    school_name = models.CharField(max_length=100, unique=True)
    science_club_members_count = models.PositiveIntegerField()
    teacher_name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=20)
    years_affiliated = models.PositiveIntegerField()
