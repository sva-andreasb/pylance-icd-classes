def createConstant():
'''public static SparseGradient createConstant(final double value)
'''
pass
def createVariable():
'''public static SparseGradient createVariable(final int idx, final double value)
'''
pass
def numVars():
'''public int numVars()
'''
pass
def getDerivative():
'''public double getDerivative(final int index)
'''
pass
def getValue():
'''public double getValue()
'''
pass
def getReal():
'''public double getReal()
'''
pass
def add():
'''public SparseGradient add(final SparseGradient a)
public SparseGradient add(final double c)
'''
pass
def addInPlace():
'''public void addInPlace(final SparseGradient a)
'''
pass
def subtract():
'''public SparseGradient subtract(final SparseGradient a)
public SparseGradient subtract(final double c)
'''
pass
def multiply():
'''public SparseGradient multiply(final SparseGradient a)
public SparseGradient multiply(final double c)
public SparseGradient multiply(final int n)
'''
pass
def multiplyInPlace():
'''public void multiplyInPlace(final SparseGradient a)
'''
pass
def divide():
'''public SparseGradient divide(final SparseGradient a)
public SparseGradient divide(final double c)
'''
pass
def negate():
'''public SparseGradient negate()
'''
pass
def getField():
'''public Field<SparseGradient> getField()
'''
pass
def getZero():
'''public SparseGradient getZero()
'''
pass
def getOne():
'''public SparseGradient getOne()
'''
pass
def remainder():
'''public SparseGradient remainder(final double a)
public SparseGradient remainder(final SparseGradient a)
'''
pass
def abs():
'''public SparseGradient abs()
'''
pass
def ceil():
'''public SparseGradient ceil()
'''
pass
def floor():
'''public SparseGradient floor()
'''
pass
def rint():
'''public SparseGradient rint()
'''
pass
def round():
'''public long round()
'''
pass
def signum():
'''public SparseGradient signum()
'''
pass
def copySign():
'''public SparseGradient copySign(final SparseGradient sign)
public SparseGradient copySign(final double sign)
'''
pass
def scalb():
'''public SparseGradient scalb(final int n)
'''
pass
def hypot():
'''public SparseGradient hypot(final SparseGradient y)
public static SparseGradient hypot(final SparseGradient x, final SparseGradient y)
'''
pass
def reciprocal():
'''public SparseGradient reciprocal()
'''
pass
def sqrt():
'''public SparseGradient sqrt()
'''
pass
def cbrt():
'''public SparseGradient cbrt()
'''
pass
def rootN():
'''public SparseGradient rootN(final int n)
'''
pass
def pow():
'''public SparseGradient pow(final double p)
public SparseGradient pow(final int n)
public SparseGradient pow(final SparseGradient e)
public static SparseGradient pow(final double a, final SparseGradient x)
'''
pass
def exp():
'''public SparseGradient exp()
'''
pass
def expm1():
'''public SparseGradient expm1()
'''
pass
def log():
'''public SparseGradient log()
'''
pass
def log10():
'''public SparseGradient log10()
'''
pass
def log1p():
'''public SparseGradient log1p()
'''
pass
def cos():
'''public SparseGradient cos()
'''
pass
def sin():
'''public SparseGradient sin()
'''
pass
def tan():
'''public SparseGradient tan()
'''
pass
def acos():
'''public SparseGradient acos()
'''
pass
def asin():
'''public SparseGradient asin()
'''
pass
def atan():
'''public SparseGradient atan()
'''
pass
def atan2():
'''public SparseGradient atan2(final SparseGradient x)
public static SparseGradient atan2(final SparseGradient y, final SparseGradient x)
'''
pass
def cosh():
'''public SparseGradient cosh()
'''
pass
def sinh():
'''public SparseGradient sinh()
'''
pass
def tanh():
'''public SparseGradient tanh()
'''
pass
def acosh():
'''public SparseGradient acosh()
'''
pass
def asinh():
'''public SparseGradient asinh()
'''
pass
def atanh():
'''public SparseGradient atanh()
'''
pass
def toDegrees():
'''public SparseGradient toDegrees()
'''
pass
def toRadians():
'''public SparseGradient toRadians()
'''
pass
def taylor():
'''public double taylor(final double... delta)
'''
pass
def compose():
'''public SparseGradient compose(final double f0, final double f1)
'''
pass
def linearCombination():
'''public SparseGradient linearCombination(final SparseGradient[] a, final SparseGradient[] b)
public SparseGradient linearCombination(final double[] a, final SparseGradient[] b)
public SparseGradient linearCombination(final SparseGradient a1, final SparseGradient b1, final SparseGradient a2, final SparseGradient b2)
public SparseGradient linearCombination(final double a1, final SparseGradient b1, final double a2, final SparseGradient b2)
public SparseGradient linearCombination(final SparseGradient a1, final SparseGradient b1, final SparseGradient a2, final SparseGradient b2, final SparseGradient a3, final SparseGradient b3)
public SparseGradient linearCombination(final double a1, final SparseGradient b1, final double a2, final SparseGradient b2, final double a3, final SparseGradient b3)
public SparseGradient linearCombination(final SparseGradient a1, final SparseGradient b1, final SparseGradient a2, final SparseGradient b2, final SparseGradient a3, final SparseGradient b3, final SparseGradient a4, final SparseGradient b4)
public SparseGradient linearCombination(final double a1, final SparseGradient b1, final double a2, final SparseGradient b2, final double a3, final SparseGradient b3, final double a4, final SparseGradient b4)
'''
pass
def equals():
'''public boolean equals(final Object other)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
