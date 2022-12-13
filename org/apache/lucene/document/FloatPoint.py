def nextUp():
    '''public static float nextUp(final float f)
    '''
def nextDown():
    '''public static float nextDown(final float f)
    '''
def setFloatValue():
    '''public void setFloatValue(final float value)
    '''
def setFloatValues():
    '''public void setFloatValues(final float... point)
    '''
def setBytesValue():
    '''public void setBytesValue(final BytesRef bytes)
    '''
def numericValue():
    '''public Number numericValue()
    '''
def pack():
    '''public static BytesRef pack(final float... point)
    '''
def FloatPoint():
    '''public FloatPoint(final String name, final float... point)
    '''
def toString():
    '''public String toString()
    '''
def encodeDimension():
    '''public static void encodeDimension(final float value, final byte[] dest, final int offset)
    '''
def decodeDimension():
    '''public static float decodeDimension(final byte[] value, final int offset)
    '''
def newExactQuery():
    '''public static Query newExactQuery(final String field, final float value)
    '''
def newRangeQuery():
    '''public static Query newRangeQuery(final String field, final float lowerValue, final float upperValue)
    public static Query newRangeQuery(final String field, final float[] lowerValue, final float[] upperValue)
    '''
def newSetQuery():
    '''public static Query newSetQuery(final String field, final float... values)
    public static Query newSetQuery(final String field, final Collection<Float> values)
    '''
def next():
    '''public BytesRef next()
    '''
