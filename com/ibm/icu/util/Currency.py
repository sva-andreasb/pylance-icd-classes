SYMBOL_NAME = "int  0"
LONG_NAME = "int  1"
PLURAL_LONG_NAME = "int  2"
NARROW_SYMBOL_NAME = "int  3"
FORMAL_SYMBOL_NAME = "int  4"
VARIANT_SYMBOL_NAME = "int  5"
def getInstance():
    '''    public static Currency getInstance(final Locale locale)
    public static Currency getInstance(final ULocale locale)
    public static Currency getInstance(final String theISOCode)
    '''
def getAvailableCurrencyCodes():
    '''    public static String[] getAvailableCurrencyCodes(final ULocale loc, final Date d)
    public static String[] getAvailableCurrencyCodes(final Locale loc, final Date d)
    '''
def getAvailableCurrencies():
    '''    public static Set<Currency> getAvailableCurrencies()
    '''
def fromJavaCurrency():
    '''    public static Currency fromJavaCurrency(final java.util.Currency currency)
    '''
def registerInstance():
    '''    public static Object registerInstance(final Currency currency, final ULocale locale)
    '''
def unregister():
    '''    public static boolean unregister(final Object registryKey)
    '''
def getAvailableLocales():
    '''    public static Locale[] getAvailableLocales()
    '''
def getAvailableULocales():
    '''    public static ULocale[] getAvailableULocales()
    '''
def getKeywordValuesForLocale():
    '''    public static final String[] getKeywordValuesForLocale(final String key, final ULocale locale, final boolean commonlyUsed)
    '''
def getCurrencyCode():
    '''    public String getCurrencyCode()
    '''
def getNumericCode():
    '''    public int getNumericCode()
    '''
def getSymbol():
    '''    public String getSymbol()
    public String getSymbol(final Locale loc)
    public String getSymbol(final ULocale uloc)
    '''
def getName():
    '''    public String getName(final Locale locale, final int nameStyle, final boolean[] isChoiceFormat)
    public String getName(final ULocale locale, final int nameStyle, final boolean[] isChoiceFormat)
    public String getName(final Locale locale, final int nameStyle, final String pluralCount, final boolean[] isChoiceFormat)
    public String getName(final ULocale locale, final int nameStyle, final String pluralCount, final boolean[] isChoiceFormat)
    '''
def getDisplayName():
    '''    public String getDisplayName()
    public String getDisplayName(final Locale locale)
    '''
def parse():
    '''    public static String parse(final ULocale locale, final String text, final int type, final ParsePosition pos)
    '''
def getParsingTrie():
    '''    public static TextTrieMap<CurrencyStringInfo> getParsingTrie(final ULocale locale, final int type)
    '''
def getDefaultFractionDigits():
    '''    public int getDefaultFractionDigits()
    public int getDefaultFractionDigits(final CurrencyUsage Usage)
    '''
def getRoundingIncrement():
    '''    public double getRoundingIncrement()
    public double getRoundingIncrement(final CurrencyUsage Usage)
    '''
def toString():
    '''    public String toString()
    '''
def isAvailable():
    '''    public static boolean isAvailable(String code, final Date from, final Date to)
    '''
def CurrencyStringInfo():
    '''    public CurrencyStringInfo(final String isoCode, final String currencyString)
    '''
def getISOCode():
    '''    public String getISOCode()
    '''
def getCurrencyString():
    '''    public String getCurrencyString()
    '''
def handlePrefixMatch():
    '''    public boolean handlePrefixMatch(final int matchLength, final Iterator<CurrencyStringInfo> values)
    '''
def getBestCurrencyISOCode():
    '''    public String getBestCurrencyISOCode()
    '''
def getBestMatchLength():
    '''    public int getBestMatchLength()
    '''
