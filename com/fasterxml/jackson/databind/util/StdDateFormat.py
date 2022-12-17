DATE_FORMAT_STR_ISO8601 = "String  \"yyyy-MM-dd'T'HH:mm:ss.SSSZ\""
def ():
    '''returns StdDateFormat\n\n
    ()\n
    (final TimeZone tz, final Locale loc)\n
    '''
def withTimeZone():
    '''returns StdDateFormat\n\n
    withTimeZone(TimeZone tz)\n
    '''
def withLocale():
    '''returns StdDateFormat\n\n
    withLocale(final Locale loc)\n
    '''
def withLenient():
    '''returns StdDateFormat\n\n
    withLenient(final Boolean b)\n
    '''
def withColonInTimeZone():
    '''returns StdDateFormat\n\n
    withColonInTimeZone(final boolean b)\n
    '''
def clone():
    '''returns StdDateFormat\n\n
    clone()\n
    '''
def getTimeZone():
    '''returns TimeZone\n\n
    getTimeZone()\n
    '''
def setTimeZone():
    '''returns None\n\n
    setTimeZone(final TimeZone tz)\n
    '''
def setLenient():
    '''returns None\n\n
    setLenient(final boolean enabled)\n
    '''
def isLenient():
    '''returns boolean\n\n
    isLenient()\n
    '''
def isColonIncludedInTimeZone():
    '''returns boolean\n\n
    isColonIncludedInTimeZone()\n
    '''
def parse():
    '''returns Date\n\n
    parse(String dateStr)\n
    parse(final String dateStr, final ParsePosition pos)\n
    '''
def format():
    '''returns StringBuffer\n\n
    format(final Date date, final StringBuffer toAppendTo, final FieldPosition fieldPosition)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def toPattern():
    '''returns String\n\n
    toPattern()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
