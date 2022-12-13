def OslcInteractionProcessor():
    '''public OslcInteractionProcessor(final OslcEndPointData epData, final String interactionName, final MboRemote mbo)
    public OslcInteractionProcessor(final String providerName)
    public OslcInteractionProcessor(final OslcEndPointData epData)
    public OslcInteractionProcessor(final OslcEndPointData epData, final MboRemote mbo, final String updatePropName, final String updatePropNs)
    '''
def getServiceProviders():
    '''public List<OslcServiceProviderInfo> getServiceProviders()
    '''
def fetchQueryResult():
    '''public void fetchQueryResult(final OslcEndPointData epData, final String spURI, MboSetRemote oslcResultSetRemote)
    '''
def fetchQueryCollection():
    '''public Resource fetchQueryCollection(final OslcEndPointData epData, String spURI)
    '''
def isPreferProviderDescForRRURI():
    '''public boolean isPreferProviderDescForRRURI(final String desc)
    '''
def getDialog():
    '''public OslcDialogInfo getDialog(final OslcEndPointData epData, final String spURI)
    '''
def nativePreview():
    '''public void nativePreview(final String resourceURI, final MboRemote linkMbo)
    '''
def getPreviewDialog():
    '''public OslcDialogInfo getPreviewDialog(final String resourceURI)
    '''
def createOslcLinkFromEvent():
    '''public void createOslcLinkFromEvent(final String event, final OslcServiceProviderInfo selectedServiceProviderInfo)
    '''
def updateLinkedResource():
    '''public void updateLinkedResource(final String contextPath)
    '''
def deleteAssociation():
    '''public void deleteAssociation(final String contextPath, final String linkedResourceURI)
    '''
def createResource():
    '''public Map<String, Object> createResource(final String resTypeURI, final Resource res, final Locale locale, final boolean errorOnStatus)
    public Map<String, Object> createResource(String resTypeURI, final Resource res, final Locale locale, final boolean errorOnStatus, final Map<String, Object> metaDataForProvider)
    '''
def getResource():
    '''public OslcResource getResource(final String uri, final Locale locale, final boolean errorOnStatus)
    public OslcResource getResource(final String uri, final Locale locale, final boolean errorOnStatus, final Map<String, Object> metaDataForProvider)
    '''
def updateResource():
    '''public Map<String, Object> updateResource(final Resource res, final String etag, final Locale locale, final boolean errorOnStatus)
    public Map<String, Object> updateResource(final Resource res, final String etag, final Locale locale, final boolean errorOnStatus, final Map<String, Object> metaDataForProvider)
    '''
def deleteResource():
    '''public Map<String, Object> deleteResource(final String resURI, final String etag, final boolean errorOnStatus)
    public Map<String, Object> deleteResource(final String resURI, final String etag, final boolean errorOnStatus, final Map<String, Object> metaDataForProvider)
    '''
