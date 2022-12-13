def schemaVersions():
    '''public static Schema[] schemaVersions()
    '''
def SaslHandshakeRequest():
    '''public SaslHandshakeRequest(final String mechanism)
    public SaslHandshakeRequest(final String mechanism, final short version)
    public SaslHandshakeRequest(final Struct struct, final short version)
    '''
def mechanism():
    '''public String mechanism()
    '''
def getErrorResponse():
    '''public AbstractResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
    '''
def parse():
    '''public static SaslHandshakeRequest parse(final ByteBuffer buffer, final short version)
    '''
def Builder():
    '''public Builder(final String mechanism)
    '''
def build():
    '''public SaslHandshakeRequest build(final short version)
    '''
def toString():
    '''public String toString()
    '''
