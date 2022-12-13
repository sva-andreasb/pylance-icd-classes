def AbstractRequest():
    '''public AbstractRequest(final short version)
    '''
def version():
    '''public short version()
    '''
def toSend():
    '''public Send toSend(final String destination, final RequestHeader header)
    '''
def serialize():
    '''public ByteBuffer serialize(final RequestHeader header)
    '''
def toString():
    '''public String toString(final boolean verbose)
    public final String toString()
    '''
def getErrorResponse():
    '''public AbstractResponse getErrorResponse(final Throwable e)
    '''
def errorCounts():
    '''public Map<Errors, Integer> errorCounts(final Throwable e)
    '''
def parseRequest():
    '''public static AbstractRequest parseRequest(final ApiKeys apiKey, final short apiVersion, final Struct struct)
    '''
def Builder():
    '''public Builder(final ApiKeys apiKey)
    public Builder(final ApiKeys apiKey, final short allowedVersion)
    public Builder(final ApiKeys apiKey, final short oldestAllowedVersion, final short latestAllowedVersion)
    '''
def apiKey():
    '''public ApiKeys apiKey()
    '''
def oldestAllowedVersion():
    '''public short oldestAllowedVersion()
    '''
def latestAllowedVersion():
    '''public short latestAllowedVersion()
    '''
def build():
    '''public T build()
    '''
