def IOContext():
    '''public IOContext(final BufferRecycler br, final Object sourceRef, final boolean managedResource)
    '''
def setEncoding():
    '''public void setEncoding(final JsonEncoding enc)
    '''
def withEncoding():
    '''public IOContext withEncoding(final JsonEncoding enc)
    '''
def getSourceReference():
    '''public Object getSourceReference()
    '''
def getEncoding():
    '''public JsonEncoding getEncoding()
    '''
def isResourceManaged():
    '''public boolean isResourceManaged()
    '''
def constructTextBuffer():
    '''public TextBuffer constructTextBuffer()
    '''
def allocReadIOBuffer():
    '''public byte[] allocReadIOBuffer()
    public byte[] allocReadIOBuffer(final int minSize)
    '''
def allocWriteEncodingBuffer():
    '''public byte[] allocWriteEncodingBuffer()
    public byte[] allocWriteEncodingBuffer(final int minSize)
    '''
def allocBase64Buffer():
    '''public byte[] allocBase64Buffer()
    public byte[] allocBase64Buffer(final int minSize)
    '''
def allocTokenBuffer():
    '''public char[] allocTokenBuffer()
    public char[] allocTokenBuffer(final int minSize)
    '''
def allocConcatBuffer():
    '''public char[] allocConcatBuffer()
    '''
def allocNameCopyBuffer():
    '''public char[] allocNameCopyBuffer(final int minSize)
    '''
def releaseReadIOBuffer():
    '''public void releaseReadIOBuffer(final byte[] buf)
    '''
def releaseWriteEncodingBuffer():
    '''public void releaseWriteEncodingBuffer(final byte[] buf)
    '''
def releaseBase64Buffer():
    '''public void releaseBase64Buffer(final byte[] buf)
    '''
def releaseTokenBuffer():
    '''public void releaseTokenBuffer(final char[] buf)
    '''
def releaseConcatBuffer():
    '''public void releaseConcatBuffer(final char[] buf)
    '''
def releaseNameCopyBuffer():
    '''public void releaseNameCopyBuffer(final char[] buf)
    '''
