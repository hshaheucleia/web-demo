
HOURS = [(0, 12)] + [(h, h if h < 13 else h - 12) for h in range(1, 24)]
MINUTES = range(0, 60, 15)

TIME_CHOICES = [('%02d:%02d' % (h[0], m), '%02d:%02d %s' % (h[1], m, 'AM' if h[0] < 12 else 'PM'))
                for h in HOURS for m in MINUTES]

OPTIONAL_TIME_CHOICES = [('', '-- Select Time --')] + TIME_CHOICES

STATE_CHOICES = [('AP', 'Andhra Pradesh'),
                ('AR', 'Arunachal Pradesh'),
                ('AS', 'Assam'),
                ('BR', 'Bihar'),
                ('CT', 'Chhattisgarh'),
                ('GA', 'Goa'),
                ('GJ', 'Gujarat'),
                ('HR', 'Haryana'),
                ('HP', 'Himachal Pradesh'),
                ('JK', 'Jammu & Kashmir'),
                ('JH', 'Jharkhand'),
                ('KA', 'Karnataka'),
                ('KL', 'Kerala'),
                ('MP', 'Madhya Pradesh'),
                ('MH', 'Maharashtra'),
                ('MN', 'Manipur'),
                ('ML', 'Meghalaya'),
                ('MZ', 'Mizoram'),
                ('NL', 'Nagaland'),
                ('OR', 'Odisha'),
                ('PB', 'Punjab'),
                ('RJ', 'Rajasthan'),
                ('SK', 'Sikkim'),
                ('TN', 'Tamil Nadu'),
                ('TR', 'Tripura'),
                ('UK', 'Uttarakhand'),
                ('UP', 'Uttar Pradesh'),
                ('WB', 'West Bengal'),
                ('AN', 'Andaman & Nicobar'),
                ('CH', 'Chandigarh'),
                ('DN', 'Dadra and Nagar Haveli'),
                ('DD', 'Daman & Diu'),
                ('DL', 'Delhi'),
                ('LD', 'Lakshadweep'),
                ('PY', 'Puducherry')]


EXAM_COVERAGE_CHOICES = [('IN','All India')] + STATE_CHOICES
