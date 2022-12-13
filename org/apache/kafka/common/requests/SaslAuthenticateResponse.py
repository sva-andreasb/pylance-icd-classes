def schemaVersions():
    '''public static Schema[] schemaVersions()
    '''
def SaslAuthenticateResponse():
    '''public SaslAuthenticateResponse(final Errors error, final String errorMessage)
    public SaslAuthenticateResponse(final Errors error, final String errorMessage, final ByteBuffer saslAuthBytes)
    public SaslAuthenticateResponse(final Struct struct)
    '''
def error():
    '''public Errors error()
    '''
def errorMessage():
    '''public String errorMessage()
    '''
def saslAuthBytes():
    '''public ByteBuffer saslAuthBytes()
    '''
def errorCounts():
    '''public Map<Errors, Integer> errorCounts()
    '''
def toStruct():
    '''public Struct toStruct(final short version)
    '''
def parse():
    '''public static SaslAuthenticateResponse parse(final ByteBuffer buffer, final short version)
    '''
