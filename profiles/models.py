from django.db import models
from django.utils.translation import ugettext_lazy as _

from userena.models import UserenaLanguageBaseProfile
from userena.utils import user_model_label
from utils.constants import STATE_CHOICES

from edu.models import Exam

import datetime

class Profile(UserenaLanguageBaseProfile):
    """ Default profile """
    GENDER_CHOICES = (
        (1, _('Male')),
        (2, _('Female')),
    )

    user = models.OneToOneField(user_model_label,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='profile')

    gender = models.PositiveSmallIntegerField(_('gender'),
                                              choices=GENDER_CHOICES,
                                              blank=True,
                                              null=True)
    #website = models.URLField(_('website'), blank=True)
    #location =  models.CharField(_('location'), max_length=255, blank=True)
    birth_date = models.DateField(_('birth date'), blank=True, null=True)
    #about_me = models.TextField(_('about me'), blank=True)
    
    mobile_phone = models.CharField(max_length=10, verbose_name='Mobile Phone')
    home_phone = models.CharField(max_length=12, blank=True, verbose_name='Home Phone')
    
    father_name = models.CharField(max_length=100, blank=True)
    mother_name = models.CharField(max_length=100, blank=True)
    
    addr_line1 = models.CharField(max_length=255, blank=True)
    addr_line2 = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    pin = models.CharField(max_length=6)
    
    exams = models.ManyToManyField(Exam, blank=True, null=True)
    marks_10_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    marks_12_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    
    photo_id = models.CharField(max_length=100, blank=True)
    photo_id_number = models.CharField(max_length=100, blank=True)
    
    def is_profile_complete(self):
        if self.exams and self.marks_10_percent and self.marks_12_percent and self.photo_id and self.pin and self.mobile_phone:
            return True
        return False

    @property
    def age(self):
        if not self.birth_date: return False
        else:
            today = datetime.date.today()
            # Raised when birth date is February 29 and the current year is not a
            # leap year.
            try:
                birthday = self.birth_date.replace(year=today.year)
            except ValueError:
                day = today.day - 1 if today.day != 1 else today.day + 2
                birthday = self.birth_date.replace(year=today.year, day=day)
            if birthday > today: return today.year - self.birth_date.year - 1
            else: return today.year - self.birth_date.year
