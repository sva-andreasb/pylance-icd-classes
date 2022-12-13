def AbstractRequest():
'''public AbstractRequest(final short version)
'''
pass
def version():
'''public short version()
'''
pass
def toSend():
'''public Send toSend(final String destination, final RequestHeader header)
'''
pass
def serialize():
'''public ByteBuffer serialize(final RequestHeader header)
'''
pass
def toString():
'''public String toString(final boolean verbose)
public final String toString()
'''
pass
def getErrorResponse():
'''public AbstractResponse getErrorResponse(final Throwable e)
'''
pass
def errorCounts():
'''public Map<Errors, Integer> errorCounts(final Throwable e)
'''
pass
def parseRequest():
'''public static AbstractRequest parseRequest(final ApiKeys apiKey, final short apiVersion, final Struct struct)
'''
pass
def Builder():
'''public Builder(final ApiKeys apiKey)
public Builder(final ApiKeys apiKey, final short allowedVersion)
public Builder(final ApiKeys apiKey, final short oldestAllowedVersion, final short latestAllowedVersion)
'''
pass
def apiKey():
'''public ApiKeys apiKey()
'''
pass
def oldestAllowedVersion():
'''public short oldestAllowedVersion()
'''
pass
def latestAllowedVersion():
'''public short latestAllowedVersion()
'''
pass
def build():
'''public T build()
'''
pass
