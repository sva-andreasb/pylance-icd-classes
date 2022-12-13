CURRENCY_SPC_CURRENCY_MATCH = "int  0"
CURRENCY_SPC_SURROUNDING_MATCH = "int  1"
CURRENCY_SPC_INSERT = "int  2"
def DecimalFormatSymbols():
    '''public DecimalFormatSymbols()
    public DecimalFormatSymbols(final Locale locale)
    public DecimalFormatSymbols(final ULocale locale)
    '''
def getInstance():
    '''public static DecimalFormatSymbols getInstance()
    public static DecimalFormatSymbols getInstance(final Locale locale)
    public static DecimalFormatSymbols getInstance(final ULocale locale)
    '''
def forNumberingSystem():
    '''public static DecimalFormatSymbols forNumberingSystem(final Locale locale, final NumberingSystem ns)
    public static DecimalFormatSymbols forNumberingSystem(final ULocale locale, final NumberingSystem ns)
    '''
def getAvailableLocales():
    '''public static Locale[] getAvailableLocales()
    '''
def getAvailableULocales():
    '''public static ULocale[] getAvailableULocales()
    '''
def getZeroDigit():
    '''public char getZeroDigit()
    '''
def getDigits():
    '''public char[] getDigits()
    '''
def setZeroDigit():
    '''public void setZeroDigit(final char zeroDigit)
    '''
def getDigitStrings():
    '''public String[] getDigitStrings()
    '''
def getDigitStringsLocal():
    '''public String[] getDigitStringsLocal()
    '''
def getCodePointZero():
    '''public int getCodePointZero()
    '''
def setDigitStrings():
    '''public void setDigitStrings(final String[] digitStrings)
    '''
def getSignificantDigit():
    '''public char getSignificantDigit()
    '''
def setSignificantDigit():
    '''public void setSignificantDigit(final char sigDigit)
    '''
def getGroupingSeparator():
    '''public char getGroupingSeparator()
    '''
def setGroupingSeparator():
    '''public void setGroupingSeparator(final char groupingSeparator)
    '''
def getGroupingSeparatorString():
    '''public String getGroupingSeparatorString()
    '''
def setGroupingSeparatorString():
    '''public void setGroupingSeparatorString(final String groupingSeparatorString)
    '''
def getDecimalSeparator():
    '''public char getDecimalSeparator()
    '''
def setDecimalSeparator():
    '''public void setDecimalSeparator(final char decimalSeparator)
    '''
def getDecimalSeparatorString():
    '''public String getDecimalSeparatorString()
    '''
def setDecimalSeparatorString():
    '''public void setDecimalSeparatorString(final String decimalSeparatorString)
    '''
def getPerMill():
    '''public char getPerMill()
    '''
def setPerMill():
    '''public void setPerMill(final char perMill)
    '''
def getPerMillString():
    '''public String getPerMillString()
    '''
def setPerMillString():
    '''public void setPerMillString(final String perMillString)
    '''
def getPercent():
    '''public char getPercent()
    '''
def setPercent():
    '''public void setPercent(final char percent)
    '''
def getPercentString():
    '''public String getPercentString()
    '''
def setPercentString():
    '''public void setPercentString(final String percentString)
    '''
def getDigit():
    '''public char getDigit()
    '''
def setDigit():
    '''public void setDigit(final char digit)
    '''
def getPatternSeparator():
    '''public char getPatternSeparator()
    '''
def setPatternSeparator():
    '''public void setPatternSeparator(final char patternSeparator)
    '''
def getInfinity():
    '''public String getInfinity()
    '''
def setInfinity():
    '''public void setInfinity(final String infinity)
    '''
def getNaN():
    '''public String getNaN()
    '''
def setNaN():
    '''public void setNaN(final String NaN)
    '''
def getMinusSign():
    '''public char getMinusSign()
    '''
def setMinusSign():
    '''public void setMinusSign(final char minusSign)
    '''
def getMinusSignString():
    '''public String getMinusSignString()
    '''
def setMinusSignString():
    '''public void setMinusSignString(final String minusSignString)
    '''
def getPlusSign():
    '''public char getPlusSign()
    '''
def setPlusSign():
    '''public void setPlusSign(final char plus)
    '''
def getPlusSignString():
    '''public String getPlusSignString()
    '''
def setPlusSignString():
    '''public void setPlusSignString(final String plusSignString)
    '''
def getCurrencySymbol():
    '''public String getCurrencySymbol()
    '''
def setCurrencySymbol():
    '''public void setCurrencySymbol(final String currency)
    '''
def getInternationalCurrencySymbol():
    '''public String getInternationalCurrencySymbol()
    '''
def setInternationalCurrencySymbol():
    '''public void setInternationalCurrencySymbol(final String currency)
    '''
def getCurrency():
    '''public Currency getCurrency()
    '''
def setCurrency():
    '''public void setCurrency(final Currency currency)
    '''
def getMonetaryDecimalSeparator():
    '''public char getMonetaryDecimalSeparator()
    '''
def setMonetaryDecimalSeparator():
    '''public void setMonetaryDecimalSeparator(final char sep)
    '''
def getMonetaryDecimalSeparatorString():
    '''public String getMonetaryDecimalSeparatorString()
    '''
def setMonetaryDecimalSeparatorString():
    '''public void setMonetaryDecimalSeparatorString(final String sep)
    '''
def getMonetaryGroupingSeparator():
    '''public char getMonetaryGroupingSeparator()
    '''
def setMonetaryGroupingSeparator():
    '''public void setMonetaryGroupingSeparator(final char sep)
    '''
def getMonetaryGroupingSeparatorString():
    '''public String getMonetaryGroupingSeparatorString()
    '''
def setMonetaryGroupingSeparatorString():
    '''public void setMonetaryGroupingSeparatorString(final String sep)
    '''
def getCurrencyPattern():
    '''public String getCurrencyPattern()
    '''
def getExponentMultiplicationSign():
    '''public String getExponentMultiplicationSign()
    '''
def setExponentMultiplicationSign():
    '''public void setExponentMultiplicationSign(final String exponentMultiplicationSign)
    '''
def getExponentSeparator():
    '''public String getExponentSeparator()
    '''
def setExponentSeparator():
    '''public void setExponentSeparator(final String exp)
    '''
def getPadEscape():
    '''public char getPadEscape()
    '''
def setPadEscape():
    '''public void setPadEscape(final char c)
    '''
def getPatternForCurrencySpacing():
    '''public String getPatternForCurrencySpacing(final int itemType, final boolean beforeCurrency)
    '''
def setPatternForCurrencySpacing():
    '''public void setPatternForCurrencySpacing(final int itemType, final boolean beforeCurrency, final String pattern)
    '''
def getLocale():
    '''public Locale getLocale()
    public final ULocale getLocale(final ULocale.Type type)
    '''
def getULocale():
    '''public ULocale getULocale()
    '''
def clone():
    '''public Object clone()
    '''
def equals():
    '''public boolean equals(final Object obj)
    '''
def hashCode():
    '''public int hashCode()
    '''
def DecFmtDataSink():
    '''public DecFmtDataSink(final String[] numberElements)
    '''
def put():
    '''public void put(final UResource.Key key, final UResource.Value value, final boolean noFallback)
    '''
def CacheData():
    '''public CacheData(final ULocale loc, final String[] digits, final String[] numberElements)
    '''
