def ():
    '''returns LocalURIResolver\n\n
    (final String resourceId, final String osName)\n
    (final String uri, final boolean create)\n
    (final String uri)\n
    ()\n
    (final boolean resolveRootCollection)\n
    (final String uri, final Map<String, String> keyMap, final UserInfo userInfo)\n
    (final String uri, final boolean create, final boolean fillKeyMap)\n
    (final String uri, final Map<String, String> keyMap, final String key, final UserInfo userInfo)\n
    '''
def isAttachment():
    '''returns boolean\n\n
    isAttachment(final MboRemote mbo, final String relation)\n
    isAttachment()\n
    '''
def resolvePath():
    '''returns ResolvedResource\n\n
    resolvePath(final String osName, final String localURI, final OslcRequest oslcRequest)\n
    resolvePath(String osName, final List<String> resPath, final OslcRequest oslcRequest)\n
    '''
def isScript():
    '''returns boolean\n\n
    isScript()\n
    '''
def getMboForURI():
    '''returns MboRemote\n\n
    getMboForURI(final UserInfo userInfo)\n
    '''
def getMboForUniformId():
    '''returns MboRemote\n\n
    getMboForUniformId(final String primaryMboName, final UserInfo userInfo)\n
    getMboForUniformId(final MboSetRemote mboSet, final OslcRequest oslcRequest)\n
    '''
def getResourceId():
    '''returns String\n\n
    getResourceId()\n
    '''
def getOSName():
    '''returns String\n\n
    getOSName()\n
    '''
def getKeyValue():
    '''returns Object\n\n
    getKeyValue()\n
    '''
def isIdURI():
    '''returns boolean\n\n
    isIdURI()\n
    '''
def getMboName():
    '''returns String\n\n
    getMboName()\n
    '''
def setMboName():
    '''returns None\n\n
    setMboName(final String mboName)\n
    '''
def getId():
    '''returns String\n\n
    getId()\n
    '''
def setId():
    '''returns None\n\n
    setId(final String id)\n
    '''
def getOsName():
    '''returns String\n\n
    getOsName()\n
    getOsName()\n
    '''
def setOsName():
    '''returns None\n\n
    setOsName(final String osName)\n
    '''
def isResourceNotModified():
    '''returns boolean\n\n
    isResourceNotModified()\n
    '''
def isQueryWhereApplied():
    '''returns boolean\n\n
    isQueryWhereApplied()\n
    '''
def setQueryWhereApplied():
    '''returns None\n\n
    setQueryWhereApplied()\n
    '''
def getLookupSrcAttr():
    '''returns String\n\n
    getLookupSrcAttr()\n
    '''
def isExtRes():
    '''returns boolean\n\n
    isExtRes()\n
    '''
def isCacheIt():
    '''returns boolean\n\n
    isCacheIt()\n
    '''
def getETag():
    '''returns String\n\n
    getETag()\n
    '''
def isThumbNail():
    '''returns boolean\n\n
    isThumbNail()\n
    '''
def getJSON():
    '''returns JSONArtifact\n\n
    getJSON()\n
    '''
def getParentPath():
    '''returns String\n\n
    getParentPath()\n
    '''
def getOSRootMbo():
    '''returns Mbo\n\n
    getOSRootMbo()\n
    '''
def setOslcResourceDetailInfo():
    '''returns None\n\n
    setOslcResourceDetailInfo(final OslcResourceDetailInfo detInfo)\n
    '''
def getOslcResourceDetailInfo():
    '''returns OslcResourceDetailInfo\n\n
    getOslcResourceDetailInfo()\n
    '''
def isCollection():
    '''returns boolean\n\n
    isCollection()\n
    '''
def isRelatedMboResource():
    '''returns boolean\n\n
    isRelatedMboResource()\n
    '''
def isMeta():
    '''returns boolean\n\n
    isMeta()\n
    '''
def getMbo():
    '''returns MboRemote\n\n
    getMbo()\n
    '''
def getMboSet():
    '''returns MboSetRemote\n\n
    getMboSet()\n
    '''
def getOverriddenCount():
    '''returns int\n\n
    getOverriddenCount()\n
    '''
def isSelfRefPrimary():
    '''returns boolean\n\n
    isSelfRefPrimary()\n
    '''
