def ScramSaslClient():
'''public ScramSaslClient(final ScramMechanism mechanism, final CallbackHandler cbh)
'''
pass
def getMechanismName():
'''public String getMechanismName()
'''
pass
def hasInitialResponse():
'''public boolean hasInitialResponse()
'''
pass
def evaluateChallenge():
'''public byte[] evaluateChallenge(final byte[] challenge)
'''
pass
def isComplete():
'''public boolean isComplete()
'''
pass
def unwrap():
'''public byte[] unwrap(final byte[] incoming, final int offset, final int len)
'''
pass
def wrap():
'''public byte[] wrap(final byte[] outgoing, final int offset, final int len)
'''
pass
def getNegotiatedProperty():
'''public Object getNegotiatedProperty(final String propName)
'''
pass
def dispose():
'''public void dispose()
'''
pass
def createSaslClient():
'''public SaslClient createSaslClient(final String[] mechanisms, final String authorizationId, final String protocol, final String serverName, final Map<String, ?> props, final CallbackHandler cbh)
'''
pass
def getMechanismNames():
'''public String[] getMechanismNames(final Map<String, ?> props)
'''
pass
