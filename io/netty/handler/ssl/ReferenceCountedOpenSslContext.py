def touch():
    '''returns ReferenceCounted\n\n
    touch(final Object hint)\n
    '''
def applicationProtocolNegotiator():
    '''returns ApplicationProtocolNegotiator\n\n
    applicationProtocolNegotiator()\n
    '''
def setRejectRemoteInitiatedRenegotiation():
    '''returns None\n\n
    setRejectRemoteInitiatedRenegotiation(final boolean rejectRemoteInitiatedRenegotiation)\n
    '''
def getRejectRemoteInitiatedRenegotiation():
    '''returns boolean\n\n
    getRejectRemoteInitiatedRenegotiation()\n
    '''
def setBioNonApplicationBufferSize():
    '''returns None\n\n
    setBioNonApplicationBufferSize(final int bioNonApplicationBufferSize)\n
    '''
def getBioNonApplicationBufferSize():
    '''returns int\n\n
    getBioNonApplicationBufferSize()\n
    '''
def protocols():
    '''returns List<String>\n\n
    protocols()\n
    '''
def remove():
    '''returns ReferenceCountedOpenSslEngine\n\n
    remove(final long ssl)\n
    '''
def add():
    '''returns None\n\n
    add(final ReferenceCountedOpenSslEngine engine)\n
    '''
def get():
    '''returns ReferenceCountedOpenSslEngine\n\n
    get(final long ssl)\n
    '''
def sign():
    '''returns byte[]\n\n
    sign(final long ssl, final int signatureAlgorithm, final byte[] digest)\n
    '''
def decrypt():
    '''returns byte[]\n\n
    decrypt(final long ssl, final byte[] input)\n
    '''
