def nextUp():
    '''public static double nextUp(final double d)
    '''
def nextDown():
    '''public static double nextDown(final double d)
    '''
def setDoubleValue():
    '''public void setDoubleValue(final double value)
    '''
def setDoubleValues():
    '''public void setDoubleValues(final double... point)
    '''
def setBytesValue():
    '''public void setBytesValue(final BytesRef bytes)
    '''
def numericValue():
    '''public Number numericValue()
    '''
def pack():
    '''public static BytesRef pack(final double... point)
    '''
def DoublePoint():
    '''public DoublePoint(final String name, final double... point)
    '''
def toString():
    '''public String toString()
    '''
def encodeDimension():
    '''public static void encodeDimension(final double value, final byte[] dest, final int offset)
    '''
def decodeDimension():
    '''public static double decodeDimension(final byte[] value, final int offset)
    '''
def newExactQuery():
    '''public static Query newExactQuery(final String field, final double value)
    '''
def newRangeQuery():
    '''public static Query newRangeQuery(final String field, final double lowerValue, final double upperValue)
    public static Query newRangeQuery(final String field, final double[] lowerValue, final double[] upperValue)
    '''
def newSetQuery():
    '''public static Query newSetQuery(final String field, final double... values)
    public static Query newSetQuery(final String field, final Collection<Double> values)
    '''
def next():
    '''public BytesRef next()
    '''
