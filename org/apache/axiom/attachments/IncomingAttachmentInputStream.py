HEADER_CONTENT_DESCRIPTION = "String  \"content-description\""
HEADER_CONTENT_TYPE = "String  \"content-type\""
HEADER_CONTENT_TRANSFER_ENCODING = "String  \"content-transfer-encoding\""
HEADER_CONTENT_TYPE_JMS = "String  \"contentType\""
HEADER_CONTENT_LENGTH = "String  \"content-length\""
HEADER_CONTENT_LOCATION = "String  \"content-location\""
HEADER_CONTENT_ID = "String  \"content-id\""
def ():
    '''returns IncomingAttachmentInputStream\n\n
    (final InputStream in, final IncomingAttachmentStreams parentContainer)\n
    '''
def getHeaders():
    '''returns Map\n\n
    getHeaders()\n
    '''
def addHeader():
    '''returns None\n\n
    addHeader(final String name, final String value)\n
    '''
def getHeader():
    '''returns String\n\n
    getHeader(final String name)\n
    '''
def getContentId():
    '''returns String\n\n
    getContentId()\n
    '''
def getContentLocation():
    '''returns String\n\n
    getContentLocation()\n
    '''
def getContentType():
    '''returns String\n\n
    getContentType()\n
    '''
def markSupported():
    '''returns boolean\n\n
    markSupported()\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def mark():
    '''returns None\n\n
    mark(final int readLimit)\n
    '''
def read():
    '''returns int\n\n
    read()\n
    read(final byte[] b)\n
    read(final byte[] b, final int off, final int len)\n
    '''
