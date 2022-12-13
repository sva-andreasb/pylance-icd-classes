def ScramSaslClient():
    '''    public ScramSaslClient(final ScramMechanism mechanism, final CallbackHandler cbh)
    '''
def getMechanismName():
    '''    public String getMechanismName()
    '''
def hasInitialResponse():
    '''    public boolean hasInitialResponse()
    '''
def evaluateChallenge():
    '''    public byte[] evaluateChallenge(final byte[] challenge)
    '''
def isComplete():
    '''    public boolean isComplete()
    '''
def unwrap():
    '''    public byte[] unwrap(final byte[] incoming, final int offset, final int len)
    '''
def wrap():
    '''    public byte[] wrap(final byte[] outgoing, final int offset, final int len)
    '''
def getNegotiatedProperty():
    '''    public Object getNegotiatedProperty(final String propName)
    '''
def dispose():
    '''    public void dispose()
    '''
def createSaslClient():
    '''    public SaslClient createSaslClient(final String[] mechanisms, final String authorizationId, final String protocol, final String serverName, final Map<String, ?> props, final CallbackHandler cbh)
    '''
def getMechanismNames():
    '''    public String[] getMechanismNames(final Map<String, ?> props)
    '''
