def ():
    '''returns IlvAugmentedICUDecimalFormat\n\n
    (final DecimalFormat a, final DecimalFormat b)\n
    '''
def getUnderlyingICUFormat():
    '''returns DecimalFormat\n\n
    getUnderlyingICUFormat()\n
    '''
def format():
    '''returns StringBuffer\n\n
    format(final Object o, final StringBuffer sb, final FieldPosition fieldPosition)\n
    format(final CurrencyAmount currencyAmount, final StringBuffer sb, final FieldPosition fieldPosition)\n
    format(final double n, final StringBuffer sb, final FieldPosition fieldPosition)\n
    format(final long n, final StringBuffer sb, final FieldPosition fieldPosition)\n
    format(final BigInteger bigInteger, final StringBuffer sb, final FieldPosition fieldPosition)\n
    format(final BigDecimal bigDecimal, final StringBuffer sb, final FieldPosition fieldPosition)\n
    format(final com.ibm.icu.math.BigDecimal bigDecimal, final StringBuffer sb, final FieldPosition fieldPosition)\n
    '''
def parse():
    '''returns Number\n\n
    parse(final String s)\n
    parse(final String s, final ParsePosition parsePosition)\n
    '''
def isParseIntegerOnly():
    '''returns boolean\n\n
    isParseIntegerOnly()\n
    '''
def setParseIntegerOnly():
    '''returns None\n\n
    setParseIntegerOnly(final boolean b)\n
    '''
def isParseStrict():
    '''returns boolean\n\n
    isParseStrict()\n
    '''
def setParseStrict():
    '''returns None\n\n
    setParseStrict(final boolean b)\n
    '''
def isGroupingUsed():
    '''returns boolean\n\n
    isGroupingUsed()\n
    '''
def setGroupingUsed():
    '''returns None\n\n
    setGroupingUsed(final boolean b)\n
    '''
def formatToCharacterIterator():
    '''returns AttributedCharacterIterator\n\n
    formatToCharacterIterator(final Object o)\n
    '''
def getDecimalFormatSymbols():
    '''returns DecimalFormatSymbols\n\n
    getDecimalFormatSymbols()\n
    '''
def setDecimalFormatSymbols():
    '''returns None\n\n
    setDecimalFormatSymbols(final DecimalFormatSymbols decimalFormatSymbols)\n
    '''
def getPositivePrefix():
    '''returns String\n\n
    getPositivePrefix()\n
    '''
def setPositivePrefix():
    '''returns None\n\n
    setPositivePrefix(final String s)\n
    '''
def getNegativePrefix():
    '''returns String\n\n
    getNegativePrefix()\n
    '''
def setNegativePrefix():
    '''returns None\n\n
    setNegativePrefix(final String s)\n
    '''
def getPositiveSuffix():
    '''returns String\n\n
    getPositiveSuffix()\n
    '''
def setPositiveSuffix():
    '''returns None\n\n
    setPositiveSuffix(final String s)\n
    '''
def getNegativeSuffix():
    '''returns String\n\n
    getNegativeSuffix()\n
    '''
def setNegativeSuffix():
    '''returns None\n\n
    setNegativeSuffix(final String s)\n
    '''
def getMultiplier():
    '''returns int\n\n
    getMultiplier()\n
    '''
def setMultiplier():
    '''returns None\n\n
    setMultiplier(final int n)\n
    '''
def getRoundingIncrement():
    '''returns BigDecimal\n\n
    getRoundingIncrement()\n
    '''
def setRoundingIncrement():
    '''returns None\n\n
    setRoundingIncrement(final BigDecimal roundingIncrement)\n
    setRoundingIncrement(final com.ibm.icu.math.BigDecimal roundingIncrement)\n
    setRoundingIncrement(final double roundingIncrement)\n
    '''
def getFormatWidth():
    '''returns int\n\n
    getFormatWidth()\n
    '''
def setFormatWidth():
    '''returns None\n\n
    setFormatWidth(final int n)\n
    '''
def getPadCharacter():
    '''returns char\n\n
    getPadCharacter()\n
    '''
def setPadCharacter():
    '''returns None\n\n
    setPadCharacter(final char c)\n
    '''
def getPadPosition():
    '''returns int\n\n
    getPadPosition()\n
    '''
def setPadPosition():
    '''returns None\n\n
    setPadPosition(final int n)\n
    '''
def isScientificNotation():
    '''returns boolean\n\n
    isScientificNotation()\n
    '''
def setScientificNotation():
    '''returns None\n\n
    setScientificNotation(final boolean b)\n
    '''
def getMinimumExponentDigits():
    '''returns byte\n\n
    getMinimumExponentDigits()\n
    '''
