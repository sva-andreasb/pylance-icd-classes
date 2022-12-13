DEFAULT_BUFFER_SIZE = "int  8192"
DEFAULT_MIN_GZIP_SIZE = "int  256"
def GzipResponseWrapper():
'''public GzipResponseWrapper(final HttpServletRequest request, final HttpServletResponse response)
'''
pass
def setMimeTypes():
'''public void setMimeTypes(final Set<String> mimeTypes)
'''
pass
def setBufferSize():
'''public void setBufferSize(final int bufferSize)
'''
pass
def setMinGzipSize():
'''public void setMinGzipSize(final int minGzipSize)
'''
pass
def setContentType():
'''public void setContentType(String ct)
'''
pass
def setStatus():
'''public void setStatus(final int sc, final String sm)
public void setStatus(final int sc)
'''
pass
def setContentLength():
'''public void setContentLength(final int length)
'''
pass
def addHeader():
'''public void addHeader(final String name, final String value)
'''
pass
def setHeader():
'''public void setHeader(final String name, final String value)
'''
pass
def setIntHeader():
'''public void setIntHeader(final String name, final int value)
'''
pass
def flushBuffer():
'''public void flushBuffer()
'''
pass
def reset():
'''public void reset()
'''
pass
def resetBuffer():
'''public void resetBuffer()
'''
pass
def sendError():
'''public void sendError(final int sc, final String msg)
public void sendError(final int sc)
'''
pass
def sendRedirect():
'''public void sendRedirect(final String location)
'''
pass
def getOutputStream():
'''public ServletOutputStream getOutputStream()
'''
pass
def getWriter():
'''public PrintWriter getWriter()
'''
pass
def noGzip():
'''public void noGzip()
'''
pass
def finish():
'''public void finish()
'''
pass
