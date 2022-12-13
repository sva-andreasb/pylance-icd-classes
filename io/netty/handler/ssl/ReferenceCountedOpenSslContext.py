def touch():
    '''public ReferenceCounted touch(final Object hint)
    public final ReferenceCounted touch()
    public final ReferenceCounted touch(final Object hint)
    '''
def cipherSuites():
    '''public final List<String> cipherSuites()
    '''
def sessionCacheSize():
    '''public final long sessionCacheSize()
    '''
def sessionTimeout():
    '''public final long sessionTimeout()
    '''
def applicationProtocolNegotiator():
    '''public ApplicationProtocolNegotiator applicationProtocolNegotiator()
    '''
def isClient():
    '''public final boolean isClient()
    '''
def newEngine():
    '''public final SSLEngine newEngine(final ByteBufAllocator alloc, final String peerHost, final int peerPort)
    public final SSLEngine newEngine(final ByteBufAllocator alloc)
    '''
def context():
    '''public final long context()
    '''
def stats():
    '''public final OpenSslSessionStats stats()
    '''
def setRejectRemoteInitiatedRenegotiation():
    '''public void setRejectRemoteInitiatedRenegotiation(final boolean rejectRemoteInitiatedRenegotiation)
    '''
def getRejectRemoteInitiatedRenegotiation():
    '''public boolean getRejectRemoteInitiatedRenegotiation()
    '''
def setBioNonApplicationBufferSize():
    '''public void setBioNonApplicationBufferSize(final int bioNonApplicationBufferSize)
    '''
def getBioNonApplicationBufferSize():
    '''public int getBioNonApplicationBufferSize()
    '''
def setTicketKeys():
    '''public final void setTicketKeys(final byte[] keys)
    '''
def sslCtxPointer():
    '''public final long sslCtxPointer()
    '''
def setPrivateKeyMethod():
    '''public final void setPrivateKeyMethod(final OpenSslPrivateKeyMethod method)
    '''
def refCnt():
    '''public final int refCnt()
    '''
def retain():
    '''public final ReferenceCounted retain()
    public final ReferenceCounted retain(final int increment)
    '''
def release():
    '''public final boolean release()
    public final boolean release(final int decrement)
    '''
def protocols():
    '''public List<String> protocols()
    '''
def verify():
    '''public final int verify(final long ssl, final byte[][] chain, final String auth)
    '''
def remove():
    '''public ReferenceCountedOpenSslEngine remove(final long ssl)
    '''
def add():
    '''public void add(final ReferenceCountedOpenSslEngine engine)
    '''
def get():
    '''public ReferenceCountedOpenSslEngine get(final long ssl)
    '''
def sign():
    '''public byte[] sign(final long ssl, final int signatureAlgorithm, final byte[] digest)
    '''
def decrypt():
    '''public byte[] decrypt(final long ssl, final byte[] input)
    '''
