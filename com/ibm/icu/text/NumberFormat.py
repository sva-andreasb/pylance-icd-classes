NUMBERSTYLE = "int  0"
CURRENCYSTYLE = "int  1"
PERCENTSTYLE = "int  2"
SCIENTIFICSTYLE = "int  3"
INTEGERSTYLE = "int  4"
ISOCURRENCYSTYLE = "int  5"
PLURALCURRENCYSTYLE = "int  6"
ACCOUNTINGCURRENCYSTYLE = "int  7"
CASHCURRENCYSTYLE = "int  8"
STANDARDCURRENCYSTYLE = "int  9"
INTEGER_FIELD = "int  0"
FRACTION_FIELD = "int  1"
FORMAT_NUMBER = "int  0"
FORMAT_CURRENCY = "int  1"
FORMAT_PERCENT = "int  2"
FORMAT_SCIENTIFIC = "int  3"
FORMAT_INTEGER = "int  4"
def format():
'''public StringBuffer format(final Object number, final StringBuffer toAppendTo, final FieldPosition pos)
public final String format(final double number)
public final String format(final long number)
public final String format(final BigInteger number)
public final String format(final BigDecimal number)
public final String format(final com.ibm.icu.math.BigDecimal number)
public final String format(final CurrencyAmount currAmt)
public StringBuffer format(final CurrencyAmount currAmt, final StringBuffer toAppendTo, final FieldPosition pos)
'''
pass
def parseObject():
'''public final Object parseObject(final String source, final ParsePosition parsePosition)
'''
pass
def parse():
'''public Number parse(final String text)
'''
pass
def parseCurrency():
'''public CurrencyAmount parseCurrency(final CharSequence text, final ParsePosition pos)
'''
pass
def isParseIntegerOnly():
'''public boolean isParseIntegerOnly()
'''
pass
def setParseIntegerOnly():
'''public void setParseIntegerOnly(final boolean value)
'''
pass
def setParseStrict():
'''public void setParseStrict(final boolean value)
'''
pass
def isParseStrict():
'''public boolean isParseStrict()
'''
pass
def setContext():
'''public void setContext(final DisplayContext context)
'''
pass
def getContext():
'''public DisplayContext getContext(final DisplayContext.Type type)
'''
pass
def getInstance():
'''public static final NumberFormat getInstance()
public static NumberFormat getInstance(final Locale inLocale)
public static NumberFormat getInstance(final ULocale inLocale)
public static final NumberFormat getInstance(final int style)
public static NumberFormat getInstance(final Locale inLocale, final int style)
public static NumberFormat getInstance(final ULocale desiredLocale, final int choice)
'''
pass
def getNumberInstance():
'''public static final NumberFormat getNumberInstance()
public static NumberFormat getNumberInstance(final Locale inLocale)
public static NumberFormat getNumberInstance(final ULocale inLocale)
'''
pass
def getIntegerInstance():
'''public static final NumberFormat getIntegerInstance()
public static NumberFormat getIntegerInstance(final Locale inLocale)
public static NumberFormat getIntegerInstance(final ULocale inLocale)
'''
pass
def getCurrencyInstance():
'''public static final NumberFormat getCurrencyInstance()
public static NumberFormat getCurrencyInstance(final Locale inLocale)
public static NumberFormat getCurrencyInstance(final ULocale inLocale)
'''
pass
def getPercentInstance():
'''public static final NumberFormat getPercentInstance()
public static NumberFormat getPercentInstance(final Locale inLocale)
public static NumberFormat getPercentInstance(final ULocale inLocale)
'''
pass
def getScientificInstance():
'''public static final NumberFormat getScientificInstance()
public static NumberFormat getScientificInstance(final Locale inLocale)
public static NumberFormat getScientificInstance(final ULocale inLocale)
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
def registerFactory():
'''public static Object registerFactory(final NumberFormatFactory factory)
'''
pass
def unregister():
'''public static boolean unregister(final Object registryKey)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def equals():
'''public boolean equals(final Object obj)
'''
pass
def clone():
'''public Object clone()
'''
pass
def isGroupingUsed():
'''public boolean isGroupingUsed()
'''
pass
def setGroupingUsed():
'''public void setGroupingUsed(final boolean newValue)
'''
pass
def getMaximumIntegerDigits():
'''public int getMaximumIntegerDigits()
'''
pass
def setMaximumIntegerDigits():
'''public void setMaximumIntegerDigits(final int newValue)
'''
pass
def getMinimumIntegerDigits():
'''public int getMinimumIntegerDigits()
'''
pass
def setMinimumIntegerDigits():
'''public void setMinimumIntegerDigits(final int newValue)
'''
pass
def getMaximumFractionDigits():
'''public int getMaximumFractionDigits()
'''
pass
def setMaximumFractionDigits():
'''public void setMaximumFractionDigits(final int newValue)
'''
pass
def getMinimumFractionDigits():
'''public int getMinimumFractionDigits()
'''
pass
def setMinimumFractionDigits():
'''public void setMinimumFractionDigits(final int newValue)
'''
pass
def setCurrency():
'''public void setCurrency(final Currency theCurrency)
'''
pass
def getCurrency():
'''public Currency getCurrency()
'''
pass
def getRoundingMode():
'''public int getRoundingMode()
'''
pass
def setRoundingMode():
'''public void setRoundingMode(final int roundingMode)
'''
pass
def getPatternForStyle():
'''public static String getPatternForStyle(final ULocale forLocale, final int choice)
'''
pass
def getPatternForStyleAndNumberingSystem():
'''public static String getPatternForStyleAndNumberingSystem(final ULocale forLocale, final String nsName, final int choice)
'''
pass
def NumberFormat():
'''public NumberFormat()
'''
pass
def visible():
'''public boolean visible()
public final boolean visible()
'''
pass
def createFormat():
'''public NumberFormat createFormat(final ULocale loc, final int formatType)
public NumberFormat createFormat(final Locale loc, final int formatType)
'''
pass
def SimpleNumberFormatFactory():
'''public SimpleNumberFormatFactory(final Locale locale)
public SimpleNumberFormatFactory(final Locale locale, final boolean visible)
public SimpleNumberFormatFactory(final ULocale locale)
public SimpleNumberFormatFactory(final ULocale locale, final boolean visible)
'''
pass
def getSupportedLocaleNames():
'''public final Set<String> getSupportedLocaleNames()
'''
pass
