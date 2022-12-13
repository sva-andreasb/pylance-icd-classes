FULL = "int  0"
LONG = "int  1"
MEDIUM = "int  2"
SHORT = "int  3"
def getInstance():
    '''public static FastDateFormat getInstance()
    public static FastDateFormat getInstance(final String pattern)
    public static FastDateFormat getInstance(final String pattern, final TimeZone timeZone)
    public static FastDateFormat getInstance(final String pattern, final Locale locale)
    public static FastDateFormat getInstance(final String pattern, final TimeZone timeZone, final Locale locale)
    '''
def getDateInstance():
    '''public static FastDateFormat getDateInstance(final int style)
    public static FastDateFormat getDateInstance(final int style, final Locale locale)
    public static FastDateFormat getDateInstance(final int style, final TimeZone timeZone)
    public static FastDateFormat getDateInstance(final int style, final TimeZone timeZone, final Locale locale)
    '''
def getTimeInstance():
    '''public static FastDateFormat getTimeInstance(final int style)
    public static FastDateFormat getTimeInstance(final int style, final Locale locale)
    public static FastDateFormat getTimeInstance(final int style, final TimeZone timeZone)
    public static FastDateFormat getTimeInstance(final int style, final TimeZone timeZone, final Locale locale)
    '''
def getDateTimeInstance():
    '''public static FastDateFormat getDateTimeInstance(final int dateStyle, final int timeStyle)
    public static FastDateFormat getDateTimeInstance(final int dateStyle, final int timeStyle, final Locale locale)
    public static FastDateFormat getDateTimeInstance(final int dateStyle, final int timeStyle, final TimeZone timeZone)
    public static FastDateFormat getDateTimeInstance(final int dateStyle, final int timeStyle, final TimeZone timeZone, final Locale locale)
    '''
def format():
    '''public StringBuilder format(final Object obj, final StringBuilder toAppendTo, final FieldPosition pos)
    public String format(final long millis)
    public String format(final Date date)
    public String format(final Calendar calendar)
    public <B extends Appendable> B format(final long millis, final B buf)
    public <B extends Appendable> B format(final Date date, final B buf)
    public <B extends Appendable> B format(final Calendar calendar, final B buf)
    '''
def parse():
    '''public Date parse(final String source)
    public Date parse(final String source, final ParsePosition pos)
    public boolean parse(final String source, final ParsePosition pos, final Calendar calendar)
    '''
def parseObject():
    '''public Object parseObject(final String source, final ParsePosition pos)
    '''
def getPattern():
    '''public String getPattern()
    '''
def getTimeZone():
    '''public TimeZone getTimeZone()
    '''
def getLocale():
    '''public Locale getLocale()
    '''
def getMaxLengthEstimate():
    '''public int getMaxLengthEstimate()
    '''
def equals():
    '''public boolean equals(final Object obj)
    '''
def hashCode():
    '''public int hashCode()
    '''
def toString():
    '''public String toString()
    '''
