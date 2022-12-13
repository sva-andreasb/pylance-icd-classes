CR = "byte  13"
LF = "byte  10"
DASH = "byte  45"
HEADER_PART_SIZE_MAX = "int  10240"
def MultipartStream():
'''public MultipartStream()
public MultipartStream(final InputStream input, final byte[] boundary, final int bufSize)
public MultipartStream(final InputStream input, final byte[] boundary, final int bufSize, final ProgressNotifier pNotifier)
public MultipartStream(final InputStream input, final byte[] boundary)
'''
pass
def getHeaderEncoding():
'''public String getHeaderEncoding()
'''
pass
def setHeaderEncoding():
'''public void setHeaderEncoding(final String encoding)
'''
pass
def readByte():
'''public byte readByte()
'''
pass
def readBoundary():
'''public boolean readBoundary()
'''
pass
def setBoundary():
'''public void setBoundary(final byte[] boundary)
'''
pass
def readHeaders():
'''public String readHeaders()
'''
pass
def readBodyData():
'''public int readBodyData(final OutputStream output)
'''
pass
def discardBodyData():
'''public int discardBodyData()
'''
pass
def skipPreamble():
'''public boolean skipPreamble()
'''
pass
def arrayequals():
'''public static boolean arrayequals(final byte[] a, final byte[] b, final int count)
'''
pass
def MalformedStreamException():
'''public MalformedStreamException()
public MalformedStreamException(final String message)
'''
pass
def IllegalBoundaryException():
'''public IllegalBoundaryException()
public IllegalBoundaryException(final String message)
'''
pass
def getBytesRead():
'''public long getBytesRead()
'''
pass
def available():
'''public int available()
'''
pass
def read():
'''public int read()
public int read(final byte[] b, final int off, final int len)
'''
pass
def close():
'''public void close()
public void close(final boolean pCloseUnderlying)
'''
pass
def skip():
'''public long skip(final long bytes)
'''
pass
def isClosed():
'''public boolean isClosed()
'''
pass
