def ServiceProviderRDFParser():
    '''    public ServiceProviderRDFParser(final byte[] rdfDoc, final String resURI)
    public ServiceProviderRDFParser(final Model spModel, final String resURI)
    public ServiceProviderRDFParser(final Resource spResource)
    '''
def getURI():
    '''    public String getURI()
    '''
def getServicesForDomain():
    '''    public List<Resource> getServicesForDomain(final String domURI)
    '''
def getService():
    '''    public Resource getService()
    '''
def getSourceRecordURI():
    '''    public String getSourceRecordURI()
    '''
def getQueryCapabilities():
    '''    public List<Resource> getQueryCapabilities(final String domURI, final String resTypeURI)
    public List<Resource> getQueryCapabilities(final Resource svcRes, final String resTypeURI)
    '''
def getCreationFactories():
    '''    public List<Resource> getCreationFactories(final String domURI, final String resTypeURI)
    public List<Resource> getCreationFactories(final Resource svcRes, final String resTypeURI)
    '''
def getAPIResourceCollection():
    '''    public List<Resource> getAPIResourceCollection(final Resource svcRes, final String resTypeURI, final Property apiProp)
    '''
def getUsageURI():
    '''    public List<String> getUsageURI(final Resource oslcOp)
    '''
def getQueryBaseURI():
    '''    public String getQueryBaseURI(final Resource queryCapabilityRes)
    '''
def getCreationURI():
    '''    public String getCreationURI(final Resource cfRes)
    '''
def getNsPrefixMap():
    '''    public Map<String, String> getNsPrefixMap()
    '''
def getPrefixNsMap():
    '''    public Map<String, String> getPrefixNsMap()
    '''
