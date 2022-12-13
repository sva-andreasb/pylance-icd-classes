def getInstance():
    '''public static TimeZoneFormat getInstance(final ULocale locale)
    public static TimeZoneFormat getInstance(final Locale locale)
    '''
def getTimeZoneNames():
    '''public TimeZoneNames getTimeZoneNames()
    '''
def setTimeZoneNames():
    '''public TimeZoneFormat setTimeZoneNames(final TimeZoneNames tznames)
    '''
def getGMTPattern():
    '''public String getGMTPattern()
    '''
def setGMTPattern():
    '''public TimeZoneFormat setGMTPattern(final String pattern)
    '''
def getGMTOffsetPattern():
    '''public String getGMTOffsetPattern(final GMTOffsetPatternType type)
    '''
def setGMTOffsetPattern():
    '''public TimeZoneFormat setGMTOffsetPattern(final GMTOffsetPatternType type, final String pattern)
    '''
def getGMTOffsetDigits():
    '''public String getGMTOffsetDigits()
    '''
def setGMTOffsetDigits():
    '''public TimeZoneFormat setGMTOffsetDigits(final String digits)
    '''
def getGMTZeroFormat():
    '''public String getGMTZeroFormat()
    '''
def setGMTZeroFormat():
    '''public TimeZoneFormat setGMTZeroFormat(final String gmtZeroFormat)
    '''
def setDefaultParseOptions():
    '''public TimeZoneFormat setDefaultParseOptions(final EnumSet<ParseOption> options)
    '''
def getDefaultParseOptions():
    '''public EnumSet<ParseOption> getDefaultParseOptions()
    '''
def formatOffsetISO8601Basic():
    '''public final String formatOffsetISO8601Basic(final int offset, final boolean useUtcIndicator, final boolean isShort, final boolean ignoreSeconds)
    '''
def formatOffsetISO8601Extended():
    '''public final String formatOffsetISO8601Extended(final int offset, final boolean useUtcIndicator, final boolean isShort, final boolean ignoreSeconds)
    '''
def formatOffsetLocalizedGMT():
    '''public String formatOffsetLocalizedGMT(final int offset)
    '''
def formatOffsetShortLocalizedGMT():
    '''public String formatOffsetShortLocalizedGMT(final int offset)
    '''
def format():
    '''public final String format(final Style style, final TimeZone tz, final long date)
    public String format(final Style style, final TimeZone tz, final long date, final Output<TimeType> timeType)
    public StringBuffer format(final Object obj, final StringBuffer toAppendTo, final FieldPosition pos)
    '''
def parseOffsetISO8601():
    '''public final int parseOffsetISO8601(final String text, final ParsePosition pos)
    '''
def parseOffsetLocalizedGMT():
    '''public int parseOffsetLocalizedGMT(final String text, final ParsePosition pos)
    '''
def parseOffsetShortLocalizedGMT():
    '''public int parseOffsetShortLocalizedGMT(final String text, final ParsePosition pos)
    '''
def parse():
    '''public TimeZone parse(final Style style, final String text, final ParsePosition pos, final EnumSet<ParseOption> options, Output<TimeType> timeType)
    public TimeZone parse(final Style style, final String text, final ParsePosition pos, final Output<TimeType> timeType)
    public final TimeZone parse(final String text, final ParsePosition pos)
    public final TimeZone parse(final String text)
    '''
def formatToCharacterIterator():
    '''public AttributedCharacterIterator formatToCharacterIterator(final Object obj)
    '''
def parseObject():
    '''public Object parseObject(final String source, final ParsePosition pos)
    '''
def isFrozen():
    '''public boolean isFrozen()
    '''
def freeze():
    '''public TimeZoneFormat freeze()
    '''
def cloneAsThawed():
    '''public TimeZoneFormat cloneAsThawed()
    '''
