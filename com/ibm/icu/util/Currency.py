SYMBOL_NAME = "int 0"
LONG_NAME = "int 1"
PLURAL_LONG_NAME = "int 2"
NARROW_SYMBOL_NAME = "int 3"
FORMAL_SYMBOL_NAME = "int 4"
VARIANT_SYMBOL_NAME = "int 5"
def getInstance():
'''public static Currency getInstance(final Locale locale)
public static Currency getInstance(final ULocale locale)
public static Currency getInstance(final String theISOCode)
'''
pass
def getAvailableCurrencyCodes():
'''public static String[] getAvailableCurrencyCodes(final ULocale loc, final Date d)
public static String[] getAvailableCurrencyCodes(final Locale loc, final Date d)
'''
pass
def getAvailableCurrencies():
'''public static Set<Currency> getAvailableCurrencies()
'''
pass
def fromJavaCurrency():
'''public static Currency fromJavaCurrency(final java.util.Currency currency)
'''
pass
def registerInstance():
'''public static Object registerInstance(final Currency currency, final ULocale locale)
'''
pass
def unregister():
'''public static boolean unregister(final Object registryKey)
'''
pass
def getAvailableLocales():
'''public static Locale[] getAvailableLocales()
'''
pass
def getAvailableULocales():
'''public static ULocale[] getAvailableULocales()
'''
pass
def getKeywordValuesForLocale():
'''public static final String[] getKeywordValuesForLocale(final String key, final ULocale locale, final boolean commonlyUsed)
'''
pass
def getCurrencyCode():
'''public String getCurrencyCode()
'''
pass
def getNumericCode():
'''public int getNumericCode()
'''
pass
def getSymbol():
'''public String getSymbol()
public String getSymbol(final Locale loc)
public String getSymbol(final ULocale uloc)
'''
pass
def getName():
'''public String getName(final Locale locale, final int nameStyle, final boolean[] isChoiceFormat)
public String getName(final ULocale locale, final int nameStyle, final boolean[] isChoiceFormat)
public String getName(final Locale locale, final int nameStyle, final String pluralCount, final boolean[] isChoiceFormat)
public String getName(final ULocale locale, final int nameStyle, final String pluralCount, final boolean[] isChoiceFormat)
'''
pass
def getDisplayName():
'''public String getDisplayName()
public String getDisplayName(final Locale locale)
'''
pass
def parse():
'''public static String parse(final ULocale locale, final String text, final int type, final ParsePosition pos)
'''
pass
def getParsingTrie():
'''public static TextTrieMap<CurrencyStringInfo> getParsingTrie(final ULocale locale, final int type)
'''
pass
def getDefaultFractionDigits():
'''public int getDefaultFractionDigits()
public int getDefaultFractionDigits(final CurrencyUsage Usage)
'''
pass
def getRoundingIncrement():
'''public double getRoundingIncrement()
public double getRoundingIncrement(final CurrencyUsage Usage)
'''
pass
def toString():
'''public String toString()
'''
pass
def isAvailable():
'''public static boolean isAvailable(String code, final Date from, final Date to)
'''
pass
def CurrencyStringInfo():
'''public CurrencyStringInfo(final String isoCode, final String currencyString)
'''
pass
def getISOCode():
'''public String getISOCode()
'''
pass
def getCurrencyString():
'''public String getCurrencyString()
'''
pass
def handlePrefixMatch():
'''public boolean handlePrefixMatch(final int matchLength, final Iterator<CurrencyStringInfo> values)
'''
pass
def getBestCurrencyISOCode():
'''public String getBestCurrencyISOCode()
'''
pass
def getBestMatchLength():
'''public int getBestMatchLength()
'''
pass
