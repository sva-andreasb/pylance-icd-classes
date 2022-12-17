def ():
    '''returns LocalTime\n\n
    ()\n
    (final DateTimeZone dateTimeZone)\n
    (final Chronology chronology)\n
    (final long n)\n
    (final long n, final DateTimeZone dateTimeZone)\n
    (final long n, Chronology iChronology)\n
    (final Object o)\n
    (final Object o, final DateTimeZone dateTimeZone)\n
    (final Object o, Chronology chronology)\n
    (final int n, final int n2)\n
    (final int n, final int n2, final int n3)\n
    (final int n, final int n2, final int n3, final int n4)\n
    (final int n, final int n2, final int n3, final int n4, Chronology withUTC)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def getValue():
    '''returns int\n\n
    getValue(final int i)\n
    '''
def get():
    '''returns int\n\n
    get(final DateTimeFieldType obj)\n
    '''
def isSupported():
    '''returns boolean\n\n
    isSupported(final DateTimeFieldType dateTimeFieldType)\n
    isSupported(final DurationFieldType durationFieldType)\n
    '''
def getChronology():
    '''returns Chronology\n\n
    getChronology()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final ReadablePartial readablePartial)\n
    '''
def withFields():
    '''returns LocalTime\n\n
    withFields(final ReadablePartial readablePartial)\n
    '''
def withField():
    '''returns LocalTime\n\n
    withField(final DateTimeFieldType obj, final int n)\n
    '''
def withFieldAdded():
    '''returns LocalTime\n\n
    withFieldAdded(final DurationFieldType obj, final int n)\n
    '''
def withPeriodAdded():
    '''returns LocalTime\n\n
    withPeriodAdded(final ReadablePeriod readablePeriod, final int n)\n
    '''
def plus():
    '''returns LocalTime\n\n
    plus(final ReadablePeriod readablePeriod)\n
    '''
def plusHours():
    '''returns LocalTime\n\n
    plusHours(final int n)\n
    '''
def plusMinutes():
    '''returns LocalTime\n\n
    plusMinutes(final int n)\n
    '''
def plusSeconds():
    '''returns LocalTime\n\n
    plusSeconds(final int n)\n
    '''
def plusMillis():
    '''returns LocalTime\n\n
    plusMillis(final int n)\n
    '''
def minus():
    '''returns LocalTime\n\n
    minus(final ReadablePeriod readablePeriod)\n
    '''
def minusHours():
    '''returns LocalTime\n\n
    minusHours(final int n)\n
    '''
def minusMinutes():
    '''returns LocalTime\n\n
    minusMinutes(final int n)\n
    '''
def minusSeconds():
    '''returns LocalTime\n\n
    minusSeconds(final int n)\n
    '''
def minusMillis():
    '''returns LocalTime\n\n
    minusMillis(final int n)\n
    '''
def property():
    '''returns Property\n\n
    property(final DateTimeFieldType obj)\n
    '''
def getHourOfDay():
    '''returns int\n\n
    getHourOfDay()\n
    '''
def getMinuteOfHour():
    '''returns int\n\n
    getMinuteOfHour()\n
    '''
def getSecondOfMinute():
    '''returns int\n\n
    getSecondOfMinute()\n
    '''
def getMillisOfSecond():
    '''returns int\n\n
    getMillisOfSecond()\n
    '''
def getMillisOfDay():
    '''returns int\n\n
    getMillisOfDay()\n
    '''
def withHourOfDay():
    '''returns LocalTime\n\n
    withHourOfDay(final int n)\n
    '''
def withMinuteOfHour():
    '''returns LocalTime\n\n
    withMinuteOfHour(final int n)\n
    '''
def withSecondOfMinute():
    '''returns LocalTime\n\n
    withSecondOfMinute(final int n)\n
    '''
def withMillisOfSecond():
    '''returns LocalTime\n\n
    withMillisOfSecond(final int n)\n
    '''
def withMillisOfDay():
    '''returns LocalTime\n\n
    withMillisOfDay(final int n)\n
    '''
def hourOfDay():
    '''returns Property\n\n
    hourOfDay()\n
    '''
def minuteOfHour():
    '''returns Property\n\n
    minuteOfHour()\n
    '''
def secondOfMinute():
    '''returns Property\n\n
    secondOfMinute()\n
    '''
def millisOfSecond():
    '''returns Property\n\n
    millisOfSecond()\n
    '''
def millisOfDay():
    '''returns Property\n\n
    millisOfDay()\n
    '''
def toDateTimeToday():
    '''returns DateTime\n\n
    toDateTimeToday()\n
    toDateTimeToday(final DateTimeZone dateTimeZone)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString(final String s)\n
    toString(final String s, final Locale locale)\n
    '''
def getField():
    '''returns DateTimeField\n\n
    getField()\n
    '''
def getLocalTime():
    '''returns LocalTime\n\n
    getLocalTime()\n
    '''
def addCopy():
    '''returns LocalTime\n\n
    addCopy(final int n)\n
    addCopy(final long n)\n
    '''
def addNoWrapToCopy():
    '''returns LocalTime\n\n
    addNoWrapToCopy(final int n)\n
    '''
def addWrapFieldToCopy():
    '''returns LocalTime\n\n
    addWrapFieldToCopy(final int n)\n
    '''
def setCopy():
    '''returns LocalTime\n\n
    setCopy(final int n)\n
    setCopy(final String s, final Locale locale)\n
    setCopy(final String s)\n
    '''
def withMaximumValue():
    '''returns LocalTime\n\n
    withMaximumValue()\n
    '''
def withMinimumValue():
    '''returns LocalTime\n\n
    withMinimumValue()\n
    '''
def roundFloorCopy():
    '''returns LocalTime\n\n
    roundFloorCopy()\n
    '''
def roundCeilingCopy():
    '''returns LocalTime\n\n
    roundCeilingCopy()\n
    '''
def roundHalfFloorCopy():
    '''returns LocalTime\n\n
    roundHalfFloorCopy()\n
    '''
def roundHalfCeilingCopy():
    '''returns LocalTime\n\n
    roundHalfCeilingCopy()\n
    '''
def roundHalfEvenCopy():
    '''returns LocalTime\n\n
    roundHalfEvenCopy()\n
    '''
