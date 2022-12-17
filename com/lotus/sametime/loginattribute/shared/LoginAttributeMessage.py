LOGIN_PUBLISH_ATTRIBUTE_REQUEST = "short  0"
LOGIN_REMOVE_ATTRIBUTE_REQUEST = "short  1"
LOGIN_PUBLISH_ATTRIBUTE_RESPONSE = "short  Short.MIN_VALUE"
LOGIN_REMOVE_ATTRIBUTE_RESPONSE = "short  -32767"
def ():
    '''returns LoginAttributeMessage\n\n
    (final short msgType, final int requestId, final int attributeId, final byte[] value)\n
    (final short msgType, final int requestId, final int status)\n
    (final short n, final NdrInputStream ndrInputStream)\n
    '''
def setResponseInfo():
    '''returns None\n\n
    setResponseInfo(final NdrOutputStream ndrOutputStream)\n
    '''
def getMsgType():
    '''returns short\n\n
    getMsgType()\n
    '''
def setRequestInfo():
    '''returns None\n\n
    setRequestInfo(final NdrOutputStream ndrOutputStream)\n
    '''
def getStatus():
    '''returns int\n\n
    getStatus()\n
    '''
def getRequestId():
    '''returns int\n\n
    getRequestId()\n
    '''
def getAttributeId():
    '''returns int\n\n
    getAttributeId()\n
    '''
def getValue():
    '''returns byte[]\n\n
    getValue()\n
    '''
