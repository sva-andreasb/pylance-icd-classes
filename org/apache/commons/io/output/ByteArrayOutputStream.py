def ByteArrayOutputStream():
    '''public ByteArrayOutputStream()
    public ByteArrayOutputStream(final int size)
    '''
def write():
    '''public void write(final byte[] b, final int off, final int len)
    public synchronized void write(final int b)
    public synchronized int write(final InputStream in)
    '''
def size():
    '''public synchronized int size()
    '''
def close():
    '''public void close()
    '''
def reset():
    '''public synchronized void reset()
    '''
def writeTo():
    '''public synchronized void writeTo(final OutputStream out)
    '''
def toBufferedInputStream():
    '''public static InputStream toBufferedInputStream(final InputStream input)
    public static InputStream toBufferedInputStream(final InputStream input, final int size)
    '''
def toInputStream():
    '''public synchronized InputStream toInputStream()
    '''
def toByteArray():
    '''public synchronized byte[] toByteArray()
    '''
def toString():
    '''public String toString()
    public String toString(final String enc)
    public String toString(final Charset charset)
    '''
