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
    '''    public StringBuffer format(final Object number, final StringBuffer toAppendTo, final FieldPosition pos)
    public final String format(final double number)
    public final String format(final long number)
    public final String format(final BigInteger number)
    public final String format(final BigDecimal number)
    public final String format(final com.ibm.icu.math.BigDecimal number)
    public final String format(final CurrencyAmount currAmt)
    public StringBuffer format(final CurrencyAmount currAmt, final StringBuffer toAppendTo, final FieldPosition pos)
    '''
def parseObject():
    '''    public final Object parseObject(final String source, final ParsePosition parsePosition)
    '''
def parse():
    '''    public Number parse(final String text)
    '''
def parseCurrency():
    '''    public CurrencyAmount parseCurrency(final CharSequence text, final ParsePosition pos)
    '''
def isParseIntegerOnly():
    '''    public boolean isParseIntegerOnly()
    '''
def setParseIntegerOnly():
    '''    public void setParseIntegerOnly(final boolean value)
    '''
def setParseStrict():
    '''    public void setParseStrict(final boolean value)
    '''
def isParseStrict():
    '''    public boolean isParseStrict()
    '''
def setContext():
    '''    public void setContext(final DisplayContext context)
    '''
def getContext():
    '''    public DisplayContext getContext(final DisplayContext.Type type)
    '''
def getInstance():
    '''    public static final NumberFormat getInstance()
    public static NumberFormat getInstance(final Locale inLocale)
    public static NumberFormat getInstance(final ULocale inLocale)
    public static final NumberFormat getInstance(final int style)
    public static NumberFormat getInstance(final Locale inLocale, final int style)
    public static NumberFormat getInstance(final ULocale desiredLocale, final int choice)
    '''
def getNumberInstance():
    '''    public static final NumberFormat getNumberInstance()
    public static NumberFormat getNumberInstance(final Locale inLocale)
    public static NumberFormat getNumberInstance(final ULocale inLocale)
    '''
def getIntegerInstance():
    '''    public static final NumberFormat getIntegerInstance()
    public static NumberFormat getIntegerInstance(final Locale inLocale)
    public static NumberFormat getIntegerInstance(final ULocale inLocale)
    '''
def getCurrencyInstance():
    '''    public static final NumberFormat getCurrencyInstance()
    public static NumberFormat getCurrencyInstance(final Locale inLocale)
    public static NumberFormat getCurrencyInstance(final ULocale inLocale)
    '''
def getPercentInstance():
    '''    public static final NumberFormat getPercentInstance()
    public static NumberFormat getPercentInstance(final Locale inLocale)
    public static NumberFormat getPercentInstance(final ULocale inLocale)
    '''
def getScientificInstance():
    '''    public static final NumberFormat getScientificInstance()
    public static NumberFormat getScientificInstance(final Locale inLocale)
    public static NumberFormat getScientificInstance(final ULocale inLocale)
    '''
def getAvailableLocales():
    '''    public static Locale[] getAvailableLocales()
    '''
def getAvailableULocales():
    '''    public static ULocale[] getAvailableULocales()
    '''
def registerFactory():
    '''    public static Object registerFactory(final NumberFormatFactory factory)
    '''
def unregister():
    '''    public static boolean unregister(final Object registryKey)
    '''
def hashCode():
    '''    public int hashCode()
    '''
def equals():
    '''    public boolean equals(final Object obj)
    '''
def clone():
    '''    public Object clone()
    '''
def isGroupingUsed():
    '''    public boolean isGroupingUsed()
    '''
def setGroupingUsed():
    '''    public void setGroupingUsed(final boolean newValue)
    '''
def getMaximumIntegerDigits():
    '''    public int getMaximumIntegerDigits()
    '''
def setMaximumIntegerDigits():
    '''    public void setMaximumIntegerDigits(final int newValue)
    '''
def getMinimumIntegerDigits():
    '''    public int getMinimumIntegerDigits()
    '''
def setMinimumIntegerDigits():
    '''    public void setMinimumIntegerDigits(final int newValue)
    '''
def getMaximumFractionDigits():
    '''    public int getMaximumFractionDigits()
    '''
def setMaximumFractionDigits():
    '''    public void setMaximumFractionDigits(final int newValue)
    '''
def getMinimumFractionDigits():
    '''    public int getMinimumFractionDigits()
    '''
def setMinimumFractionDigits():
    '''    public void setMinimumFractionDigits(final int newValue)
    '''
def setCurrency():
    '''    public void setCurrency(final Currency theCurrency)
    '''
def getCurrency():
    '''    public Currency getCurrency()
    '''
def getRoundingMode():
    '''    public int getRoundingMode()
    '''
def setRoundingMode():
    '''    public void setRoundingMode(final int roundingMode)
    '''
def getPatternForStyle():
    '''    public static String getPatternForStyle(final ULocale forLocale, final int choice)
    '''
def getPatternForStyleAndNumberingSystem():
    '''    public static String getPatternForStyleAndNumberingSystem(final ULocale forLocale, final String nsName, final int choice)
    '''
def NumberFormat():
    '''    public NumberFormat()
    '''
def visible():
    '''    public boolean visible()
    public final boolean visible()
    '''
def createFormat():
    '''    public NumberFormat createFormat(final ULocale loc, final int formatType)
    public NumberFormat createFormat(final Locale loc, final int formatType)
    '''
def SimpleNumberFormatFactory():
    '''    public SimpleNumberFormatFactory(final Locale locale)
    public SimpleNumberFormatFactory(final Locale locale, final boolean visible)
    public SimpleNumberFormatFactory(final ULocale locale)
    public SimpleNumberFormatFactory(final ULocale locale, final boolean visible)
    '''
def getSupportedLocaleNames():
    '''    public final Set<String> getSupportedLocaleNames()
    '''
