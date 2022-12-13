FORM_ENCODED = "String  \"application/x-www-form-urlencoded\""
MESSAGE_HTTP = "String  \"message/http\""
MULTIPART_BYTERANGES = "String  \"multipart/byteranges\""
TEXT_HTML = "String  \"text/html\""
TEXT_PLAIN = "String  \"text/plain\""
TEXT_XML = "String  \"text/xml\""
TEXT_JSON = "String  \"text/json\""
TEXT_HTML_8859_1 = "String  \"text/html;charset=ISO-8859-1\""
TEXT_PLAIN_8859_1 = "String  \"text/plain;charset=ISO-8859-1\""
TEXT_XML_8859_1 = "String  \"text/xml;charset=ISO-8859-1\""
TEXT_HTML_UTF_8 = "String  \"text/html;charset=UTF-8\""
TEXT_PLAIN_UTF_8 = "String  \"text/plain;charset=UTF-8\""
TEXT_XML_UTF_8 = "String  \"text/xml;charset=UTF-8\""
TEXT_JSON_UTF_8 = "String  \"text/json;charset=UTF-8\""
def getMimeMap():
    '''    public synchronized Map getMimeMap()
    '''
def setMimeMap():
    '''    public void setMimeMap(final Map mimeMap)
    '''
def getMimeByExtension():
    '''    public Buffer getMimeByExtension(final String filename)
    '''
def addMimeMapping():
    '''    public void addMimeMapping(final String extension, final String type)
    '''
def getCharsetFromContentType():
    '''    public static String getCharsetFromContentType(final Buffer value)
    '''
