def ():
    '''returns ServiceProviderRDFParser\n\n
    (final byte[] rdfDoc, final String resURI)\n
    (final Model spModel, final String resURI)\n
    (final Resource spResource)\n
    '''
def getURI():
    '''returns String\n\n
    getURI()\n
    '''
def getServicesForDomain():
    '''returns List<Resource>\n\n
    getServicesForDomain(final String domURI)\n
    '''
def getService():
    '''returns Resource\n\n
    getService()\n
    '''
def getSourceRecordURI():
    '''returns String\n\n
    getSourceRecordURI()\n
    '''
def getQueryCapabilities():
    '''returns List<Resource>\n\n
    getQueryCapabilities(final String domURI, final String resTypeURI)\n
    getQueryCapabilities(final Resource svcRes, final String resTypeURI)\n
    '''
def getCreationFactories():
    '''returns List<Resource>\n\n
    getCreationFactories(final String domURI, final String resTypeURI)\n
    getCreationFactories(final Resource svcRes, final String resTypeURI)\n
    '''
def getAPIResourceCollection():
    '''returns List<Resource>\n\n
    getAPIResourceCollection(final Resource svcRes, final String resTypeURI, final Property apiProp)\n
    '''
def getUsageURI():
    '''returns List<String>\n\n
    getUsageURI(final Resource oslcOp)\n
    '''
def getQueryBaseURI():
    '''returns String\n\n
    getQueryBaseURI(final Resource queryCapabilityRes)\n
    '''
def getCreationURI():
    '''returns String\n\n
    getCreationURI(final Resource cfRes)\n
    '''
