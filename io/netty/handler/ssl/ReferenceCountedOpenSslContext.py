def touch():
'''public ReferenceCounted touch(final Object hint)
public final ReferenceCounted touch()
public final ReferenceCounted touch(final Object hint)
'''
pass
def cipherSuites():
'''public final List<String> cipherSuites()
'''
pass
def sessionCacheSize():
'''public final long sessionCacheSize()
'''
pass
def sessionTimeout():
'''public final long sessionTimeout()
'''
pass
def applicationProtocolNegotiator():
'''public ApplicationProtocolNegotiator applicationProtocolNegotiator()
'''
pass
def isClient():
'''public final boolean isClient()
'''
pass
def newEngine():
'''public final SSLEngine newEngine(final ByteBufAllocator alloc, final String peerHost, final int peerPort)
public final SSLEngine newEngine(final ByteBufAllocator alloc)
'''
pass
def context():
'''public final long context()
'''
pass
def stats():
'''public final OpenSslSessionStats stats()
'''
pass
def setRejectRemoteInitiatedRenegotiation():
'''public void setRejectRemoteInitiatedRenegotiation(final boolean rejectRemoteInitiatedRenegotiation)
'''
pass
def getRejectRemoteInitiatedRenegotiation():
'''public boolean getRejectRemoteInitiatedRenegotiation()
'''
pass
def setBioNonApplicationBufferSize():
'''public void setBioNonApplicationBufferSize(final int bioNonApplicationBufferSize)
'''
pass
def getBioNonApplicationBufferSize():
'''public int getBioNonApplicationBufferSize()
'''
pass
def setTicketKeys():
'''public final void setTicketKeys(final byte[] keys)
'''
pass
def sslCtxPointer():
'''public final long sslCtxPointer()
'''
pass
def setPrivateKeyMethod():
'''public final void setPrivateKeyMethod(final OpenSslPrivateKeyMethod method)
'''
pass
def refCnt():
'''public final int refCnt()
'''
pass
def retain():
'''public final ReferenceCounted retain()
public final ReferenceCounted retain(final int increment)
'''
pass
def release():
'''public final boolean release()
public final boolean release(final int decrement)
'''
pass
def protocols():
'''public List<String> protocols()
'''
pass
def verify():
'''public final int verify(final long ssl, final byte[][] chain, final String auth)
'''
pass
def remove():
'''public ReferenceCountedOpenSslEngine remove(final long ssl)
'''
pass
def add():
'''public void add(final ReferenceCountedOpenSslEngine engine)
'''
pass
def get():
'''public ReferenceCountedOpenSslEngine get(final long ssl)
'''
pass
def sign():
'''public byte[] sign(final long ssl, final int signatureAlgorithm, final byte[] digest)
'''
pass
def decrypt():
'''public byte[] decrypt(final long ssl, final byte[] input)
'''
pass
