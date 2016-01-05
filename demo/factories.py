import factory
import string
import random

from django.contrib.auth.models import User

from .models import AffiliatedSchool

CHARS = string.ascii_uppercase + string.ascii_lowercase + string.digits


class AffiliatedSchoolFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = AffiliatedSchool
        django_get_or_create = ('school_name',)

    school_name = factory.Sequence(lambda n: 'School%d' % n)
    science_club_members_count = random.randrange(1, 101)
    teacher_name = factory.Faker('name')
    contact_no = "09" + ''.join(random.choice(string.digits) for _ in range(9))
    years_affiliated = random.randrange(1, 10)


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User
        django_get_or_create = ('username',)

    username = factory.Sequence(lambda n: 'user%d' % n)
    email = factory.LazyAttribute(lambda obj: '%s@test.com' % obj.username)
    password = (factory
                .PostGenerationMethodCall('set_password',
                                          ''.join(random.choice(CHARS)
                                                  for _ in range(8))))

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop('password', None)
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        if password:
            user.raw_password = password
            user.set_password(password)
            if create:
                user.save()
        return user
