def ScramFormatter():
'''public ScramFormatter(final ScramMechanism mechanism)
'''
pass
def hmac():
'''public byte[] hmac(final byte[] key, final byte[] bytes)
'''
pass
def hash():
'''public byte[] hash(final byte[] str)
'''
pass
def xor():
'''public byte[] xor(final byte[] first, final byte[] second)
'''
pass
def hi():
'''public byte[] hi(final byte[] str, final byte[] salt, final int iterations)
'''
pass
def normalize():
'''public byte[] normalize(final String str)
'''
pass
def saltedPassword():
'''public byte[] saltedPassword(final String password, final byte[] salt, final int iterations)
'''
pass
def clientKey():
'''public byte[] clientKey(final byte[] saltedPassword)
'''
pass
def storedKey():
'''public byte[] storedKey(final byte[] clientKey)
public byte[] storedKey(final byte[] clientSignature, final byte[] clientProof)
'''
pass
def saslName():
'''public String saslName(final String username)
'''
pass
def username():
'''public String username(final String saslName)
'''
pass
def authMessage():
'''public String authMessage(final String clientFirstMessageBare, final String serverFirstMessage, final String clientFinalMessageWithoutProof)
'''
pass
def clientSignature():
'''public byte[] clientSignature(final byte[] storedKey, final ScramMessages.ClientFirstMessage clientFirstMessage, final ScramMessages.ServerFirstMessage serverFirstMessage, final ScramMessages.ClientFinalMessage clientFinalMessage)
'''
pass
def clientProof():
'''public byte[] clientProof(final byte[] saltedPassword, final ScramMessages.ClientFirstMessage clientFirstMessage, final ScramMessages.ServerFirstMessage serverFirstMessage, final ScramMessages.ClientFinalMessage clientFinalMessage)
'''
pass
def serverKey():
'''public byte[] serverKey(final byte[] saltedPassword)
'''
pass
def serverSignature():
'''public byte[] serverSignature(final byte[] serverKey, final ScramMessages.ClientFirstMessage clientFirstMessage, final ScramMessages.ServerFirstMessage serverFirstMessage, final ScramMessages.ClientFinalMessage clientFinalMessage)
'''
pass
def secureRandomString():
'''public String secureRandomString()
'''
pass
def secureRandomBytes():
'''public byte[] secureRandomBytes()
'''
pass
def toBytes():
'''public byte[] toBytes(final String str)
'''
pass
def generateCredential():
'''public ScramCredential generateCredential(final String password, final int iterations)
'''
pass
