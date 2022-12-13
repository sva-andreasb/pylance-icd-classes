def setIntValue():
    '''    public void setIntValue(final int value)
    '''
def setIntValues():
    '''    public void setIntValues(final int... point)
    '''
def setBytesValue():
    '''    public void setBytesValue(final BytesRef bytes)
    '''
def numericValue():
    '''    public Number numericValue()
    '''
def pack():
    '''    public static BytesRef pack(final int... point)
    '''
def IntPoint():
    '''    public IntPoint(final String name, final int... point)
    '''
def toString():
    '''    public String toString()
    '''
def encodeDimension():
    '''    public static void encodeDimension(final int value, final byte[] dest, final int offset)
    '''
def decodeDimension():
    '''    public static int decodeDimension(final byte[] value, final int offset)
    '''
def newExactQuery():
    '''    public static Query newExactQuery(final String field, final int value)
    '''
def newRangeQuery():
    '''    public static Query newRangeQuery(final String field, final int lowerValue, final int upperValue)
    public static Query newRangeQuery(final String field, final int[] lowerValue, final int[] upperValue)
    '''
def newSetQuery():
    '''    public static Query newSetQuery(final String field, final int... values)
    public static Query newSetQuery(final String field, final Collection<Integer> values)
    '''
def next():
    '''    public BytesRef next()
    '''
