DEFAULT_WAIT_FOR_CONTINUE = "int  3000"
def ():
    '''returns HttpRequestExecutor\n\n
    (final int waitForContinue)\n
    ()\n
    '''
def execute():
    '''returns HttpResponse\n\n
    execute(final HttpRequest request, final HttpClientConnection conn, final HttpContext context)\n
    '''
def preProcess():
    '''returns None\n\n
    preProcess(final HttpRequest request, final HttpProcessor processor, final HttpContext context)\n
    '''
def postProcess():
    '''returns None\n\n
    postProcess(final HttpResponse response, final HttpProcessor processor, final HttpContext context)\n
    '''
