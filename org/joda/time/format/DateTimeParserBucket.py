def ():
    '''returns DateTimeParserBucket\n\n
    (final long n, final Chronology chronology, final Locale locale)\n
    (final long n, final Chronology chronology, final Locale locale, final Integer n2)\n
    (final long iMillis, Chronology chronology, final Locale locale, final Integer iDefaultPivotYear, final int iDefaultYear)\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def parseMillis():
    '''returns long\n\n
    parseMillis(final DateTimeParser dateTimeParser, final CharSequence charSequence)\n
    '''
def getChronology():
    '''returns Chronology\n\n
    getChronology()\n
    '''
def getLocale():
    '''returns Locale\n\n
    getLocale()\n
    '''
def getZone():
    '''returns DateTimeZone\n\n
    getZone()\n
    '''
def setZone():
    '''returns None\n\n
    setZone(final DateTimeZone iZone)\n
    '''
def getOffset():
    '''returns int\n\n
    getOffset()\n
    '''
def getOffsetInteger():
    '''returns Integer\n\n
    getOffsetInteger()\n
    '''
def setOffset():
    '''returns None\n\n
    setOffset(final int i)\n
    setOffset(final Integer iOffset)\n
    '''
def getPivotYear():
    '''returns Integer\n\n
    getPivotYear()\n
    '''
def setPivotYear():
    '''returns None\n\n
    setPivotYear(final Integer iPivotYear)\n
    '''
def saveField():
    '''returns None\n\n
    saveField(final DateTimeField dateTimeField, final int n)\n
    saveField(final DateTimeFieldType dateTimeFieldType, final int n)\n
    saveField(final DateTimeFieldType dateTimeFieldType, final String s, final Locale locale)\n
    '''
def saveState():
    '''returns Object\n\n
    saveState()\n
    '''
def restoreState():
    '''returns boolean\n\n
    restoreState(final Object iSavedState)\n
    '''
def computeMillis():
    '''returns long\n\n
    computeMillis()\n
    computeMillis(final boolean b)\n
    computeMillis(final boolean b, final String s)\n
    computeMillis(final boolean b, final CharSequence charSequence)\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final SavedField savedField)\n
    '''
