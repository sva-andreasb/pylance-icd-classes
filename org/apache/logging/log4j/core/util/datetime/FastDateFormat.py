FULL = "int  0"
LONG = "int  1"
MEDIUM = "int  2"
SHORT = "int  3"
def format():
    '''returns String\n\n
    format(final Object obj, final StringBuilder toAppendTo, final FieldPosition pos)\n
    format(final long millis)\n
    format(final Date date)\n
    format(final Calendar calendar)\n
    '''
def parse():
    '''returns boolean\n\n
    parse(final String source)\n
    parse(final String source, final ParsePosition pos)\n
    parse(final String source, final ParsePosition pos, final Calendar calendar)\n
    '''
def parseObject():
    '''returns Object\n\n
    parseObject(final String source, final ParsePosition pos)\n
    '''
def getPattern():
    '''returns String\n\n
    getPattern()\n
    '''
def getTimeZone():
    '''returns TimeZone\n\n
    getTimeZone()\n
    '''
def getLocale():
    '''returns Locale\n\n
    getLocale()\n
    '''
def getMaxLengthEstimate():
    '''returns int\n\n
    getMaxLengthEstimate()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
