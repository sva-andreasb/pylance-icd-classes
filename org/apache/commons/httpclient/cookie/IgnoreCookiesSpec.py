def parse():
    '''public Cookie[] parse(final String host, final int port, final String path, final boolean secure, final String header)
    public Cookie[] parse(final String host, final int port, final String path, final boolean secure, final Header header)
    '''
def getValidDateFormats():
    '''public Collection getValidDateFormats()
    '''
def setValidDateFormats():
    '''public void setValidDateFormats(final Collection datepatterns)
    '''
def formatCookie():
    '''public String formatCookie(final Cookie cookie)
    '''
def formatCookieHeader():
    '''public Header formatCookieHeader(final Cookie cookie)
    public Header formatCookieHeader(final Cookie[] cookies)
    '''
def formatCookies():
    '''public String formatCookies(final Cookie[] cookies)
    '''
def match():
    '''public boolean match(final String host, final int port, final String path, final boolean secure, final Cookie cookie)
    public Cookie[] match(final String host, final int port, final String path, final boolean secure, final Cookie[] cookies)
    '''
def parseAttribute():
    '''public void parseAttribute(final NameValuePair attribute, final Cookie cookie)
    '''
def validate():
    '''public void validate(final String host, final int port, final String path, final boolean secure, final Cookie cookie)
    '''
def domainMatch():
    '''public boolean domainMatch(final String host, final String domain)
    '''
def pathMatch():
    '''public boolean pathMatch(final String path, final String topmostPath)
    '''
