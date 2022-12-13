STATUS_OK = "int  0"
STATUS_EOF = "int  1"
STATUS_NO_SUCH_FILE = "int  2"
STATUS_PERMISSION_DENIED = "int  3"
STATUS_FAILURE = "int  4"
STATUS_BAD_MESSAGE = "int  5"
STATUS_NO_CONNECTION = "int  6"
STATUS_CONNECTION_LOST = "int  7"
STATUS_OP_UNSUPPORTED = "int  8"
STATUS_INVALID_HANDLE = "int  9"
STATUS_NO_SUCH_PATH = "int  10"
STATUS_FILE_ALREADY_EXISTS = "int  11"
STATUS_WRITE_PROTECT = "int  12"
STATUS_NO_MEDIA = "int  13"
STATUS_NO_SPACE_ON_FILESYSTEM = "int  14"
STATUS_QUOTA_EXCEEDED = "int  15"
STATUS_UNKNOWN_PRINCIPLE = "int  16"
STATUS_LOCK_CONFLICT = "int  17"
STATUS_DIR_NOT_EMPTY = "int  18"
STATUS_NOT_A_DIRECTORY = "int  19"
STATUS_INVALID_FILENAME = "int  20"
STATUS_LINK_LOOP = "int  21"
STATUS_CANNOT_DELETE = "int  22"
STATUS_INVALID_PARAMETER = "int  23"
STATUS_FILE_IS_A_DIRECTORY = "int  24"
STATUS_BYTE_RANGE_LOCK_CONFLICT = "int  25"
STATUS_BYTE_RANGE_LOCK_REFUSED = "int  26"
STATUS_DELETE_PENDING = "int  27"
STATUS_FILE_CORRUPT = "int  28"
STATUS_OWNER_INVALID = "int  29"
STATUS_GROUP_INVALID = "int  30"
STATUS_ACCESS_DENIED = "int  1"
STATUS_STORAGE_EXCEEDED = "int  2"
STATUS_VERSION_NOT_SUPPORTED = "int  3"
STATUS_KEY_NOT_FOUND = "int  4"
STATUS_KEY_NOT_SUPPORTED = "int  5"
STATUS_KEY_ALREADY_PRESENT = "int  6"
STATUS_GENERAL_FAILURE = "int  7"
STATUS_REQUEST_NOT_SUPPORTED = "int  8"
SFTP_STATUS = "int  0"
PUBLICKEY_STATUS = "int  1"
def getErrorCode():
    '''public int getErrorCode()
    '''
def getErrorCodeAsString():
    '''public String getErrorCodeAsString()
    public static String getErrorCodeAsString(final int statusType, final int errorNum)
    '''
def getErrorMessage():
    '''public String getErrorMessage()
    '''
def getUnknownNames():
    '''public String[] getUnknownNames()
    '''
