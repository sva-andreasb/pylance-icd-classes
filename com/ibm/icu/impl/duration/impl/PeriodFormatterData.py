def ():
    '''returns PeriodFormatterData\n\n
    (final String localeName, final DataRecord dr)\n
    '''
def pluralization():
    '''returns int\n\n
    pluralization()\n
    '''
def allowZero():
    '''returns boolean\n\n
    allowZero()\n
    '''
def weeksAloneOnly():
    '''returns boolean\n\n
    weeksAloneOnly()\n
    '''
def useMilliseconds():
    '''returns int\n\n
    useMilliseconds()\n
    '''
def appendPrefix():
    '''returns boolean\n\n
    appendPrefix(final int tl, final int td, final StringBuffer sb)\n
    '''
def appendSuffix():
    '''returns None\n\n
    appendSuffix(final int tl, final int td, final StringBuffer sb)\n
    '''
def appendUnit():
    '''returns boolean\n\n
    appendUnit(final TimeUnit unit, int count, int cv, final int uv, final boolean useCountSep, final boolean useDigitPrefix, final boolean multiple, final boolean last, final boolean wasSkipped, final StringBuffer sb)\n
    '''
def appendCount():
    '''returns int\n\n
    appendCount(final TimeUnit unit, final boolean omitCount, final boolean useDigitPrefix, final int count, int cv, final boolean useSep, String name, final boolean last, final StringBuffer sb)\n
    '''
def appendCountValue():
    '''returns None\n\n
    appendCountValue(final int count, final int integralDigits, final int decimalDigits, final StringBuffer sb)\n
    '''
def appendInteger():
    '''returns None\n\n
    appendInteger(final int num, final int mindigits, final int maxdigits, final StringBuffer sb)\n
    '''
def appendDigits():
    '''returns None\n\n
    appendDigits(long num, final int mindigits, final int maxdigits, final StringBuffer sb)\n
    '''
def appendSkippedUnit():
    '''returns None\n\n
    appendSkippedUnit(final StringBuffer sb)\n
    '''
def appendUnitSeparator():
    '''returns boolean\n\n
    appendUnitSeparator(final TimeUnit unit, final boolean longSep, final boolean afterFirst, final boolean beforeLast, final StringBuffer sb)\n
    '''
