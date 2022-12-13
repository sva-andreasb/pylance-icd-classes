def ExpireDelegationTokenRequest():
    '''public ExpireDelegationTokenRequest(final Struct struct, final short versionId)
    '''
def parse():
    '''public static ExpireDelegationTokenRequest parse(final ByteBuffer buffer, final short version)
    '''
def schemaVersions():
    '''public static Schema[] schemaVersions()
    '''
def getErrorResponse():
    '''public AbstractResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
    '''
def hmac():
    '''public ByteBuffer hmac()
    '''
def expiryTimePeriod():
    '''public long expiryTimePeriod()
    '''
def Builder():
    '''public Builder(final ByteBuffer hmac, final long expiryTimePeriod)
    '''
def build():
    '''public ExpireDelegationTokenRequest build(final short version)
    '''
def toString():
    '''public String toString()
    '''
