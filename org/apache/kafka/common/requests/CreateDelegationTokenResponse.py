def CreateDelegationTokenResponse():
    '''public CreateDelegationTokenResponse(final int throttleTimeMs, final Errors error, final KafkaPrincipal owner, final long issueTimestamp, final long expiryTimestamp, final long maxTimestamp, final String tokenId, final ByteBuffer hmac)
    public CreateDelegationTokenResponse(final int throttleTimeMs, final Errors error, final KafkaPrincipal owner)
    public CreateDelegationTokenResponse(final Struct struct)
    '''
def parse():
    '''public static CreateDelegationTokenResponse parse(final ByteBuffer buffer, final short version)
    '''
def schemaVersions():
    '''public static Schema[] schemaVersions()
    '''
def errorCounts():
    '''public Map<Errors, Integer> errorCounts()
    '''
def error():
    '''public Errors error()
    '''
def owner():
    '''public KafkaPrincipal owner()
    '''
def issueTimestamp():
    '''public long issueTimestamp()
    '''
def expiryTimestamp():
    '''public long expiryTimestamp()
    '''
def maxTimestamp():
    '''public long maxTimestamp()
    '''
def tokenId():
    '''public String tokenId()
    '''
def hmacBytes():
    '''public byte[] hmacBytes()
    '''
def throttleTimeMs():
    '''public int throttleTimeMs()
    '''
def hasError():
    '''public boolean hasError()
    '''
