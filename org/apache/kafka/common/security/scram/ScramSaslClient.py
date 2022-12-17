def ():
    '''returns ScramSaslClient\n\n
    (final ScramMechanism mechanism, final CallbackHandler cbh)\n
    '''
def getMechanismName():
    '''returns String\n\n
    getMechanismName()\n
    '''
def hasInitialResponse():
    '''returns boolean\n\n
    hasInitialResponse()\n
    '''
def evaluateChallenge():
    '''returns byte[]\n\n
    evaluateChallenge(final byte[] challenge)\n
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
def getNegotiatedProperty():
    '''returns Object\n\n
    getNegotiatedProperty(final String propName)\n
    '''
def dispose():
    '''returns None\n\n
    dispose()\n
    '''
def createSaslClient():
    '''returns SaslClient\n\n
    createSaslClient(final String[] mechanisms, final String authorizationId, final String protocol, final String serverName, final Map<String, ?> props, final CallbackHandler cbh)\n
    '''
def getMechanismNames():
    '''returns String[]\n\n
    getMechanismNames(final Map<String, ?> props)\n
    '''
