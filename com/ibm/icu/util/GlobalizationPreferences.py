NF_NUMBER = "int  0"
NF_CURRENCY = "int  1"
NF_PERCENT = "int  2"
NF_SCIENTIFIC = "int  3"
NF_INTEGER = "int  4"
DF_FULL = "int  0"
DF_LONG = "int  1"
DF_MEDIUM = "int  2"
DF_SHORT = "int  3"
DF_NONE = "int  4"
ID_LOCALE = "int  0"
ID_LANGUAGE = "int  1"
ID_SCRIPT = "int  2"
ID_TERRITORY = "int  3"
ID_VARIANT = "int  4"
ID_KEYWORD = "int  5"
ID_KEYWORD_VALUE = "int  6"
ID_CURRENCY = "int  7"
ID_CURRENCY_SYMBOL = "int  8"
ID_TIMEZONE = "int  9"
BI_CHARACTER = "int  0"
BI_WORD = "int  1"
BI_LINE = "int  2"
BI_SENTENCE = "int  3"
BI_TITLE = "int  4"
def ():
    '''returns GlobalizationPreferences\n\n
    ()\n
    '''
def setLocales():
    '''returns GlobalizationPreferences\n\n
    setLocales(final List<ULocale> inputLocales)\n
    setLocales(final ULocale[] uLocales)\n
    setLocales(final String acceptLanguageString)\n
    '''
def getLocales():
    '''returns List<ULocale>\n\n
    getLocales()\n
    '''
def getLocale():
    '''returns ULocale\n\n
    getLocale(final int index)\n
    '''
def setLocale():
    '''returns GlobalizationPreferences\n\n
    setLocale(final ULocale uLocale)\n
    '''
def getResourceBundle():
    '''returns ResourceBundle\n\n
    getResourceBundle(final String baseName)\n
    getResourceBundle(final String baseName, final ClassLoader loader)\n
    '''
def setTerritory():
    '''returns GlobalizationPreferences\n\n
    setTerritory(final String territory)\n
    '''
def getTerritory():
    '''returns String\n\n
    getTerritory()\n
    '''
def setCurrency():
    '''returns GlobalizationPreferences\n\n
    setCurrency(final Currency currency)\n
    '''
def getCurrency():
    '''returns Currency\n\n
    getCurrency()\n
    '''
def setCalendar():
    '''returns GlobalizationPreferences\n\n
    setCalendar(final Calendar calendar)\n
    '''
def getCalendar():
    '''returns Calendar\n\n
    getCalendar()\n
    '''
def setTimeZone():
    '''returns GlobalizationPreferences\n\n
    setTimeZone(final TimeZone timezone)\n
    '''
def getTimeZone():
    '''returns TimeZone\n\n
    getTimeZone()\n
    '''
def getCollator():
    '''returns Collator\n\n
    getCollator()\n
    '''
def setCollator():
    '''returns GlobalizationPreferences\n\n
    setCollator(final Collator collator)\n
    '''
def getBreakIterator():
    '''returns BreakIterator\n\n
    getBreakIterator(final int type)\n
    '''
def setBreakIterator():
    '''returns GlobalizationPreferences\n\n
    setBreakIterator(final int type, final BreakIterator iterator)\n
    '''
def getDisplayName():
    '''returns String\n\n
    getDisplayName(final String id, final int type)\n
    '''
def setDateFormat():
    '''returns GlobalizationPreferences\n\n
    setDateFormat(final int dateStyle, final int timeStyle, final DateFormat format)\n
    '''
def getDateFormat():
    '''returns DateFormat\n\n
    getDateFormat(final int dateStyle, final int timeStyle)\n
    '''
def getNumberFormat():
    '''returns NumberFormat\n\n
    getNumberFormat(final int style)\n
    '''
def setNumberFormat():
    '''returns GlobalizationPreferences\n\n
    setNumberFormat(final int style, final NumberFormat format)\n
    '''
def reset():
    '''returns GlobalizationPreferences\n\n
    reset()\n
    '''
def isFrozen():
    '''returns boolean\n\n
    isFrozen()\n
    '''
def freeze():
    '''returns GlobalizationPreferences\n\n
    freeze()\n
    '''
def cloneAsThawed():
    '''returns GlobalizationPreferences\n\n
    cloneAsThawed()\n
    '''
