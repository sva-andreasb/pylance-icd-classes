def HeapInvocationBuffer():
    '''public HeapInvocationBuffer(final Function function)
    public HeapInvocationBuffer(final CallContext callContext)
    public HeapInvocationBuffer(final CallContext context, final int objectCount)
    '''
def putByte():
    '''public final void putByte(final int value)
    public final int putByte(final byte[] buffer, final int offset, final int value)
    public final void putByte(final byte[] buffer, final int offset, final int value)
    public final void putByte(final byte[] buffer, final int offset, final int value)
    public void putByte(final byte[] buffer, final int offset, final int value)
    '''
def putShort():
    '''public final void putShort(final int value)
    public final int putShort(final byte[] buffer, final int offset, final int value)
    public final void putShort(final byte[] buffer, final int offset, final int value)
    public final void putShort(final byte[] buffer, final int offset, final int value)
    public void putShort(final byte[] buffer, final int offset, final int value)
    '''
def putInt():
    '''public final void putInt(final int value)
    public final int putInt(final byte[] buffer, final int offset, final int value)
    public final void putInt(final byte[] buffer, final int offset, final int value)
    public final void putInt(final byte[] buffer, final int offset, final int value)
    public void putInt(final byte[] buffer, final int offset, final int value)
    '''
def putLong():
    '''public final void putLong(final long value)
    public final int putLong(final byte[] buffer, final int offset, final long value)
    public final void putLong(final byte[] buffer, final int offset, final long value)
    public final void putLong(final byte[] buffer, final int offset, final long value)
    public void putLong(final byte[] buffer, final int offset, final long value)
    '''
def putFloat():
    '''public final void putFloat(final float value)
    public final int putFloat(final byte[] buffer, final int offset, final float value)
    public final void putFloat(final byte[] buffer, final int offset, final float value)
    '''
def putDouble():
    '''public final void putDouble(final double value)
    public final int putDouble(final byte[] buffer, final int offset, final double value)
    public final void putDouble(final byte[] buffer, final int offset, final double value)
    '''
def putLongDouble():
    '''public final void putLongDouble(final double value)
    public final void putLongDouble(final BigDecimal value)
    '''
def putAddress():
    '''public final void putAddress(final long value)
    public final int putAddress(final byte[] buffer, final int offset, final long value)
    public final void putAddress(final byte[] buffer, final int offset, final long value)
    public final void putAddress(final byte[] buffer, final int offset, final long value)
    public void putAddress(final byte[] buffer, final int offset, final long value)
    public void putAddress(final byte[] buffer, final int offset, final long value)
    public void putAddress(final byte[] buffer, final int offset, final long value)
    '''
def putArray():
    '''public final void putArray(final byte[] array, final int offset, final int length, final int flags)
    public final void putArray(final short[] array, final int offset, final int length, final int flags)
    public final void putArray(final int[] array, final int offset, final int length, final int flags)
    public final void putArray(final long[] array, final int offset, final int length, final int flags)
    public final void putArray(final float[] array, final int offset, final int length, final int flags)
    public final void putArray(final double[] array, final int offset, final int length, final int flags)
    '''
def putDirectBuffer():
    '''public final void putDirectBuffer(final Buffer value, final int offset, final int length)
    '''
def putStruct():
    '''public final void putStruct(final byte[] struct, final int offset)
    public final void putStruct(final long struct)
    '''
def putObject():
    '''public final void putObject(final Object o, final ObjectParameterStrategy strategy, final ObjectParameterInfo info)
    public final void putObject(final Object o, final ObjectParameterStrategy strategy, final int flags)
    '''
def putJNIEnvironment():
    '''public final void putJNIEnvironment()
    '''
def putJNIObject():
    '''public final void putJNIObject(final Object obj)
    '''
def DefaultEncoder():
    '''public DefaultEncoder(final ArrayIO io)
    '''
def getBufferSize():
    '''public final int getBufferSize(final CallContext callContext)
    '''
def skipAddress():
    '''public int skipAddress(final int offset)
    '''
