def ():
    '''returns AbstractBufferMemoryIO\n\n
    (final Runtime runtime, final ByteBuffer buffer, final long address)\n
    '''
def size():
    '''returns long\n\n
    size()\n
    '''
def arrayLength():
    '''returns int\n\n
    arrayLength()\n
    '''
def arrayOffset():
    '''returns int\n\n
    arrayOffset()\n
    '''
def array():
    '''returns Object\n\n
    array()\n
    '''
def hasArray():
    '''returns boolean\n\n
    hasArray()\n
    '''
def getByte():
    '''returns byte\n\n
    getByte(final long offset)\n
    '''
def getShort():
    '''returns short\n\n
    getShort(final long offset)\n
    '''
def getInt():
    '''returns int\n\n
    getInt(final long offset)\n
    '''
def getLongLong():
    '''returns long\n\n
    getLongLong(final long offset)\n
    '''
def getFloat():
    '''returns float\n\n
    getFloat(final long offset)\n
    '''
def getDouble():
    '''returns double\n\n
    getDouble(final long offset)\n
    '''
def putByte():
    '''returns None\n\n
    putByte(final long offset, final byte value)\n
    '''
def putShort():
    '''returns None\n\n
    putShort(final long offset, final short value)\n
    '''
def putInt():
    '''returns None\n\n
    putInt(final long offset, final int value)\n
    '''
def putLongLong():
    '''returns None\n\n
    putLongLong(final long offset, final long value)\n
    '''
def putFloat():
    '''returns None\n\n
    putFloat(final long offset, final float value)\n
    '''
def putDouble():
    '''returns None\n\n
    putDouble(final long offset, final double value)\n
    '''
def getString():
    '''returns String\n\n
    getString(final long offset, final int size)\n
    getString(final long offset)\n
    getString(final long offset, final int maxLength, final Charset cs)\n
    '''
def putString():
    '''returns None\n\n
    putString(final long offset, final String string)\n
    putString(final long offset, final String string, final int maxLength, final Charset cs)\n
    '''
def get():
    '''returns None\n\n
    get(final long offset, final byte[] dst, final int off, final int len)\n
    get(final long offset, final short[] dst, final int off, final int len)\n
    get(final long offset, final int[] dst, final int off, final int len)\n
    get(final long offset, final long[] dst, final int off, final int len)\n
    get(final long offset, final float[] dst, final int off, final int len)\n
    get(final long offset, final double[] dst, final int off, final int len)\n
    '''
def put():
    '''returns None\n\n
    put(final long offset, final byte[] dst, final int off, final int len)\n
    put(final long offset, final short[] dst, final int off, final int len)\n
    put(final long offset, final int[] src, final int off, final int len)\n
    put(final long offset, final long[] src, final int off, final int len)\n
    put(final long offset, final float[] src, final int off, final int len)\n
    put(final long offset, final double[] src, final int off, final int len)\n
    '''
def indexOf():
    '''returns int\n\n
    indexOf(long offset, final byte value, final int maxlen)\n
    '''
def setMemory():
    '''returns None\n\n
    setMemory(final long offset, final long size, final byte value)\n
    '''
