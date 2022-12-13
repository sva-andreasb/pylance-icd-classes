def setNewMboAction():
    '''    public void setNewMboAction(final boolean newMboAction)
    '''
def getContentType():
    '''    public String getContentType()
    '''
def setIgnoreCollectionRefs():
    '''    public void setIgnoreCollectionRefs(final boolean ignoreCollectionRefs)
    '''
def setIgnorePrefixMeta():
    '''    public void setIgnorePrefixMeta(final boolean ignorePrefixMeta)
    '''
def getMaxRowStamp():
    '''    public Long getMaxRowStamp()
    '''
def OSOslcJsonSerializer():
    '''    public OSOslcJsonSerializer(final String osName, final OslcRequest oslcRequest, final Map<String, JSONObject> linkedResourceCache)
    public OSOslcJsonSerializer(final String osName, final OslcRequest oslcRequest, final boolean leanJson)
    '''
def serializeWalkUpChildMbo():
    '''    public OslcResourceResponse serializeWalkUpChildMbo(final MboRemote mr)
    '''
def serializeResolvedResource():
    '''    public OslcResourceResponse serializeResolvedResource(final LocalURIResolver.ResolvedResource rr)
    '''
def setObjectID():
    '''    public void setObjectID(final JSONObject mboOjo, final MboRemote mbo, final MosDetailInfo oslcResInfo)
    '''
def serializeResourceAsObject():
    '''    public JSONObject serializeResourceAsObject(final MboIterator mboSet)
    public JSONObject serializeResourceAsObject(final Mbo mbo)
    '''
def serializeResource():
    '''    public OslcResourceResponse serializeResource(final MboIterator mboSet)
    public OslcResourceResponse serializeResource(final Mbo mbo)
    '''
def useThisResourceProperties():
    '''    public void useThisResourceProperties(final Map<String, OslcResourceProperty> resourceProperties)
    '''
def serializeAttachment():
    '''    public OslcResourceResponse serializeAttachment(final MboSetRemote attachments, final OslcResourceDetailInfo resDetInfo)
    public OslcResourceResponse serializeAttachment(final MboRemote attachment, final OslcResourceDetailInfo resDetInfo, final boolean meta, final boolean thumbNail)
    '''
def overrideResourceURI():
    '''    public void overrideResourceURI(final String resURI)
    '''
def isBranchFilterOn():
    '''    public boolean isBranchFilterOn()
    '''
def isAllowedBranchObject():
    '''    public boolean isAllowedBranchObject(final MboRemote mbo)
    '''
def isAllowedBranchObjectType():
    '''    public boolean isAllowedBranchObjectType(final String mboName)
    '''
