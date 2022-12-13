def getInstance():
'''public static MemoryIO getInstance()
'''
pass
def getCheckedInstance():
'''public static MemoryIO getCheckedInstance()
'''
pass
def copyMemory():
'''public final void copyMemory(final long src, final long dst, final long size)
'''
pass
def memset():
'''public final void memset(final long address, final int value, final long size)
'''
pass
def allocateMemory():
'''public final long allocateMemory(final long size, final boolean clear)
'''
pass
def freeMemory():
'''public final void freeMemory(final long address)
'''
pass
def getZeroTerminatedByteArray():
'''public final byte[] getZeroTerminatedByteArray(final long address, final long maxlen)
public final byte[] getZeroTerminatedByteArray(final long address)
public final byte[] getZeroTerminatedByteArray(final long address, final int maxlen)
public final byte[] getZeroTerminatedByteArray(final long address)
public final byte[] getZeroTerminatedByteArray(final long address, final int maxlen)
public final byte[] getZeroTerminatedByteArray(final long address)
public final byte[] getZeroTerminatedByteArray(final long address, final int maxlen)
'''
pass
def indexOf():
'''public final long indexOf(final long address, final byte value)
public final long indexOf(final long address, final byte value, final int maxlen)
'''
pass
def newDirectByteBuffer():
'''public final ByteBuffer newDirectByteBuffer(final long address, final int capacity)
'''
pass
def getDirectBufferAddress():
'''public final long getDirectBufferAddress(final Buffer buffer)
'''
pass
def getByte():
'''public final byte getByte(final long address)
public final byte getByte(final long address)
public final byte getByte(final long address)
'''
pass
def getShort():
'''public final short getShort(final long address)
public final short getShort(final long address)
public final short getShort(final long address)
'''
pass
def getInt():
'''public final int getInt(final long address)
public final int getInt(final long address)
public final int getInt(final long address)
'''
pass
def getLong():
'''public final long getLong(final long address)
public final long getLong(final long address)
public final long getLong(final long address)
'''
pass
def getFloat():
'''public final float getFloat(final long address)
public final float getFloat(final long address)
public final float getFloat(final long address)
'''
pass
def getDouble():
'''public final double getDouble(final long address)
public final double getDouble(final long address)
public final double getDouble(final long address)
'''
pass
def putByte():
'''public final void putByte(final long address, final byte value)
public final void putByte(final long address, final byte value)
public final void putByte(final long address, final byte value)
'''
pass
def putShort():
'''public final void putShort(final long address, final short value)
public final void putShort(final long address, final short value)
public final void putShort(final long address, final short value)
'''
pass
def putInt():
'''public final void putInt(final long address, final int value)
public final void putInt(final long address, final int value)
public final void putInt(final long address, final int value)
'''
pass
def putLong():
'''public final void putLong(final long address, final long value)
public final void putLong(final long address, final long value)
public final void putLong(final long address, final long value)
'''
pass
def putFloat():
'''public final void putFloat(final long address, final float value)
public final void putFloat(final long address, final float value)
public final void putFloat(final long address, final float value)
'''
pass
def putDouble():
'''public final void putDouble(final long address, final double value)
public final void putDouble(final long address, final double value)
public final void putDouble(final long address, final double value)
'''
pass
def setMemory():
'''public final void setMemory(final long address, final long size, final byte value)
public final void setMemory(final long address, final long size, final byte value)
public final void setMemory(final long src, final long size, final byte value)
'''
pass
def _copyMemory():
'''public final void _copyMemory(final long src, final long dst, final long size)
public final void _copyMemory(final long src, final long dst, final long size)
public final void _copyMemory(final long src, final long dst, final long size)
'''
pass
def memcpy():
'''public final void memcpy(final long dst, final long src, final long size)
public final void memcpy(final long dst, final long src, final long size)
public final void memcpy(final long dst, final long src, final long size)
'''
pass
def memmove():
'''public final void memmove(final long dst, final long src, final long size)
public final void memmove(final long dst, final long src, final long size)
public final void memmove(final long dst, final long src, final long size)
'''
pass
def memchr():
'''public final long memchr(final long address, final int value, final long size)
public final long memchr(final long address, final int value, final long size)
public final long memchr(final long address, final int value, final long size)
'''
pass
def putByteArray():
'''public final void putByteArray(final long address, final byte[] data, final int offset, final int length)
public final void putByteArray(final long address, final byte[] data, final int offset, final int length)
public final void putByteArray(final long address, final byte[] data, final int offset, final int length)
'''
pass
def getByteArray():
'''public final void getByteArray(final long address, final byte[] data, final int offset, final int length)
public final void getByteArray(final long address, final byte[] data, final int offset, final int length)
public final void getByteArray(final long address, final byte[] data, final int offset, final int length)
'''
pass
def putCharArray():
'''public final void putCharArray(final long address, final char[] data, final int offset, final int length)
public final void putCharArray(final long address, final char[] data, final int offset, final int length)
public final void putCharArray(final long address, final char[] data, final int offset, final int length)
'''
pass
def getCharArray():
'''public final void getCharArray(final long address, final char[] data, final int offset, final int length)
public final void getCharArray(final long address, final char[] data, final int offset, final int length)
public final void getCharArray(final long address, final char[] data, final int offset, final int length)
'''
pass
def putShortArray():
'''public final void putShortArray(final long address, final short[] data, final int offset, final int length)
public final void putShortArray(final long address, final short[] data, final int offset, final int length)
public final void putShortArray(final long address, final short[] data, final int offset, final int length)
'''
pass
def getShortArray():
'''public final void getShortArray(final long address, final short[] data, final int offset, final int length)
public final void getShortArray(final long address, final short[] data, final int offset, final int length)
public final void getShortArray(final long address, final short[] data, final int offset, final int length)
'''
pass
def putIntArray():
'''public final void putIntArray(final long address, final int[] data, final int offset, final int length)
public final void putIntArray(final long address, final int[] data, final int offset, final int length)
public final void putIntArray(final long address, final int[] data, final int offset, final int length)
'''
pass
def getIntArray():
'''public final void getIntArray(final long address, final int[] data, final int offset, final int length)
public final void getIntArray(final long address, final int[] data, final int offset, final int length)
public final void getIntArray(final long address, final int[] data, final int offset, final int length)
'''
pass
def putLongArray():
'''public final void putLongArray(final long address, final long[] data, final int offset, final int length)
public final void putLongArray(final long address, final long[] data, final int offset, final int length)
public final void putLongArray(final long address, final long[] data, final int offset, final int length)
'''
pass
def getLongArray():
'''public final void getLongArray(final long address, final long[] data, final int offset, final int length)
public final void getLongArray(final long address, final long[] data, final int offset, final int length)
public final void getLongArray(final long address, final long[] data, final int offset, final int length)
'''
pass
def putFloatArray():
'''public final void putFloatArray(final long address, final float[] data, final int offset, final int length)
public final void putFloatArray(final long address, final float[] data, final int offset, final int length)
public final void putFloatArray(final long address, final float[] data, final int offset, final int length)
'''
pass
def getFloatArray():
'''public final void getFloatArray(final long address, final float[] data, final int offset, final int length)
public final void getFloatArray(final long address, final float[] data, final int offset, final int length)
public final void getFloatArray(final long address, final float[] data, final int offset, final int length)
'''
pass
def putDoubleArray():
'''public final void putDoubleArray(final long address, final double[] data, final int offset, final int length)
public final void putDoubleArray(final long address, final double[] data, final int offset, final int length)
public final void putDoubleArray(final long address, final double[] data, final int offset, final int length)
'''
pass
def getDoubleArray():
'''public final void getDoubleArray(final long address, final double[] data, final int offset, final int length)
public final void getDoubleArray(final long address, final double[] data, final int offset, final int length)
public final void getDoubleArray(final long address, final double[] data, final int offset, final int length)
'''
pass
def getStringLength():
'''public final long getStringLength(final long address)
public final long getStringLength(final long address)
public final long getStringLength(final long address)
'''
pass
def putZeroTerminatedByteArray():
'''public final void putZeroTerminatedByteArray(final long address, final byte[] data, final int offset, final int length)
public final void putZeroTerminatedByteArray(final long address, final byte[] data, final int offset, final int length)
public final void putZeroTerminatedByteArray(final long address, final byte[] data, final int offset, final int length)
'''
pass
def getAddress():
'''public final long getAddress(final long address)
public final long getAddress(final long address)
public final long getAddress(final long address)
public final long getAddress(final long address)
public final long getAddress(final long address)
'''
pass
def putAddress():
'''public final void putAddress(final long address, final long value)
public final void putAddress(final long address, final long value)
public final void putAddress(final long address, final long value)
public final void putAddress(final long address, final long value)
public final void putAddress(final long address, final long value)
'''
pass
