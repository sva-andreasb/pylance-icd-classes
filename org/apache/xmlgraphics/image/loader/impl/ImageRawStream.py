def ImageRawStream():
    '''    public ImageRawStream(final ImageInfo info, final ImageFlavor flavor, final InputStreamFactory streamFactory)
    public ImageRawStream(final ImageInfo info, final ImageFlavor flavor, final InputStream in)
    '''
def getFlavor():
    '''    public ImageFlavor getFlavor()
    '''
def getMimeType():
    '''    public String getMimeType()
    '''
def isCacheable():
    '''    public boolean isCacheable()
    '''
def setInputStreamFactory():
    '''    public void setInputStreamFactory(final InputStreamFactory factory)
    '''
def createInputStream():
    '''    public InputStream createInputStream()
    public synchronized InputStream createInputStream()
    public InputStream createInputStream()
    '''
def writeTo():
    '''    public void writeTo(final OutputStream out)
    '''
def SingleStreamFactory():
    '''    public SingleStreamFactory(final InputStream in)
    '''
def close():
    '''    public synchronized void close()
    public void close()
    '''
def isUsedOnceOnly():
    '''    public boolean isUsedOnceOnly()
    public boolean isUsedOnceOnly()
    '''
def ByteArrayStreamFactory():
    '''    public ByteArrayStreamFactory(final byte[] data)
    '''
