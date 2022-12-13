def SimpleDateFormat():
'''public SimpleDateFormat()
public SimpleDateFormat(final String pattern)
public SimpleDateFormat(final String pattern, final Locale loc)
public SimpleDateFormat(final String pattern, final ULocale loc)
public SimpleDateFormat(final String pattern, final String override, final ULocale loc)
public SimpleDateFormat(final String pattern, final DateFormatSymbols formatData)
public SimpleDateFormat(final String pattern, final DateFormatSymbols formatData, final ULocale loc)
'''
pass
def getInstance():
'''public static SimpleDateFormat getInstance(final Calendar.FormatConfiguration formatConfig)
'''
pass
def set2DigitYearStart():
'''public void set2DigitYearStart(final Date startDate)
'''
pass
def get2DigitYearStart():
'''public Date get2DigitYearStart()
'''
pass
def setContext():
'''public void setContext(final DisplayContext context)
'''
pass
def format():
'''public StringBuffer format(final Calendar cal, final StringBuffer toAppendTo, final FieldPosition pos)
'''
pass
def setNumberFormat():
'''public void setNumberFormat(final NumberFormat newNumberFormat)
public void setNumberFormat(final String fields, final NumberFormat overrideNF)
'''
pass
def parse():
'''public void parse(final String text, Calendar cal, final ParsePosition parsePos)
'''
pass
def toPattern():
'''public String toPattern()
'''
pass
def toLocalizedPattern():
'''public String toLocalizedPattern()
'''
pass
def applyPattern():
'''public void applyPattern(final String pat)
'''
pass
def applyLocalizedPattern():
'''public void applyLocalizedPattern(final String pat)
'''
pass
def getDateFormatSymbols():
'''public DateFormatSymbols getDateFormatSymbols()
'''
pass
def setDateFormatSymbols():
'''public void setDateFormatSymbols(final DateFormatSymbols newFormatSymbols)
'''
pass
def getTimeZoneFormat():
'''public TimeZoneFormat getTimeZoneFormat()
'''
pass
def setTimeZoneFormat():
'''public void setTimeZoneFormat(final TimeZoneFormat tzfmt)
'''
pass
def clone():
'''public Object clone()
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def equals():
'''public boolean equals(final Object obj)
'''
pass
def formatToCharacterIterator():
'''public AttributedCharacterIterator formatToCharacterIterator(final Object obj)
'''
pass
def intervalFormatByAlgorithm():
'''public final StringBuffer intervalFormatByAlgorithm(final Calendar fromCalendar, final Calendar toCalendar, final StringBuffer appendTo, final FieldPosition pos)
'''
pass
def getNumberFormat():
'''public NumberFormat getNumberFormat(final char field)
'''
pass
