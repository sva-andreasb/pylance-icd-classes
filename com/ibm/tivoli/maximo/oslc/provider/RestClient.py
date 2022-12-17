HTTPMETHOD_GET = "String  \"GET\""
HTTPMETHOD_HEAD = "String  \"HEAD\""
HTTPMETHOD_POST = "String  \"POST\""
HTTPMETHOD_PUT = "String  \"PUT\""
HTTPMETHOD_DELETE = "String  \"DELETE\""
def ():
    '''returns RestClient\n\n
    (final String[] args)\n
    (final String uri)\n
    '''
def withQueryParams():
    '''returns RestClient\n\n
    withQueryParams(final Map<String, String> qparams)\n
    '''
def withHeaders():
    '''returns RestClient\n\n
    withHeaders(final Map<String, String> headers)\n
    '''
def withMethod():
    '''returns RestClient\n\n
    withMethod(final String httpMethod)\n
    '''
def withApiKey():
    '''returns RestClient\n\n
    withApiKey(final String apikey)\n
    '''
def invokeJson():
    '''returns JSONArtifact\n\n
    invokeJson()\n
    '''
def bytesToJSON():
    '''returns JSONArtifact\n\n
    bytesToJSON(final byte[] data)\n
    '''
def invoke():
    '''returns byte[]\n\n
    invoke()\n
    invoke(final JSONArtifact jo)\n
    invoke(final byte[] data)\n
    '''
