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
def GlobalizationPreferences():
    '''public GlobalizationPreferences()
    '''
def setLocales():
    '''public GlobalizationPreferences setLocales(final List<ULocale> inputLocales)
    public GlobalizationPreferences setLocales(final ULocale[] uLocales)
    public GlobalizationPreferences setLocales(final String acceptLanguageString)
    '''
def getLocales():
    '''public List<ULocale> getLocales()
    '''
def getLocale():
    '''public ULocale getLocale(final int index)
    '''
def setLocale():
    '''public GlobalizationPreferences setLocale(final ULocale uLocale)
    '''
def getResourceBundle():
    '''public ResourceBundle getResourceBundle(final String baseName)
    public ResourceBundle getResourceBundle(final String baseName, final ClassLoader loader)
    '''
def setTerritory():
    '''public GlobalizationPreferences setTerritory(final String territory)
    '''
def getTerritory():
    '''public String getTerritory()
    '''
def setCurrency():
    '''public GlobalizationPreferences setCurrency(final Currency currency)
    '''
def getCurrency():
    '''public Currency getCurrency()
    '''
def setCalendar():
    '''public GlobalizationPreferences setCalendar(final Calendar calendar)
    '''
def getCalendar():
    '''public Calendar getCalendar()
    '''
def setTimeZone():
    '''public GlobalizationPreferences setTimeZone(final TimeZone timezone)
    '''
def getTimeZone():
    '''public TimeZone getTimeZone()
    '''
def getCollator():
    '''public Collator getCollator()
    '''
def setCollator():
    '''public GlobalizationPreferences setCollator(final Collator collator)
    '''
def getBreakIterator():
    '''public BreakIterator getBreakIterator(final int type)
    '''
def setBreakIterator():
    '''public GlobalizationPreferences setBreakIterator(final int type, final BreakIterator iterator)
    '''
def getDisplayName():
    '''public String getDisplayName(final String id, final int type)
    '''
def setDateFormat():
    '''public GlobalizationPreferences setDateFormat(final int dateStyle, final int timeStyle, final DateFormat format)
    '''
def getDateFormat():
    '''public DateFormat getDateFormat(final int dateStyle, final int timeStyle)
    '''
def getNumberFormat():
    '''public NumberFormat getNumberFormat(final int style)
    '''
def setNumberFormat():
    '''public GlobalizationPreferences setNumberFormat(final int style, final NumberFormat format)
    '''
def reset():
    '''public GlobalizationPreferences reset()
    '''
def isFrozen():
    '''public boolean isFrozen()
    '''
def freeze():
    '''public GlobalizationPreferences freeze()
    '''
def cloneAsThawed():
    '''public GlobalizationPreferences cloneAsThawed()
    '''
