def ():
    '''returns DerivativeStructure\n\n
    (final int parameters, final int order)\n
    (final int parameters, final int order, final double value)\n
    (final int parameters, final int order, final int index, final double value)\n
    (final double a1, final DerivativeStructure ds1, final double a2, final DerivativeStructure ds2)\n
    (final double a1, final DerivativeStructure ds1, final double a2, final DerivativeStructure ds2, final double a3, final DerivativeStructure ds3)\n
    (final double a1, final DerivativeStructure ds1, final double a2, final DerivativeStructure ds2, final double a3, final DerivativeStructure ds3, final double a4, final DerivativeStructure ds4)\n
    (final int parameters, final int order, final double... derivatives)\n
    '''
def getFreeParameters():
    '''returns int\n\n
    getFreeParameters()\n
    '''
def getOrder():
    '''returns int\n\n
    getOrder()\n
    '''
def createConstant():
    '''returns DerivativeStructure\n\n
    createConstant(final double c)\n
    '''
def getReal():
    '''returns double\n\n
    getReal()\n
    '''
def getValue():
    '''returns double\n\n
    getValue()\n
    '''
def getPartialDerivative():
    '''returns double\n\n
    getPartialDerivative(final int... orders)\n
    '''
def getAllDerivatives():
    '''returns double[]\n\n
    getAllDerivatives()\n
    '''
def add():
    '''returns DerivativeStructure\n\n
    add(final double a)\n
    add(final DerivativeStructure a)\n
    '''
def subtract():
    '''returns DerivativeStructure\n\n
    subtract(final double a)\n
    subtract(final DerivativeStructure a)\n
    '''
def multiply():
    '''returns DerivativeStructure\n\n
    multiply(final int n)\n
    multiply(final double a)\n
    multiply(final DerivativeStructure a)\n
    '''
def divide():
    '''returns DerivativeStructure\n\n
    divide(final double a)\n
    divide(final DerivativeStructure a)\n
    '''
def remainder():
    '''returns DerivativeStructure\n\n
    remainder(final double a)\n
    remainder(final DerivativeStructure a)\n
    '''
def negate():
    '''returns DerivativeStructure\n\n
    negate()\n
    '''
def abs():
    '''returns DerivativeStructure\n\n
    abs()\n
    '''
def ceil():
    '''returns DerivativeStructure\n\n
    ceil()\n
    '''
def floor():
    '''returns DerivativeStructure\n\n
    floor()\n
    '''
def rint():
    '''returns DerivativeStructure\n\n
    rint()\n
    '''
def round():
    '''returns long\n\n
    round()\n
    '''
def signum():
    '''returns DerivativeStructure\n\n
    signum()\n
    '''
def copySign():
    '''returns DerivativeStructure\n\n
    copySign(final DerivativeStructure sign)\n
    copySign(final double sign)\n
    '''
def getExponent():
    '''returns int\n\n
    getExponent()\n
    '''
def scalb():
    '''returns DerivativeStructure\n\n
    scalb(final int n)\n
    '''
def hypot():
    '''returns DerivativeStructure\n\n
    hypot(final DerivativeStructure y)\n
    '''
def compose():
    '''returns DerivativeStructure\n\n
    compose(final double... f)\n
    '''
def reciprocal():
    '''returns DerivativeStructure\n\n
    reciprocal()\n
    '''
def sqrt():
    '''returns DerivativeStructure\n\n
    sqrt()\n
    '''
def cbrt():
    '''returns DerivativeStructure\n\n
    cbrt()\n
    '''
def rootN():
    '''returns DerivativeStructure\n\n
    rootN(final int n)\n
    '''
def getField():
    '''returns Field<DerivativeStructure>\n\n
    getField()\n
    '''
def getZero():
    '''returns DerivativeStructure\n\n
    getZero()\n
    '''
def getOne():
    '''returns DerivativeStructure\n\n
    getOne()\n
    '''
def pow():
    '''returns DerivativeStructure\n\n
    pow(final double p)\n
    pow(final int n)\n
    pow(final DerivativeStructure e)\n
    '''
def exp():
    '''returns DerivativeStructure\n\n
    exp()\n
    '''
def expm1():
    '''returns DerivativeStructure\n\n
    expm1()\n
    '''
def log():
    '''returns DerivativeStructure\n\n
    log()\n
    '''
def log1p():
    '''returns DerivativeStructure\n\n
    log1p()\n
    '''
def log10():
    '''returns DerivativeStructure\n\n
    log10()\n
    '''
def cos():
    '''returns DerivativeStructure\n\n
    cos()\n
    '''
def sin():
    '''returns DerivativeStructure\n\n
    sin()\n
    '''
def tan():
    '''returns DerivativeStructure\n\n
    tan()\n
    '''
def acos():
    '''returns DerivativeStructure\n\n
    acos()\n
    '''
def asin():
    '''returns DerivativeStructure\n\n
    asin()\n
    '''
def atan():
    '''returns DerivativeStructure\n\n
    atan()\n
    '''
def atan2():
    '''returns DerivativeStructure\n\n
    atan2(final DerivativeStructure x)\n
    '''
def cosh():
    '''returns DerivativeStructure\n\n
    cosh()\n
    '''
def sinh():
    '''returns DerivativeStructure\n\n
    sinh()\n
    '''
def tanh():
    '''returns DerivativeStructure\n\n
    tanh()\n
    '''
def acosh():
    '''returns DerivativeStructure\n\n
    acosh()\n
    '''
def asinh():
    '''returns DerivativeStructure\n\n
    asinh()\n
    '''
def atanh():
    '''returns DerivativeStructure\n\n
    atanh()\n
    '''
def toDegrees():
    '''returns DerivativeStructure\n\n
    toDegrees()\n
    '''
def toRadians():
    '''returns DerivativeStructure\n\n
    toRadians()\n
    '''
def taylor():
    '''returns double\n\n
    taylor(final double... delta)\n
    '''
def linearCombination():
    '''returns DerivativeStructure\n\n
    linearCombination(final DerivativeStructure[] a, final DerivativeStructure[] b)\n
    linearCombination(final double[] a, final DerivativeStructure[] b)\n
    linearCombination(final DerivativeStructure a1, final DerivativeStructure b1, final DerivativeStructure a2, final DerivativeStructure b2)\n
    linearCombination(final double a1, final DerivativeStructure b1, final double a2, final DerivativeStructure b2)\n
    linearCombination(final DerivativeStructure a1, final DerivativeStructure b1, final DerivativeStructure a2, final DerivativeStructure b2, final DerivativeStructure a3, final DerivativeStructure b3)\n
    linearCombination(final double a1, final DerivativeStructure b1, final double a2, final DerivativeStructure b2, final double a3, final DerivativeStructure b3)\n
    linearCombination(final DerivativeStructure a1, final DerivativeStructure b1, final DerivativeStructure a2, final DerivativeStructure b2, final DerivativeStructure a3, final DerivativeStructure b3, final DerivativeStructure a4, final DerivativeStructure b4)\n
    linearCombination(final double a1, final DerivativeStructure b1, final double a2, final DerivativeStructure b2, final double a3, final DerivativeStructure b3, final double a4, final DerivativeStructure b4)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
