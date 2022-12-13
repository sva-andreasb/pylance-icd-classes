def toBytes():
'''public byte[] toBytes()
'''
pass
def ClientFirstMessage():
'''public ClientFirstMessage(final byte[] messageBytes)
public ClientFirstMessage(final String saslName, final String nonce, final Map<String, String> extensions)
'''
pass
def saslName():
'''public String saslName()
'''
pass
def nonce():
'''public String nonce()
public String nonce()
public String nonce()
'''
pass
def authorizationId():
'''public String authorizationId()
'''
pass
def gs2Header():
'''public String gs2Header()
'''
pass
def extensions():
'''public ScramExtensions extensions()
'''
pass
def clientFirstMessageBare():
'''public String clientFirstMessageBare()
'''
pass
def ServerFirstMessage():
'''public ServerFirstMessage(final byte[] messageBytes)
public ServerFirstMessage(final String clientNonce, final String serverNonce, final byte[] salt, final int iterations)
'''
pass
def salt():
'''public byte[] salt()
'''
pass
def iterations():
'''public int iterations()
'''
pass
def ClientFinalMessage():
'''public ClientFinalMessage(final byte[] messageBytes)
public ClientFinalMessage(final byte[] channelBinding, final String nonce)
'''
pass
def channelBinding():
'''public byte[] channelBinding()
'''
pass
def proof():
'''public byte[] proof()
public void proof(final byte[] proof)
'''
pass
def clientFinalMessageWithoutProof():
'''public String clientFinalMessageWithoutProof()
'''
pass
def ServerFinalMessage():
'''public ServerFinalMessage(final byte[] messageBytes)
public ServerFinalMessage(final String error, final byte[] serverSignature)
'''
pass
def error():
'''public String error()
'''
pass
def serverSignature():
'''public byte[] serverSignature()
'''
pass
