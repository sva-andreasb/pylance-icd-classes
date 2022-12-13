NF_NUMBER = "int 0"
NF_CURRENCY = "int 1"
NF_PERCENT = "int 2"
NF_SCIENTIFIC = "int 3"
NF_INTEGER = "int 4"
DF_FULL = "int 0"
DF_LONG = "int 1"
DF_MEDIUM = "int 2"
DF_SHORT = "int 3"
DF_NONE = "int 4"
ID_LOCALE = "int 0"
ID_LANGUAGE = "int 1"
ID_SCRIPT = "int 2"
ID_TERRITORY = "int 3"
ID_VARIANT = "int 4"
ID_KEYWORD = "int 5"
ID_KEYWORD_VALUE = "int 6"
ID_CURRENCY = "int 7"
ID_CURRENCY_SYMBOL = "int 8"
ID_TIMEZONE = "int 9"
BI_CHARACTER = "int 0"
BI_WORD = "int 1"
BI_LINE = "int 2"
BI_SENTENCE = "int 3"
BI_TITLE = "int 4"
def GlobalizationPreferences():
'''public GlobalizationPreferences()
'''
pass
def setLocales():
'''public GlobalizationPreferences setLocales(final List<ULocale> inputLocales)
public GlobalizationPreferences setLocales(final ULocale[] uLocales)
public GlobalizationPreferences setLocales(final String acceptLanguageString)
'''
pass
def getLocales():
'''public List<ULocale> getLocales()
'''
pass
def getLocale():
'''public ULocale getLocale(final int index)
'''
pass
def setLocale():
'''public GlobalizationPreferences setLocale(final ULocale uLocale)
'''
pass
def getResourceBundle():
'''public ResourceBundle getResourceBundle(final String baseName)
public ResourceBundle getResourceBundle(final String baseName, final ClassLoader loader)
'''
pass
def setTerritory():
'''public GlobalizationPreferences setTerritory(final String territory)
'''
pass
def getTerritory():
'''public String getTerritory()
'''
pass
def setCurrency():
'''public GlobalizationPreferences setCurrency(final Currency currency)
'''
pass
def getCurrency():
'''public Currency getCurrency()
'''
pass
def setCalendar():
'''public GlobalizationPreferences setCalendar(final Calendar calendar)
'''
pass
def getCalendar():
'''public Calendar getCalendar()
'''
pass
def setTimeZone():
'''public GlobalizationPreferences setTimeZone(final TimeZone timezone)
'''
pass
def getTimeZone():
'''public TimeZone getTimeZone()
'''
pass
def getCollator():
'''public Collator getCollator()
'''
pass
def setCollator():
'''public GlobalizationPreferences setCollator(final Collator collator)
'''
pass
def getBreakIterator():
'''public BreakIterator getBreakIterator(final int type)
'''
pass
def setBreakIterator():
'''public GlobalizationPreferences setBreakIterator(final int type, final BreakIterator iterator)
'''
pass
def getDisplayName():
'''public String getDisplayName(final String id, final int type)
'''
pass
def setDateFormat():
'''public GlobalizationPreferences setDateFormat(final int dateStyle, final int timeStyle, final DateFormat format)
'''
pass
def getDateFormat():
'''public DateFormat getDateFormat(final int dateStyle, final int timeStyle)
'''
pass
def getNumberFormat():
'''public NumberFormat getNumberFormat(final int style)
'''
pass
def setNumberFormat():
'''public GlobalizationPreferences setNumberFormat(final int style, final NumberFormat format)
'''
pass
def reset():
'''public GlobalizationPreferences reset()
'''
pass
def isFrozen():
'''public boolean isFrozen()
'''
pass
def freeze():
'''public GlobalizationPreferences freeze()
'''
pass
def cloneAsThawed():
'''public GlobalizationPreferences cloneAsThawed()
'''
pass
