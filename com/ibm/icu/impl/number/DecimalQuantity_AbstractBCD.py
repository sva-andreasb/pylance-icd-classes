def ():
    '''returns DecimalQuantity_AbstractBCD\n\n
    ()\n
    '''
def copyFrom():
    '''returns None\n\n
    copyFrom(final DecimalQuantity _other)\n
    '''
def clear():
    '''returns DecimalQuantity_AbstractBCD\n\n
    clear()\n
    '''
def setMinInteger():
    '''returns None\n\n
    setMinInteger(int minInt)\n
    '''
def setMinFraction():
    '''returns None\n\n
    setMinFraction(final int minFrac)\n
    '''
def applyMaxInteger():
    '''returns None\n\n
    applyMaxInteger(final int maxInt)\n
    '''
def getPositionFingerprint():
    '''returns long\n\n
    getPositionFingerprint()\n
    '''
def roundToIncrement():
    '''returns None\n\n
    roundToIncrement(final BigDecimal roundingIncrement, final MathContext mathContext)\n
    '''
def multiplyBy():
    '''returns None\n\n
    multiplyBy(final BigDecimal multiplicand)\n
    '''
def negate():
    '''returns None\n\n
    negate()\n
    '''
def getMagnitude():
    '''returns int\n\n
    getMagnitude()\n
    '''
def adjustMagnitude():
    '''returns None\n\n
    adjustMagnitude(final int delta)\n
    '''
def getExponent():
    '''returns int\n\n
    getExponent()\n
    '''
def adjustExponent():
    '''returns None\n\n
    adjustExponent(final int delta)\n
    '''
def getStandardPlural():
    '''returns StandardPlural\n\n
    getStandardPlural(final PluralRules rules)\n
    '''
def getPluralOperand():
    '''returns double\n\n
    getPluralOperand(final PluralRules.Operand operand)\n
    '''
def populateUFieldPosition():
    '''returns None\n\n
    populateUFieldPosition(final FieldPosition fp)\n
    '''
def getUpperDisplayMagnitude():
    '''returns int\n\n
    getUpperDisplayMagnitude()\n
    '''
def getLowerDisplayMagnitude():
    '''returns int\n\n
    getLowerDisplayMagnitude()\n
    '''
def getDigit():
    '''returns byte\n\n
    getDigit(final int magnitude)\n
    '''
def isNegative():
    '''returns boolean\n\n
    isNegative()\n
    '''
def isInfinite():
    '''returns boolean\n\n
    isInfinite()\n
    '''
def isNaN():
    '''returns boolean\n\n
    isNaN()\n
    '''
def isZeroish():
    '''returns boolean\n\n
    isZeroish()\n
    '''
def setToInt():
    '''returns None\n\n
    setToInt(int n)\n
    '''
def setToLong():
    '''returns None\n\n
    setToLong(long n)\n
    '''
def setToBigInteger():
    '''returns None\n\n
    setToBigInteger(BigInteger n)\n
    '''
def setToDouble():
    '''returns None\n\n
    setToDouble(double n)\n
    '''
def setToBigDecimal():
    '''returns None\n\n
    setToBigDecimal(BigDecimal n)\n
    '''
def toLong():
    '''returns long\n\n
    toLong(final boolean truncateIfOverflow)\n
    '''
def toFractionLong():
    '''returns long\n\n
    toFractionLong(final boolean includeTrailingZeros)\n
    '''
def fitsInLong():
    '''returns boolean\n\n
    fitsInLong()\n
    '''
def toDouble():
    '''returns double\n\n
    toDouble()\n
    '''
def toBigDecimal():
    '''returns BigDecimal\n\n
    toBigDecimal()\n
    '''
def truncate():
    '''returns None\n\n
    truncate()\n
    '''
def roundToNickel():
    '''returns None\n\n
    roundToNickel(final int magnitude, final MathContext mathContext)\n
    '''
def roundToMagnitude():
    '''returns None\n\n
    roundToMagnitude(final int magnitude, final MathContext mathContext)\n
    '''
def roundToInfinity():
    '''returns None\n\n
    roundToInfinity()\n
    '''
def appendDigit():
    '''returns None\n\n
    appendDigit(final byte value, int leadingZeros, final boolean appendAsInteger)\n
    '''
def toPlainString():
    '''returns None\n\n
    toPlainString()\n
    toPlainString(final StringBuilder result)\n
    '''
def toScientificString():
    '''returns None\n\n
    toScientificString()\n
    toScientificString(final StringBuilder result)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
