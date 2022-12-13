PAD_BEFORE_PREFIX = "int 0"
PAD_AFTER_PREFIX = "int 1"
PAD_BEFORE_SUFFIX = "int 2"
PAD_AFTER_SUFFIX = "int 3"
def DecimalFormat():
'''public DecimalFormat()
public DecimalFormat(final String pattern)
public DecimalFormat(final String pattern, final DecimalFormatSymbols symbols)
public DecimalFormat(final String pattern, final DecimalFormatSymbols symbols, final CurrencyPluralInfo infoInput, final int style)
'''
pass
def applyPattern():
'''public synchronized void applyPattern(final String pattern)
'''
pass
def applyLocalizedPattern():
'''public synchronized void applyLocalizedPattern(final String localizedPattern)
'''
pass
def clone():
'''public Object clone()
'''
pass
def format():
'''public StringBuffer format(final double number, final StringBuffer result, final FieldPosition fieldPosition)
public StringBuffer format(final long number, final StringBuffer result, final FieldPosition fieldPosition)
public StringBuffer format(final BigInteger number, final StringBuffer result, final FieldPosition fieldPosition)
public StringBuffer format(final BigDecimal number, final StringBuffer result, final FieldPosition fieldPosition)
public StringBuffer format(final com.ibm.icu.math.BigDecimal number, final StringBuffer result, final FieldPosition fieldPosition)
public StringBuffer format(final CurrencyAmount currAmt, final StringBuffer result, final FieldPosition fieldPosition)
'''
pass
def formatToCharacterIterator():
'''public AttributedCharacterIterator formatToCharacterIterator(final Object obj)
'''
pass
def parse():
'''public Number parse(final String text, ParsePosition parsePosition)
'''
pass
def parseCurrency():
'''public CurrencyAmount parseCurrency(final CharSequence text, ParsePosition parsePosition)
'''
pass
def getDecimalFormatSymbols():
'''public synchronized DecimalFormatSymbols getDecimalFormatSymbols()
'''
pass
def setDecimalFormatSymbols():
'''public synchronized void setDecimalFormatSymbols(final DecimalFormatSymbols newSymbols)
'''
pass
def getPositivePrefix():
'''public synchronized String getPositivePrefix()
'''
pass
def setPositivePrefix():
'''public synchronized void setPositivePrefix(final String prefix)
'''
pass
def getNegativePrefix():
'''public synchronized String getNegativePrefix()
'''
pass
def setNegativePrefix():
'''public synchronized void setNegativePrefix(final String prefix)
'''
pass
def getPositiveSuffix():
'''public synchronized String getPositiveSuffix()
'''
pass
def setPositiveSuffix():
'''public synchronized void setPositiveSuffix(final String suffix)
'''
pass
def getNegativeSuffix():
'''public synchronized String getNegativeSuffix()
'''
pass
def setNegativeSuffix():
'''public synchronized void setNegativeSuffix(final String suffix)
'''
pass
def isSignAlwaysShown():
'''public synchronized boolean isSignAlwaysShown()
'''
pass
def setSignAlwaysShown():
'''public synchronized void setSignAlwaysShown(final boolean value)
'''
pass
def getMultiplier():
'''public synchronized int getMultiplier()
'''
pass
def setMultiplier():
'''public synchronized void setMultiplier(final int multiplier)
'''
pass
def getRoundingIncrement():
'''public synchronized BigDecimal getRoundingIncrement()
'''
pass
def setRoundingIncrement():
'''public synchronized void setRoundingIncrement(final BigDecimal increment)
public synchronized void setRoundingIncrement(final com.ibm.icu.math.BigDecimal increment)
public synchronized void setRoundingIncrement(final double increment)
'''
pass
def getRoundingMode():
'''public synchronized int getRoundingMode()
'''
pass
def setRoundingMode():
'''public synchronized void setRoundingMode(final int roundingMode)
'''
pass
def setMathContext():
'''public synchronized void setMathContext(final java.math.MathContext mathContext)
'''
pass
def getMathContextICU():
'''public synchronized MathContext getMathContextICU()
'''
pass
def setMathContextICU():
'''public synchronized void setMathContextICU(final MathContext mathContextICU)
'''
pass
def getMinimumIntegerDigits():
'''public synchronized int getMinimumIntegerDigits()
'''
pass
def setMinimumIntegerDigits():
'''public synchronized void setMinimumIntegerDigits(final int value)
'''
pass
def getMaximumIntegerDigits():
'''public synchronized int getMaximumIntegerDigits()
'''
pass
def setMaximumIntegerDigits():
'''public synchronized void setMaximumIntegerDigits(final int value)
'''
pass
def getMinimumFractionDigits():
'''public synchronized int getMinimumFractionDigits()
'''
pass
def setMinimumFractionDigits():
'''public synchronized void setMinimumFractionDigits(final int value)
'''
pass
def getMaximumFractionDigits():
'''public synchronized int getMaximumFractionDigits()
'''
pass
def setMaximumFractionDigits():
'''public synchronized void setMaximumFractionDigits(final int value)
'''
pass
def areSignificantDigitsUsed():
'''public synchronized boolean areSignificantDigitsUsed()
'''
pass
def setSignificantDigitsUsed():
'''public synchronized void setSignificantDigitsUsed(final boolean useSignificantDigits)
'''
pass
def getMinimumSignificantDigits():
'''public synchronized int getMinimumSignificantDigits()
'''
pass
def setMinimumSignificantDigits():
'''public synchronized void setMinimumSignificantDigits(final int value)
'''
pass
def getMaximumSignificantDigits():
'''public synchronized int getMaximumSignificantDigits()
'''
pass
def setMaximumSignificantDigits():
'''public synchronized void setMaximumSignificantDigits(final int value)
'''
pass
def getFormatWidth():
'''public synchronized int getFormatWidth()
'''
pass
def setFormatWidth():
'''public synchronized void setFormatWidth(final int width)
'''
pass
def getPadCharacter():
'''public synchronized char getPadCharacter()
'''
pass
def setPadCharacter():
'''public synchronized void setPadCharacter(final char padChar)
'''
pass
def getPadPosition():
'''public synchronized int getPadPosition()
'''
pass
def setPadPosition():
'''public synchronized void setPadPosition(final int padPos)
'''
pass
def isScientificNotation():
'''public synchronized boolean isScientificNotation()
'''
pass
def setScientificNotation():
'''public synchronized void setScientificNotation(final boolean useScientific)
'''
pass
def getMinimumExponentDigits():
'''public synchronized byte getMinimumExponentDigits()
'''
pass
def setMinimumExponentDigits():
'''public synchronized void setMinimumExponentDigits(final byte minExpDig)
'''
pass
def isExponentSignAlwaysShown():
'''public synchronized boolean isExponentSignAlwaysShown()
'''
pass
def setExponentSignAlwaysShown():
'''public synchronized void setExponentSignAlwaysShown(final boolean expSignAlways)
'''
pass
def isGroupingUsed():
'''public synchronized boolean isGroupingUsed()
'''
pass
def setGroupingUsed():
'''public synchronized void setGroupingUsed(final boolean enabled)
'''
pass
def getGroupingSize():
'''public synchronized int getGroupingSize()
'''
pass
def setGroupingSize():
'''public synchronized void setGroupingSize(final int width)
'''
pass
def getSecondaryGroupingSize():
'''public synchronized int getSecondaryGroupingSize()
'''
pass
def setSecondaryGroupingSize():
'''public synchronized void setSecondaryGroupingSize(final int width)
'''
pass
def getMinimumGroupingDigits():
'''public synchronized int getMinimumGroupingDigits()
'''
pass
def setMinimumGroupingDigits():
'''public synchronized void setMinimumGroupingDigits(final int number)
'''
pass
def isDecimalSeparatorAlwaysShown():
'''public synchronized boolean isDecimalSeparatorAlwaysShown()
'''
pass
def setDecimalSeparatorAlwaysShown():
'''public synchronized void setDecimalSeparatorAlwaysShown(final boolean value)
'''
pass
def getCurrency():
'''public synchronized Currency getCurrency()
'''
pass
def setCurrency():
'''public synchronized void setCurrency(final Currency currency)
'''
pass
def setCurrencyUsage():
'''public synchronized void setCurrencyUsage(final Currency.CurrencyUsage usage)
'''
pass
def getCurrencyPluralInfo():
'''public synchronized CurrencyPluralInfo getCurrencyPluralInfo()
'''
pass
def setCurrencyPluralInfo():
'''public synchronized void setCurrencyPluralInfo(final CurrencyPluralInfo newInfo)
'''
pass
def isParseBigDecimal():
'''public synchronized boolean isParseBigDecimal()
'''
pass
def setParseBigDecimal():
'''public synchronized void setParseBigDecimal(final boolean value)
'''
pass
def getParseMaxDigits():
'''public int getParseMaxDigits()
'''
pass
def setParseMaxDigits():
'''public void setParseMaxDigits(final int maxDigits)
'''
pass
def isParseStrict():
'''public synchronized boolean isParseStrict()
'''
pass
def setParseStrict():
'''public synchronized void setParseStrict(final boolean parseStrict)
'''
pass
def setParseStrictMode():
'''public synchronized void setParseStrictMode(final DecimalFormatProperties.ParseMode parseMode)
'''
pass
def isParseIntegerOnly():
'''public synchronized boolean isParseIntegerOnly()
'''
pass
def setParseIntegerOnly():
'''public synchronized void setParseIntegerOnly(final boolean parseIntegerOnly)
'''
pass
def isDecimalPatternMatchRequired():
'''public synchronized boolean isDecimalPatternMatchRequired()
'''
pass
def setDecimalPatternMatchRequired():
'''public synchronized void setDecimalPatternMatchRequired(final boolean value)
'''
pass
def isParseNoExponent():
'''public synchronized boolean isParseNoExponent()
'''
pass
def setParseNoExponent():
'''public synchronized void setParseNoExponent(final boolean value)
'''
pass
def isParseCaseSensitive():
'''public synchronized boolean isParseCaseSensitive()
'''
pass
def setParseCaseSensitive():
'''public synchronized void setParseCaseSensitive(final boolean value)
'''
pass
def equals():
'''public synchronized boolean equals(final Object obj)
'''
pass
def hashCode():
'''public synchronized int hashCode()
'''
pass
def toString():
'''public String toString()
'''
pass
def toPattern():
'''public synchronized String toPattern()
'''
pass
def toLocalizedPattern():
'''public synchronized String toLocalizedPattern()
'''
pass
def toNumberFormatter():
'''public LocalizedNumberFormatter toNumberFormatter()
'''
pass
def setProperties():
'''public synchronized void setProperties(final PropertySetter func)
'''
pass
