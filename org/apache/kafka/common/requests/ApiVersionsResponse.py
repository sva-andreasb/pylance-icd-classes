def schemaVersions():
    '''public static Schema[] schemaVersions()
    '''
def ApiVersionsResponse():
    '''public ApiVersionsResponse(final Errors error, final List<ApiVersion> apiVersions)
    public ApiVersionsResponse(final int throttleTimeMs, final Errors error, final List<ApiVersion> apiVersions)
    public ApiVersionsResponse(final Struct struct)
    '''
def apiVersionsResponse():
    '''public static ApiVersionsResponse apiVersionsResponse(final int throttleTimeMs, final byte maxMagic)
    '''
def throttleTimeMs():
    '''public int throttleTimeMs()
    '''
def apiVersions():
    '''public Collection<ApiVersion> apiVersions()
    '''
def apiVersion():
    '''public ApiVersion apiVersion(final short apiKey)
    '''
def error():
    '''public Errors error()
    '''
def errorCounts():
    '''public Map<Errors, Integer> errorCounts()
    '''
def parse():
    '''public static ApiVersionsResponse parse(final ByteBuffer buffer, final short version)
    '''
def createApiVersionsResponse():
    '''public static ApiVersionsResponse createApiVersionsResponse(final int throttleTimeMs, final byte minMagic)
    '''
def defaultApiVersionsResponse():
    '''public static ApiVersionsResponse defaultApiVersionsResponse()
    '''
def ApiVersion():
    '''public ApiVersion(final ApiKeys apiKey)
    public ApiVersion(final short apiKey, final short minVersion, final short maxVersion)
    '''
def toString():
    '''public String toString()
    '''
