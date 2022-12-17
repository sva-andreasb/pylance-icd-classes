def ():
    '''returns IOContext\n\n
    (final BufferRecycler br, final Object sourceRef, final boolean managedResource)\n
    '''
def setEncoding():
    '''returns None\n\n
    setEncoding(final JsonEncoding enc)\n
    '''
def withEncoding():
    '''returns IOContext\n\n
    withEncoding(final JsonEncoding enc)\n
    '''
def getSourceReference():
    '''returns Object\n\n
    getSourceReference()\n
    '''
def getEncoding():
    '''returns JsonEncoding\n\n
    getEncoding()\n
    '''
def isResourceManaged():
    '''returns boolean\n\n
    isResourceManaged()\n
    '''
def constructTextBuffer():
    '''returns TextBuffer\n\n
    constructTextBuffer()\n
    '''
def allocReadIOBuffer():
    '''returns byte[]\n\n
    allocReadIOBuffer()\n
    allocReadIOBuffer(final int minSize)\n
    '''
def allocWriteEncodingBuffer():
    '''returns byte[]\n\n
    allocWriteEncodingBuffer()\n
    allocWriteEncodingBuffer(final int minSize)\n
    '''
def allocBase64Buffer():
    '''returns byte[]\n\n
    allocBase64Buffer()\n
    allocBase64Buffer(final int minSize)\n
    '''
def allocTokenBuffer():
    '''returns char[]\n\n
    allocTokenBuffer()\n
    allocTokenBuffer(final int minSize)\n
    '''
def allocConcatBuffer():
    '''returns char[]\n\n
    allocConcatBuffer()\n
    '''
def allocNameCopyBuffer():
    '''returns char[]\n\n
    allocNameCopyBuffer(final int minSize)\n
    '''
def releaseReadIOBuffer():
    '''returns None\n\n
    releaseReadIOBuffer(final byte[] buf)\n
    '''
def releaseWriteEncodingBuffer():
    '''returns None\n\n
    releaseWriteEncodingBuffer(final byte[] buf)\n
    '''
def releaseBase64Buffer():
    '''returns None\n\n
    releaseBase64Buffer(final byte[] buf)\n
    '''
def releaseTokenBuffer():
    '''returns None\n\n
    releaseTokenBuffer(final char[] buf)\n
    '''
def releaseConcatBuffer():
    '''returns None\n\n
    releaseConcatBuffer(final char[] buf)\n
    '''
def releaseNameCopyBuffer():
    '''returns None\n\n
    releaseNameCopyBuffer(final char[] buf)\n
    '''
