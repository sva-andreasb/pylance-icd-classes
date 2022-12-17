DEFAULT_BUFFER_SIZE = "int  8192"
DEFAULT_MIN_GZIP_SIZE = "int  256"
def ():
    '''returns GzipResponseWrapper\n\n
    (final HttpServletRequest request, final HttpServletResponse response)\n
    '''
def setMimeTypes():
    '''returns None\n\n
    setMimeTypes(final Set<String> mimeTypes)\n
    '''
def setBufferSize():
    '''returns None\n\n
    setBufferSize(final int bufferSize)\n
    '''
def setMinGzipSize():
    '''returns None\n\n
    setMinGzipSize(final int minGzipSize)\n
    '''
def setContentType():
    '''returns None\n\n
    setContentType(String ct)\n
    '''
def setStatus():
    '''returns None\n\n
    setStatus(final int sc, final String sm)\n
    setStatus(final int sc)\n
    '''
def setContentLength():
    '''returns None\n\n
    setContentLength(final int length)\n
    '''
def addHeader():
    '''returns None\n\n
    addHeader(final String name, final String value)\n
    '''
def setHeader():
    '''returns None\n\n
    setHeader(final String name, final String value)\n
    '''
def setIntHeader():
    '''returns None\n\n
    setIntHeader(final String name, final int value)\n
    '''
def flushBuffer():
    '''returns None\n\n
    flushBuffer()\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def resetBuffer():
    '''returns None\n\n
    resetBuffer()\n
    '''
def sendError():
    '''returns None\n\n
    sendError(final int sc, final String msg)\n
    sendError(final int sc)\n
    '''
def sendRedirect():
    '''returns None\n\n
    sendRedirect(final String location)\n
    '''
def getOutputStream():
    '''returns ServletOutputStream\n\n
    getOutputStream()\n
    '''
def getWriter():
    '''returns PrintWriter\n\n
    getWriter()\n
    '''
def noGzip():
    '''returns None\n\n
    noGzip()\n
    '''
def finish():
    '''returns None\n\n
    finish()\n
    '''
