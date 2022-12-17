URLTYPE_FILE = "String  \"FILE\""
URLTYPE_WWW = "String  \"WWW\""
URLTYPE_DMS = "String  \"DMS\""
def ():
    '''returns DoclinkService\n\n
    ()\n
    (final MXServer mxServer)\n
    '''
def doclinkExists():
    '''returns boolean\n\n
    doclinkExists(final String keytable, final String keycolumn, final String keyvalue, final UserInfo userInfo)\n
    '''
def getAppDoctypeLinks():
    '''returns TreeMap\n\n
    getAppDoctypeLinks(final String appName, final String keyTable, final String keyColumn, final int keyValue, final UserInfo userInfo)\n
    '''
def addDocinfoAndLinks():
    '''returns MboSetRemote\n\n
    addDocinfoAndLinks(final String urlname, final String description, final String[] urlparam, final String doctype, final String urltype, final String keytable, final String keycolumn, final String[] keyvalue, final boolean forceAutokey, final String application, final UserInfo userInfo)\n
    addDocinfoAndLinks(final String urlname, final String description, final String assetType, final String[] keyvalue, final UserInfo userInfo)\n
    '''
def getFullPathFromRelativePath():
    '''returns String\n\n
    getFullPathFromRelativePath(final String path, final String rootKey, final UserInfo ui)\n
    '''
def getDefaultFilePath():
    '''returns String\n\n
    getDefaultFilePath(final String doctype, final UserInfo userInfo)\n
    '''
def copyAssocDoclinks():
    '''returns None\n\n
    copyAssocDoclinks(final MboSetRemote sourcelinks, final MboSetRemote targetLinks, final long targetId, final String targetMboName)\n
    '''
