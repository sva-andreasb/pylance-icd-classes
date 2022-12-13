SET_COOKIE2_KEY = "String  \"set-cookie2\""
def RFC2965Spec():
    '''    public RFC2965Spec()
    '''
def parse():
    '''    public Cookie[] parse(final String host, final int port, final String path, final boolean secure, final Header header)
    public Cookie[] parse(String host, final int port, String path, final boolean secure, final String header)
    public void parse(final Cookie cookie, final String path)
    public void parse(final Cookie cookie, String domain)
    public void parse(final Cookie cookie, final String portValue)
    public void parse(final Cookie cookie, final String value)
    public void parse(final Cookie cookie, final String secure)
    public void parse(final Cookie cookie, final String comment)
    public void parse(final Cookie cookie, final String commenturl)
    public void parse(final Cookie cookie, final String commenturl)
    public void parse(final Cookie cookie, final String value)
    '''
def parseAttribute():
    '''    public void parseAttribute(final NameValuePair attribute, final Cookie cookie)
    '''
def validate():
    '''    public void validate(final String host, final int port, final String path, final boolean secure, final Cookie cookie)
    public void validate(final Cookie cookie, final CookieOrigin origin)
    public void validate(final Cookie cookie, final CookieOrigin origin)
    public void validate(final Cookie cookie, final CookieOrigin origin)
    public void validate(final Cookie cookie, final CookieOrigin origin)
    public void validate(final Cookie cookie, final CookieOrigin origin)
    public void validate(final Cookie cookie, final CookieOrigin origin)
    public void validate(final Cookie cookie, final CookieOrigin origin)
    public void validate(final Cookie cookie, final CookieOrigin origin)
    public void validate(final Cookie cookie, final CookieOrigin origin)
    '''
def match():
    '''    public boolean match(final String host, final int port, final String path, final boolean secure, final Cookie cookie)
    public boolean match(final Cookie cookie, final CookieOrigin origin)
    public boolean match(final Cookie cookie, final CookieOrigin origin)
    public boolean match(final Cookie cookie, final CookieOrigin origin)
    public boolean match(final Cookie cookie, final CookieOrigin origin)
    public boolean match(final Cookie cookie, final CookieOrigin origin)
    public boolean match(final Cookie cookie, final CookieOrigin origin)
    public boolean match(final Cookie cookie, final CookieOrigin origin)
    public boolean match(final Cookie cookie, final CookieOrigin origin)
    public boolean match(final Cookie cookie, final CookieOrigin origin)
    '''
def formatCookie():
    '''    public String formatCookie(final Cookie cookie)
    '''
def formatCookies():
    '''    public String formatCookies(final Cookie[] cookies)
    '''
def domainMatch():
    '''    public boolean domainMatch(final String host, final String domain)
    '''
def getVersion():
    '''    public int getVersion()
    '''
def getVersionHeader():
    '''    public Header getVersionHeader()
    '''
