def toBytes():
    '''public byte[] toBytes()
    '''
def ClientFirstMessage():
    '''public ClientFirstMessage(final byte[] messageBytes)
    public ClientFirstMessage(final String saslName, final String nonce, final Map<String, String> extensions)
    '''
def saslName():
    '''public String saslName()
    '''
def nonce():
    '''public String nonce()
    public String nonce()
    public String nonce()
    '''
def authorizationId():
    '''public String authorizationId()
    '''
def gs2Header():
    '''public String gs2Header()
    '''
def extensions():
    '''public ScramExtensions extensions()
    '''
def clientFirstMessageBare():
    '''public String clientFirstMessageBare()
    '''
def ServerFirstMessage():
    '''public ServerFirstMessage(final byte[] messageBytes)
    public ServerFirstMessage(final String clientNonce, final String serverNonce, final byte[] salt, final int iterations)
    '''
def salt():
    '''public byte[] salt()
    '''
def iterations():
    '''public int iterations()
    '''
def ClientFinalMessage():
    '''public ClientFinalMessage(final byte[] messageBytes)
    public ClientFinalMessage(final byte[] channelBinding, final String nonce)
    '''
def channelBinding():
    '''public byte[] channelBinding()
    '''
def proof():
    '''public byte[] proof()
    public void proof(final byte[] proof)
    '''
def clientFinalMessageWithoutProof():
    '''public String clientFinalMessageWithoutProof()
    '''
def ServerFinalMessage():
    '''public ServerFinalMessage(final byte[] messageBytes)
    public ServerFinalMessage(final String error, final byte[] serverSignature)
    '''
def error():
    '''public String error()
    '''
def serverSignature():
    '''public byte[] serverSignature()
    '''
