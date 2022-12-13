ED = "String  \"-edition\""
EDITION_PROP_FILE = "String  \"ibm-edition-metadata.props\""
EDITION_PROP_DELIM = "String  \"-\""
BASE_EDITION = "String  \"BASE\""
DEFAULT_EDITION = "String  \"DEFAULT\""
ACTIVE_EDITION_PROP = "String  \"config.active\""
DEFAULT_EDITION_PROP = "String  \"config.default\""
STATE_EDITION_PROP = "String  \"config.state\""
Edition_INACTIVE = "String  \"INACTIVE\""
Edition_ACTIVE = "String  \"ACTIVE\""
Edition_VALIDATE = "String  \"VALIDATE\""
EDITION_PROP_HEADER = "String  \"File contains metadata for all editions of the application\""
DESC_EDITION_PROP = "String  \"edition.desc\""
def getAppAndEdition():
    '''    public static String[] getAppAndEdition(final String mangledName)
    public static String[] getAppAndEdition(final String mangledName, final Hashtable props)
    '''
def getCompositeName():
    '''    public static String getCompositeName(final String appName, final String edition)
    public static String getCompositeName(final String appName, final Hashtable props)
    '''
def getAppEarName():
    '''    public static String getAppEarName(final String appName, final String edition)
    public static String getAppEarName(final String appName, final Hashtable props)
    '''
def getEditionDescPropName():
    '''    public static String getEditionDescPropName(final String mangledName)
    '''
def getActiveEditionPropName():
    '''    public static String getActiveEditionPropName(final String mangledName)
    '''
def getDefaultEditionPropName():
    '''    public static String getDefaultEditionPropName(final String mangledName)
    '''
def getEditionPropSuffix():
    '''    public static String getEditionPropSuffix(final String mangledName)
    '''
def isEditionSupportEnabled():
    '''    public static synchronized boolean isEditionSupportEnabled()
    '''
def isXDAugmented():
    '''    public static synchronized boolean isXDAugmented()
    '''
def isXDInstalled():
    '''    public static synchronized boolean isXDInstalled()
    '''
def checkIfEditionValid():
    '''    public static boolean checkIfEditionValid(final String edition)
    '''
def getApplicationEditions():
    '''    public static EditionInfo[] getApplicationEditions(final String appName)
    public static EditionInfo[] getApplicationEditions(final String appName, final AppManagement appMgmt_)
    '''
def getActiveEditionOnServer():
    '''    public static String getActiveEditionOnServer(final String appName, final List applications)
    '''
def getEditionStatePropName():
    '''    public static String getEditionStatePropName(final String mangledName)
    '''
def isAppActive():
    '''    public static boolean isAppActive(final String mangledName)
    '''
def getEditionState():
    '''    public static String getEditionState(final String mangledName)
    '''
