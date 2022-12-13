DEFAULT_BUFFER_SIZE = "int  8192"
DEFAULT_MIN_GZIP_SIZE = "int  256"
def GzipResponseWrapper():
    '''    public GzipResponseWrapper(final HttpServletRequest request, final HttpServletResponse response)
    '''
def setMimeTypes():
    '''    public void setMimeTypes(final Set<String> mimeTypes)
    '''
def setBufferSize():
    '''    public void setBufferSize(final int bufferSize)
    '''
def setMinGzipSize():
    '''    public void setMinGzipSize(final int minGzipSize)
    '''
def setContentType():
    '''    public void setContentType(String ct)
    '''
def setStatus():
    '''    public void setStatus(final int sc, final String sm)
    public void setStatus(final int sc)
    '''
def setContentLength():
    '''    public void setContentLength(final int length)
    '''
def addHeader():
    '''    public void addHeader(final String name, final String value)
    '''
def setHeader():
    '''    public void setHeader(final String name, final String value)
    '''
def setIntHeader():
    '''    public void setIntHeader(final String name, final int value)
    '''
def flushBuffer():
    '''    public void flushBuffer()
    '''
def reset():
    '''    public void reset()
    '''
def resetBuffer():
    '''    public void resetBuffer()
    '''
def sendError():
    '''    public void sendError(final int sc, final String msg)
    public void sendError(final int sc)
    '''
def sendRedirect():
    '''    public void sendRedirect(final String location)
    '''
def getOutputStream():
    '''    public ServletOutputStream getOutputStream()
    '''
def getWriter():
    '''    public PrintWriter getWriter()
    '''
def noGzip():
    '''    public void noGzip()
    '''
def finish():
    '''    public void finish()
    '''
