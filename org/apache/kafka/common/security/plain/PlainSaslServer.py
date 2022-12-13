PLAIN_MECHANISM = "String  \"PLAIN\""
def PlainSaslServer():
    '''public PlainSaslServer(final JaasContext jaasContext)
    '''
def evaluateResponse():
    '''public byte[] evaluateResponse(final byte[] response)
    '''
def getAuthorizationID():
    '''public String getAuthorizationID()
    '''
def getMechanismName():
    '''public String getMechanismName()
    '''
def getNegotiatedProperty():
    '''public Object getNegotiatedProperty(final String propName)
    '''
def isComplete():
    '''public boolean isComplete()
    '''
def unwrap():
    '''public byte[] unwrap(final byte[] incoming, final int offset, final int len)
    '''
def wrap():
    '''public byte[] wrap(final byte[] outgoing, final int offset, final int len)
    '''
def dispose():
    '''public void dispose()
    '''
def createSaslServer():
    '''public SaslServer createSaslServer(final String mechanism, final String protocol, final String serverName, final Map<String, ?> props, final CallbackHandler cbh)
    '''
def getMechanismNames():
    '''public String[] getMechanismNames(final Map<String, ?> props)
    '''
