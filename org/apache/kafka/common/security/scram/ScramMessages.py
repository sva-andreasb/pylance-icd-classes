def toBytes():
    '''returns byte[]\n\n
    toBytes()\n
    '''
def ():
    '''returns ServerFinalMessage\n\n
    (final byte[] messageBytes)\n
    (final String saslName, final String nonce, final Map<String, String> extensions)\n
    (final byte[] messageBytes)\n
    (final String clientNonce, final String serverNonce, final byte[] salt, final int iterations)\n
    (final byte[] messageBytes)\n
    (final byte[] channelBinding, final String nonce)\n
    (final byte[] messageBytes)\n
    (final String error, final byte[] serverSignature)\n
    '''
def saslName():
    '''returns String\n\n
    saslName()\n
    '''
def nonce():
    '''returns String\n\n
    nonce()\n
    nonce()\n
    nonce()\n
    '''
def authorizationId():
    '''returns String\n\n
    authorizationId()\n
    '''
def gs2Header():
    '''returns String\n\n
    gs2Header()\n
    '''
def extensions():
    '''returns ScramExtensions\n\n
    extensions()\n
    '''
def clientFirstMessageBare():
    '''returns String\n\n
    clientFirstMessageBare()\n
    '''
def salt():
    '''returns byte[]\n\n
    salt()\n
    '''
def iterations():
    '''returns int\n\n
    iterations()\n
    '''
def channelBinding():
    '''returns byte[]\n\n
    channelBinding()\n
    '''
def proof():
    '''returns None\n\n
    proof()\n
    proof(final byte[] proof)\n
    '''
def clientFinalMessageWithoutProof():
    '''returns String\n\n
    clientFinalMessageWithoutProof()\n
    '''
def error():
    '''returns String\n\n
    error()\n
    '''
def serverSignature():
    '''returns byte[]\n\n
    serverSignature()\n
    '''
