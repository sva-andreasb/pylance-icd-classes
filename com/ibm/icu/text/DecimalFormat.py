PAD_BEFORE_PREFIX = "int  0"
PAD_AFTER_PREFIX = "int  1"
PAD_BEFORE_SUFFIX = "int  2"
PAD_AFTER_SUFFIX = "int  3"
def ():
    '''returns AffixForCurrency\n\n
    ()\n
    (final String pattern)\n
    (final String pattern, final DecimalFormatSymbols symbols)\n
    (final String pattern, final DecimalFormatSymbols symbols, final CurrencyPluralInfo infoInput, final int style)\n
    (final String negPrefix, final String negSuffix, final String posPrefix, final String posSuffix, final int type)\n
    '''
def format():
    '''returns StringBuffer\n\n
    format(final double number, final StringBuffer result, final FieldPosition fieldPosition)\n
    format(final long number, final StringBuffer result, final FieldPosition fieldPosition)\n
    format(final BigInteger number, final StringBuffer result, final FieldPosition fieldPosition)\n
    format(final BigDecimal number, final StringBuffer result, final FieldPosition fieldPosition)\n
    format(com.ibm.icu.math.BigDecimal number, final StringBuffer result, final FieldPosition fieldPosition)\n
    '''
def parse():
    '''returns Number\n\n
    parse(final String text, final ParsePosition parsePosition)\n
    '''
def getDecimalFormatSymbols():
    '''returns DecimalFormatSymbols\n\n
    getDecimalFormatSymbols()\n
    '''
def setDecimalFormatSymbols():
    '''returns None\n\n
    setDecimalFormatSymbols(final DecimalFormatSymbols newSymbols)\n
    '''
def getPositivePrefix():
    '''returns String\n\n
    getPositivePrefix()\n
    '''
def setPositivePrefix():
    '''returns None\n\n
    setPositivePrefix(final String newValue)\n
    '''
def getNegativePrefix():
    '''returns String\n\n
    getNegativePrefix()\n
    '''
def setNegativePrefix():
    '''returns None\n\n
    setNegativePrefix(final String newValue)\n
    '''
def getPositiveSuffix():
    '''returns String\n\n
    getPositiveSuffix()\n
    '''
def setPositiveSuffix():
    '''returns None\n\n
    setPositiveSuffix(final String newValue)\n
    '''
def getNegativeSuffix():
    '''returns String\n\n
    getNegativeSuffix()\n
    '''
def setNegativeSuffix():
    '''returns None\n\n
    setNegativeSuffix(final String newValue)\n
    '''
def getMultiplier():
    '''returns int\n\n
    getMultiplier()\n
    '''
def setMultiplier():
    '''returns None\n\n
    setMultiplier(final int newValue)\n
    '''
def getRoundingIncrement():
    '''returns BigDecimal\n\n
    getRoundingIncrement()\n
    '''
def setRoundingIncrement():
    '''returns None\n\n
    setRoundingIncrement(final BigDecimal newValue)\n
    setRoundingIncrement(final com.ibm.icu.math.BigDecimal newValue)\n
    setRoundingIncrement(final double newValue)\n
    '''
def getRoundingMode():
    '''returns int\n\n
    getRoundingMode()\n
    '''
def setRoundingMode():
    '''returns None\n\n
    setRoundingMode(final int roundingMode)\n
    '''
def getFormatWidth():
    '''returns int\n\n
    getFormatWidth()\n
    '''
def setFormatWidth():
    '''returns None\n\n
    setFormatWidth(final int width)\n
    '''
def getPadCharacter():
    '''returns char\n\n
    getPadCharacter()\n
    '''
def setPadCharacter():
    '''returns None\n\n
    setPadCharacter(final char padChar)\n
    '''
def getPadPosition():
    '''returns int\n\n
    getPadPosition()\n
    '''
def setPadPosition():
    '''returns None\n\n
    setPadPosition(final int padPos)\n
    '''
def isScientificNotation():
    '''returns boolean\n\n
    isScientificNotation()\n
    '''
def setScientificNotation():
    '''returns None\n\n
    setScientificNotation(final boolean useScientific)\n
    '''
def getMinimumExponentDigits():
    '''returns byte\n\n
    getMinimumExponentDigits()\n
    '''
def setMinimumExponentDigits():
    '''returns None\n\n
    setMinimumExponentDigits(final byte minExpDig)\n
    '''
