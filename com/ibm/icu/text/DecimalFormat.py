PAD_BEFORE_PREFIX = "int  0"
PAD_AFTER_PREFIX = "int  1"
PAD_BEFORE_SUFFIX = "int  2"
PAD_AFTER_SUFFIX = "int  3"
def DecimalFormat():
    '''    public DecimalFormat()
    public DecimalFormat(final String pattern)
    public DecimalFormat(final String pattern, final DecimalFormatSymbols symbols)
    public DecimalFormat(final String pattern, final DecimalFormatSymbols symbols, final CurrencyPluralInfo infoInput, final int style)
    '''
def applyPattern():
    '''    public synchronized void applyPattern(final String pattern)
    '''
def applyLocalizedPattern():
    '''    public synchronized void applyLocalizedPattern(final String localizedPattern)
    '''
def clone():
    '''    public Object clone()
    '''
def format():
    '''    public StringBuffer format(final double number, final StringBuffer result, final FieldPosition fieldPosition)
    public StringBuffer format(final long number, final StringBuffer result, final FieldPosition fieldPosition)
    public StringBuffer format(final BigInteger number, final StringBuffer result, final FieldPosition fieldPosition)
    public StringBuffer format(final BigDecimal number, final StringBuffer result, final FieldPosition fieldPosition)
    public StringBuffer format(final com.ibm.icu.math.BigDecimal number, final StringBuffer result, final FieldPosition fieldPosition)
    public StringBuffer format(final CurrencyAmount currAmt, final StringBuffer result, final FieldPosition fieldPosition)
    '''
def formatToCharacterIterator():
    '''    public AttributedCharacterIterator formatToCharacterIterator(final Object obj)
    '''
def parse():
    '''    public Number parse(final String text, ParsePosition parsePosition)
    '''
def parseCurrency():
    '''    public CurrencyAmount parseCurrency(final CharSequence text, ParsePosition parsePosition)
    '''
def getDecimalFormatSymbols():
    '''    public synchronized DecimalFormatSymbols getDecimalFormatSymbols()
    '''
def setDecimalFormatSymbols():
    '''    public synchronized void setDecimalFormatSymbols(final DecimalFormatSymbols newSymbols)
    '''
def getPositivePrefix():
    '''    public synchronized String getPositivePrefix()
    '''
def setPositivePrefix():
    '''    public synchronized void setPositivePrefix(final String prefix)
    '''
def getNegativePrefix():
    '''    public synchronized String getNegativePrefix()
    '''
def setNegativePrefix():
    '''    public synchronized void setNegativePrefix(final String prefix)
    '''
def getPositiveSuffix():
    '''    public synchronized String getPositiveSuffix()
    '''
def setPositiveSuffix():
    '''    public synchronized void setPositiveSuffix(final String suffix)
    '''
def getNegativeSuffix():
    '''    public synchronized String getNegativeSuffix()
    '''
def setNegativeSuffix():
    '''    public synchronized void setNegativeSuffix(final String suffix)
    '''
def isSignAlwaysShown():
    '''    public synchronized boolean isSignAlwaysShown()
    '''
def setSignAlwaysShown():
    '''    public synchronized void setSignAlwaysShown(final boolean value)
    '''
def getMultiplier():
    '''    public synchronized int getMultiplier()
    '''
def setMultiplier():
    '''    public synchronized void setMultiplier(final int multiplier)
    '''
def getRoundingIncrement():
    '''    public synchronized BigDecimal getRoundingIncrement()
    '''
def setRoundingIncrement():
    '''    public synchronized void setRoundingIncrement(final BigDecimal increment)
    public synchronized void setRoundingIncrement(final com.ibm.icu.math.BigDecimal increment)
    public synchronized void setRoundingIncrement(final double increment)
    '''
def getRoundingMode():
    '''    public synchronized int getRoundingMode()
    '''
def setRoundingMode():
    '''    public synchronized void setRoundingMode(final int roundingMode)
    '''
def setMathContext():
    '''    public synchronized void setMathContext(final java.math.MathContext mathContext)
    '''
def getMathContextICU():
    '''    public synchronized MathContext getMathContextICU()
    '''
def setMathContextICU():
    '''    public synchronized void setMathContextICU(final MathContext mathContextICU)
    '''
def getMinimumIntegerDigits():
    '''    public synchronized int getMinimumIntegerDigits()
    '''
def setMinimumIntegerDigits():
    '''    public synchronized void setMinimumIntegerDigits(final int value)
    '''
def getMaximumIntegerDigits():
    '''    public synchronized int getMaximumIntegerDigits()
    '''
def setMaximumIntegerDigits():
    '''    public synchronized void setMaximumIntegerDigits(final int value)
    '''
def getMinimumFractionDigits():
    '''    public synchronized int getMinimumFractionDigits()
    '''
def setMinimumFractionDigits():
    '''    public synchronized void setMinimumFractionDigits(final int value)
    '''
def getMaximumFractionDigits():
    '''    public synchronized int getMaximumFractionDigits()
    '''
def setMaximumFractionDigits():
    '''    public synchronized void setMaximumFractionDigits(final int value)
    '''
def areSignificantDigitsUsed():
    '''    public synchronized boolean areSignificantDigitsUsed()
    '''
def setSignificantDigitsUsed():
    '''    public synchronized void setSignificantDigitsUsed(final boolean useSignificantDigits)
    '''
def getMinimumSignificantDigits():
    '''    public synchronized int getMinimumSignificantDigits()
    '''
