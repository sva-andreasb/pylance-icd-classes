SYMBOL_NAME = "int  0"
LONG_NAME = "int  1"
PLURAL_LONG_NAME = "int  2"
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object rhs)\n
    '''
def getCurrencyCode():
    '''returns String\n\n
    getCurrencyCode()\n
    '''
def getSymbol():
    '''returns String\n\n
    getSymbol()\n
    getSymbol(final Locale loc)\n
    getSymbol(final ULocale uloc)\n
    '''
def getName():
    '''returns String\n\n
    getName(final Locale locale, final int nameStyle, final boolean[] isChoiceFormat)\n
    getName(final ULocale locale, final int nameStyle, final boolean[] isChoiceFormat)\n
    getName(final Locale locale, final int nameStyle, final String pluralCount, final boolean[] isChoiceFormat)\n
    getName(final ULocale locale, final int nameStyle, final String pluralCount, final boolean[] isChoiceFormat)\n
    '''
def getDefaultFractionDigits():
    '''returns int\n\n
    getDefaultFractionDigits()\n
    '''
def getRoundingIncrement():
    '''returns double\n\n
    getRoundingIncrement()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def ():
    '''returns CurrencyStringInfo\n\n
    (final String isoCode, final String currencyString)\n
    '''
def handlePrefixMatch():
    '''returns boolean\n\n
    handlePrefixMatch(final int matchLength, final Iterator<CurrencyStringInfo> values)\n
    '''
