__PUT = "String  \"PUT\""
__DELETE = "String  \"DELETE\""
__MOVE = "String  \"MOVE\""
__OPTIONS = "String  \"OPTIONS\""
def ():
    '''returns PutFilter\n\n
    ()\n
    '''
def init():
    '''returns None\n\n
    init(final FilterConfig config)\n
    '''
def doFilter():
    '''returns None\n\n
    doFilter(final ServletRequest req, final ServletResponse res, final FilterChain chain)\n
    '''
def destroy():
    '''returns None\n\n
    destroy()\n
    '''
def handlePut():
    '''returns None\n\n
    handlePut(final HttpServletRequest request, final HttpServletResponse response, final String pathInContext, final File file)\n
    '''
def handleDelete():
    '''returns None\n\n
    handleDelete(final HttpServletRequest request, final HttpServletResponse response, final String pathInContext, final File file)\n
    '''
def handleMove():
    '''returns None\n\n
    handleMove(final HttpServletRequest request, final HttpServletResponse response, final String pathInContext, final File file)\n
    '''
def handleOptions():
    '''returns None\n\n
    handleOptions(final FilterChain chain, final HttpServletRequest request, final HttpServletResponse response)\n
    '''
def setHeader():
    '''returns None\n\n
    setHeader(final String name, String value)\n
    '''
