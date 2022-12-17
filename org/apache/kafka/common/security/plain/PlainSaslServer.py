PLAIN_MECHANISM = "String  \"PLAIN\""
def ():
    '''returns PlainSaslServer\n\n
    (final JaasContext jaasContext)\n
    '''
def evaluateResponse():
    '''returns byte[]\n\n
    evaluateResponse(final byte[] response)\n
    '''
def getAuthorizationID():
    '''returns String\n\n
    getAuthorizationID()\n
    '''
def getMechanismName():
    '''returns String\n\n
    getMechanismName()\n
    '''
def getNegotiatedProperty():
    '''returns Object\n\n
    getNegotiatedProperty(final String propName)\n
    '''
def isComplete():
    '''returns boolean\n\n
    isComplete()\n
    '''
def unwrap():
    '''returns byte[]\n\n
    unwrap(final byte[] incoming, final int offset, final int len)\n
    '''
def wrap():
    '''returns byte[]\n\n
    wrap(final byte[] outgoing, final int offset, final int len)\n
    '''
def dispose():
    '''returns None\n\n
    dispose()\n
    '''
def createSaslServer():
    '''returns SaslServer\n\n
    createSaslServer(final String mechanism, final String protocol, final String serverName, final Map<String, ?> props, final CallbackHandler cbh)\n
    '''
def getMechanismNames():
    '''returns String[]\n\n
    getMechanismNames(final Map<String, ?> props)\n
    '''
