def ():
    '''returns GDateBuilder\n\n
    ()\n
    (final GDateSpecification gdate)\n
    (final CharSequence string)\n
    (final Calendar calendar)\n
    (final int year, final int month, final int day, final int hour, final int minute, final int second, final BigDecimal fraction)\n
    (final int year, final int month, final int day, final int hour, final int minute, final int second, final BigDecimal fraction, final int tzSign, final int tzHour, final int tzMinute)\n
    (final Date date)\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def toGDate():
    '''returns GDate\n\n
    toGDate()\n
    '''
def isImmutable():
    '''returns boolean\n\n
    isImmutable()\n
    '''
def getFlags():
    '''returns int\n\n
    getFlags()\n
    '''
def setYear():
    '''returns None\n\n
    setYear(final int year)\n
    '''
def setMonth():
    '''returns None\n\n
    setMonth(final int month)\n
    '''
def setDay():
    '''returns None\n\n
    setDay(final int day)\n
    '''
def setTime():
    '''returns None\n\n
    setTime(final int hour, final int minute, final int second, final BigDecimal fraction)\n
    '''
def setTimeZone():
    '''returns None\n\n
    setTimeZone(final int tzSign, final int tzHour, final int tzMinute)\n
    setTimeZone(int tzTotalMinutes)\n
    '''
def clearYear():
    '''returns None\n\n
    clearYear()\n
    '''
def clearMonth():
    '''returns None\n\n
    clearMonth()\n
    '''
def clearDay():
    '''returns None\n\n
    clearDay()\n
    '''
def clearTime():
    '''returns None\n\n
    clearTime()\n
    '''
def clearTimeZone():
    '''returns None\n\n
    clearTimeZone()\n
    '''
def isValid():
    '''returns boolean\n\n
    isValid()\n
    '''
def normalize():
    '''returns None\n\n
    normalize()\n
    '''
def normalizeToTimeZone():
    '''returns None\n\n
    normalizeToTimeZone(final int tzSign, final int tzHour, final int tzMinute)\n
    normalizeToTimeZone(int tzTotalMinutes)\n
    '''
def addGDuration():
    '''returns None\n\n
    addGDuration(final GDurationSpecification duration)\n
    '''
def subtractGDuration():
    '''returns None\n\n
    subtractGDuration(final GDurationSpecification duration)\n
    '''
def addDuration():
    '''returns None\n\n
    addDuration(final int sign, final int year, final int month, final int day, final int hour, final int minute, final int second, final BigDecimal fraction)\n
    '''
def setJulianDate():
    '''returns None\n\n
    setJulianDate(final int julianday)\n
    '''
def setDate():
    '''returns None\n\n
    setDate(final Date date)\n
    '''
def setGDate():
    '''returns None\n\n
    setGDate(final GDateSpecification gdate)\n
    '''
def getCalendar():
    '''returns XmlCalendar\n\n
    getCalendar()\n
    '''
def getDate():
    '''returns Date\n\n
    getDate()\n
    '''
def setBuiltinTypeCode():
    '''returns None\n\n
    setBuiltinTypeCode(final int typeCode)\n
    '''
def canonicalString():
    '''returns String\n\n
    canonicalString()\n
    '''
