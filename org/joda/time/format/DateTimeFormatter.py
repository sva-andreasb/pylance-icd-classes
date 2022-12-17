def ():
    '''returns DateTimeFormatter\n\n
    (final DateTimePrinter dateTimePrinter, final DateTimeParser dateTimeParser)\n
    '''
def isPrinter():
    '''returns boolean\n\n
    isPrinter()\n
    '''
def getPrinter():
    '''returns DateTimePrinter\n\n
    getPrinter()\n
    '''
def isParser():
    '''returns boolean\n\n
    isParser()\n
    '''
def getParser():
    '''returns DateTimeParser\n\n
    getParser()\n
    '''
def withLocale():
    '''returns DateTimeFormatter\n\n
    withLocale(final Locale locale)\n
    '''
def getLocale():
    '''returns Locale\n\n
    getLocale()\n
    '''
def withOffsetParsed():
    '''returns DateTimeFormatter\n\n
    withOffsetParsed()\n
    '''
def isOffsetParsed():
    '''returns boolean\n\n
    isOffsetParsed()\n
    '''
def withChronology():
    '''returns DateTimeFormatter\n\n
    withChronology(final Chronology chronology)\n
    '''
def getChronology():
    '''returns Chronology\n\n
    getChronology()\n
    '''
def getChronolgy():
    '''returns Chronology\n\n
    getChronolgy()\n
    '''
def withZoneUTC():
    '''returns DateTimeFormatter\n\n
    withZoneUTC()\n
    '''
def withZone():
    '''returns DateTimeFormatter\n\n
    withZone(final DateTimeZone dateTimeZone)\n
    '''
def getZone():
    '''returns DateTimeZone\n\n
    getZone()\n
    '''
def withPivotYear():
    '''returns DateTimeFormatter\n\n
    withPivotYear(final Integer obj)\n
    withPivotYear(final int i)\n
    '''
def getPivotYear():
    '''returns Integer\n\n
    getPivotYear()\n
    '''
def withDefaultYear():
    '''returns DateTimeFormatter\n\n
    withDefaultYear(final int n)\n
    '''
def getDefaultYear():
    '''returns int\n\n
    getDefaultYear()\n
    '''
def printTo():
    '''returns None\n\n
    printTo(final StringBuffer sb, final ReadableInstant readableInstant)\n
    printTo(final Writer writer, final ReadableInstant readableInstant)\n
    printTo(final Appendable appendable, final ReadableInstant readableInstant)\n
    printTo(final StringBuffer sb, final long n)\n
    printTo(final Writer writer, final long n)\n
    printTo(final Appendable appendable, final long n)\n
    printTo(final StringBuffer sb, final ReadablePartial readablePartial)\n
    printTo(final Writer writer, final ReadablePartial readablePartial)\n
    printTo(final Appendable appendable, final ReadablePartial readablePartial)\n
    '''
def print():
    '''returns String\n\n
    print(final ReadableInstant readableInstant)\n
    print(final long n)\n
    print(final ReadablePartial readablePartial)\n
    '''
def parseInto():
    '''returns int\n\n
    parseInto(final ReadWritableInstant readWritableInstant, final String s, final int n)\n
    '''
def parseMillis():
    '''returns long\n\n
    parseMillis(final String s)\n
    '''
def parseLocalDate():
    '''returns LocalDate\n\n
    parseLocalDate(final String s)\n
    '''
def parseLocalTime():
    '''returns LocalTime\n\n
    parseLocalTime(final String s)\n
    '''
def parseLocalDateTime():
    '''returns LocalDateTime\n\n
    parseLocalDateTime(final String s)\n
    '''
def parseDateTime():
    '''returns DateTime\n\n
    parseDateTime(final String s)\n
    '''
def parseMutableDateTime():
    '''returns MutableDateTime\n\n
    parseMutableDateTime(final String s)\n
    '''
