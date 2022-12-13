CONTINUE_100 = "int  100"
SWITCHING_PROTOCOLS_101 = "int  101"
PROCESSING_102 = "int  102"
OK_200 = "int  200"
CREATED_201 = "int  201"
ACCEPTED_202 = "int  202"
NON_AUTHORITATIVE_INFORMATION_203 = "int  203"
NO_CONTENT_204 = "int  204"
RESET_CONTENT_205 = "int  205"
PARTIAL_CONTENT_206 = "int  206"
MULTI_STATUS_207 = "int  207"
MULTIPLE_CHOICES_300 = "int  300"
MOVED_PERMANENTLY_301 = "int  301"
MOVED_TEMPORARILY_302 = "int  302"
FOUND_302 = "int  302"
SEE_OTHER_303 = "int  303"
NOT_MODIFIED_304 = "int  304"
USE_PROXY_305 = "int  305"
TEMPORARY_REDIRECT_307 = "int  307"
BAD_REQUEST_400 = "int  400"
UNAUTHORIZED_401 = "int  401"
PAYMENT_REQUIRED_402 = "int  402"
FORBIDDEN_403 = "int  403"
NOT_FOUND_404 = "int  404"
METHOD_NOT_ALLOWED_405 = "int  405"
NOT_ACCEPTABLE_406 = "int  406"
PROXY_AUTHENTICATION_REQUIRED_407 = "int  407"
REQUEST_TIMEOUT_408 = "int  408"
CONFLICT_409 = "int  409"
GONE_410 = "int  410"
LENGTH_REQUIRED_411 = "int  411"
PRECONDITION_FAILED_412 = "int  412"
REQUEST_ENTITY_TOO_LARGE_413 = "int  413"
REQUEST_URI_TOO_LONG_414 = "int  414"
UNSUPPORTED_MEDIA_TYPE_415 = "int  415"
REQUESTED_RANGE_NOT_SATISFIABLE_416 = "int  416"
EXPECTATION_FAILED_417 = "int  417"
UNPROCESSABLE_ENTITY_422 = "int  422"
LOCKED_423 = "int  423"
FAILED_DEPENDENCY_424 = "int  424"
INTERNAL_SERVER_ERROR_500 = "int  500"
NOT_IMPLEMENTED_501 = "int  501"
BAD_GATEWAY_502 = "int  502"
SERVICE_UNAVAILABLE_503 = "int  503"
GATEWAY_TIMEOUT_504 = "int  504"
HTTP_VERSION_NOT_SUPPORTED_505 = "int  505"
INSUFFICIENT_STORAGE_507 = "int  507"
MAX_CODE = "int  507"
def getCode():
    '''public static Code getCode(final int code)
    public int getCode()
    '''
def getMessage():
    '''public static String getMessage(final int code)
    public String getMessage()
    '''
def isInformational():
    '''public static boolean isInformational(final int code)
    public boolean isInformational()
    '''
def isSuccess():
    '''public static boolean isSuccess(final int code)
    public boolean isSuccess()
    '''
def isRedirection():
    '''public static boolean isRedirection(final int code)
    public boolean isRedirection()
    '''
def isClientError():
    '''public static boolean isClientError(final int code)
    public boolean isClientError()
    '''
def isServerError():
    '''public static boolean isServerError(final int code)
    public boolean isServerError()
    '''
def equals():
    '''public boolean equals(final int code)
    '''
def toString():
    '''public String toString()
    '''
