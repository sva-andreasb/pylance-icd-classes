HTTPMETHOD_GET = "String  \"GET\""
HTTPMETHOD_HEAD = "String  \"HEAD\""
HTTPMETHOD_POST = "String  \"POST\""
HTTPMETHOD_PUT = "String  \"PUT\""
HTTPMETHOD_DELETE = "String  \"DELETE\""
def RestClient():
    '''    public RestClient(final String[] args)
    public RestClient(final String uri)
    '''
def withQueryParams():
    '''    public RestClient withQueryParams(final Map<String, String> qparams)
    '''
def withHeaders():
    '''    public RestClient withHeaders(final Map<String, String> headers)
    '''
def withMethod():
    '''    public RestClient withMethod(final String httpMethod)
    '''
def withApiKey():
    '''    public RestClient withApiKey(final String apikey)
    '''
def invokeJson():
    '''    public JSONArtifact invokeJson()
    '''
def bytesToJSON():
    '''    public JSONArtifact bytesToJSON(final byte[] data)
    '''
def invoke():
    '''    public byte[] invoke()
    public JSONArtifact invoke(final JSONArtifact jo)
    public byte[] invoke(final byte[] data)
    '''
def encode():
    '''    public static String encode(final String userName, final String password)
    '''
