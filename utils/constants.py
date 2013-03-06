
HOURS = [(0, 12)] + [(h, h if h < 13 else h - 12) for h in range(1, 24)]
MINUTES = range(0, 60, 15)

TIME_CHOICES = [('%02d:%02d' % (h[0], m), '%02d:%02d %s' % (h[1], m, 'AM' if h[0] < 12 else 'PM'))
                for h in HOURS for m in MINUTES]

OPTIONAL_TIME_CHOICES = [('', '-- Select Time --')] + TIME_CHOICES
