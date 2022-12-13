def getCompiler():
'''public static DSCompiler getCompiler(final int parameters, final int order)
'''
pass
def getPartialDerivativeIndex():
'''public int getPartialDerivativeIndex(final int... orders)
'''
pass
def getPartialDerivativeOrders():
'''public int[] getPartialDerivativeOrders(final int index)
'''
pass
def getFreeParameters():
'''public int getFreeParameters()
'''
pass
def getOrder():
'''public int getOrder()
'''
pass
def getSize():
'''public int getSize()
'''
pass
def linearCombination():
'''public void linearCombination(final double a1, final double[] c1, final int offset1, final double a2, final double[] c2, final int offset2, final double[] result, final int resultOffset)
public void linearCombination(final double a1, final double[] c1, final int offset1, final double a2, final double[] c2, final int offset2, final double a3, final double[] c3, final int offset3, final double[] result, final int resultOffset)
public void linearCombination(final double a1, final double[] c1, final int offset1, final double a2, final double[] c2, final int offset2, final double a3, final double[] c3, final int offset3, final double a4, final double[] c4, final int offset4, final double[] result, final int resultOffset)
'''
pass
def add():
'''public void add(final double[] lhs, final int lhsOffset, final double[] rhs, final int rhsOffset, final double[] result, final int resultOffset)
'''
pass
def subtract():
'''public void subtract(final double[] lhs, final int lhsOffset, final double[] rhs, final int rhsOffset, final double[] result, final int resultOffset)
'''
pass
def multiply():
'''public void multiply(final double[] lhs, final int lhsOffset, final double[] rhs, final int rhsOffset, final double[] result, final int resultOffset)
'''
pass
def divide():
'''public void divide(final double[] lhs, final int lhsOffset, final double[] rhs, final int rhsOffset, final double[] result, final int resultOffset)
'''
pass
def remainder():
'''public void remainder(final double[] lhs, final int lhsOffset, final double[] rhs, final int rhsOffset, final double[] result, final int resultOffset)
'''
pass
def pow():
'''public void pow(final double a, final double[] operand, final int operandOffset, final double[] result, final int resultOffset)
public void pow(final double[] operand, final int operandOffset, final double p, final double[] result, final int resultOffset)
public void pow(final double[] operand, final int operandOffset, final int n, final double[] result, final int resultOffset)
public void pow(final double[] x, final int xOffset, final double[] y, final int yOffset, final double[] result, final int resultOffset)
'''
pass
def rootN():
'''public void rootN(final double[] operand, final int operandOffset, final int n, final double[] result, final int resultOffset)
'''
pass
def exp():
'''public void exp(final double[] operand, final int operandOffset, final double[] result, final int resultOffset)
'''
pass
def expm1():
'''public void expm1(final double[] operand, final int operandOffset, final double[] result, final int resultOffset)
'''
pass
def log():
'''public void log(final double[] operand, final int operandOffset, final double[] result, final int resultOffset)
'''
pass
def log1p():
'''public void log1p(final double[] operand, final int operandOffset, final double[] result, final int resultOffset)
'''
pass
def log10():
'''public void log10(final double[] operand, final int operandOffset, final double[] result, final int resultOffset)
'''
pass
def cos():
'''public void cos(final double[] operand, final int operandOffset, final double[] result, final int resultOffset)
'''
pass
def sin():
'''public void sin(final double[] operand, final int operandOffset, final double[] result, final int resultOffset)
'''
pass
def tan():
'''public void tan(final double[] operand, final int operandOffset, final double[] result, final int resultOffset)
'''
pass
def acos():
'''public void acos(final double[] operand, final int operandOffset, final double[] result, final int resultOffset)
'''
pass
def asin():
'''public void asin(final double[] operand, final int operandOffset, final double[] result, final int resultOffset)
'''
pass
def atan():
'''public void atan(final double[] operand, final int operandOffset, final double[] result, final int resultOffset)
'''
pass
def atan2():
'''public void atan2(final double[] y, final int yOffset, final double[] x, final int xOffset, final double[] result, final int resultOffset)
'''
pass
def cosh():
'''public void cosh(final double[] operand, final int operandOffset, final double[] result, final int resultOffset)
'''
pass
def sinh():
'''public void sinh(final double[] operand, final int operandOffset, final double[] result, final int resultOffset)
'''
pass
def tanh():
'''public void tanh(final double[] operand, final int operandOffset, final double[] result, final int resultOffset)
'''
pass
def acosh():
'''public void acosh(final double[] operand, final int operandOffset, final double[] result, final int resultOffset)
'''
pass
def asinh():
'''public void asinh(final double[] operand, final int operandOffset, final double[] result, final int resultOffset)
'''
pass
def atanh():
'''public void atanh(final double[] operand, final int operandOffset, final double[] result, final int resultOffset)
'''
pass
def compose():
'''public void compose(final double[] operand, final int operandOffset, final double[] f, final double[] result, final int resultOffset)
'''
pass
def taylor():
'''public double taylor(final double[] ds, final int dsOffset, final double... delta)
'''
pass
def checkCompatibility():
'''public void checkCompatibility(final DSCompiler compiler)
'''
pass
