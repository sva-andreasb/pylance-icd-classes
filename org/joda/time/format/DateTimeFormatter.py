def DateTimeFormatter():
    '''public DateTimeFormatter(final DateTimePrinter dateTimePrinter, final DateTimeParser dateTimeParser)
    '''
def isPrinter():
    '''public boolean isPrinter()
    '''
def getPrinter():
    '''public DateTimePrinter getPrinter()
    '''
def isParser():
    '''public boolean isParser()
    '''
def getParser():
    '''public DateTimeParser getParser()
    '''
def withLocale():
    '''public DateTimeFormatter withLocale(final Locale locale)
    '''
def getLocale():
    '''public Locale getLocale()
    '''
def withOffsetParsed():
    '''public DateTimeFormatter withOffsetParsed()
    '''
def isOffsetParsed():
    '''public boolean isOffsetParsed()
    '''
def withChronology():
    '''public DateTimeFormatter withChronology(final Chronology chronology)
    '''
def getChronology():
    '''public Chronology getChronology()
    '''
def getChronolgy():
    '''public Chronology getChronolgy()
    '''
def withZoneUTC():
    '''public DateTimeFormatter withZoneUTC()
    '''
def withZone():
    '''public DateTimeFormatter withZone(final DateTimeZone dateTimeZone)
    '''
def getZone():
    '''public DateTimeZone getZone()
    '''
def withPivotYear():
    '''public DateTimeFormatter withPivotYear(final Integer obj)
    public DateTimeFormatter withPivotYear(final int i)
    '''
def getPivotYear():
    '''public Integer getPivotYear()
    '''
def withDefaultYear():
    '''public DateTimeFormatter withDefaultYear(final int n)
    '''
def getDefaultYear():
    '''public int getDefaultYear()
    '''
def printTo():
    '''public void printTo(final StringBuffer sb, final ReadableInstant readableInstant)
    public void printTo(final Writer writer, final ReadableInstant readableInstant)
    public void printTo(final Appendable appendable, final ReadableInstant readableInstant)
    public void printTo(final StringBuffer sb, final long n)
    public void printTo(final Writer writer, final long n)
    public void printTo(final Appendable appendable, final long n)
    public void printTo(final StringBuffer sb, final ReadablePartial readablePartial)
    public void printTo(final Writer writer, final ReadablePartial readablePartial)
    public void printTo(final Appendable appendable, final ReadablePartial readablePartial)
    '''
def print():
    '''public String print(final ReadableInstant readableInstant)
    public String print(final long n)
    public String print(final ReadablePartial readablePartial)
    '''
def parseInto():
    '''public int parseInto(final ReadWritableInstant readWritableInstant, final String s, final int n)
    '''
def parseMillis():
    '''public long parseMillis(final String s)
    '''
def parseLocalDate():
    '''public LocalDate parseLocalDate(final String s)
    '''
def parseLocalTime():
    '''public LocalTime parseLocalTime(final String s)
    '''
def parseLocalDateTime():
    '''public LocalDateTime parseLocalDateTime(final String s)
    '''
def parseDateTime():
    '''public DateTime parseDateTime(final String s)
    '''
def parseMutableDateTime():
    '''public MutableDateTime parseMutableDateTime(final String s)
    '''
