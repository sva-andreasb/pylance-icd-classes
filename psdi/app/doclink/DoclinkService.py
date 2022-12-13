URLTYPE_FILE = "String  \"FILE\""
URLTYPE_WWW = "String  \"WWW\""
URLTYPE_DMS = "String  \"DMS\""
def DoclinkService():
    '''public DoclinkService()
    public DoclinkService(final MXServer mxServer)
    '''
def doclinkExists():
    '''public boolean doclinkExists(final String keytable, final String keycolumn, final String keyvalue, final UserInfo userInfo)
    '''
def getAppDoctypeLinks():
    '''public TreeMap getAppDoctypeLinks(final String appName, final String keyTable, final String keyColumn, final int keyValue, final UserInfo userInfo)
    '''
def addDocinfoAndLinks():
    '''public MboSetRemote addDocinfoAndLinks(final String urlname, final String description, final String[] urlparam, final String doctype, final String urltype, final String keytable, final String keycolumn, final String[] keyvalue, final boolean forceAutokey, final String application, final UserInfo userInfo)
    public MboSetRemote addDocinfoAndLinks(final String urlname, final String description, final String assetType, final String[] keyvalue, final UserInfo userInfo)
    '''
def getTenantFolderPathRootAsEntered():
    '''public static String getTenantFolderPathRootAsEntered(final String path)
    '''
def getFullPathFromRelativePath():
    '''public String getFullPathFromRelativePath(final String path, final String rootKey, final UserInfo ui)
    '''
def getDefaultFilePath():
    '''public String getDefaultFilePath(final String doctype, final UserInfo userInfo)
    '''
def copyAssocDoclinks():
    '''public void copyAssocDoclinks(final MboSetRemote sourcelinks, final MboSetRemote targetLinks, final long targetId, final String targetMboName)
    '''
