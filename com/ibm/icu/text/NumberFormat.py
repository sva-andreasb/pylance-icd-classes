NUMBERSTYLE = "int  0"
CURRENCYSTYLE = "int  1"
PERCENTSTYLE = "int  2"
SCIENTIFICSTYLE = "int  3"
INTEGERSTYLE = "int  4"
ISOCURRENCYSTYLE = "int  5"
PLURALCURRENCYSTYLE = "int  6"
INTEGER_FIELD = "int  0"
FRACTION_FIELD = "int  1"
FORMAT_NUMBER = "int  0"
FORMAT_CURRENCY = "int  1"
FORMAT_PERCENT = "int  2"
FORMAT_SCIENTIFIC = "int  3"
FORMAT_INTEGER = "int  4"
def format():
    '''returns StringBuffer\n\n
    format(final Object number, final StringBuffer toAppendTo, final FieldPosition pos)\n
    format(final CurrencyAmount currAmt, final StringBuffer toAppendTo, final FieldPosition pos)\n
    '''
def parse():
    '''returns Number\n\n
    parse(final String text)\n
    '''
def isParseIntegerOnly():
    '''returns boolean\n\n
    isParseIntegerOnly()\n
    '''
def setParseIntegerOnly():
    '''returns None\n\n
    setParseIntegerOnly(final boolean value)\n
    '''
def setParseStrict():
    '''returns None\n\n
    setParseStrict(final boolean value)\n
    '''
def isParseStrict():
    '''returns boolean\n\n
    isParseStrict()\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def isGroupingUsed():
    '''returns boolean\n\n
    isGroupingUsed()\n
    '''
def setGroupingUsed():
    '''returns None\n\n
    setGroupingUsed(final boolean newValue)\n
    '''
def getMaximumIntegerDigits():
    '''returns int\n\n
    getMaximumIntegerDigits()\n
    '''
def setMaximumIntegerDigits():
    '''returns None\n\n
    setMaximumIntegerDigits(final int newValue)\n
    '''
def getMinimumIntegerDigits():
    '''returns int\n\n
    getMinimumIntegerDigits()\n
    '''
def setMinimumIntegerDigits():
    '''returns None\n\n
    setMinimumIntegerDigits(final int newValue)\n
    '''
def getMaximumFractionDigits():
    '''returns int\n\n
    getMaximumFractionDigits()\n
    '''
def setMaximumFractionDigits():
    '''returns None\n\n
    setMaximumFractionDigits(final int newValue)\n
    '''
def getMinimumFractionDigits():
    '''returns int\n\n
    getMinimumFractionDigits()\n
    '''
def setMinimumFractionDigits():
    '''returns None\n\n
    setMinimumFractionDigits(final int newValue)\n
    '''
def setCurrency():
    '''returns None\n\n
    setCurrency(final Currency theCurrency)\n
    '''
def getCurrency():
    '''returns Currency\n\n
    getCurrency()\n
    '''
def getRoundingMode():
    '''returns int\n\n
    getRoundingMode()\n
    '''
def setRoundingMode():
    '''returns None\n\n
    setRoundingMode(final int roundingMode)\n
    '''
def ():
    '''returns SimpleNumberFormatFactory\n\n
    ()\n
    (final Locale locale)\n
    (final Locale locale, final boolean visible)\n
    (final ULocale locale)\n
    (final ULocale locale, final boolean visible)\n
    '''
def visible():
    '''returns boolean\n\n
    visible()\n
    '''
def createFormat():
    '''returns NumberFormat\n\n
    createFormat(final ULocale loc, final int formatType)\n
    createFormat(final Locale loc, final int formatType)\n
    '''
