SUCCESS = "int  0"
OPERATIONS_ERROR = "int  1"
PROTOCOL_ERROR = "int  2"
TIME_LIMIT_EXCEEDED = "int  3"
SIZE_LIMIT_EXCEEDED = "int  4"
COMPARE_FALSE = "int  5"
COMPARE_TRUE = "int  6"
AUTH_METHOD_NOT_SUPPORTED = "int  7"
STRONG_AUTH_REQUIRED = "int  8"
LDAP_PARTIAL_RESULTS = "int  9"
REFERRAL = "int  10"
ADMIN_LIMIT_EXCEEDED = "int  11"
UNAVAILABLE_CRITICAL_EXTENSION = "int  12"
CONFIDENTIALITY_REQUIRED = "int  13"
SASL_BIND_IN_PROGRESS = "int  14"
NO_SUCH_ATTRIBUTE = "int  16"
UNDEFINED_ATTRIBUTE_TYPE = "int  17"
INAPPROPRIATE_MATCHING = "int  18"
CONSTRAINT_VIOLATION = "int  19"
ATTRIBUTE_OR_VALUE_EXISTS = "int  20"
INVALID_ATTRIBUTE_SYNTAX = "int  21"
NO_SUCH_OBJECT = "int  32"
ALIAS_PROBLEM = "int  33"
INVALID_DN_SYNTAX = "int  34"
IS_LEAF = "int  35"
ALIAS_DEREFERENCING_PROBLEM = "int  36"
INAPPROPRIATE_AUTHENTICATION = "int  48"
INVALID_CREDENTIALS = "int  49"
INSUFFICIENT_ACCESS_RIGHTS = "int  50"
BUSY = "int  51"
UNAVAILABLE = "int  52"
UNWILLING_TO_PERFORM = "int  53"
LOOP_DETECT = "int  54"
NAMING_VIOLATION = "int  64"
OBJECT_CLASS_VIOLATION = "int  65"
NOT_ALLOWED_ON_NONLEAF = "int  66"
NOT_ALLOWED_ON_RDN = "int  67"
ENTRY_ALREADY_EXISTS = "int  68"
OBJECT_CLASS_MODS_PROHIBITED = "int  69"
AFFECTS_MULTIPLE_DSAS = "int  71"
OTHER = "int  80"
SERVER_DOWN = "int  81"
LOCAL_ERROR = "int  82"
ENCODING_ERROR = "int  83"
DECODING_ERROR = "int  84"
LDAP_TIMEOUT = "int  85"
AUTH_UNKNOWN = "int  86"
FILTER_ERROR = "int  87"
USER_CANCELLED = "int  88"
NO_MEMORY = "int  90"
CONNECT_ERROR = "int  91"
LDAP_NOT_SUPPORTED = "int  92"
CONTROL_NOT_FOUND = "int  93"
NO_RESULTS_RETURNED = "int  94"
MORE_RESULTS_TO_RETURN = "int  95"
CLIENT_LOOP = "int  96"
REFERRAL_LIMIT_EXCEEDED = "int  97"
INVALID_RESPONSE = "int  100"
AMBIGUOUS_RESPONSE = "int  101"
TLS_NOT_SUPPORTED = "int  112"
def LDAPException():
    '''    public LDAPException()
    public LDAPException(final String s, final int n, final String s2)
    public LDAPException(final String s, final Object[] array, final int n, final String s2)
    public LDAPException(final String s, final int n, final String s2, final Throwable t)
    public LDAPException(final String s, final Object[] array, final int n, final String s2, final Throwable t)
    public LDAPException(final String s, final int n, final String s2, final String s3)
    public LDAPException(final String s, final Object[] array, final int n, final String s2, final String s3)
    '''
def resultCodeToString():
    '''    public String resultCodeToString()
    public static String resultCodeToString(final int n)
    public String resultCodeToString(final Locale locale)
    public static String resultCodeToString(final int n, final Locale locale)
    '''
def getLDAPErrorMessage():
    '''    public String getLDAPErrorMessage()
    '''
def getCause():
    '''    public Throwable getCause()
    '''
def getResultCode():
    '''    public int getResultCode()
    '''
def getMatchedDN():
    '''    public String getMatchedDN()
    '''
def getMessage():
    '''    public String getMessage()
    '''
def getLocalizedMessage():
    '''    public String getLocalizedMessage()
    '''
def toString():
    '''    public String toString()
    '''
