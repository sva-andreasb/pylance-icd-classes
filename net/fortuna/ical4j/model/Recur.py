SECONDLY = "String  \"SECONDLY\""
MINUTELY = "String  \"MINUTELY\""
HOURLY = "String  \"HOURLY\""
DAILY = "String  \"DAILY\""
WEEKLY = "String  \"WEEKLY\""
MONTHLY = "String  \"MONTHLY\""
YEARLY = "String  \"YEARLY\""
KEY_MAX_INCREMENT_COUNT = "String  \"net.fortuna.ical4j.recur.maxincrementcount\""
def ():
    '''returns Recur\n\n
    (final String aValue)\n
    (final String frequency, final Date until)\n
    (final Frequency frequency, final Date until)\n
    (final String frequency, final int count)\n
    (final Frequency frequency, final int count)\n
    '''
def frequency():
    '''returns Builder\n\n
    frequency(final Frequency frequency)\n
    '''
def until():
    '''returns Builder\n\n
    until(final Date until)\n
    '''
def count():
    '''returns Builder\n\n
    count(final Integer count)\n
    '''
def interval():
    '''returns Builder\n\n
    interval(final Integer interval)\n
    '''
def secondList():
    '''returns Builder\n\n
    secondList(final NumberList secondList)\n
    '''
def minuteList():
    '''returns Builder\n\n
    minuteList(final NumberList minuteList)\n
    '''
def hourList():
    '''returns Builder\n\n
    hourList(final NumberList hourList)\n
    '''
def dayList():
    '''returns Builder\n\n
    dayList(final WeekDayList dayList)\n
    '''
def monthDayList():
    '''returns Builder\n\n
    monthDayList(final NumberList monthDayList)\n
    '''
def yearDayList():
    '''returns Builder\n\n
    yearDayList(final NumberList yearDayList)\n
    '''
def weekNoList():
    '''returns Builder\n\n
    weekNoList(final NumberList weekNoList)\n
    '''
def monthList():
    '''returns Builder\n\n
    monthList(final NumberList monthList)\n
    '''
def setPosList():
    '''returns Builder\n\n
    setPosList(final NumberList setPosList)\n
    '''
def weekStartDay():
    '''returns Builder\n\n
    weekStartDay(final WeekDay.Day weekStartDay)\n
    '''
def build():
    '''returns Recur\n\n
    build()\n
    '''
