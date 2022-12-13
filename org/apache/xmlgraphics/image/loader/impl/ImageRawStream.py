def ImageRawStream():
'''public ImageRawStream(final ImageInfo info, final ImageFlavor flavor, final InputStreamFactory streamFactory)
public ImageRawStream(final ImageInfo info, final ImageFlavor flavor, final InputStream in)
'''
pass
def getFlavor():
'''public ImageFlavor getFlavor()
'''
pass
def getMimeType():
'''public String getMimeType()
'''
pass
def isCacheable():
'''public boolean isCacheable()
'''
pass
def setInputStreamFactory():
'''public void setInputStreamFactory(final InputStreamFactory factory)
'''
pass
def createInputStream():
'''public InputStream createInputStream()
public synchronized InputStream createInputStream()
public InputStream createInputStream()
'''
pass
def writeTo():
'''public void writeTo(final OutputStream out)
'''
pass
def SingleStreamFactory():
'''public SingleStreamFactory(final InputStream in)
'''
pass
def close():
'''public synchronized void close()
public void close()
'''
pass
def isUsedOnceOnly():
'''public boolean isUsedOnceOnly()
public boolean isUsedOnceOnly()
'''
pass
def ByteArrayStreamFactory():
'''public ByteArrayStreamFactory(final byte[] data)
'''
pass
