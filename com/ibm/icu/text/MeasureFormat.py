def getInstance():
    '''    public static MeasureFormat getInstance(final ULocale locale, final FormatWidth formatWidth)
    public static MeasureFormat getInstance(final Locale locale, final FormatWidth formatWidth)
    public static MeasureFormat getInstance(final ULocale locale, final FormatWidth formatWidth, final NumberFormat format)
    public static MeasureFormat getInstance(final Locale locale, final FormatWidth formatWidth, final NumberFormat format)
    '''
def format():
    '''    public StringBuffer format(final Object obj, final StringBuffer toAppendTo, final FieldPosition fpos)
    '''
def parseObject():
    '''    public Measure parseObject(final String source, final ParsePosition pos)
    '''
def formatMeasures():
    '''    public final String formatMeasures(final Measure... measures)
    public StringBuilder formatMeasures(final StringBuilder appendTo, final FieldPosition fpos, final Measure... measures)
    '''
def formatMeasurePerUnit():
    '''    public StringBuilder formatMeasurePerUnit(final Measure measure, final MeasureUnit perUnit, final StringBuilder appendTo, final FieldPosition pos)
    '''
def getUnitDisplayName():
    '''    public String getUnitDisplayName(final MeasureUnit unit)
    '''
def equals():
    '''    public final boolean equals(final Object other)
    '''
def hashCode():
    '''    public final int hashCode()
    '''
def getWidth():
    '''    public FormatWidth getWidth()
    '''
def getLocale():
    '''    public final ULocale getLocale()
    '''
def getNumberFormat():
    '''    public NumberFormat getNumberFormat()
    '''
def getCurrencyFormat():
    '''    public static MeasureFormat getCurrencyFormat(final ULocale locale)
    public static MeasureFormat getCurrencyFormat(final Locale locale)
    public static MeasureFormat getCurrencyFormat()
    '''
def getRangeFormat():
    '''    public static String getRangeFormat(final ULocale forLocale, final FormatWidth width)
    '''
def NumericFormatters():
    '''    public NumericFormatters(final String hourMinute, final String minuteSecond, final String hourMinuteSecond)
    '''
def getHourMinute():
    '''    public String getHourMinute()
    '''
def getMinuteSecond():
    '''    public String getMinuteSecond()
    '''
def getHourMinuteSecond():
    '''    public String getHourMinuteSecond()
    '''
def MeasureProxy():
    '''    public MeasureProxy(final ULocale locale, final FormatWidth width, final NumberFormat numberFormat, final int subClass)
    public MeasureProxy()
    '''
def writeExternal():
    '''    public void writeExternal(final ObjectOutput out)
    '''
def readExternal():
    '''    public void readExternal(final ObjectInput in)
    '''
