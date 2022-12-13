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
pass
def getDateInstance():
'''public static FastDateFormat getDateInstance(final int style)
public static FastDateFormat getDateInstance(final int style, final Locale locale)
public static FastDateFormat getDateInstance(final int style, final TimeZone timeZone)
public static FastDateFormat getDateInstance(final int style, final TimeZone timeZone, final Locale locale)
'''
pass
def getTimeInstance():
'''public static FastDateFormat getTimeInstance(final int style)
public static FastDateFormat getTimeInstance(final int style, final Locale locale)
public static FastDateFormat getTimeInstance(final int style, final TimeZone timeZone)
public static FastDateFormat getTimeInstance(final int style, final TimeZone timeZone, final Locale locale)
'''
pass
def getDateTimeInstance():
'''public static FastDateFormat getDateTimeInstance(final int dateStyle, final int timeStyle)
public static FastDateFormat getDateTimeInstance(final int dateStyle, final int timeStyle, final Locale locale)
public static FastDateFormat getDateTimeInstance(final int dateStyle, final int timeStyle, final TimeZone timeZone)
public static FastDateFormat getDateTimeInstance(final int dateStyle, final int timeStyle, final TimeZone timeZone, final Locale locale)
'''
pass
def format():
'''public StringBuffer format(final Object obj, final StringBuffer toAppendTo, final FieldPosition pos)
public String format(final long millis)
public String format(final Date date)
public String format(final Calendar calendar)
public StringBuffer format(final long millis, final StringBuffer buf)
public StringBuffer format(final Date date, final StringBuffer buf)
public StringBuffer format(final Calendar calendar, final StringBuffer buf)
'''
pass
def parse():
'''public Date parse(final String source)
public Date parse(final String source, final ParsePosition pos)
'''
pass
def parseObject():
'''public Object parseObject(final String source, final ParsePosition pos)
'''
pass
def getPattern():
'''public String getPattern()
'''
pass
def getTimeZone():
'''public TimeZone getTimeZone()
'''
pass
def getLocale():
'''public Locale getLocale()
'''
pass
def getMaxLengthEstimate():
'''public int getMaxLengthEstimate()
'''
pass
def equals():
'''public boolean equals(final Object obj)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def toString():
'''public String toString()
'''
pass
