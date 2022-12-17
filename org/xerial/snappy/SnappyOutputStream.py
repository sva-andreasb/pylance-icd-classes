def ():
    '''returns SnappyOutputStream\n\n
    (final OutputStream outputStream)\n
    (final OutputStream outputStream, final int n)\n
    (final OutputStream out, final int b, final BufferAllocatorFactory bufferAllocatorFactory)\n
    '''
def write():
    '''returns None\n\n
    write(final byte[] array, final int n, final int n2)\n
    write(final long[] array, final int n, final int n2)\n
    write(final double[] array, final int n, final int n2)\n
    write(final float[] array, final int n, final int n2)\n
    write(final int[] array, final int n, final int n2)\n
    write(final short[] array, final int n, final int n2)\n
    write(final long[] array)\n
    write(final double[] array)\n
    write(final float[] array)\n
    write(final int[] array)\n
    write(final short[] array)\n
    write(final int n)\n
    '''
def rawWrite():
    '''returns None\n\n
    rawWrite(final Object o, final int n, final int n2)\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
