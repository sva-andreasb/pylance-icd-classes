def schemaVersions():
    '''public static Schema[] schemaVersions()
    '''
def SaslHandshakeResponse():
    '''public SaslHandshakeResponse(final Errors error, final Collection<String> enabledMechanisms)
    public SaslHandshakeResponse(final Struct struct)
    '''
def error():
    '''public Errors error()
    '''
def errorCounts():
    '''public Map<Errors, Integer> errorCounts()
    '''
def toStruct():
    '''public Struct toStruct(final short version)
    '''
def enabledMechanisms():
    '''public List<String> enabledMechanisms()
    '''
def parse():
    '''public static SaslHandshakeResponse parse(final ByteBuffer buffer, final short version)
    '''
