INVALID_CLASS = "int  1001"
ERROR_TEXT_INVALID_CLASS = "String  The class type specified is not a valid CDM class type""
NO_VALID_NAME = "int  1002"
ERROR_TEXT_NO_VALID_NAME = "String  Insufficient identifying attributes were provided to construct a valid name based on the naming rule. ""
SUPERIOR_NOT_FOUND = "int  1003"
ERROR_TEXT_NAMING_CONTEXT_NOT_FOUND = "String  The provided naming context does not exist in the Naming and Reconciliation database. ""
NAME_NOT_FOUND = "int  1004"
ERROR_TEXT_NAME_NOT_FOUND = "String  The provided alias or master does not exist in the Naming and Reconciliation database. ""
NOT_A_MASTER = "int  1005"
ERROR_TEXT_NOT_A_MASTER = "String  The provided name or GUID is not that of a master. ""
MISSING_REQUIRED_PARAMETER = "int  1006"
ERROR_TEXT_MISSING_REQUIRED_PARAMETER = "String  A required parameter is not provided in the call. ""
INVALID_NAMING_RULES_FILE = "int  1007"
ERROR_TEXT_INVALID_NAMING_RULES_FILE = "String  Could not load the NamingRules XML file.""
INVALID_IDENTIFYING_ATT = "int  1008"
ERROR_TEXT_INVALID_IDENTIFYING_ATT = "String  A null identifying attribute was passed.""
RUNTIME_EXCEPTION = "int  1009"
ERROR_TEXT_RUNTIME_EXCEPTION = "String  A Java runtime exception has been thrown or a underline component has thrown an exception.""
INVALID_GRAPH = "int  1010"
ERROR_TEXT_INVALID_GRAPH = "String  There are errors or cycles in the input graphs.""
UPDATING_IDENTIFYING_ATTRIBUTE = "int  1011"
ERROR_TEXT_UPDATING_IDENTIFYING_ATTRIBUTE = "String  Attempt to update an identifying attribute""
NON_IDENTIFYING_ATTRIBUTE_NOT_PROVIDED = "int  1012"
ERROR_TEXT_NON_IDENTIFYING_ATTRIBUTE_NOT_PROVIDED = "String  At least one non-identifying attribute must be provided.""
MANAGED_ELEMENT_NOT_FOUND = "int  1013"
ERROR_TEXT_MANAGED_ELEMENT_NOT_FOUND = "String  The specified managed element does not exist in the databas.""
MSS_NOT_FOUND = "int  1014"
ERROR_TEXT_MSS_NOT_FOUND = "String  The specified MSS does not exist in the database""
UNSUPPORTED_CDM_VERSION = "int  1015"
ERROR_TEXT_UNSUPPORTED_CDM_VERSION = "String  Either the CDM verion is not supported or the CDM version.release.modifier of this MSS is newer than that of the DIS database.  Please upgrade the CDM metadata stored in the DIS database.  ""
GUID_FORMAT_EXCEPTION = "int  1101"
ERROR_TEXT_GUID_FORMAT_EXCEPTION = "String  A Guid format exception has occurred. ""
CACHE_IN_USE = "int  3001"
ERROR_TEXT_CACHE_IN_USE = "String  The metadata chache is being used by another DIS service. Try again later.""
REFRESH_METADATA_CACHE = "int  3002"
ERROR_TEXT_REFRESH_METADATA_CACHE = "String  CDM metadata stored in the DIS database has been updated.Call init() method to refresh the metadata caches with the latest CDM metadata.""
METADATA_NO_MODEL_LEVELS = "int  3003"
ERROR_TEXT_NO_MODEL_LEVELS = "String  No model levels found in the database.""
NULL_ARGUMENTS = "int  5001"
ERROR_TEXT_NULL_ARGUMENTS = "String  ERROR: Unable to get the arguments from command line. Please, contact system administrator.""
MISSING_DRIVER = "int  5002"
ERROR_TEXT_MISSING_DRIVER = "String  ERROR: Unable to find driver for the database.""
NULL_DB_PROPS_FILE = "int  6001"
ERROR_TEXT_NULL_DB_PROPS_FILE = "String  The configuration file to the database was not found. Please, contact the system administrator.""
CANNOT_READ_DB_PROPS_FILE = "int  6002"
ERROR_TEXT_CANNOT_READ_DB_PROPS_FILE = "String  Could not read the database properties file. Please, contact the system administrator.""
NULL_USERNAME = "int  6003"
ERROR_TEXT_NULL_USERNAME = "String  ERROR: Parameter 'username' for the database was not found!""
ERROR_USERNAME = "int  6004"
ERROR_TEXT_ERROR_USERNAME = "String  ERROR: The database username property is not set correctly.""
NULL_PASSWORD = "int  6005"
ERROR_TEXT_NULL_PASSWORD = "String  ERROR: Parameter 'password' for the database was not found!""
ERROR_PASSWORD = "int  6006"
ERROR_TEXT_ERROR_PASSWORD = "String  ERROR: The database password property is not set correctly.""
NULL_URL = "int  6007"
ERROR_TEXT_NULL_URL = "String  ERROR: Parameter 'url' for the database was not found!""
ERROR_URL = "int  6008"
ERROR_TEXT_ERROR_URL = "String  ERROR: The url property is not set correctly.""
NULL_DRIVER = "int  6009"
ERROR_TEXT_NULL_DRIVER = "String  ERROR: Parameter 'driver' for the database was not found!""
ERROR_DRIVER = "int  6010"
ERROR_TEXT_ERROR_DRIVER = "String  ERROR: The driver property is not set correctly.""
def NrsApiException():
'''public NrsApiException(final int errorCode, final String errorDetails)
'''
pass
def getErrorDetails():
'''public String getErrorDetails()
'''
pass
def getErrorText():
'''public static String getErrorText(final int errorCode)
'''
pass
def toString():
'''public String toString()
'''
pass
