from django.db import models

from userena.utils import user_model_label

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
HIGHEST = 0
HIGH = 1
MEDIUM = 2
LOW = 3
LOWEST = 4
PRIORITY_CHOICES = (
    (HIGHEST, 'Highest'),
    (HIGH, 'High'),
    (MEDIUM, 'Medium'),
    (LOW, 'Low'),
    (LOWEST, 'Lowest'),
)

class XLAT(models.Model):
    field_name = models.CharField(max_length=255,unique=True)
    field_value = models.CharField(max_length=255)
    description = models.TextField()
    effective_date = models.DateField()
    status = models.CharField(max_length=1,choices=STATUS_CHOICES)
    created_by = models.ForeignKey(user_model_label)
    created_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.field_name

class University(models.Model):
    univ_id = models.CharField(max_length=6,unique=True,verbose_name='University ID')
    name = models.CharField(max_length=255,verbose_name='University Name')
    status = models.CharField(max_length=1,choices=STATUS_CHOICES)
    addr_line1 = models.CharField(max_length=100)
    addr_line2 = models.CharField(max_length=100,blank=True)
    state = models.CharField(max_length=40)
    pin = models.CharField(max_length=6)
    aicte_approv_status = models.CharField(max_length=1,choices=STATUS_CHOICES)
    created_by = models.ForeignKey(user_model_label)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Universities'
    
    def __unicode__(self):
        return self.name
    
class Stream(models.Model):
    name = models.CharField(max_length=100)
    stream_code = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(user_model_label)
    created_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.name
    
class Institute(models.Model):
    inst_id = models.CharField(max_length=8,unique=True,verbose_name='Institute ID')
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES)
    deemed_univ = models.CharField(max_length=1,choices=YESNO_CHOICES)
    university = models.ForeignKey(University)
    aicte_approv_status = models.CharField(max_length=1,choices=STATUS_CHOICES)
    streams = models.ManyToManyField(Stream)
    reg_date = models.DateField('registered_Date')
    aff_date = models.DateField('affiliated_Date')
    aff_expiry_date = models.DateField('affiliation_expiry_date')
    reg_addr_line1 = models.CharField(max_length=100,verbose_name='Registered Address Line 1')
    reg_addr_line2 = models.CharField(max_length=100,blank=True,verbose_name='Registered Address Line 2')
    cur_addr_line1 = models.CharField(max_length=100,blank=True,verbose_name='Current Address Line 1')
    cur_addr_line2 = models.CharField(max_length=100,blank=True,verbose_name='Current Address Line 2')
    reg_state = models.CharField(max_length=40,verbose_name='Registered State')
    cur_state = models.CharField(max_length=40,verbose_name='Current State')
    reg_pin = models.CharField(max_length=6,verbose_name='Registered PIN')
    cur_pin = models.CharField(max_length=6,verbose_name='Current PIN')
    accr_status = models.CharField(max_length=1,choices=AVAILABILITY_CHOICES,verbose_name='Accredition Status')
    last_accr_date = models.DateField('last_accredited_date')
    nominal_fee = models.DecimalField(max_digits=9,decimal_places=2)
    created_by = models.ForeignKey(user_model_label)
    created_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.name

class Application(models.Model):
    appln_id = models.CharField(max_length=255,unique=True,verbose_name='Application ID')
    user = models.ForeignKey(user_model_label, related_name='applications')
    institute = models.ForeignKey(Institute)
    stream = models.ForeignKey(Stream)
    priority_number = models.IntegerField(choices=PRIORITY_CHOICES, default=MEDIUM, db_index=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    last_updated_by = models.ForeignKey(user_model_label, related_name='applications_last_updated')
    def __unicode__(self):
        return self.appln_id
    