def isExponentSignAlwaysShown():
    '''returns boolean\n\n
    isExponentSignAlwaysShown()\n
    '''
def setExponentSignAlwaysShown():
    '''returns None\n\n
    setExponentSignAlwaysShown(final boolean expSignAlways)\n
    '''
def getGroupingSize():
    '''returns int\n\n
    getGroupingSize()\n
    '''
def setGroupingSize():
    '''returns None\n\n
    setGroupingSize(final int newValue)\n
    '''
def getSecondaryGroupingSize():
    '''returns int\n\n
    getSecondaryGroupingSize()\n
    '''
def setSecondaryGroupingSize():
    '''returns None\n\n
    setSecondaryGroupingSize(final int newValue)\n
    '''
def getMathContextICU():
    '''returns MathContext\n\n
    getMathContextICU()\n
    '''
def setMathContextICU():
    '''returns None\n\n
    setMathContextICU(final MathContext newValue)\n
    '''
def setMathContext():
    '''returns None\n\n
    setMathContext(final java.math.MathContext newValue)\n
    '''
def isDecimalSeparatorAlwaysShown():
    '''returns boolean\n\n
    isDecimalSeparatorAlwaysShown()\n
    '''
def setDecimalSeparatorAlwaysShown():
    '''returns None\n\n
    setDecimalSeparatorAlwaysShown(final boolean newValue)\n
    '''
def getCurrencyPluralInfo():
    '''returns CurrencyPluralInfo\n\n
    getCurrencyPluralInfo()\n
    '''
def setCurrencyPluralInfo():
    '''returns None\n\n
    setCurrencyPluralInfo(final CurrencyPluralInfo newInfo)\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def toPattern():
    '''returns String\n\n
    toPattern()\n
    '''
def toLocalizedPattern():
    '''returns String\n\n
    toLocalizedPattern()\n
    '''
def formatToCharacterIterator():
    '''returns AttributedCharacterIterator\n\n
    formatToCharacterIterator(final Object obj)\n
    '''
def applyPattern():
    '''returns None\n\n
    applyPattern(final String pattern)\n
    '''
def applyLocalizedPattern():
    '''returns None\n\n
    applyLocalizedPattern(final String pattern)\n
    '''
def setMaximumIntegerDigits():
    '''returns None\n\n
    setMaximumIntegerDigits(final int newValue)\n
    '''
def setMinimumIntegerDigits():
    '''returns None\n\n
    setMinimumIntegerDigits(final int newValue)\n
    '''
def getMinimumSignificantDigits():
    '''returns int\n\n
    getMinimumSignificantDigits()\n
    '''
def getMaximumSignificantDigits():
    '''returns int\n\n
    getMaximumSignificantDigits()\n
    '''
def setMinimumSignificantDigits():
    '''returns None\n\n
    setMinimumSignificantDigits(int min)\n
    '''
def setMaximumSignificantDigits():
    '''returns None\n\n
    setMaximumSignificantDigits(int max)\n
    '''
def areSignificantDigitsUsed():
    '''returns boolean\n\n
    areSignificantDigitsUsed()\n
    '''
def setSignificantDigitsUsed():
    '''returns None\n\n
    setSignificantDigitsUsed(final boolean useSignificantDigits)\n
    '''
def setCurrency():
    '''returns None\n\n
    setCurrency(final Currency theCurrency)\n
    '''
def setMaximumFractionDigits():
    '''returns None\n\n
    setMaximumFractionDigits(final int newValue)\n
    '''
def setMinimumFractionDigits():
    '''returns None\n\n
    setMinimumFractionDigits(final int newValue)\n
    '''
def setParseBigDecimal():
    '''returns None\n\n
    setParseBigDecimal(final boolean value)\n
    '''
def isParseBigDecimal():
    '''returns boolean\n\n
    isParseBigDecimal()\n
    '''
def getNegPrefix():
    '''returns String\n\n
    getNegPrefix()\n
    '''
def getNegSuffix():
    '''returns String\n\n
    getNegSuffix()\n
    '''
def getPosPrefix():
    '''returns String\n\n
    getPosPrefix()\n
    '''
def getPosSuffix():
    '''returns String\n\n
    getPosSuffix()\n
    '''
def getPatternType():
    '''returns int\n\n
    getPatternType()\n
    '''
