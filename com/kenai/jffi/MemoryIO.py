def getInstance():
    '''    public static MemoryIO getInstance()
    '''
def getCheckedInstance():
    '''    public static MemoryIO getCheckedInstance()
    '''
def copyMemory():
    '''    public final void copyMemory(final long src, final long dst, final long size)
    '''
def memset():
    '''    public final void memset(final long address, final int value, final long size)
    '''
def allocateMemory():
    '''    public final long allocateMemory(final long size, final boolean clear)
    '''
def freeMemory():
    '''    public final void freeMemory(final long address)
    '''
def getZeroTerminatedByteArray():
    '''    public final byte[] getZeroTerminatedByteArray(final long address, final long maxlen)
    public final byte[] getZeroTerminatedByteArray(final long address)
    public final byte[] getZeroTerminatedByteArray(final long address, final int maxlen)
    public final byte[] getZeroTerminatedByteArray(final long address)
    public final byte[] getZeroTerminatedByteArray(final long address, final int maxlen)
    public final byte[] getZeroTerminatedByteArray(final long address)
    public final byte[] getZeroTerminatedByteArray(final long address, final int maxlen)
    '''
def indexOf():
    '''    public final long indexOf(final long address, final byte value)
    public final long indexOf(final long address, final byte value, final int maxlen)
    '''
def newDirectByteBuffer():
    '''    public final ByteBuffer newDirectByteBuffer(final long address, final int capacity)
    '''
def getDirectBufferAddress():
    '''    public final long getDirectBufferAddress(final Buffer buffer)
    '''
def getByte():
    '''    public final byte getByte(final long address)
    public final byte getByte(final long address)
    public final byte getByte(final long address)
    '''
def getShort():
    '''    public final short getShort(final long address)
    public final short getShort(final long address)
    public final short getShort(final long address)
    '''
def getInt():
    '''    public final int getInt(final long address)
    public final int getInt(final long address)
    public final int getInt(final long address)
    '''
def getLong():
    '''    public final long getLong(final long address)
    public final long getLong(final long address)
    public final long getLong(final long address)
    '''
def getFloat():
    '''    public final float getFloat(final long address)
    public final float getFloat(final long address)
    public final float getFloat(final long address)
    '''
def getDouble():
    '''    public final double getDouble(final long address)
    public final double getDouble(final long address)
    public final double getDouble(final long address)
    '''
def putByte():
    '''    public final void putByte(final long address, final byte value)
    public final void putByte(final long address, final byte value)
    public final void putByte(final long address, final byte value)
    '''
def putShort():
    '''    public final void putShort(final long address, final short value)
    public final void putShort(final long address, final short value)
    public final void putShort(final long address, final short value)
    '''
def putInt():
    '''    public final void putInt(final long address, final int value)
    public final void putInt(final long address, final int value)
    public final void putInt(final long address, final int value)
    '''
def putLong():
    '''    public final void putLong(final long address, final long value)
    public final void putLong(final long address, final long value)
    public final void putLong(final long address, final long value)
    '''
def putFloat():
    '''    public final void putFloat(final long address, final float value)
    public final void putFloat(final long address, final float value)
    public final void putFloat(final long address, final float value)
    '''
def putDouble():
    '''    public final void putDouble(final long address, final double value)
    public final void putDouble(final long address, final double value)
    public final void putDouble(final long address, final double value)
    '''
def setMemory():
    '''    public final void setMemory(final long address, final long size, final byte value)
    public final void setMemory(final long address, final long size, final byte value)
    public final void setMemory(final long src, final long size, final byte value)
    '''
def _copyMemory():
    '''    public final void _copyMemory(final long src, final long dst, final long size)
    public final void _copyMemory(final long src, final long dst, final long size)
    public final void _copyMemory(final long src, final long dst, final long size)
    '''
def memcpy():
    '''    public final void memcpy(final long dst, final long src, final long size)
    public final void memcpy(final long dst, final long src, final long size)
    public final void memcpy(final long dst, final long src, final long size)
    '''
def memmove():
    '''    public final void memmove(final long dst, final long src, final long size)
    public final void memmove(final long dst, final long src, final long size)
    public final void memmove(final long dst, final long src, final long size)
    '''
def memchr():
    '''    public final long memchr(final long address, final int value, final long size)
    public final long memchr(final long address, final int value, final long size)
    public final long memchr(final long address, final int value, final long size)
    '''
def putByteArray():
    '''    public final void putByteArray(final long address, final byte[] data, final int offset, final int length)
    public final void putByteArray(final long address, final byte[] data, final int offset, final int length)
    public final void putByteArray(final long address, final byte[] data, final int offset, final int length)
    '''
