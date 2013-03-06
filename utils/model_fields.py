
from django.core.validators import validate_email
from django.db import models


def validate_comma_separated_email_list(value):
    emails = value.split(',')
    for email in emails:
        validate_email(email)


class CommaSeparatedEmailField(models.CharField):
    default_validators = [validate_comma_separated_email_list]
    description = "Comma-separated emails"

    def formfield(self, **kwargs):
        defaults = {
            'error_messages': {
                'invalid': 'Enter valid email-ids separated by commas.',
            }
        }
        defaults.update(kwargs)
        return super(CommaSeparatedEmailField, self).formfield(**defaults)
