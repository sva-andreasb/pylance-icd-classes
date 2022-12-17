def ():
    '''returns CacheProxyResponse\n\n
    (final HttpServletResponse proxiedResponse)\n
    '''
def finished():
    '''returns None\n\n
    finished()\n
    '''
def getHeaderTable():
    '''returns Vector[]\n\n
    getHeaderTable()\n
    '''
def setFragmentComposer():
    '''returns None\n\n
    setFragmentComposer(final FragmentComposer fragmentComposer)\n
    '''
def getFragmentComposer():
    '''returns FragmentComposer\n\n
    getFragmentComposer()\n
    '''
def setComposerActive():
    '''returns None\n\n
    setComposerActive(final boolean active)\n
    '''
def getComposerActive():
    '''returns boolean\n\n
    getComposerActive()\n
    '''
def flushBuffer():
    '''returns None\n\n
    flushBuffer()\n
    flushBuffer(final boolean flushToWire)\n
    '''
def isCommitted():
    '''returns boolean\n\n
    isCommitted()\n
    '''
def getOutputStream():
    '''returns ServletOutputStream\n\n
    getOutputStream()\n
    '''
def getWriter():
    '''returns PrintWriter\n\n
    getWriter()\n
    '''
def getBufferedOutputStream():
    '''returns ServletOutputStream\n\n
    getBufferedOutputStream()\n
    '''
def getBufferedWriter():
    '''returns PrintWriter\n\n
    getBufferedWriter()\n
    '''
def resetBuffer():
    '''returns None\n\n
    resetBuffer()\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def getContainsESIContent():
    '''returns boolean\n\n
    getContainsESIContent()\n
    '''
def setContainsESIContent():
    '''returns None\n\n
    setContainsESIContent(final boolean b)\n
    '''
def setBufferSize():
    '''returns None\n\n
    setBufferSize(final int size)\n
    '''
def getBufferSize():
    '''returns int\n\n
    getBufferSize()\n
    '''
def _include():
    '''returns None\n\n
    _include(final String template, final HttpServletRequest request)\n
    '''
def _forward():
    '''returns None\n\n
    _forward(final String template, final HttpServletRequest request)\n
    '''
def callPage():
    '''returns None\n\n
    callPage(final String fileName, final HttpServletRequest hreq)\n
    '''
def setHeader():
    '''returns None\n\n
    setHeader(final String key, final String value)\n
    '''
def addHeader():
    '''returns None\n\n
    addHeader(final String key, final String value)\n
    '''
def addCookie():
    '''returns None\n\n
    addCookie(final Cookie cookie)\n
    '''
def addDynamicContentProvider():
    '''returns None\n\n
    addDynamicContentProvider(final DynamicContentProvider dynamicContentProvider)\n
    '''
def setDateHeader():
    '''returns None\n\n
    setDateHeader(final String name, final long value)\n
    '''
def addDateHeader():
    '''returns None\n\n
    addDateHeader(final String name, final long value)\n
    '''
def setIntHeader():
    '''returns None\n\n
    setIntHeader(final String name, final int value)\n
    '''
def addIntHeader():
    '''returns None\n\n
    addIntHeader(final String name, final int value)\n
    '''
def setStatus():
    '''returns None\n\n
    setStatus(final int statusCode)\n
    setStatus(final int statusCode, final String comment)\n
    '''
def sendError():
    '''returns None\n\n
    sendError(final int statusCode)\n
    sendError(final int statusCode, final String comment)\n
    '''
def setContentLength():
    '''returns None\n\n
    setContentLength(final int contentLength)\n
    '''
def setCharacterEncoding():
    '''returns None\n\n
    setCharacterEncoding(final String charEnc)\n
    '''
def setContentType():
    '''returns None\n\n
    setContentType(final String contentType)\n
    '''
def setLocale():
    '''returns None\n\n
    setLocale(final Locale locale)\n
    '''
def sendRedirect():
    '''returns None\n\n
    sendRedirect(final String location)\n
    '''
def setDoNotConsume():
    '''returns None\n\n
    setDoNotConsume(final boolean doNotConsume)\n
    '''
def writerObtained():
    '''returns boolean\n\n
    writerObtained()\n
    '''
def outputStreamObtained():
    '''returns boolean\n\n
    outputStreamObtained()\n
    '''
def setArd():
    '''returns None\n\n
    setArd(final boolean a)\n
    '''
