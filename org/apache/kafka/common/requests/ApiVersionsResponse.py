def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def ApiVersionsResponse():
'''public ApiVersionsResponse(final Errors error, final List<ApiVersion> apiVersions)
public ApiVersionsResponse(final int throttleTimeMs, final Errors error, final List<ApiVersion> apiVersions)
public ApiVersionsResponse(final Struct struct)
'''
pass
def apiVersionsResponse():
'''public static ApiVersionsResponse apiVersionsResponse(final int throttleTimeMs, final byte maxMagic)
'''
pass
def throttleTimeMs():
'''public int throttleTimeMs()
'''
pass
def apiVersions():
'''public Collection<ApiVersion> apiVersions()
'''
pass
def apiVersion():
'''public ApiVersion apiVersion(final short apiKey)
'''
pass
def error():
'''public Errors error()
'''
pass
def errorCounts():
'''public Map<Errors, Integer> errorCounts()
'''
pass
def parse():
'''public static ApiVersionsResponse parse(final ByteBuffer buffer, final short version)
'''
pass
def createApiVersionsResponse():
'''public static ApiVersionsResponse createApiVersionsResponse(final int throttleTimeMs, final byte minMagic)
'''
pass
def defaultApiVersionsResponse():
'''public static ApiVersionsResponse defaultApiVersionsResponse()
'''
pass
def ApiVersion():
'''public ApiVersion(final ApiKeys apiKey)
public ApiVersion(final short apiKey, final short minVersion, final short maxVersion)
'''
pass
def toString():
'''public String toString()
'''
pass
