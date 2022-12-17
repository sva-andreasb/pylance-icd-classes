REQUEST = "String  \"HTTP request\""
RESPONSE = "String  \"HTTP response\""
STATUS_CODE = "String  \"HTTP status\""
ACCEPT_ENCODING = "String  \"Accept-Encoding\""
CONTENT_ENCODING = "String  \"Content-Encoding\""
CONTENT_LENGTH = "String  \"Content-Length\""
CONTENT_TYPE = "String  \"Content-Type\""
DEFAULT_CHARSET = "String  \"ISO-8859-1\""
def ():
    '''returns HttpMessage\n\n
    ()\n
    (final String method, final URL url)\n
    (final String method, final URL url, final InputStream body)\n
    '''
def removeHeaders():
    '''returns String\n\n
    removeHeaders(final String name)\n
    '''
def dump():
    '''returns None\n\n
    dump(final Map<String, Object> into)\n
    '''
