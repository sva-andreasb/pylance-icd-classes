def ():
    '''returns ScramFormatter\n\n
    (final ScramMechanism mechanism)\n
    '''
def hmac():
    '''returns byte[]\n\n
    hmac(final byte[] key, final byte[] bytes)\n
    '''
def hash():
    '''returns byte[]\n\n
    hash(final byte[] str)\n
    '''
def xor():
    '''returns byte[]\n\n
    xor(final byte[] first, final byte[] second)\n
    '''
def hi():
    '''returns byte[]\n\n
    hi(final byte[] str, final byte[] salt, final int iterations)\n
    '''
def normalize():
    '''returns byte[]\n\n
    normalize(final String str)\n
    '''
def saltedPassword():
    '''returns byte[]\n\n
    saltedPassword(final String password, final byte[] salt, final int iterations)\n
    '''
def clientKey():
    '''returns byte[]\n\n
    clientKey(final byte[] saltedPassword)\n
    '''
def storedKey():
    '''returns byte[]\n\n
    storedKey(final byte[] clientKey)\n
    storedKey(final byte[] clientSignature, final byte[] clientProof)\n
    '''
def saslName():
    '''returns String\n\n
    saslName(final String username)\n
    '''
def username():
    '''returns String\n\n
    username(final String saslName)\n
    '''
def authMessage():
    '''returns String\n\n
    authMessage(final String clientFirstMessageBare, final String serverFirstMessage, final String clientFinalMessageWithoutProof)\n
    '''
def clientSignature():
    '''returns byte[]\n\n
    clientSignature(final byte[] storedKey, final ScramMessages.ClientFirstMessage clientFirstMessage, final ScramMessages.ServerFirstMessage serverFirstMessage, final ScramMessages.ClientFinalMessage clientFinalMessage)\n
    '''
def clientProof():
    '''returns byte[]\n\n
    clientProof(final byte[] saltedPassword, final ScramMessages.ClientFirstMessage clientFirstMessage, final ScramMessages.ServerFirstMessage serverFirstMessage, final ScramMessages.ClientFinalMessage clientFinalMessage)\n
    '''
def serverKey():
    '''returns byte[]\n\n
    serverKey(final byte[] saltedPassword)\n
    '''
def serverSignature():
    '''returns byte[]\n\n
    serverSignature(final byte[] serverKey, final ScramMessages.ClientFirstMessage clientFirstMessage, final ScramMessages.ServerFirstMessage serverFirstMessage, final ScramMessages.ClientFinalMessage clientFinalMessage)\n
    '''
def secureRandomString():
    '''returns String\n\n
    secureRandomString()\n
    '''
def secureRandomBytes():
    '''returns byte[]\n\n
    secureRandomBytes()\n
    '''
def toBytes():
    '''returns byte[]\n\n
    toBytes(final String str)\n
    '''
def generateCredential():
    '''returns ScramCredential\n\n
    generateCredential(final String password, final int iterations)\n
    '''
