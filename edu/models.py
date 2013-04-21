from django.db import models
from django.utils import timezone
from userena.utils import user_model_label
from django.http import HttpRequest
from utils.constants import STATE_CHOICES, EXAM_COVERAGE_CHOICES

ACTIVE = 'A'
INACTIVE = 'I'
STATUS_CHOICES = (
    (ACTIVE,'Active'),
    (INACTIVE,'Inactive'),
)
AVAILABLE = 'A'
UNAVAILABLE = 'U'
AVAILABILITY_CHOICES = (
    (AVAILABLE,'Available'),
    (UNAVAILABLE,'Unavailable'),
)
YES = 'Y'
NO = 'N'
YESNO_CHOICES = (
    (YES,'Yes'),
    (NO,'No'),
)


class XLAT(models.Model):
    field_name = models.CharField(max_length=255,unique=True)
    field_value = models.CharField(max_length=255)
    description = models.TextField()
    effective_date = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    created_by = models.ForeignKey(user_model_label, editable=False)
    created_date = models.DateTimeField(auto_now=True, auto_now_add=True, default=timezone.now)
    def __unicode__(self):
        return self.field_name

class University(models.Model):
    univ_id = models.CharField(max_length=6, unique=True, verbose_name='University ID')
    name = models.CharField(max_length=255, verbose_name='University Name')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    addr_line1 = models.CharField(max_length=100)
    addr_line2 = models.CharField(max_length=100,blank=True)
    state = models.CharField(max_length=30, choices=STATE_CHOICES)
    pin = models.CharField(max_length=6)
    aicte_approv_status = models.CharField(max_length=1,choices=STATUS_CHOICES)
    created_by = models.ForeignKey(user_model_label, editable=False)
    created_date = models.DateTimeField(auto_now=True, auto_now_add=True, default=timezone.now)
	
    class Meta:
        verbose_name_plural = 'Universities'
    
    def __unicode__(self):
        return self.name
		
	
    
class Stream(models.Model):
    name = models.CharField(max_length=100)
    stream_code = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(user_model_label, editable=False)
    created_date = models.DateTimeField(auto_now=True, auto_now_add=True, default=timezone.now)
    def __unicode__(self):
        return self.name
    
class Institute(models.Model):
    inst_id = models.CharField(max_length=8, unique=True, verbose_name='Institute ID')
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    deemed_univ = models.CharField(max_length=1, choices=YESNO_CHOICES)
    university = models.ForeignKey(University)
    aicte_approv_status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    streams = models.ManyToManyField(Stream)
    reg_date = models.DateField('registered_Date')
    aff_date = models.DateField('affiliated_Date')
    aff_expiry_date = models.DateField('affiliation_expiry_date')
    reg_addr_line1 = models.CharField(max_length=100, verbose_name='Registered Address Line 1')
    reg_addr_line2 = models.CharField(max_length=100, blank=True, verbose_name='Registered Address Line 2')
    cur_addr_line1 = models.CharField(max_length=100, blank=True, verbose_name='Current Address Line 1')
    cur_addr_line2 = models.CharField(max_length=100, blank=True, verbose_name='Current Address Line 2')
    reg_state = models.CharField(max_length=30, choices=STATE_CHOICES, verbose_name='Registered State')
    cur_state = models.CharField(max_length=30, choices=STATE_CHOICES, verbose_name='Current State')
    reg_pin = models.CharField(max_length=6,verbose_name='Registered PIN')
    cur_pin = models.CharField(max_length=6,verbose_name='Current PIN')
    accr_status = models.CharField(max_length=1,choices=AVAILABILITY_CHOICES,verbose_name='Accredition Status')
    last_accr_date = models.DateField('last_accredited_date')
    nominal_fee = models.DecimalField(max_digits=9,decimal_places=2)
    about_info = models.TextField(blank=True)
    created_by = models.ForeignKey(user_model_label, editable=False)
    created_date = models.DateTimeField(auto_now=True, auto_now_add=True, default=timezone.now)
    
    def __unicode__(self):
        return self.name

class Application(models.Model):
    appln_id = models.CharField(max_length=255,unique=True,verbose_name='Application ID')
    user = models.ForeignKey(user_model_label, related_name='applications')
    institute = models.ForeignKey(Institute)
    stream = models.ForeignKey(Stream)
    priority_number = models.PositiveSmallIntegerField(default=5)
    created_date = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True, auto_now_add=True, default=timezone.now)
    last_updated_by = models.ForeignKey(user_model_label, related_name='applications_last_updated', editable=False)
    
    class Meta:
        ordering = ['priority_number']
    
    def __unicode__(self):
        return self.appln_id

class Exam(models.Model):
    exam_id = models.CharField(max_length=10, unique=True, verbose_name='Exam Id')
    abbr = models.CharField(max_length=10, verbose_name='Exam Short Code')
    full_name = models.CharField(max_length=255)
    coverage = models.CharField(max_length=40, choices=EXAM_COVERAGE_CHOICES)
    created_by = models.ForeignKey(user_model_label, editable=False)
    created_date = models.DateTimeField(auto_now=True, auto_now_add=True, default=timezone.now)
    
    def __unicode__(self):
        return "%s" % (self.abbr)
    
    class Meta:
        ordering = ['full_name']
    
    