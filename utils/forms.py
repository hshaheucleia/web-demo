
from django.forms import *


class SmallTextarea(Textarea):
    pass


class CharField(CharField):
    pass
    """def widget_attrs(self, widget):
        attrs = super(CharField, self).widget_attrs(widget) or {}
        if isinstance(widget, SmallTextarea):
            attrs.update({'class': 'textarea', 'rows': 2, 'cols': 30})
        elif isinstance(widget, Textarea):
            #attrs.setdefault('class', 'textarea')
            #attrs.setdefault('rows', 5)
            #attrs.setdefault('cols', 30)
            #attrs.update(widget.attrs)
        else:
            attrs.update({'class': 'textbox_25'})
        return attrs"""


class EmailField(EmailField):
    pass
    '''def widget_attrs(self, widget):
        attrs = super(EmailField, self).widget_attrs(widget) or {}
        attrs.update({'class': 'textbox_25 email'})
        return attrs'''


class ChoiceField(ChoiceField):
    pass
    '''def widget_attrs(self, widget):
        attrs = super(ChoiceField, self).widget_attrs(widget) or {}
        attrs.update({'class': 'dropdown_25'})
        return attrs'''


class DateField(DateField):
    pass
    #widget = DateInput(format='%d/%m/%Y')

    '''def __init__(self, allow_past=False, *args, **kwargs):
        kwargs['input_formats'] = ['%d/%m/%Y']
        self.allow_past = allow_past
        super(DateField, self).__init__(*args, **kwargs)

    def widget_attrs(self, widget):
        attrs = super(DateField, self).widget_attrs(widget) or {}
        if self.allow_past:
            attrs.update({'class': 'textbox_25 pastdatefield', 'readonly': 'readonly', 'autocomplete': 'off'})
        else:
            attrs.update({'class': 'textbox_25 datefield', 'readonly': 'readonly', 'autocomplete': 'off'})
        return attrs'''


class DecimalField(DecimalField):
    pass
    '''def widget_attrs(self, widget):
        attrs = super(DecimalField, self).widget_attrs(widget) or {}
        attrs.update({'class': 'textbox_25'})
        return attrs'''


class IntegerField(DecimalField):
    pass
    '''def widget_attrs(self, widget):
        attrs = super(DecimalField, self).widget_attrs(widget) or {}
        attrs.update({'class': 'textbox_25'})
        return attrs'''


class ModelChoiceField(ModelChoiceField):
    pass
    '''def widget_attrs(self, widget):
        attrs = super(ModelChoiceField, self).widget_attrs(widget) or {}
        attrs.update({'class': 'dropdown_25'})
        return attrs'''


class BooleanField(BooleanField):
    pass
    '''def widget_attrs(self, widget):
        attrs = super(BooleanField, self).widget_attrs(widget) or {}
        attrs.update({'class': ''})
        return attrs'''


class NumericMathField(RegexField):
    '''
        Field to take Numeric equations as input
        ex: 180 + 10 * 13
    '''
    def __init__(self, *args, **kwargs):
        # Allow numbers, brackets and math operators
        regex = r'^[0-9+*-/() ]+$'
        super(NumericMathField, self).__init__(regex, *args, **kwargs)

    def clean(self, value):
        self.validate(value)
        self.run_validators(value)

        if not value:
            return value

        try:
            eval(value)
            return value
        except:
            raise ValidationError(self.error_messages['invalid'])

    def widget_attrs(self, widget):
        attrs = super(NumericMathField, self).widget_attrs(widget) or {}
        attrs.update({'class': 'textbox_25'})
        return attrs


class PhoneNumberField(RegexField):
    def __init__(self, *args, **kwargs):
        # regex
        # 0 or one '+' at the begining of the number and
        # followed by 10 or more digits
        regex = '^[+]?\d{10,}$'
        super(PhoneNumberField, self).__init__(regex, *args, **kwargs)

    def widget_attrs(self, widget):
        attrs = super(PhoneNumberField, self).widget_attrs(widget) or {}
        #attrs.update({'class': 'textbox_25'})
        return attrs