def getByteArray():
    '''    public final void getByteArray(final long address, final byte[] data, final int offset, final int length)
    public final void getByteArray(final long address, final byte[] data, final int offset, final int length)
    public final void getByteArray(final long address, final byte[] data, final int offset, final int length)
    '''
def putCharArray():
    '''    public final void putCharArray(final long address, final char[] data, final int offset, final int length)
    public final void putCharArray(final long address, final char[] data, final int offset, final int length)
    public final void putCharArray(final long address, final char[] data, final int offset, final int length)
    '''
def getCharArray():
    '''    public final void getCharArray(final long address, final char[] data, final int offset, final int length)
    public final void getCharArray(final long address, final char[] data, final int offset, final int length)
    public final void getCharArray(final long address, final char[] data, final int offset, final int length)
    '''
def putShortArray():
    '''    public final void putShortArray(final long address, final short[] data, final int offset, final int length)
    public final void putShortArray(final long address, final short[] data, final int offset, final int length)
    public final void putShortArray(final long address, final short[] data, final int offset, final int length)
    '''
def getShortArray():
    '''    public final void getShortArray(final long address, final short[] data, final int offset, final int length)
    public final void getShortArray(final long address, final short[] data, final int offset, final int length)
    public final void getShortArray(final long address, final short[] data, final int offset, final int length)
    '''
def putIntArray():
    '''    public final void putIntArray(final long address, final int[] data, final int offset, final int length)
    public final void putIntArray(final long address, final int[] data, final int offset, final int length)
    public final void putIntArray(final long address, final int[] data, final int offset, final int length)
    '''
def getIntArray():
    '''    public final void getIntArray(final long address, final int[] data, final int offset, final int length)
    public final void getIntArray(final long address, final int[] data, final int offset, final int length)
    public final void getIntArray(final long address, final int[] data, final int offset, final int length)
    '''
def putLongArray():
    '''    public final void putLongArray(final long address, final long[] data, final int offset, final int length)
    public final void putLongArray(final long address, final long[] data, final int offset, final int length)
    public final void putLongArray(final long address, final long[] data, final int offset, final int length)
    '''
def getLongArray():
    '''    public final void getLongArray(final long address, final long[] data, final int offset, final int length)
    public final void getLongArray(final long address, final long[] data, final int offset, final int length)
    public final void getLongArray(final long address, final long[] data, final int offset, final int length)
    '''
def putFloatArray():
    '''    public final void putFloatArray(final long address, final float[] data, final int offset, final int length)
    public final void putFloatArray(final long address, final float[] data, final int offset, final int length)
    public final void putFloatArray(final long address, final float[] data, final int offset, final int length)
    '''
def getFloatArray():
    '''    public final void getFloatArray(final long address, final float[] data, final int offset, final int length)
    public final void getFloatArray(final long address, final float[] data, final int offset, final int length)
    public final void getFloatArray(final long address, final float[] data, final int offset, final int length)
    '''
def putDoubleArray():
    '''    public final void putDoubleArray(final long address, final double[] data, final int offset, final int length)
    public final void putDoubleArray(final long address, final double[] data, final int offset, final int length)
    public final void putDoubleArray(final long address, final double[] data, final int offset, final int length)
    '''
def getDoubleArray():
    '''    public final void getDoubleArray(final long address, final double[] data, final int offset, final int length)
    public final void getDoubleArray(final long address, final double[] data, final int offset, final int length)
    public final void getDoubleArray(final long address, final double[] data, final int offset, final int length)
    '''
def getStringLength():
    '''    public final long getStringLength(final long address)
    public final long getStringLength(final long address)
    public final long getStringLength(final long address)
    '''
def putZeroTerminatedByteArray():
    '''    public final void putZeroTerminatedByteArray(final long address, final byte[] data, final int offset, final int length)
    public final void putZeroTerminatedByteArray(final long address, final byte[] data, final int offset, final int length)
    public final void putZeroTerminatedByteArray(final long address, final byte[] data, final int offset, final int length)
    '''
def getAddress():
    '''    public final long getAddress(final long address)
    public final long getAddress(final long address)
    public final long getAddress(final long address)
    public final long getAddress(final long address)
    public final long getAddress(final long address)
    '''
def putAddress():
    '''    public final void putAddress(final long address, final long value)
    public final void putAddress(final long address, final long value)
    public final void putAddress(final long address, final long value)
    public final void putAddress(final long address, final long value)
    public final void putAddress(final long address, final long value)
    '''
