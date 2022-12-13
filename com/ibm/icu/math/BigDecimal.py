ROUND_CEILING = "int  2"
ROUND_DOWN = "int  1"
ROUND_FLOOR = "int  3"
ROUND_HALF_DOWN = "int  5"
ROUND_HALF_EVEN = "int  6"
ROUND_HALF_UP = "int  4"
ROUND_UNNECESSARY = "int  7"
ROUND_UP = "int  0"
def BigDecimal():
    '''public BigDecimal(final java.math.BigDecimal bd)
    public BigDecimal(final BigInteger bi)
    public BigDecimal(final BigInteger bi, final int scale)
    public BigDecimal(final char[] inchars)
    public BigDecimal(final char[] inchars, int offset, int length)
    public BigDecimal(final double num)
    public BigDecimal(int num)
    public BigDecimal(long num)
    public BigDecimal(final String string)
    '''
def abs():
    '''public BigDecimal abs()
    public BigDecimal abs(final MathContext set)
    '''
def add():
    '''public BigDecimal add(final BigDecimal rhs)
    public BigDecimal add(BigDecimal rhs, final MathContext set)
    '''
def compareTo():
    '''public int compareTo(final BigDecimal rhs)
    public int compareTo(final BigDecimal rhs, final MathContext set)
    '''
def divide():
    '''public BigDecimal divide(final BigDecimal rhs)
    public BigDecimal divide(final BigDecimal rhs, final int round)
    public BigDecimal divide(final BigDecimal rhs, final int scale, final int round)
    public BigDecimal divide(final BigDecimal rhs, final MathContext set)
    '''
def divideInteger():
    '''public BigDecimal divideInteger(final BigDecimal rhs)
    public BigDecimal divideInteger(final BigDecimal rhs, final MathContext set)
    '''
def max():
    '''public BigDecimal max(final BigDecimal rhs)
    public BigDecimal max(final BigDecimal rhs, final MathContext set)
    '''
def min():
    '''public BigDecimal min(final BigDecimal rhs)
    public BigDecimal min(final BigDecimal rhs, final MathContext set)
    '''
def multiply():
    '''public BigDecimal multiply(final BigDecimal rhs)
    public BigDecimal multiply(BigDecimal rhs, final MathContext set)
    '''
def negate():
    '''public BigDecimal negate()
    public BigDecimal negate(final MathContext set)
    '''
def plus():
    '''public BigDecimal plus()
    public BigDecimal plus(final MathContext set)
    '''
def pow():
    '''public BigDecimal pow(final BigDecimal rhs)
    public BigDecimal pow(final BigDecimal rhs, final MathContext set)
    '''
def remainder():
    '''public BigDecimal remainder(final BigDecimal rhs)
    public BigDecimal remainder(final BigDecimal rhs, final MathContext set)
    '''
def subtract():
    '''public BigDecimal subtract(final BigDecimal rhs)
    public BigDecimal subtract(final BigDecimal rhs, final MathContext set)
    '''
def byteValueExact():
    '''public byte byteValueExact()
    '''
def doubleValue():
    '''public double doubleValue()
    '''
def equals():
    '''public boolean equals(final Object obj)
    '''
def floatValue():
    '''public float floatValue()
    '''
def format():
    '''public String format(final int before, final int after)
    public String format(final int before, final int after, final int explaces, final int exdigits, int exformint, int exround)
    '''
def hashCode():
    '''public int hashCode()
    '''
def intValue():
    '''public int intValue()
    '''
def intValueExact():
    '''public int intValueExact()
    '''
def longValue():
    '''public long longValue()
    '''
def longValueExact():
    '''public long longValueExact()
    '''
def movePointLeft():
    '''public BigDecimal movePointLeft(final int n)
    '''
def movePointRight():
    '''public BigDecimal movePointRight(final int n)
    '''
def scale():
    '''public int scale()
    '''
def setScale():
    '''public BigDecimal setScale(final int scale)
    public BigDecimal setScale(final int scale, final int round)
    '''
def shortValueExact():
    '''public short shortValueExact()
    '''
def signum():
    '''public int signum()
    '''
def toBigInteger():
    '''public BigInteger toBigInteger()
    '''
def toBigIntegerExact():
    '''public BigInteger toBigIntegerExact()
    '''
def toCharArray():
    '''public char[] toCharArray()
    '''
def toString():
    '''public String toString()
    '''
def unscaledValue():
    '''public BigInteger unscaledValue()
    '''
def valueOf():
    '''public static BigDecimal valueOf(final double dub)
    public static BigDecimal valueOf(final long lint)
    public static BigDecimal valueOf(final long lint, final int scale)
    '''
