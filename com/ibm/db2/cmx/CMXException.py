QUERY_SERVICE_NOT_AVAILABLE = "int  1"
INVALID_CACHED_OBJECT_UPDATE = "int  2"
CONTROLLER_NOT_AVAILABLE = "int  3"
CONTROLLER_NOT_INITIALIZED = "int  4"
UNABLE_TO_LOAD_CLIENT_CACHE_FILE__NO_RW_ACCESS = "int  5"
UNABLE_TO_DISCOVER_PROFILE = "int  6"
NOT_SUPPORTED = "int  100"
UNABLE_TO_DELETE_CLIENT_CACHE_FILE = "int  101"
UNABLE_TO_CLEAR_SERVER_CACHE = "int  102"
def CMXException():
    '''    public CMXException(final int reasonCode_)
    public CMXException(final Throwable cause, final int reasonCode_)
    '''
def getReasonCode():
    '''    public int getReasonCode()
    '''
