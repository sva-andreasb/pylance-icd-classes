def CookieSpecBase():
    '''    public CookieSpecBase()
    '''
def parse():
    '''    public Cookie[] parse(String host, final int port, String path, final boolean secure, final String header)
    public Cookie[] parse(final String host, final int port, final String path, final boolean secure, final Header header)
    '''
def parseAttribute():
    '''    public void parseAttribute(final NameValuePair attribute, final Cookie cookie)
    '''
def getValidDateFormats():
    '''    public Collection getValidDateFormats()
    '''
def setValidDateFormats():
    '''    public void setValidDateFormats(final Collection datepatterns)
    '''
def validate():
    '''    public void validate(String host, final int port, String path, final boolean secure, final Cookie cookie)
    '''
def match():
    '''    public boolean match(String host, final int port, String path, final boolean secure, final Cookie cookie)
    public Cookie[] match(final String host, final int port, final String path, final boolean secure, final Cookie[] cookies)
    '''
def domainMatch():
    '''    public boolean domainMatch(final String host, String domain)
    '''
def pathMatch():
    '''    public boolean pathMatch(final String path, final String topmostPath)
    '''
def formatCookie():
    '''    public String formatCookie(final Cookie cookie)
    '''
def formatCookies():
    '''    public String formatCookies(final Cookie[] cookies)
    '''
def formatCookieHeader():
    '''    public Header formatCookieHeader(final Cookie[] cookies)
    public Header formatCookieHeader(final Cookie cookie)
    '''
