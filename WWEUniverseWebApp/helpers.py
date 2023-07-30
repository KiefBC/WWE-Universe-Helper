MONTHS = [
    ('01', 'January'),
    ('02', 'February'),
    ('03', 'March'),
    ('04', 'April'),
    ('05', 'May'),
    ('06', 'June'),
    ('07', 'July'),
    ('08', 'August'),
    ('09', 'September'),
    ('10', 'October'),
    ('11', 'November'),
    ('12', 'December')
]

WEIGHT_CLASSES = [
    ('HW', 'Heavyweight'),
    ('CW', 'Cruiserweight'),
    ('LHW', 'Light Heavyweight'),
    ('SHW', 'Super Heavyweight')
]

DAYS_OF_WEEK = [
    ('MON', 'Monday'),
    ('TUE', 'Tuesday'),
    ('WED', 'Wednesday'),
    ('THU', 'Thursday'),
    ('FRI', 'Friday'),
    ('SAT', 'Saturday'),
    ('SUN', 'Sunday')
]

# A dictionary of days from 1 to 31
DAYS_OF_MONTH = [(str(day), str(day)) for day in range(1, 32)]

# A dictionary of years From 1970 to 2030
YEARS = [(str(year), str(year)) for year in range(1, 50)]