def setMinimumExponentDigits():
    '''returns None\n\n
    setMinimumExponentDigits(final byte b)\n
    '''
def isExponentSignAlwaysShown():
    '''returns boolean\n\n
    isExponentSignAlwaysShown()\n
    '''
def setExponentSignAlwaysShown():
    '''returns None\n\n
    setExponentSignAlwaysShown(final boolean b)\n
    '''
def getGroupingSize():
    '''returns int\n\n
    getGroupingSize()\n
    '''
def setGroupingSize():
    '''returns None\n\n
    setGroupingSize(final int n)\n
    '''
def getSecondaryGroupingSize():
    '''returns int\n\n
    getSecondaryGroupingSize()\n
    '''
def setSecondaryGroupingSize():
    '''returns None\n\n
    setSecondaryGroupingSize(final int n)\n
    '''
def getMathContext():
    '''returns MathContext\n\n
    getMathContext()\n
    '''
def setMathContext():
    '''returns None\n\n
    setMathContext(final MathContext mathContext)\n
    '''
def setMathContextICU():
    '''returns None\n\n
    setMathContextICU(final com.ibm.icu.math.MathContext mathContext)\n
    '''
def isDecimalSeparatorAlwaysShown():
    '''returns boolean\n\n
    isDecimalSeparatorAlwaysShown()\n
    '''
def setDecimalSeparatorAlwaysShown():
    '''returns None\n\n
    setDecimalSeparatorAlwaysShown(final boolean decimalSeparatorAlwaysShown)\n
    '''
def getCurrencyPluralInfo():
    '''returns CurrencyPluralInfo\n\n
    getCurrencyPluralInfo()\n
    '''
def setCurrencyPluralInfo():
    '''returns None\n\n
    setCurrencyPluralInfo(final CurrencyPluralInfo currencyPluralInfo)\n
    '''
def isParseBigDecimal():
    '''returns boolean\n\n
    isParseBigDecimal()\n
    '''
def setParseBigDecimal():
    '''returns None\n\n
    setParseBigDecimal(final boolean b)\n
    '''
def toPattern():
    '''returns String\n\n
    toPattern()\n
    '''
def toLocalizedPattern():
    '''returns String\n\n
    toLocalizedPattern()\n
    '''
def applyPattern():
    '''returns None\n\n
    applyPattern(final String s)\n
    '''
def applyLocalizedPattern():
    '''returns None\n\n
    applyLocalizedPattern(final String s)\n
    '''
def getMinimumSignificantDigits():
    '''returns int\n\n
    getMinimumSignificantDigits()\n
    '''
def setMinimumSignificantDigits():
    '''returns None\n\n
    setMinimumSignificantDigits(final int minimumSignificantDigits)\n
    '''
def getMaximumSignificantDigits():
    '''returns int\n\n
    getMaximumSignificantDigits()\n
    '''
def setMaximumSignificantDigits():
    '''returns None\n\n
    setMaximumSignificantDigits(final int maximumSignificantDigits)\n
    '''
def areSignificantDigitsUsed():
    '''returns boolean\n\n
    areSignificantDigitsUsed()\n
    '''
def setSignificantDigitsUsed():
    '''returns None\n\n
    setSignificantDigitsUsed(final boolean significantDigitsUsed)\n
    '''
def getMaximumIntegerDigits():
    '''returns int\n\n
    getMaximumIntegerDigits()\n
    '''
def setMaximumIntegerDigits():
    '''returns None\n\n
    setMaximumIntegerDigits(final int n)\n
    '''
def getMinimumIntegerDigits():
    '''returns int\n\n
    getMinimumIntegerDigits()\n
    '''
def setMinimumIntegerDigits():
    '''returns None\n\n
    setMinimumIntegerDigits(final int n)\n
    '''
def getMaximumFractionDigits():
    '''returns int\n\n
    getMaximumFractionDigits()\n
    '''
def setMaximumFractionDigits():
    '''returns None\n\n
    setMaximumFractionDigits(final int maximumFractionDigits)\n
    '''
def getMinimumFractionDigits():
    '''returns int\n\n
    getMinimumFractionDigits()\n
    '''
def setMinimumFractionDigits():
    '''returns None\n\n
    setMinimumFractionDigits(final int minimumFractionDigits)\n
    '''
def getCurrency():
    '''returns Currency\n\n
    getCurrency()\n
    '''
def setCurrency():
    '''returns None\n\n
    setCurrency(final Currency currency)\n
    '''
def getRoundingMode():
    '''returns int\n\n
    getRoundingMode()\n
    '''
def setRoundingMode():
    '''returns None\n\n
    setRoundingMode(final int roundingMode)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
