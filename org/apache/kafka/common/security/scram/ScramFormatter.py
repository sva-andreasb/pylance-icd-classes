def ScramFormatter():
    '''public ScramFormatter(final ScramMechanism mechanism)
    '''
def hmac():
    '''public byte[] hmac(final byte[] key, final byte[] bytes)
    '''
def hash():
    '''public byte[] hash(final byte[] str)
    '''
def xor():
    '''public byte[] xor(final byte[] first, final byte[] second)
    '''
def hi():
    '''public byte[] hi(final byte[] str, final byte[] salt, final int iterations)
    '''
def normalize():
    '''public byte[] normalize(final String str)
    '''
def saltedPassword():
    '''public byte[] saltedPassword(final String password, final byte[] salt, final int iterations)
    '''
def clientKey():
    '''public byte[] clientKey(final byte[] saltedPassword)
    '''
def storedKey():
    '''public byte[] storedKey(final byte[] clientKey)
    public byte[] storedKey(final byte[] clientSignature, final byte[] clientProof)
    '''
def saslName():
    '''public String saslName(final String username)
    '''
def username():
    '''public String username(final String saslName)
    '''
def authMessage():
    '''public String authMessage(final String clientFirstMessageBare, final String serverFirstMessage, final String clientFinalMessageWithoutProof)
    '''
def clientSignature():
    '''public byte[] clientSignature(final byte[] storedKey, final ScramMessages.ClientFirstMessage clientFirstMessage, final ScramMessages.ServerFirstMessage serverFirstMessage, final ScramMessages.ClientFinalMessage clientFinalMessage)
    '''
def clientProof():
    '''public byte[] clientProof(final byte[] saltedPassword, final ScramMessages.ClientFirstMessage clientFirstMessage, final ScramMessages.ServerFirstMessage serverFirstMessage, final ScramMessages.ClientFinalMessage clientFinalMessage)
    '''
def serverKey():
    '''public byte[] serverKey(final byte[] saltedPassword)
    '''
def serverSignature():
    '''public byte[] serverSignature(final byte[] serverKey, final ScramMessages.ClientFirstMessage clientFirstMessage, final ScramMessages.ServerFirstMessage serverFirstMessage, final ScramMessages.ClientFinalMessage clientFinalMessage)
    '''
def secureRandomString():
    '''public String secureRandomString()
    '''
def secureRandomBytes():
    '''public byte[] secureRandomBytes()
    '''
def toBytes():
    '''public byte[] toBytes(final String str)
    '''
def generateCredential():
    '''public ScramCredential generateCredential(final String password, final int iterations)
    '''
