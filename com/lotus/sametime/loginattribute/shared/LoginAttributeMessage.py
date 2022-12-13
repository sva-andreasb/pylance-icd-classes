LOGIN_PUBLISH_ATTRIBUTE_REQUEST = "short  0"
LOGIN_REMOVE_ATTRIBUTE_REQUEST = "short  1"
LOGIN_PUBLISH_ATTRIBUTE_RESPONSE = "short  Short.MIN_VALUE"
LOGIN_REMOVE_ATTRIBUTE_RESPONSE = "short  -32767"
def LoginAttributeMessage():
    '''public LoginAttributeMessage(final short msgType, final int requestId, final int attributeId, final byte[] value)
    public LoginAttributeMessage(final short msgType, final int requestId, final int status)
    public LoginAttributeMessage(final short n, final NdrInputStream ndrInputStream)
    '''
def setResponseInfo():
    '''public void setResponseInfo(final NdrOutputStream ndrOutputStream)
    '''
def getMsgType():
    '''public short getMsgType()
    '''
def setRequestInfo():
    '''public void setRequestInfo(final NdrOutputStream ndrOutputStream)
    '''
def getStatus():
    '''public int getStatus()
    '''
def getRequestId():
    '''public int getRequestId()
    '''
def getAttributeId():
    '''public int getAttributeId()
    '''
def getValue():
    '''public byte[] getValue()
    '''
