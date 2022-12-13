def schemaVersions():
    '''    public static Schema[] schemaVersions()
    '''
def ApiVersionsRequest():
    '''    public ApiVersionsRequest(final short version)
    public ApiVersionsRequest(final short version, final Short unsupportedRequestVersion)
    public ApiVersionsRequest(final Struct struct, final short version)
    '''
def hasUnsupportedRequestVersion():
    '''    public boolean hasUnsupportedRequestVersion()
    '''
def getErrorResponse():
    '''    public ApiVersionsResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
    '''
def parse():
    '''    public static ApiVersionsRequest parse(final ByteBuffer buffer, final short version)
    '''
def Builder():
    '''    public Builder()
    public Builder(final short version)
    '''
def build():
    '''    public ApiVersionsRequest build(final short version)
    '''
def toString():
    '''    public String toString()
    '''
