def SimpleDateFormat():
    '''    public SimpleDateFormat()
    public SimpleDateFormat(final String pattern)
    public SimpleDateFormat(final String pattern, final Locale loc)
    public SimpleDateFormat(final String pattern, final ULocale loc)
    public SimpleDateFormat(final String pattern, final String override, final ULocale loc)
    public SimpleDateFormat(final String pattern, final DateFormatSymbols formatData)
    public SimpleDateFormat(final String pattern, final DateFormatSymbols formatData, final ULocale loc)
    '''
def getInstance():
    '''    public static SimpleDateFormat getInstance(final Calendar.FormatConfiguration formatConfig)
    '''
def set2DigitYearStart():
    '''    public void set2DigitYearStart(final Date startDate)
    '''
def get2DigitYearStart():
    '''    public Date get2DigitYearStart()
    '''
def setContext():
    '''    public void setContext(final DisplayContext context)
    '''
def format():
    '''    public StringBuffer format(final Calendar cal, final StringBuffer toAppendTo, final FieldPosition pos)
    '''
def setNumberFormat():
    '''    public void setNumberFormat(final NumberFormat newNumberFormat)
    public void setNumberFormat(final String fields, final NumberFormat overrideNF)
    '''
def parse():
    '''    public void parse(final String text, Calendar cal, final ParsePosition parsePos)
    '''
def toPattern():
    '''    public String toPattern()
    '''
def toLocalizedPattern():
    '''    public String toLocalizedPattern()
    '''
def applyPattern():
    '''    public void applyPattern(final String pat)
    '''
def applyLocalizedPattern():
    '''    public void applyLocalizedPattern(final String pat)
    '''
def getDateFormatSymbols():
    '''    public DateFormatSymbols getDateFormatSymbols()
    '''
def setDateFormatSymbols():
    '''    public void setDateFormatSymbols(final DateFormatSymbols newFormatSymbols)
    '''
def getTimeZoneFormat():
    '''    public TimeZoneFormat getTimeZoneFormat()
    '''
def setTimeZoneFormat():
    '''    public void setTimeZoneFormat(final TimeZoneFormat tzfmt)
    '''
def clone():
    '''    public Object clone()
    '''
def hashCode():
    '''    public int hashCode()
    '''
def equals():
    '''    public boolean equals(final Object obj)
    '''
def formatToCharacterIterator():
    '''    public AttributedCharacterIterator formatToCharacterIterator(final Object obj)
    '''
def intervalFormatByAlgorithm():
    '''    public final StringBuffer intervalFormatByAlgorithm(final Calendar fromCalendar, final Calendar toCalendar, final StringBuffer appendTo, final FieldPosition pos)
    '''
def getNumberFormat():
    '''    public NumberFormat getNumberFormat(final char field)
    '''
