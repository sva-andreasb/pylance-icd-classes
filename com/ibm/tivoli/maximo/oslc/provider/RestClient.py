HTTPMETHOD_GET = "String GET""
HTTPMETHOD_HEAD = "String HEAD""
HTTPMETHOD_POST = "String POST""
HTTPMETHOD_PUT = "String PUT""
HTTPMETHOD_DELETE = "String DELETE""
def RestClient():
'''public RestClient(final String[] args)
public RestClient(final String uri)
'''
pass
def withQueryParams():
'''public RestClient withQueryParams(final Map<String, String> qparams)
'''
pass
def withHeaders():
'''public RestClient withHeaders(final Map<String, String> headers)
'''
pass
def withMethod():
'''public RestClient withMethod(final String httpMethod)
'''
pass
def withApiKey():
'''public RestClient withApiKey(final String apikey)
'''
pass
def invokeJson():
'''public JSONArtifact invokeJson()
'''
pass
def bytesToJSON():
'''public JSONArtifact bytesToJSON(final byte[] data)
'''
pass
def invoke():
'''public byte[] invoke()
public JSONArtifact invoke(final JSONArtifact jo)
public byte[] invoke(final byte[] data)
'''
pass
def encode():
'''public static String encode(final String userName, final String password)
'''
pass
