def setIntValue():
'''public void setIntValue(final int value)
'''
pass
def setIntValues():
'''public void setIntValues(final int... point)
'''
pass
def setBytesValue():
'''public void setBytesValue(final BytesRef bytes)
'''
pass
def numericValue():
'''public Number numericValue()
'''
pass
def pack():
'''public static BytesRef pack(final int... point)
'''
pass
def IntPoint():
'''public IntPoint(final String name, final int... point)
'''
pass
def toString():
'''public String toString()
'''
pass
def encodeDimension():
'''public static void encodeDimension(final int value, final byte[] dest, final int offset)
'''
pass
def decodeDimension():
'''public static int decodeDimension(final byte[] value, final int offset)
'''
pass
def newExactQuery():
'''public static Query newExactQuery(final String field, final int value)
'''
pass
def newRangeQuery():
'''public static Query newRangeQuery(final String field, final int lowerValue, final int upperValue)
public static Query newRangeQuery(final String field, final int[] lowerValue, final int[] upperValue)
'''
pass
def newSetQuery():
'''public static Query newSetQuery(final String field, final int... values)
public static Query newSetQuery(final String field, final Collection<Integer> values)
'''
pass
def next():
'''public BytesRef next()
'''
pass
