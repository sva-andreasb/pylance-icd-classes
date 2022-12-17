def setNewMboAction():
    '''returns None\n\n
    setNewMboAction(final boolean newMboAction)\n
    '''
def getContentType():
    '''returns String\n\n
    getContentType()\n
    '''
def setIgnoreCollectionRefs():
    '''returns None\n\n
    setIgnoreCollectionRefs(final boolean ignoreCollectionRefs)\n
    '''
def setIgnorePrefixMeta():
    '''returns None\n\n
    setIgnorePrefixMeta(final boolean ignorePrefixMeta)\n
    '''
def getMaxRowStamp():
    '''returns Long\n\n
    getMaxRowStamp()\n
    '''
def ():
    '''returns OSOslcJsonSerializer\n\n
    (final String osName, final OslcRequest oslcRequest, final Map<String, JSONObject> linkedResourceCache)\n
    (final String osName, final OslcRequest oslcRequest, final boolean leanJson)\n
    '''
def serializeWalkUpChildMbo():
    '''returns OslcResourceResponse\n\n
    serializeWalkUpChildMbo(final MboRemote mr)\n
    '''
def serializeResolvedResource():
    '''returns OslcResourceResponse\n\n
    serializeResolvedResource(final LocalURIResolver.ResolvedResource rr)\n
    '''
def setObjectID():
    '''returns None\n\n
    setObjectID(final JSONObject mboOjo, final MboRemote mbo, final MosDetailInfo oslcResInfo)\n
    '''
def serializeResourceAsObject():
    '''returns JSONObject\n\n
    serializeResourceAsObject(final MboIterator mboSet)\n
    serializeResourceAsObject(final Mbo mbo)\n
    '''
def serializeResource():
    '''returns OslcResourceResponse\n\n
    serializeResource(final MboIterator mboSet)\n
    serializeResource(final Mbo mbo)\n
    '''
def useThisResourceProperties():
    '''returns None\n\n
    useThisResourceProperties(final Map<String, OslcResourceProperty> resourceProperties)\n
    '''
def serializeAttachment():
    '''returns OslcResourceResponse\n\n
    serializeAttachment(final MboSetRemote attachments, final OslcResourceDetailInfo resDetInfo)\n
    serializeAttachment(final MboRemote attachment, final OslcResourceDetailInfo resDetInfo, final boolean meta, final boolean thumbNail)\n
    '''
def overrideResourceURI():
    '''returns None\n\n
    overrideResourceURI(final String resURI)\n
    '''
def isBranchFilterOn():
    '''returns boolean\n\n
    isBranchFilterOn()\n
    '''
def isAllowedBranchObject():
    '''returns boolean\n\n
    isAllowedBranchObject(final MboRemote mbo)\n
    '''
def isAllowedBranchObjectType():
    '''returns boolean\n\n
    isAllowedBranchObjectType(final String mboName)\n
    '''
