def getMimeType():
    '''    public String getMimeType()
    '''
def getCharset():
    '''    public Charset getCharset()
    '''
def getParameter():
    '''    public String getParameter(final String name)
    '''
def toString():
    '''    public String toString()
    '''
def create():
    '''    public static ContentType create(final String mimeType, final Charset charset)
    public static ContentType create(final String mimeType)
    public static ContentType create(final String mimeType, final String charset)
    public static ContentType create(final String mimeType, final NameValuePair... params)
    '''
def parse():
    '''    public static ContentType parse(final String s)
    '''
def get():
    '''    public static ContentType get(final HttpEntity entity)
    '''
def getLenient():
    '''    public static ContentType getLenient(final HttpEntity entity)
    '''
def getOrDefault():
    '''    public static ContentType getOrDefault(final HttpEntity entity)
    '''
def getLenientOrDefault():
    '''    public static ContentType getLenientOrDefault(final HttpEntity entity)
    '''
def withCharset():
    '''    public ContentType withCharset(final Charset charset)
    public ContentType withCharset(final String charset)
    '''
def withParameters():
    '''    public ContentType withParameters(final NameValuePair... params)
    '''
