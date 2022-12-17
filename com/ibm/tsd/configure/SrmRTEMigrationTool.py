USER_KEY = "String  \"-u\""
PASSWORD_KEY = "String  \"-p\""
DEFAULT_FONT_SIZE = "String  \"-x\""
DEFAULT_FONT_NAME = "String  \"-y\""
VALIDATE_ONLY = "String  \"-v\""
PROP_FILE_NAME = "String  \"-f\""
PROP_DIR = "String  \"-k\""
DB_ALIAS = "String  \"-a\""
SRM_RTE_MIGRATION_TOOL_PROP = "String  \"com.ibm.tsd.configure.SrmRTEMigrationBundle\""
CON_ERROR_MESSAGE = "String  \"CTGRD8203E\""
LOG_DIR_ERROR_MESSAGE = "String  \"CTGRD8202I\""
UPDATE_ERROR_MESSAGE = "String  \"CTGRD8204E\""
PROMPT_USER = "String  \"CTGRD8205E\""
SUCCESS_MESSAGE = "String  \"CTGRD8206E\""
USAGE = "String  \"CTGRD8201I\""
NO_USER_EXCEPTION = "String  \"CTGRD82011E\""
NO_PASSWORD_EXCEPTION = "String  \"CTGRD82012E\""
NO_PROP_FILE_EXCEPTION = "String  \"CTGRD82013E\""
NO_PROP_DIR_EXCEPTION = "String  \"CTGRD82015E\""
NO_DB_ALIAS__EXCEPTION = "String  \"CTGRD82016E\""
NO_DEFAULT_FONT_SIZE_EXCEPTION = "String  \"CTGRD82017E\""
NO_DEFAULT_FONT_EXCEPTION = "String  \"CTGRD82018E\""
NO_VALUE_EXCEPTION = "String  \"CTGRD82019E\""
INVALID_FONT_SIZE_EXCEPTION = "String  \"CTGRD82020E\""
INVALID_INPUTS_EXCEPTION = "String  \"CTGRD82021E\""
INVALID_INPUT_EXCEPTION = "String  \"CTGRD82022E\""
DISABLED_MESSAGE = "String  \"CTGRD82023I\""
SQLFILE = "int  1"
ORAFILE = "int  2"
SQSFILE = "int  3"
MXSFILE = "int  4"
CLASSFILE = "int  5"
MSGFILE = "int  6"
DB2FILE = "int  7"
DBCFILE = "int  8"
def ():
    '''returns SrmRTEMigrationTool\n\n
    ()\n
    '''
def getConnection():
    '''returns Connection\n\n
    getConnection()\n
    '''
def getRootDirectory():
    '''returns String\n\n
    getRootDirectory()\n
    '''
def getMaximoRootDirectory():
    '''returns String\n\n
    getMaximoRootDirectory()\n
    '''
def setup():
    '''returns None\n\n
    setup(final HashMap<String, String> params)\n
    '''
def getDBType():
    '''returns int\n\n
    getDBType(final Connection con)\n
    '''
