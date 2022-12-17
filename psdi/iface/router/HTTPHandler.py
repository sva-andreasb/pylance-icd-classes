HTTPMETHOD_GET = "String  \"GET\""
HTTPMETHOD_HEAD = "String  \"HEAD\""
HTTPMETHOD_POST = "String  \"POST\""
HTTPMETHOD_PATCH = "String  \"PATCH\""
HTTPMETHOD_PUT = "String  \"PUT\""
HTTPMETHOD_DELETE = "String  \"DELETE\""
RESPONSE_HEADERS = "String  \"RESPONSE_HEADERS\""
HTTPGET_URLPROPS = "String  \"GETURLPROPS\""
HTTP_HEADERPROPS = "String  \"HEADERPROPS\""
HTTP_REQUEST_COOKIES = "String  \"REQUEST_COOKIES\""
HTTP_ETAG = "String  \"Etag\""
HTTPEXIT = "String  \"HTTPEXIT\""
HTTPMETHOD = "String  \"HTTPMETHOD\""
HEADERS = "String  \"HEADERS\""
COOKIES = "String  \"COOKIES\""
URL = "String  \"URL\""
CONNECTTIMEOUT = "String  \"CONNECTTIMEOUT\""
READTIMEOUT = "String  \"READTIMEOUT\""
ERRORONSTATUS = "String  \"ERRORONSTATUS\""
ALLRESPONSEHEADERS = "String  \"ALLRESPONSEHEADERS\""
RESPONSE_STATUS = "String  \"RESPONSE_STATUS\""
RESPONSE_STATUS_TEXT = "String  \"RESPONSE_STATUS_TEXT\""
FIREANDFORGET = "String  \"FIREANDFORGET\""
def ():
    '''returns HTTPHandler\n\n
    (final MaxEndPointInfo endPointInfo)\n
    ()\n
    '''
def invoke():
    '''returns byte[]\n\n
    invoke(final Map metaData, byte[] data)\n
    '''
def getProperties():
    '''returns List<RouterPropsInfo>\n\n
    getProperties()\n
    '''
def getReadTimeout():
    '''returns int\n\n
    getReadTimeout()\n
    '''
def getConnectTimeout():
    '''returns int\n\n
    getConnectTimeout()\n
    '''
def getHttpExitName():
    '''returns String\n\n
    getHttpExitName()\n
    '''
def getUrl():
    '''returns String\n\n
    getUrl()\n
    '''
def getUserName():
    '''returns String\n\n
    getUserName()\n
    '''
def getHttpMethod():
    '''returns String\n\n
    getHttpMethod()\n
    '''
