def DerivativeStructure():
'''public DerivativeStructure(final int parameters, final int order)
public DerivativeStructure(final int parameters, final int order, final double value)
public DerivativeStructure(final int parameters, final int order, final int index, final double value)
public DerivativeStructure(final double a1, final DerivativeStructure ds1, final double a2, final DerivativeStructure ds2)
public DerivativeStructure(final double a1, final DerivativeStructure ds1, final double a2, final DerivativeStructure ds2, final double a3, final DerivativeStructure ds3)
public DerivativeStructure(final double a1, final DerivativeStructure ds1, final double a2, final DerivativeStructure ds2, final double a3, final DerivativeStructure ds3, final double a4, final DerivativeStructure ds4)
public DerivativeStructure(final int parameters, final int order, final double... derivatives)
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
def createConstant():
'''public DerivativeStructure createConstant(final double c)
'''
pass
def getReal():
'''public double getReal()
'''
pass
def getValue():
'''public double getValue()
'''
pass
def getPartialDerivative():
'''public double getPartialDerivative(final int... orders)
'''
pass
def getAllDerivatives():
'''public double[] getAllDerivatives()
'''
pass
def add():
'''public DerivativeStructure add(final double a)
public DerivativeStructure add(final DerivativeStructure a)
'''
pass
def subtract():
'''public DerivativeStructure subtract(final double a)
public DerivativeStructure subtract(final DerivativeStructure a)
'''
pass
def multiply():
'''public DerivativeStructure multiply(final int n)
public DerivativeStructure multiply(final double a)
public DerivativeStructure multiply(final DerivativeStructure a)
'''
pass
def divide():
'''public DerivativeStructure divide(final double a)
public DerivativeStructure divide(final DerivativeStructure a)
'''
pass
def remainder():
'''public DerivativeStructure remainder(final double a)
public DerivativeStructure remainder(final DerivativeStructure a)
'''
pass
def negate():
'''public DerivativeStructure negate()
'''
pass
def abs():
'''public DerivativeStructure abs()
'''
pass
def ceil():
'''public DerivativeStructure ceil()
'''
pass
def floor():
'''public DerivativeStructure floor()
'''
pass
def rint():
'''public DerivativeStructure rint()
'''
pass
def round():
'''public long round()
'''
pass
def signum():
'''public DerivativeStructure signum()
'''
pass
def copySign():
'''public DerivativeStructure copySign(final DerivativeStructure sign)
public DerivativeStructure copySign(final double sign)
'''
pass
def getExponent():
'''public int getExponent()
'''
pass
def scalb():
'''public DerivativeStructure scalb(final int n)
'''
pass
def hypot():
'''public DerivativeStructure hypot(final DerivativeStructure y)
public static DerivativeStructure hypot(final DerivativeStructure x, final DerivativeStructure y)
'''
pass
def compose():
'''public DerivativeStructure compose(final double... f)
'''
pass
def reciprocal():
'''public DerivativeStructure reciprocal()
'''
pass
def sqrt():
'''public DerivativeStructure sqrt()
'''
pass
def cbrt():
'''public DerivativeStructure cbrt()
'''
pass
def rootN():
'''public DerivativeStructure rootN(final int n)
'''
pass
def getField():
'''public Field<DerivativeStructure> getField()
'''
pass
def getZero():
'''public DerivativeStructure getZero()
'''
pass
def getOne():
'''public DerivativeStructure getOne()
'''
pass
def pow():
'''public static DerivativeStructure pow(final double a, final DerivativeStructure x)
public DerivativeStructure pow(final double p)
public DerivativeStructure pow(final int n)
public DerivativeStructure pow(final DerivativeStructure e)
'''
pass
def exp():
'''public DerivativeStructure exp()
'''
pass
def expm1():
'''public DerivativeStructure expm1()
'''
pass
def log():
'''public DerivativeStructure log()
'''
pass
def log1p():
'''public DerivativeStructure log1p()
'''
pass
def log10():
'''public DerivativeStructure log10()
'''
pass
def cos():
'''public DerivativeStructure cos()
'''
pass
def sin():
'''public DerivativeStructure sin()
'''
pass
def tan():
'''public DerivativeStructure tan()
'''
pass
def acos():
'''public DerivativeStructure acos()
'''
pass
def asin():
'''public DerivativeStructure asin()
'''
pass
def atan():
'''public DerivativeStructure atan()
'''
pass
def atan2():
'''public DerivativeStructure atan2(final DerivativeStructure x)
public static DerivativeStructure atan2(final DerivativeStructure y, final DerivativeStructure x)
'''
pass
def cosh():
'''public DerivativeStructure cosh()
'''
pass
def sinh():
'''public DerivativeStructure sinh()
'''
pass
def tanh():
'''public DerivativeStructure tanh()
'''
pass
def acosh():
'''public DerivativeStructure acosh()
'''
pass
def asinh():
'''public DerivativeStructure asinh()
'''
pass
def atanh():
'''public DerivativeStructure atanh()
'''
pass
def toDegrees():
'''public DerivativeStructure toDegrees()
'''
pass
def toRadians():
'''public DerivativeStructure toRadians()
'''
pass
def taylor():
'''public double taylor(final double... delta)
'''
pass
def linearCombination():
'''public DerivativeStructure linearCombination(final DerivativeStructure[] a, final DerivativeStructure[] b)
public DerivativeStructure linearCombination(final double[] a, final DerivativeStructure[] b)
public DerivativeStructure linearCombination(final DerivativeStructure a1, final DerivativeStructure b1, final DerivativeStructure a2, final DerivativeStructure b2)
public DerivativeStructure linearCombination(final double a1, final DerivativeStructure b1, final double a2, final DerivativeStructure b2)
public DerivativeStructure linearCombination(final DerivativeStructure a1, final DerivativeStructure b1, final DerivativeStructure a2, final DerivativeStructure b2, final DerivativeStructure a3, final DerivativeStructure b3)
public DerivativeStructure linearCombination(final double a1, final DerivativeStructure b1, final double a2, final DerivativeStructure b2, final double a3, final DerivativeStructure b3)
public DerivativeStructure linearCombination(final DerivativeStructure a1, final DerivativeStructure b1, final DerivativeStructure a2, final DerivativeStructure b2, final DerivativeStructure a3, final DerivativeStructure b3, final DerivativeStructure a4, final DerivativeStructure b4)
public DerivativeStructure linearCombination(final double a1, final DerivativeStructure b1, final double a2, final DerivativeStructure b2, final double a3, final DerivativeStructure b3, final double a4, final DerivativeStructure b4)
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
