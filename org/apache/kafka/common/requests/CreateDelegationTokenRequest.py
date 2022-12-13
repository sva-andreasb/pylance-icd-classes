def CreateDelegationTokenRequest():
    '''public CreateDelegationTokenRequest(final Struct struct, final short version)
    '''
def parse():
    '''public static CreateDelegationTokenRequest parse(final ByteBuffer buffer, final short version)
    '''
def schemaVersions():
    '''public static Schema[] schemaVersions()
    '''
def getErrorResponse():
    '''public AbstractResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
    '''
def renewers():
    '''public List<KafkaPrincipal> renewers()
    '''
def maxLifeTime():
    '''public long maxLifeTime()
    '''
def Builder():
    '''public Builder(final List<KafkaPrincipal> renewers, final long maxLifeTime)
    '''
def build():
    '''public CreateDelegationTokenRequest build(final short version)
    '''
def toString():
    '''public String toString()
    '''