def setMinimumSignificantDigits():
    '''    public synchronized void setMinimumSignificantDigits(final int value)
    '''
def getMaximumSignificantDigits():
    '''    public synchronized int getMaximumSignificantDigits()
    '''
def setMaximumSignificantDigits():
    '''    public synchronized void setMaximumSignificantDigits(final int value)
    '''
def getFormatWidth():
    '''    public synchronized int getFormatWidth()
    '''
def setFormatWidth():
    '''    public synchronized void setFormatWidth(final int width)
    '''
def getPadCharacter():
    '''    public synchronized char getPadCharacter()
    '''
def setPadCharacter():
    '''    public synchronized void setPadCharacter(final char padChar)
    '''
def getPadPosition():
    '''    public synchronized int getPadPosition()
    '''
def setPadPosition():
    '''    public synchronized void setPadPosition(final int padPos)
    '''
def isScientificNotation():
    '''    public synchronized boolean isScientificNotation()
    '''
def setScientificNotation():
    '''    public synchronized void setScientificNotation(final boolean useScientific)
    '''
def getMinimumExponentDigits():
    '''    public synchronized byte getMinimumExponentDigits()
    '''
def setMinimumExponentDigits():
    '''    public synchronized void setMinimumExponentDigits(final byte minExpDig)
    '''
def isExponentSignAlwaysShown():
    '''    public synchronized boolean isExponentSignAlwaysShown()
    '''
def setExponentSignAlwaysShown():
    '''    public synchronized void setExponentSignAlwaysShown(final boolean expSignAlways)
    '''
def isGroupingUsed():
    '''    public synchronized boolean isGroupingUsed()
    '''
def setGroupingUsed():
    '''    public synchronized void setGroupingUsed(final boolean enabled)
    '''
def getGroupingSize():
    '''    public synchronized int getGroupingSize()
    '''
def setGroupingSize():
    '''    public synchronized void setGroupingSize(final int width)
    '''
def getSecondaryGroupingSize():
    '''    public synchronized int getSecondaryGroupingSize()
    '''
def setSecondaryGroupingSize():
    '''    public synchronized void setSecondaryGroupingSize(final int width)
    '''
def getMinimumGroupingDigits():
    '''    public synchronized int getMinimumGroupingDigits()
    '''
def setMinimumGroupingDigits():
    '''    public synchronized void setMinimumGroupingDigits(final int number)
    '''
def isDecimalSeparatorAlwaysShown():
    '''    public synchronized boolean isDecimalSeparatorAlwaysShown()
    '''
def setDecimalSeparatorAlwaysShown():
    '''    public synchronized void setDecimalSeparatorAlwaysShown(final boolean value)
    '''
def getCurrency():
    '''    public synchronized Currency getCurrency()
    '''
def setCurrency():
    '''    public synchronized void setCurrency(final Currency currency)
    '''
def setCurrencyUsage():
    '''    public synchronized void setCurrencyUsage(final Currency.CurrencyUsage usage)
    '''
def getCurrencyPluralInfo():
    '''    public synchronized CurrencyPluralInfo getCurrencyPluralInfo()
    '''
def setCurrencyPluralInfo():
    '''    public synchronized void setCurrencyPluralInfo(final CurrencyPluralInfo newInfo)
    '''
def isParseBigDecimal():
    '''    public synchronized boolean isParseBigDecimal()
    '''
def setParseBigDecimal():
    '''    public synchronized void setParseBigDecimal(final boolean value)
    '''
def getParseMaxDigits():
    '''    public int getParseMaxDigits()
    '''
def setParseMaxDigits():
    '''    public void setParseMaxDigits(final int maxDigits)
    '''
def isParseStrict():
    '''    public synchronized boolean isParseStrict()
    '''
def setParseStrict():
    '''    public synchronized void setParseStrict(final boolean parseStrict)
    '''
def setParseStrictMode():
    '''    public synchronized void setParseStrictMode(final DecimalFormatProperties.ParseMode parseMode)
    '''
def isParseIntegerOnly():
    '''    public synchronized boolean isParseIntegerOnly()
    '''
def setParseIntegerOnly():
    '''    public synchronized void setParseIntegerOnly(final boolean parseIntegerOnly)
    '''
def isDecimalPatternMatchRequired():
    '''    public synchronized boolean isDecimalPatternMatchRequired()
    '''
def setDecimalPatternMatchRequired():
    '''    public synchronized void setDecimalPatternMatchRequired(final boolean value)
    '''
def isParseNoExponent():
    '''    public synchronized boolean isParseNoExponent()
    '''
def setParseNoExponent():
    '''    public synchronized void setParseNoExponent(final boolean value)
    '''
def isParseCaseSensitive():
    '''    public synchronized boolean isParseCaseSensitive()
    '''
def setParseCaseSensitive():
    '''    public synchronized void setParseCaseSensitive(final boolean value)
    '''
def equals():
    '''    public synchronized boolean equals(final Object obj)
    '''
def hashCode():
    '''    public synchronized int hashCode()
    '''
def toString():
    '''    public String toString()
    '''
def toPattern():
    '''    public synchronized String toPattern()
    '''
def toLocalizedPattern():
    '''    public synchronized String toLocalizedPattern()
    '''
def toNumberFormatter():
    '''    public LocalizedNumberFormatter toNumberFormatter()
    '''
def setProperties():
    '''    public synchronized void setProperties(final PropertySetter func)
    '''
