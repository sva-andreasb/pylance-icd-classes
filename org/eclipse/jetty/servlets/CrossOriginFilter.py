ACCESS_CONTROL_REQUEST_METHOD_HEADER = "String  \"Access-Control-Request-Method\""
ACCESS_CONTROL_REQUEST_HEADERS_HEADER = "String  \"Access-Control-Request-Headers\""
ACCESS_CONTROL_ALLOW_ORIGIN_HEADER = "String  \"Access-Control-Allow-Origin\""
ACCESS_CONTROL_ALLOW_METHODS_HEADER = "String  \"Access-Control-Allow-Methods\""
ACCESS_CONTROL_ALLOW_HEADERS_HEADER = "String  \"Access-Control-Allow-Headers\""
ACCESS_CONTROL_MAX_AGE_HEADER = "String  \"Access-Control-Max-Age\""
ACCESS_CONTROL_ALLOW_CREDENTIALS_HEADER = "String  \"Access-Control-Allow-Credentials\""
ALLOWED_ORIGINS_PARAM = "String  \"allowedOrigins\""
ALLOWED_METHODS_PARAM = "String  \"allowedMethods\""
ALLOWED_HEADERS_PARAM = "String  \"allowedHeaders\""
PREFLIGHT_MAX_AGE_PARAM = "String  \"preflightMaxAge\""
ALLOW_CREDENTIALS_PARAM = "String  \"allowCredentials\""
def ():
    '''returns CrossOriginFilter\n\n
    ()\n
    '''
def init():
    '''returns None\n\n
    init(final FilterConfig config)\n
    '''
def doFilter():
    '''returns None\n\n
    doFilter(final ServletRequest request, final ServletResponse response, final FilterChain chain)\n
    '''
def destroy():
    '''returns None\n\n
    destroy()\n
    '''
