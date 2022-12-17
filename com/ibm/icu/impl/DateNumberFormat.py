def ():
    '''returns DateNumberFormat\n\n
    (final ULocale loc, final char zeroDigitIn)\n
    '''
def setMaximumIntegerDigits():
    '''returns None\n\n
    setMaximumIntegerDigits(final int newValue)\n
    '''
def getMaximumIntegerDigits():
    '''returns int\n\n
    getMaximumIntegerDigits()\n
    '''
def setMinimumIntegerDigits():
    '''returns None\n\n
    setMinimumIntegerDigits(final int newValue)\n
    '''
def getMinimumIntegerDigits():
    '''returns int\n\n
    getMinimumIntegerDigits()\n
    '''
def setParsePositiveOnly():
    '''returns None\n\n
    setParsePositiveOnly(final boolean isPositiveOnly)\n
    '''
def getZeroDigit():
    '''returns char\n\n
    getZeroDigit()\n
    '''
def setZeroDigit():
    '''returns None\n\n
    setZeroDigit(final char zero)\n
    '''
def format():
    '''returns StringBuffer\n\n
    format(final double number, final StringBuffer toAppendTo, final FieldPosition pos)\n
    format(final long numberL, final StringBuffer toAppendTo, final FieldPosition pos)\n
    format(final BigInteger number, final StringBuffer toAppendTo, final FieldPosition pos)\n
    format(final BigDecimal number, final StringBuffer toAppendTo, final FieldPosition pos)\n
    format(final com.ibm.icu.math.BigDecimal number, final StringBuffer toAppendTo, final FieldPosition pos)\n
    '''
def parse():
    '''returns Number\n\n
    parse(final String text, final ParsePosition parsePosition)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
