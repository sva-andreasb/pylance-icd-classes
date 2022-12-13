def BinaryPoint():
    '''    public BinaryPoint(final String name, final byte[]... point)
    public BinaryPoint(final String name, final byte[] packedPoint, final IndexableFieldType type)
    '''
def newExactQuery():
    '''    public static Query newExactQuery(final String field, final byte[] value)
    '''
def newRangeQuery():
    '''    public static Query newRangeQuery(final String field, final byte[] lowerValue, final byte[] upperValue)
    public static Query newRangeQuery(final String field, final byte[][] lowerValue, final byte[][] upperValue)
    '''
def newSetQuery():
    '''    public static Query newSetQuery(final String field, final byte[]... values)
    '''
def compare():
    '''    public int compare(final byte[] a, final byte[] b)
    '''
def next():
    '''    public BytesRef next()
    '''
