def ():
    '''returns MetadataCache\n\n
    ()\n
    '''
def searchCache():
    '''returns MetadataCacheResults\n\n
    searchCache(final List<SourceInfo> list, final Constants.SourceOpType sourceOpType, final String s, final String s2)\n
    '''
def addToSourceCache():
    '''returns None\n\n
    addToSourceCache(final int n, final List<SourceInfo> list)\n
    '''
def addToStmtCache():
    '''returns None\n\n
    addToStmtCache(final int n, final String s)\n
    '''
def addToPackageInfoCache():
    '''returns None\n\n
    addToPackageInfoCache(final int i, final String s)\n
    '''
def addToSrcStmtCache():
    '''returns None\n\n
    addToSrcStmtCache(final int n, final int n2, final Constants.SourceOpType sourceOpType, final Integer n3)\n
    '''
def addToMetadataSourceStmtCache():
    '''returns None\n\n
    addToMetadataSourceStmtCache(final int i, final int j, final Integer n, final Integer n2)\n
    '''
def setAppKey():
    '''returns None\n\n
    setAppKey(final Integer appKey)\n
    '''
def getAppKey():
    '''returns Integer\n\n
    getAppKey()\n
    '''
def setProjectKey():
    '''returns None\n\n
    setProjectKey(final Integer projectKey)\n
    '''
def clearProjectKey():
    '''returns None\n\n
    clearProjectKey()\n
    '''
def setMetadataSourceKey():
    '''returns None\n\n
    setMetadataSourceKey(final Integer metadataSourceKey)\n
    '''
def setSavedExplainData():
    '''returns None\n\n
    setSavedExplainData(final SavedExplainData explainData)\n
    '''
def getExplainValuesFor():
    '''returns ExplainSQLInfo\n\n
    getExplainValuesFor(final String s)\n
    '''
def notifyKeysCreated():
    '''returns None\n\n
    notifyKeysCreated(final MetadataCacheResults metadataCacheResults)\n
    '''
def getMetadataSrcKey():
    '''returns Integer\n\n
    getMetadataSrcKey()\n
    '''
def getDbInfoCache():
    '''returns DbInfoCache\n\n
    getDbInfoCache()\n
    '''
def getSourceTableCache():
    '''returns SourceTableCache\n\n
    getSourceTableCache()\n
    '''
def getMetadataSourceStmtCache():
    '''returns MetadataSourceStmtCache\n\n
    getMetadataSourceStmtCache()\n
    '''
def add():
    '''returns None\n\n
    add(final int n, final String s)\n
    '''
def getKey():
    '''returns long\n\n
    getKey(final String s)\n
    '''
def addRelationship():
    '''returns None\n\n
    addRelationship(final int n, final Constants.SourceOpType sourceOpType, final int n2, final Integer n3)\n
    '''
def doesRelationshipExist():
    '''returns boolean\n\n
    doesRelationshipExist(final int n, final Constants.SourceOpType sourceOpType, final int n2, final Integer n3)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
