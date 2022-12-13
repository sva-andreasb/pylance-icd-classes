def DerivativeStructure():
    '''    public DerivativeStructure(final int parameters, final int order)
    public DerivativeStructure(final int parameters, final int order, final double value)
    public DerivativeStructure(final int parameters, final int order, final int index, final double value)
    public DerivativeStructure(final double a1, final DerivativeStructure ds1, final double a2, final DerivativeStructure ds2)
    public DerivativeStructure(final double a1, final DerivativeStructure ds1, final double a2, final DerivativeStructure ds2, final double a3, final DerivativeStructure ds3)
    public DerivativeStructure(final double a1, final DerivativeStructure ds1, final double a2, final DerivativeStructure ds2, final double a3, final DerivativeStructure ds3, final double a4, final DerivativeStructure ds4)
    public DerivativeStructure(final int parameters, final int order, final double... derivatives)
    '''
def getFreeParameters():
    '''    public int getFreeParameters()
    '''
def getOrder():
    '''    public int getOrder()
    '''
def createConstant():
    '''    public DerivativeStructure createConstant(final double c)
    '''
def getReal():
    '''    public double getReal()
    '''
def getValue():
    '''    public double getValue()
    '''
def getPartialDerivative():
    '''    public double getPartialDerivative(final int... orders)
    '''
def getAllDerivatives():
    '''    public double[] getAllDerivatives()
    '''
def add():
    '''    public DerivativeStructure add(final double a)
    public DerivativeStructure add(final DerivativeStructure a)
    '''
def subtract():
    '''    public DerivativeStructure subtract(final double a)
    public DerivativeStructure subtract(final DerivativeStructure a)
    '''
def multiply():
    '''    public DerivativeStructure multiply(final int n)
    public DerivativeStructure multiply(final double a)
    public DerivativeStructure multiply(final DerivativeStructure a)
    '''
def divide():
    '''    public DerivativeStructure divide(final double a)
    public DerivativeStructure divide(final DerivativeStructure a)
    '''
def remainder():
    '''    public DerivativeStructure remainder(final double a)
    public DerivativeStructure remainder(final DerivativeStructure a)
    '''
def negate():
    '''    public DerivativeStructure negate()
    '''
def abs():
    '''    public DerivativeStructure abs()
    '''
def ceil():
    '''    public DerivativeStructure ceil()
    '''
def floor():
    '''    public DerivativeStructure floor()
    '''
def rint():
    '''    public DerivativeStructure rint()
    '''
def round():
    '''    public long round()
    '''
def signum():
    '''    public DerivativeStructure signum()
    '''
def copySign():
    '''    public DerivativeStructure copySign(final DerivativeStructure sign)
    public DerivativeStructure copySign(final double sign)
    '''
def getExponent():
    '''    public int getExponent()
    '''
def scalb():
    '''    public DerivativeStructure scalb(final int n)
    '''
def hypot():
    '''    public DerivativeStructure hypot(final DerivativeStructure y)
    public static DerivativeStructure hypot(final DerivativeStructure x, final DerivativeStructure y)
    '''
def compose():
    '''    public DerivativeStructure compose(final double... f)
    '''
def reciprocal():
    '''    public DerivativeStructure reciprocal()
    '''
def sqrt():
    '''    public DerivativeStructure sqrt()
    '''
def cbrt():
    '''    public DerivativeStructure cbrt()
    '''
def rootN():
    '''    public DerivativeStructure rootN(final int n)
    '''
def getField():
    '''    public Field<DerivativeStructure> getField()
    '''
def getZero():
    '''    public DerivativeStructure getZero()
    '''
def getOne():
    '''    public DerivativeStructure getOne()
    '''
def pow():
    '''    public static DerivativeStructure pow(final double a, final DerivativeStructure x)
    public DerivativeStructure pow(final double p)
    public DerivativeStructure pow(final int n)
    public DerivativeStructure pow(final DerivativeStructure e)
    '''
def exp():
    '''    public DerivativeStructure exp()
    '''
def expm1():
    '''    public DerivativeStructure expm1()
    '''
def log():
    '''    public DerivativeStructure log()
    '''
def log1p():
    '''    public DerivativeStructure log1p()
    '''
def log10():
    '''    public DerivativeStructure log10()
    '''
def cos():
    '''    public DerivativeStructure cos()
    '''
def sin():
    '''    public DerivativeStructure sin()
    '''
def tan():
    '''    public DerivativeStructure tan()
    '''
def acos():
    '''    public DerivativeStructure acos()
    '''
def asin():
    '''    public DerivativeStructure asin()
    '''
def atan():
    '''    public DerivativeStructure atan()
    '''
def atan2():
    '''    public DerivativeStructure atan2(final DerivativeStructure x)
    public static DerivativeStructure atan2(final DerivativeStructure y, final DerivativeStructure x)
    '''
def cosh():
    '''    public DerivativeStructure cosh()
    '''
def sinh():
    '''    public DerivativeStructure sinh()
    '''
def tanh():
    '''    public DerivativeStructure tanh()
    '''
def acosh():
    '''    public DerivativeStructure acosh()
    '''
def asinh():
    '''    public DerivativeStructure asinh()
    '''
def atanh():
    '''    public DerivativeStructure atanh()
    '''
def toDegrees():
    '''    public DerivativeStructure toDegrees()
    '''
def toRadians():
    '''    public DerivativeStructure toRadians()
    '''
def taylor():
    '''    public double taylor(final double... delta)
    '''
def linearCombination():
    '''    public DerivativeStructure linearCombination(final DerivativeStructure[] a, final DerivativeStructure[] b)
    public DerivativeStructure linearCombination(final double[] a, final DerivativeStructure[] b)
    public DerivativeStructure linearCombination(final DerivativeStructure a1, final DerivativeStructure b1, final DerivativeStructure a2, final DerivativeStructure b2)
    public DerivativeStructure linearCombination(final double a1, final DerivativeStructure b1, final double a2, final DerivativeStructure b2)
    public DerivativeStructure linearCombination(final DerivativeStructure a1, final DerivativeStructure b1, final DerivativeStructure a2, final DerivativeStructure b2, final DerivativeStructure a3, final DerivativeStructure b3)
    public DerivativeStructure linearCombination(final double a1, final DerivativeStructure b1, final double a2, final DerivativeStructure b2, final double a3, final DerivativeStructure b3)
    public DerivativeStructure linearCombination(final DerivativeStructure a1, final DerivativeStructure b1, final DerivativeStructure a2, final DerivativeStructure b2, final DerivativeStructure a3, final DerivativeStructure b3, final DerivativeStructure a4, final DerivativeStructure b4)
    public DerivativeStructure linearCombination(final double a1, final DerivativeStructure b1, final double a2, final DerivativeStructure b2, final double a3, final DerivativeStructure b3, final double a4, final DerivativeStructure b4)
    '''
def equals():
    '''    public boolean equals(final Object other)
    '''
def hashCode():
    '''    public int hashCode()
    '''
