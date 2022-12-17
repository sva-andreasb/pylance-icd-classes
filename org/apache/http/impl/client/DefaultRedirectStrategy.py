REDIRECT_LOCATIONS = "String  \"http.protocol.redirect-locations\""
def ():
    '''returns DefaultRedirectStrategy\n\n
    ()\n
    '''
def isRedirected():
    '''returns boolean\n\n
    isRedirected(final HttpRequest request, final HttpResponse response, final HttpContext context)\n
    '''
def getLocationURI():
    '''returns URI\n\n
    getLocationURI(final HttpRequest request, final HttpResponse response, final HttpContext context)\n
    '''
def getRedirect():
    '''returns HttpUriRequest\n\n
    getRedirect(final HttpRequest request, final HttpResponse response, final HttpContext context)\n
    '''
