def getInstance():
'''public static MeasureFormat getInstance(final ULocale locale, final FormatWidth formatWidth)
public static MeasureFormat getInstance(final Locale locale, final FormatWidth formatWidth)
public static MeasureFormat getInstance(final ULocale locale, final FormatWidth formatWidth, final NumberFormat format)
public static MeasureFormat getInstance(final Locale locale, final FormatWidth formatWidth, final NumberFormat format)
'''
pass
def format():
'''public StringBuffer format(final Object obj, final StringBuffer toAppendTo, final FieldPosition fpos)
'''
pass
def parseObject():
'''public Measure parseObject(final String source, final ParsePosition pos)
'''
pass
def formatMeasures():
'''public final String formatMeasures(final Measure... measures)
public StringBuilder formatMeasures(final StringBuilder appendTo, final FieldPosition fpos, final Measure... measures)
'''
pass
def formatMeasurePerUnit():
'''public StringBuilder formatMeasurePerUnit(final Measure measure, final MeasureUnit perUnit, final StringBuilder appendTo, final FieldPosition pos)
'''
pass
def getUnitDisplayName():
'''public String getUnitDisplayName(final MeasureUnit unit)
'''
pass
def equals():
'''public final boolean equals(final Object other)
'''
pass
def hashCode():
'''public final int hashCode()
'''
pass
def getWidth():
'''public FormatWidth getWidth()
'''
pass
def getLocale():
'''public final ULocale getLocale()
'''
pass
def getNumberFormat():
'''public NumberFormat getNumberFormat()
'''
pass
def getCurrencyFormat():
'''public static MeasureFormat getCurrencyFormat(final ULocale locale)
public static MeasureFormat getCurrencyFormat(final Locale locale)
public static MeasureFormat getCurrencyFormat()
'''
pass
def getRangeFormat():
'''public static String getRangeFormat(final ULocale forLocale, final FormatWidth width)
'''
pass
def NumericFormatters():
'''public NumericFormatters(final String hourMinute, final String minuteSecond, final String hourMinuteSecond)
'''
pass
def getHourMinute():
'''public String getHourMinute()
'''
pass
def getMinuteSecond():
'''public String getMinuteSecond()
'''
pass
def getHourMinuteSecond():
'''public String getHourMinuteSecond()
'''
pass
def MeasureProxy():
'''public MeasureProxy(final ULocale locale, final FormatWidth width, final NumberFormat numberFormat, final int subClass)
public MeasureProxy()
'''
pass
def writeExternal():
'''public void writeExternal(final ObjectOutput out)
'''
pass
def readExternal():
'''public void readExternal(final ObjectInput in)
'''
pass
