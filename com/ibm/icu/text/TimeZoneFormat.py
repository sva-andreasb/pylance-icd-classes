def getTimeZoneNames():
    '''returns TimeZoneNames\n\n
    getTimeZoneNames()\n
    '''
def setTimeZoneNames():
    '''returns TimeZoneFormat\n\n
    setTimeZoneNames(final TimeZoneNames tznames)\n
    '''
def getGMTPattern():
    '''returns String\n\n
    getGMTPattern()\n
    '''
def setGMTPattern():
    '''returns TimeZoneFormat\n\n
    setGMTPattern(final String pattern)\n
    '''
def getGMTOffsetPattern():
    '''returns String\n\n
    getGMTOffsetPattern(final GMTOffsetPatternType type)\n
    '''
def setGMTOffsetPattern():
    '''returns TimeZoneFormat\n\n
    setGMTOffsetPattern(final GMTOffsetPatternType type, final String pattern)\n
    '''
def getGMTOffsetDigits():
    '''returns String\n\n
    getGMTOffsetDigits()\n
    '''
def setGMTOffsetDigits():
    '''returns TimeZoneFormat\n\n
    setGMTOffsetDigits(final String digits)\n
    '''
def getGMTZeroFormat():
    '''returns String\n\n
    getGMTZeroFormat()\n
    '''
def setGMTZeroFormat():
    '''returns TimeZoneFormat\n\n
    setGMTZeroFormat(final String gmtZeroFormat)\n
    '''
def setDefaultParseOptions():
    '''returns TimeZoneFormat\n\n
    setDefaultParseOptions(final EnumSet<ParseOption> options)\n
    '''
def getDefaultParseOptions():
    '''returns EnumSet<ParseOption>\n\n
    getDefaultParseOptions()\n
    '''
def formatOffsetLocalizedGMT():
    '''returns String\n\n
    formatOffsetLocalizedGMT(final int offset)\n
    '''
def formatOffsetShortLocalizedGMT():
    '''returns String\n\n
    formatOffsetShortLocalizedGMT(final int offset)\n
    '''
def format():
    '''returns StringBuffer\n\n
    format(final Style style, final TimeZone tz, final long date, final Output<TimeType> timeType)\n
    format(final Object obj, final StringBuffer toAppendTo, final FieldPosition pos)\n
    '''
def parseOffsetLocalizedGMT():
    '''returns int\n\n
    parseOffsetLocalizedGMT(final String text, final ParsePosition pos)\n
    '''
def parseOffsetShortLocalizedGMT():
    '''returns int\n\n
    parseOffsetShortLocalizedGMT(final String text, final ParsePosition pos)\n
    '''
def parse():
    '''returns TimeZone\n\n
    parse(final Style style, final String text, final ParsePosition pos, final EnumSet<ParseOption> options, Output<TimeType> timeType)\n
    parse(final Style style, final String text, final ParsePosition pos, final Output<TimeType> timeType)\n
    '''
def formatToCharacterIterator():
    '''returns AttributedCharacterIterator\n\n
    formatToCharacterIterator(final Object obj)\n
    '''
def parseObject():
    '''returns Object\n\n
    parseObject(final String source, final ParsePosition pos)\n
    '''
def isFrozen():
    '''returns boolean\n\n
    isFrozen()\n
    '''
def freeze():
    '''returns TimeZoneFormat\n\n
    freeze()\n
    '''
def cloneAsThawed():
    '''returns TimeZoneFormat\n\n
    cloneAsThawed()\n
    '''
