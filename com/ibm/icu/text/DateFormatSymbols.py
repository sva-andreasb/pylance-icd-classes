FORMAT = "int  0"
STANDALONE = "int  1"
DT_CONTEXT_COUNT = "int  2"
ABBREVIATED = "int  0"
WIDE = "int  1"
NARROW = "int  2"
DT_WIDTH_COUNT = "int  3"
def ():
    '''returns DateFormatSymbols\n\n
    ()\n
    (final Locale locale)\n
    (final ULocale locale)\n
    (final Calendar cal, final Locale locale)\n
    (final Calendar cal, final ULocale locale)\n
    (final Class<? extends Calendar> calendarClass, final Locale locale)\n
    (final Class<? extends Calendar> calendarClass, final ULocale locale)\n
    (final ResourceBundle bundle, final Locale locale)\n
    (final ResourceBundle bundle, final ULocale locale)\n
    '''
def getEras():
    '''returns String[]\n\n
    getEras()\n
    '''
def setEras():
    '''returns None\n\n
    setEras(final String[] newEras)\n
    '''
def getEraNames():
    '''returns String[]\n\n
    getEraNames()\n
    '''
def setEraNames():
    '''returns None\n\n
    setEraNames(final String[] newEraNames)\n
    '''
def getMonths():
    '''returns String[]\n\n
    getMonths()\n
    getMonths(final int context, final int width)\n
    '''
def setMonths():
    '''returns None\n\n
    setMonths(final String[] newMonths)\n
    setMonths(final String[] newMonths, final int context, final int width)\n
    '''
def getShortMonths():
    '''returns String[]\n\n
    getShortMonths()\n
    '''
def setShortMonths():
    '''returns None\n\n
    setShortMonths(final String[] newShortMonths)\n
    '''
def getWeekdays():
    '''returns String[]\n\n
    getWeekdays()\n
    getWeekdays(final int context, final int width)\n
    '''
def setWeekdays():
    '''returns None\n\n
    setWeekdays(final String[] newWeekdays, final int context, final int width)\n
    setWeekdays(final String[] newWeekdays)\n
    '''
def getShortWeekdays():
    '''returns String[]\n\n
    getShortWeekdays()\n
    '''
def setShortWeekdays():
    '''returns None\n\n
    setShortWeekdays(final String[] newShortWeekdays)\n
    '''
def getQuarters():
    '''returns String[]\n\n
    getQuarters(final int context, final int width)\n
    '''
def setQuarters():
    '''returns None\n\n
    setQuarters(final String[] newQuarters, final int context, final int width)\n
    '''
def getAmPmStrings():
    '''returns String[]\n\n
    getAmPmStrings()\n
    '''
def setAmPmStrings():
    '''returns None\n\n
    setAmPmStrings(final String[] newAmpms)\n
    '''
def getZoneStrings():
    '''returns String[][]\n\n
    getZoneStrings()\n
    '''
def setZoneStrings():
    '''returns None\n\n
    setZoneStrings(final String[][] newZoneStrings)\n
    '''
def getLocalPatternChars():
    '''returns String\n\n
    getLocalPatternChars()\n
    '''
def setLocalPatternChars():
    '''returns None\n\n
    setLocalPatternChars(final String newLocalPatternChars)\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
