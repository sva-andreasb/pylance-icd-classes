def IOContext():
'''public IOContext(final BufferRecycler br, final Object sourceRef, final boolean managedResource)
'''
pass
def setEncoding():
'''public void setEncoding(final JsonEncoding enc)
'''
pass
def withEncoding():
'''public IOContext withEncoding(final JsonEncoding enc)
'''
pass
def getSourceReference():
'''public Object getSourceReference()
'''
pass
def getEncoding():
'''public JsonEncoding getEncoding()
'''
pass
def isResourceManaged():
'''public boolean isResourceManaged()
'''
pass
def constructTextBuffer():
'''public TextBuffer constructTextBuffer()
'''
pass
def allocReadIOBuffer():
'''public byte[] allocReadIOBuffer()
public byte[] allocReadIOBuffer(final int minSize)
'''
pass
def allocWriteEncodingBuffer():
'''public byte[] allocWriteEncodingBuffer()
public byte[] allocWriteEncodingBuffer(final int minSize)
'''
pass
def allocBase64Buffer():
'''public byte[] allocBase64Buffer()
public byte[] allocBase64Buffer(final int minSize)
'''
pass
def allocTokenBuffer():
'''public char[] allocTokenBuffer()
public char[] allocTokenBuffer(final int minSize)
'''
pass
def allocConcatBuffer():
'''public char[] allocConcatBuffer()
'''
pass
def allocNameCopyBuffer():
'''public char[] allocNameCopyBuffer(final int minSize)
'''
pass
def releaseReadIOBuffer():
'''public void releaseReadIOBuffer(final byte[] buf)
'''
pass
def releaseWriteEncodingBuffer():
'''public void releaseWriteEncodingBuffer(final byte[] buf)
'''
pass
def releaseBase64Buffer():
'''public void releaseBase64Buffer(final byte[] buf)
'''
pass
def releaseTokenBuffer():
'''public void releaseTokenBuffer(final char[] buf)
'''
pass
def releaseConcatBuffer():
'''public void releaseConcatBuffer(final char[] buf)
'''
pass
def releaseNameCopyBuffer():
'''public void releaseNameCopyBuffer(final char[] buf)
'''
pass
