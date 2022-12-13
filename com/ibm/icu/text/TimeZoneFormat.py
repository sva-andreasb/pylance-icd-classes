def getInstance():
'''public static TimeZoneFormat getInstance(final ULocale locale)
public static TimeZoneFormat getInstance(final Locale locale)
'''
pass
def getTimeZoneNames():
'''public TimeZoneNames getTimeZoneNames()
'''
pass
def setTimeZoneNames():
'''public TimeZoneFormat setTimeZoneNames(final TimeZoneNames tznames)
'''
pass
def getGMTPattern():
'''public String getGMTPattern()
'''
pass
def setGMTPattern():
'''public TimeZoneFormat setGMTPattern(final String pattern)
'''
pass
def getGMTOffsetPattern():
'''public String getGMTOffsetPattern(final GMTOffsetPatternType type)
'''
pass
def setGMTOffsetPattern():
'''public TimeZoneFormat setGMTOffsetPattern(final GMTOffsetPatternType type, final String pattern)
'''
pass
def getGMTOffsetDigits():
'''public String getGMTOffsetDigits()
'''
pass
def setGMTOffsetDigits():
'''public TimeZoneFormat setGMTOffsetDigits(final String digits)
'''
pass
def getGMTZeroFormat():
'''public String getGMTZeroFormat()
'''
pass
def setGMTZeroFormat():
'''public TimeZoneFormat setGMTZeroFormat(final String gmtZeroFormat)
'''
pass
def setDefaultParseOptions():
'''public TimeZoneFormat setDefaultParseOptions(final EnumSet<ParseOption> options)
'''
pass
def getDefaultParseOptions():
'''public EnumSet<ParseOption> getDefaultParseOptions()
'''
pass
def formatOffsetISO8601Basic():
'''public final String formatOffsetISO8601Basic(final int offset, final boolean useUtcIndicator, final boolean isShort, final boolean ignoreSeconds)
'''
pass
def formatOffsetISO8601Extended():
'''public final String formatOffsetISO8601Extended(final int offset, final boolean useUtcIndicator, final boolean isShort, final boolean ignoreSeconds)
'''
pass
def formatOffsetLocalizedGMT():
'''public String formatOffsetLocalizedGMT(final int offset)
'''
pass
def formatOffsetShortLocalizedGMT():
'''public String formatOffsetShortLocalizedGMT(final int offset)
'''
pass
def format():
'''public final String format(final Style style, final TimeZone tz, final long date)
public String format(final Style style, final TimeZone tz, final long date, final Output<TimeType> timeType)
public StringBuffer format(final Object obj, final StringBuffer toAppendTo, final FieldPosition pos)
'''
pass
def parseOffsetISO8601():
'''public final int parseOffsetISO8601(final String text, final ParsePosition pos)
'''
pass
def parseOffsetLocalizedGMT():
'''public int parseOffsetLocalizedGMT(final String text, final ParsePosition pos)
'''
pass
def parseOffsetShortLocalizedGMT():
'''public int parseOffsetShortLocalizedGMT(final String text, final ParsePosition pos)
'''
pass
def parse():
'''public TimeZone parse(final Style style, final String text, final ParsePosition pos, final EnumSet<ParseOption> options, Output<TimeType> timeType)
public TimeZone parse(final Style style, final String text, final ParsePosition pos, final Output<TimeType> timeType)
public final TimeZone parse(final String text, final ParsePosition pos)
public final TimeZone parse(final String text)
'''
pass
def formatToCharacterIterator():
'''public AttributedCharacterIterator formatToCharacterIterator(final Object obj)
'''
pass
def parseObject():
'''public Object parseObject(final String source, final ParsePosition pos)
'''
pass
def isFrozen():
'''public boolean isFrozen()
'''
pass
def freeze():
'''public TimeZoneFormat freeze()
'''
pass
def cloneAsThawed():
'''public TimeZoneFormat cloneAsThawed()
'''
pass
