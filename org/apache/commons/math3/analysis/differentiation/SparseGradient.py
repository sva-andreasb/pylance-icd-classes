def createConstant():
    '''    public static SparseGradient createConstant(final double value)
    '''
def createVariable():
    '''    public static SparseGradient createVariable(final int idx, final double value)
    '''
def numVars():
    '''    public int numVars()
    '''
def getDerivative():
    '''    public double getDerivative(final int index)
    '''
def getValue():
    '''    public double getValue()
    '''
def getReal():
    '''    public double getReal()
    '''
def add():
    '''    public SparseGradient add(final SparseGradient a)
    public SparseGradient add(final double c)
    '''
def addInPlace():
    '''    public void addInPlace(final SparseGradient a)
    '''
def subtract():
    '''    public SparseGradient subtract(final SparseGradient a)
    public SparseGradient subtract(final double c)
    '''
def multiply():
    '''    public SparseGradient multiply(final SparseGradient a)
    public SparseGradient multiply(final double c)
    public SparseGradient multiply(final int n)
    '''
def multiplyInPlace():
    '''    public void multiplyInPlace(final SparseGradient a)
    '''
def divide():
    '''    public SparseGradient divide(final SparseGradient a)
    public SparseGradient divide(final double c)
    '''
def negate():
    '''    public SparseGradient negate()
    '''
def getField():
    '''    public Field<SparseGradient> getField()
    '''
def getZero():
    '''    public SparseGradient getZero()
    '''
def getOne():
    '''    public SparseGradient getOne()
    '''
def remainder():
    '''    public SparseGradient remainder(final double a)
    public SparseGradient remainder(final SparseGradient a)
    '''
def abs():
    '''    public SparseGradient abs()
    '''
def ceil():
    '''    public SparseGradient ceil()
    '''
def floor():
    '''    public SparseGradient floor()
    '''
def rint():
    '''    public SparseGradient rint()
    '''
def round():
    '''    public long round()
    '''
def signum():
    '''    public SparseGradient signum()
    '''
def copySign():
    '''    public SparseGradient copySign(final SparseGradient sign)
    public SparseGradient copySign(final double sign)
    '''
def scalb():
    '''    public SparseGradient scalb(final int n)
    '''
def hypot():
    '''    public SparseGradient hypot(final SparseGradient y)
    public static SparseGradient hypot(final SparseGradient x, final SparseGradient y)
    '''
def reciprocal():
    '''    public SparseGradient reciprocal()
    '''
def sqrt():
    '''    public SparseGradient sqrt()
    '''
def cbrt():
    '''    public SparseGradient cbrt()
    '''
def rootN():
    '''    public SparseGradient rootN(final int n)
    '''
def pow():
    '''    public SparseGradient pow(final double p)
    public SparseGradient pow(final int n)
    public SparseGradient pow(final SparseGradient e)
    public static SparseGradient pow(final double a, final SparseGradient x)
    '''
def exp():
    '''    public SparseGradient exp()
    '''
def expm1():
    '''    public SparseGradient expm1()
    '''
def log():
    '''    public SparseGradient log()
    '''
def log10():
    '''    public SparseGradient log10()
    '''
def log1p():
    '''    public SparseGradient log1p()
    '''
def cos():
    '''    public SparseGradient cos()
    '''
def sin():
    '''    public SparseGradient sin()
    '''
def tan():
    '''    public SparseGradient tan()
    '''
def acos():
    '''    public SparseGradient acos()
    '''
def asin():
    '''    public SparseGradient asin()
    '''
def atan():
    '''    public SparseGradient atan()
    '''
def atan2():
    '''    public SparseGradient atan2(final SparseGradient x)
    public static SparseGradient atan2(final SparseGradient y, final SparseGradient x)
    '''
def cosh():
    '''    public SparseGradient cosh()
    '''
def sinh():
    '''    public SparseGradient sinh()
    '''
def tanh():
    '''    public SparseGradient tanh()
    '''
def acosh():
    '''    public SparseGradient acosh()
    '''
def asinh():
    '''    public SparseGradient asinh()
    '''
def atanh():
    '''    public SparseGradient atanh()
    '''
def toDegrees():
    '''    public SparseGradient toDegrees()
    '''
def toRadians():
    '''    public SparseGradient toRadians()
    '''
def taylor():
    '''    public double taylor(final double... delta)
    '''
def compose():
    '''    public SparseGradient compose(final double f0, final double f1)
    '''
def linearCombination():
    '''    public SparseGradient linearCombination(final SparseGradient[] a, final SparseGradient[] b)
    public SparseGradient linearCombination(final double[] a, final SparseGradient[] b)
    public SparseGradient linearCombination(final SparseGradient a1, final SparseGradient b1, final SparseGradient a2, final SparseGradient b2)
    public SparseGradient linearCombination(final double a1, final SparseGradient b1, final double a2, final SparseGradient b2)
    public SparseGradient linearCombination(final SparseGradient a1, final SparseGradient b1, final SparseGradient a2, final SparseGradient b2, final SparseGradient a3, final SparseGradient b3)
    public SparseGradient linearCombination(final double a1, final SparseGradient b1, final double a2, final SparseGradient b2, final double a3, final SparseGradient b3)
    public SparseGradient linearCombination(final SparseGradient a1, final SparseGradient b1, final SparseGradient a2, final SparseGradient b2, final SparseGradient a3, final SparseGradient b3, final SparseGradient a4, final SparseGradient b4)
    public SparseGradient linearCombination(final double a1, final SparseGradient b1, final double a2, final SparseGradient b2, final double a3, final SparseGradient b3, final double a4, final SparseGradient b4)
    '''
def equals():
    '''    public boolean equals(final Object other)
    '''
def hashCode():
    '''    public int hashCode()
    '''
