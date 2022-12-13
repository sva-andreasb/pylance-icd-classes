def BinaryPoint():
'''public BinaryPoint(final String name, final byte[]... point)
public BinaryPoint(final String name, final byte[] packedPoint, final IndexableFieldType type)
'''
pass
def newExactQuery():
'''public static Query newExactQuery(final String field, final byte[] value)
'''
pass
def newRangeQuery():
'''public static Query newRangeQuery(final String field, final byte[] lowerValue, final byte[] upperValue)
public static Query newRangeQuery(final String field, final byte[][] lowerValue, final byte[][] upperValue)
'''
pass
def newSetQuery():
'''public static Query newSetQuery(final String field, final byte[]... values)
'''
pass
def compare():
'''public int compare(final byte[] a, final byte[] b)
'''
pass
def next():
'''public BytesRef next()
'''
pass
