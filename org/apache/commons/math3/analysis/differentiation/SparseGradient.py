def numVars():
    '''returns int\n\n
    numVars()\n
    '''
def getDerivative():
    '''returns double\n\n
    getDerivative(final int index)\n
    '''
def getValue():
    '''returns double\n\n
    getValue()\n
    '''
def getReal():
    '''returns double\n\n
    getReal()\n
    '''
def add():
    '''returns SparseGradient\n\n
    add(final SparseGradient a)\n
    add(final double c)\n
    '''
def addInPlace():
    '''returns None\n\n
    addInPlace(final SparseGradient a)\n
    '''
def subtract():
    '''returns SparseGradient\n\n
    subtract(final SparseGradient a)\n
    subtract(final double c)\n
    '''
def multiply():
    '''returns SparseGradient\n\n
    multiply(final SparseGradient a)\n
    multiply(final double c)\n
    multiply(final int n)\n
    '''
def multiplyInPlace():
    '''returns None\n\n
    multiplyInPlace(final SparseGradient a)\n
    '''
def divide():
    '''returns SparseGradient\n\n
    divide(final SparseGradient a)\n
    divide(final double c)\n
    '''
def negate():
    '''returns SparseGradient\n\n
    negate()\n
    '''
def getField():
    '''returns Field<SparseGradient>\n\n
    getField()\n
    '''
def getZero():
    '''returns SparseGradient\n\n
    getZero()\n
    '''
def getOne():
    '''returns SparseGradient\n\n
    getOne()\n
    '''
def remainder():
    '''returns SparseGradient\n\n
    remainder(final double a)\n
    remainder(final SparseGradient a)\n
    '''
def abs():
    '''returns SparseGradient\n\n
    abs()\n
    '''
def ceil():
    '''returns SparseGradient\n\n
    ceil()\n
    '''
def floor():
    '''returns SparseGradient\n\n
    floor()\n
    '''
def rint():
    '''returns SparseGradient\n\n
    rint()\n
    '''
def round():
    '''returns long\n\n
    round()\n
    '''
def signum():
    '''returns SparseGradient\n\n
    signum()\n
    '''
def copySign():
    '''returns SparseGradient\n\n
    copySign(final SparseGradient sign)\n
    copySign(final double sign)\n
    '''
def scalb():
    '''returns SparseGradient\n\n
    scalb(final int n)\n
    '''
def hypot():
    '''returns SparseGradient\n\n
    hypot(final SparseGradient y)\n
    '''
def reciprocal():
    '''returns SparseGradient\n\n
    reciprocal()\n
    '''
def sqrt():
    '''returns SparseGradient\n\n
    sqrt()\n
    '''
def cbrt():
    '''returns SparseGradient\n\n
    cbrt()\n
    '''
def rootN():
    '''returns SparseGradient\n\n
    rootN(final int n)\n
    '''
def pow():
    '''returns SparseGradient\n\n
    pow(final double p)\n
    pow(final int n)\n
    pow(final SparseGradient e)\n
    '''
def exp():
    '''returns SparseGradient\n\n
    exp()\n
    '''
def expm1():
    '''returns SparseGradient\n\n
    expm1()\n
    '''
def log():
    '''returns SparseGradient\n\n
    log()\n
    '''
def log10():
    '''returns SparseGradient\n\n
    log10()\n
    '''
def log1p():
    '''returns SparseGradient\n\n
    log1p()\n
    '''
def cos():
    '''returns SparseGradient\n\n
    cos()\n
    '''
def sin():
    '''returns SparseGradient\n\n
    sin()\n
    '''
def tan():
    '''returns SparseGradient\n\n
    tan()\n
    '''
def acos():
    '''returns SparseGradient\n\n
    acos()\n
    '''
def asin():
    '''returns SparseGradient\n\n
    asin()\n
    '''
def atan():
    '''returns SparseGradient\n\n
    atan()\n
    '''
def atan2():
    '''returns SparseGradient\n\n
    atan2(final SparseGradient x)\n
    '''
def cosh():
    '''returns SparseGradient\n\n
    cosh()\n
    '''
def sinh():
    '''returns SparseGradient\n\n
    sinh()\n
    '''
def tanh():
    '''returns SparseGradient\n\n
    tanh()\n
    '''
def acosh():
    '''returns SparseGradient\n\n
    acosh()\n
    '''
def asinh():
    '''returns SparseGradient\n\n
    asinh()\n
    '''
def atanh():
    '''returns SparseGradient\n\n
    atanh()\n
    '''
def toDegrees():
    '''returns SparseGradient\n\n
    toDegrees()\n
    '''
def toRadians():
    '''returns SparseGradient\n\n
    toRadians()\n
    '''
def taylor():
    '''returns double\n\n
    taylor(final double... delta)\n
    '''
def compose():
    '''returns SparseGradient\n\n
    compose(final double f0, final double f1)\n
    '''
def linearCombination():
    '''returns SparseGradient\n\n
    linearCombination(final SparseGradient[] a, final SparseGradient[] b)\n
    linearCombination(final double[] a, final SparseGradient[] b)\n
    linearCombination(final SparseGradient a1, final SparseGradient b1, final SparseGradient a2, final SparseGradient b2)\n
    linearCombination(final double a1, final SparseGradient b1, final double a2, final SparseGradient b2)\n
    linearCombination(final SparseGradient a1, final SparseGradient b1, final SparseGradient a2, final SparseGradient b2, final SparseGradient a3, final SparseGradient b3)\n
    linearCombination(final double a1, final SparseGradient b1, final double a2, final SparseGradient b2, final double a3, final SparseGradient b3)\n
    linearCombination(final SparseGradient a1, final SparseGradient b1, final SparseGradient a2, final SparseGradient b2, final SparseGradient a3, final SparseGradient b3, final SparseGradient a4, final SparseGradient b4)\n
    linearCombination(final double a1, final SparseGradient b1, final double a2, final SparseGradient b2, final double a3, final SparseGradient b3, final double a4, final SparseGradient b4)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
