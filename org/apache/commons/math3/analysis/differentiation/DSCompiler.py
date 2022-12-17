def getPartialDerivativeIndex():
    '''returns int\n\n
    getPartialDerivativeIndex(final int... orders)\n
    '''
def getPartialDerivativeOrders():
    '''returns int[]\n\n
    getPartialDerivativeOrders(final int index)\n
    '''
def getFreeParameters():
    '''returns int\n\n
    getFreeParameters()\n
    '''
def getOrder():
    '''returns int\n\n
    getOrder()\n
    '''
def getSize():
    '''returns int\n\n
    getSize()\n
    '''
def linearCombination():
    '''returns None\n\n
    linearCombination(final double a1, final double[] c1, final int offset1, final double a2, final double[] c2, final int offset2, final double[] result, final int resultOffset)\n
    linearCombination(final double a1, final double[] c1, final int offset1, final double a2, final double[] c2, final int offset2, final double a3, final double[] c3, final int offset3, final double[] result, final int resultOffset)\n
    linearCombination(final double a1, final double[] c1, final int offset1, final double a2, final double[] c2, final int offset2, final double a3, final double[] c3, final int offset3, final double a4, final double[] c4, final int offset4, final double[] result, final int resultOffset)\n
    '''
def add():
    '''returns None\n\n
    add(final double[] lhs, final int lhsOffset, final double[] rhs, final int rhsOffset, final double[] result, final int resultOffset)\n
    '''
def subtract():
    '''returns None\n\n
    subtract(final double[] lhs, final int lhsOffset, final double[] rhs, final int rhsOffset, final double[] result, final int resultOffset)\n
    '''
def multiply():
    '''returns None\n\n
    multiply(final double[] lhs, final int lhsOffset, final double[] rhs, final int rhsOffset, final double[] result, final int resultOffset)\n
    '''
def divide():
    '''returns None\n\n
    divide(final double[] lhs, final int lhsOffset, final double[] rhs, final int rhsOffset, final double[] result, final int resultOffset)\n
    '''
def remainder():
    '''returns None\n\n
    remainder(final double[] lhs, final int lhsOffset, final double[] rhs, final int rhsOffset, final double[] result, final int resultOffset)\n
    '''
def pow():
    '''returns None\n\n
    pow(final double a, final double[] operand, final int operandOffset, final double[] result, final int resultOffset)\n
    pow(final double[] operand, final int operandOffset, final double p, final double[] result, final int resultOffset)\n
    pow(final double[] operand, final int operandOffset, final int n, final double[] result, final int resultOffset)\n
    pow(final double[] x, final int xOffset, final double[] y, final int yOffset, final double[] result, final int resultOffset)\n
    '''
def rootN():
    '''returns None\n\n
    rootN(final double[] operand, final int operandOffset, final int n, final double[] result, final int resultOffset)\n
    '''
def exp():
    '''returns None\n\n
    exp(final double[] operand, final int operandOffset, final double[] result, final int resultOffset)\n
    '''
def expm1():
    '''returns None\n\n
    expm1(final double[] operand, final int operandOffset, final double[] result, final int resultOffset)\n
    '''
def log():
    '''returns None\n\n
    log(final double[] operand, final int operandOffset, final double[] result, final int resultOffset)\n
    '''
def log1p():
    '''returns None\n\n
    log1p(final double[] operand, final int operandOffset, final double[] result, final int resultOffset)\n
    '''
def log10():
    '''returns None\n\n
    log10(final double[] operand, final int operandOffset, final double[] result, final int resultOffset)\n
    '''
def cos():
    '''returns None\n\n
    cos(final double[] operand, final int operandOffset, final double[] result, final int resultOffset)\n
    '''
def sin():
    '''returns None\n\n
    sin(final double[] operand, final int operandOffset, final double[] result, final int resultOffset)\n
    '''
def tan():
    '''returns None\n\n
    tan(final double[] operand, final int operandOffset, final double[] result, final int resultOffset)\n
    '''
def acos():
    '''returns None\n\n
    acos(final double[] operand, final int operandOffset, final double[] result, final int resultOffset)\n
    '''
def asin():
    '''returns None\n\n
    asin(final double[] operand, final int operandOffset, final double[] result, final int resultOffset)\n
    '''
def atan():
    '''returns None\n\n
    atan(final double[] operand, final int operandOffset, final double[] result, final int resultOffset)\n
    '''
def atan2():
    '''returns None\n\n
    atan2(final double[] y, final int yOffset, final double[] x, final int xOffset, final double[] result, final int resultOffset)\n
    '''
def cosh():
    '''returns None\n\n
    cosh(final double[] operand, final int operandOffset, final double[] result, final int resultOffset)\n
    '''
def sinh():
    '''returns None\n\n
    sinh(final double[] operand, final int operandOffset, final double[] result, final int resultOffset)\n
    '''
def tanh():
    '''returns None\n\n
    tanh(final double[] operand, final int operandOffset, final double[] result, final int resultOffset)\n
    '''
def acosh():
    '''returns None\n\n
    acosh(final double[] operand, final int operandOffset, final double[] result, final int resultOffset)\n
    '''
def asinh():
    '''returns None\n\n
    asinh(final double[] operand, final int operandOffset, final double[] result, final int resultOffset)\n
    '''
def atanh():
    '''returns None\n\n
    atanh(final double[] operand, final int operandOffset, final double[] result, final int resultOffset)\n
    '''
def compose():
    '''returns None\n\n
    compose(final double[] operand, final int operandOffset, final double[] f, final double[] result, final int resultOffset)\n
    '''
def taylor():
    '''returns double\n\n
    taylor(final double[] ds, final int dsOffset, final double... delta)\n
    '''
def checkCompatibility():
    '''returns None\n\n
    checkCompatibility(final DSCompiler compiler)\n
    '''
