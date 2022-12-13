__PUT = "String  \"PUT\""
__DELETE = "String  \"DELETE\""
__MOVE = "String  \"MOVE\""
__OPTIONS = "String  \"OPTIONS\""
def PutFilter():
    '''public PutFilter()
    '''
def init():
    '''public void init(final FilterConfig config)
    '''
def doFilter():
    '''public void doFilter(final ServletRequest req, final ServletResponse res, final FilterChain chain)
    '''
def destroy():
    '''public void destroy()
    '''
def handlePut():
    '''public void handlePut(final HttpServletRequest request, final HttpServletResponse response, final String pathInContext, final File file)
    '''
def handleDelete():
    '''public void handleDelete(final HttpServletRequest request, final HttpServletResponse response, final String pathInContext, final File file)
    '''
def handleMove():
    '''public void handleMove(final HttpServletRequest request, final HttpServletResponse response, final String pathInContext, final File file)
    '''
def handleOptions():
    '''public void handleOptions(final FilterChain chain, final HttpServletRequest request, final HttpServletResponse response)
    '''
def setHeader():
    '''public void setHeader(final String name, String value)
    '''
