def ():
    '''returns OslcInteractionProcessor\n\n
    (final OslcEndPointData epData, final String interactionName, final MboRemote mbo)\n
    (final String providerName)\n
    (final OslcEndPointData epData)\n
    (final OslcEndPointData epData, final MboRemote mbo, final String updatePropName, final String updatePropNs)\n
    '''
def getServiceProviders():
    '''returns List<OslcServiceProviderInfo>\n\n
    getServiceProviders()\n
    '''
def fetchQueryResult():
    '''returns None\n\n
    fetchQueryResult(final OslcEndPointData epData, final String spURI, MboSetRemote oslcResultSetRemote)\n
    '''
def fetchQueryCollection():
    '''returns Resource\n\n
    fetchQueryCollection(final OslcEndPointData epData, String spURI)\n
    '''
def isPreferProviderDescForRRURI():
    '''returns boolean\n\n
    isPreferProviderDescForRRURI(final String desc)\n
    '''
def getDialog():
    '''returns OslcDialogInfo\n\n
    getDialog(final OslcEndPointData epData, final String spURI)\n
    '''
def nativePreview():
    '''returns None\n\n
    nativePreview(final String resourceURI, final MboRemote linkMbo)\n
    '''
def getPreviewDialog():
    '''returns OslcDialogInfo\n\n
    getPreviewDialog(final String resourceURI)\n
    '''
def createOslcLinkFromEvent():
    '''returns None\n\n
    createOslcLinkFromEvent(final String event, final OslcServiceProviderInfo selectedServiceProviderInfo)\n
    '''
def updateLinkedResource():
    '''returns None\n\n
    updateLinkedResource(final String contextPath)\n
    '''
def deleteAssociation():
    '''returns None\n\n
    deleteAssociation(final String contextPath, final String linkedResourceURI)\n
    '''
def getResource():
    '''returns OslcResource\n\n
    getResource(final String uri, final Locale locale, final boolean errorOnStatus)\n
    getResource(final String uri, final Locale locale, final boolean errorOnStatus, final Map<String, Object> metaDataForProvider)\n
    '''
