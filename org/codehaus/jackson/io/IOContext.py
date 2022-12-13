def IOContext():
    '''public IOContext(final BufferRecycler br, final Object sourceRef, final boolean managedResource)
    '''
def setEncoding():
    '''public void setEncoding(final JsonEncoding enc)
    '''
def getSourceReference():
    '''public final Object getSourceReference()
    '''
def getEncoding():
    '''public final JsonEncoding getEncoding()
    '''
def isResourceManaged():
    '''public final boolean isResourceManaged()
    '''
def constructTextBuffer():
    '''public final TextBuffer constructTextBuffer()
    '''
def allocReadIOBuffer():
    '''public final byte[] allocReadIOBuffer()
    '''
def allocWriteEncodingBuffer():
    '''public final byte[] allocWriteEncodingBuffer()
    '''
def allocTokenBuffer():
    '''public final char[] allocTokenBuffer()
    '''
def allocConcatBuffer():
    '''public final char[] allocConcatBuffer()
    '''
def allocNameCopyBuffer():
    '''public final char[] allocNameCopyBuffer(final int minSize)
    '''
def releaseReadIOBuffer():
    '''public final void releaseReadIOBuffer(final byte[] buf)
    '''
def releaseWriteEncodingBuffer():
    '''public final void releaseWriteEncodingBuffer(final byte[] buf)
    '''
def releaseTokenBuffer():
    '''public final void releaseTokenBuffer(final char[] buf)
    '''
def releaseConcatBuffer():
    '''public final void releaseConcatBuffer(final char[] buf)
    '''
def releaseNameCopyBuffer():
    '''public final void releaseNameCopyBuffer(final char[] buf)
    '''
