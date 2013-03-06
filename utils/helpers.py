
import datetime
import decimal
import httplib
import math
import re
import sys
import urllib, urllib2
from xml.etree import ElementTree

from django.conf import settings
from django.core.mail import mail_admins, EmailMultiAlternatives
from django.utils import simplejson
from django.template.loader import render_to_string

class DecimalEncoder(simplejson.JSONEncoder):
    """JSON encoder which understands decimals."""

    def default(self, obj):
        '''Convert object to JSON encodable type.'''
        if isinstance(obj, decimal.Decimal):
            return int(obj)
        return simplejson.JSONEncoder.default(self, obj)
