TYPE_BSI = "int  0"
TYPE_MWI = "int  1"
TYPE_CFG_UI = "int  2"
TYPE_BSI_MWI = "int  3"
MWI_INSTALL = "String  \"MWI_INSTALL\""
TPAE_INSTALL = "String  \"TPAE_INSTALL\""
TPAE_CONFIG = "String  \"TPAE_CONFIG\""
WINDOWS_OS = "String  \"WINDOWS\""
LINUX_OS = "String  \"LINUX\""
AIX_OS = "String  \"AIX\""
ITDS_VENDOR = "String  \"IDS\""
MSAD_VENDOR = "String  \"AD\""
WAS_CLUSTER_FUNCTION_UI = "String  \"_UI_FUNCTION\""
WAS_CLUSTER_FUNCTION_CRON = "String  \"_CRON_FUNCTION\""
WAS_CLUSTER_FUNCTION_REP = "String  \"_REP_FUNCTION\""
WAS_CLUSTER_FUNCTION_MIF = "String  \"_MIF_FUNCTION\""
DYNAMIC_PROPERTY_INITIAL_SUFFIX = "int  1"
def getPropertyName():
    '''returns String\n\n
    getPropertyName()\n
    getPropertyName(final int suffix)\n
    '''
def getDescription():
    '''returns String\n\n
    getDescription()\n
    '''
def isPasswordProperty():
    '''returns boolean\n\n
    isPasswordProperty()\n
    '''
def isBSIProperty():
    '''returns boolean\n\n
    isBSIProperty()\n
    '''
def isMWIProperty():
    '''returns boolean\n\n
    isMWIProperty()\n
    '''
def isConfigProperty():
    '''returns boolean\n\n
    isConfigProperty()\n
    '''
def getDefaultValue():
    '''returns String\n\n
    getDefaultValue()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
