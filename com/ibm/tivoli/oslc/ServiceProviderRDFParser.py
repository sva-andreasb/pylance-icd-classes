def ServiceProviderRDFParser():
'''public ServiceProviderRDFParser(final byte[] rdfDoc, final String resURI)
public ServiceProviderRDFParser(final Model spModel, final String resURI)
public ServiceProviderRDFParser(final Resource spResource)
'''
pass
def getURI():
'''public String getURI()
'''
pass
def getServicesForDomain():
'''public List<Resource> getServicesForDomain(final String domURI)
'''
pass
def getService():
'''public Resource getService()
'''
pass
def getSourceRecordURI():
'''public String getSourceRecordURI()
'''
pass
def getQueryCapabilities():
'''public List<Resource> getQueryCapabilities(final String domURI, final String resTypeURI)
public List<Resource> getQueryCapabilities(final Resource svcRes, final String resTypeURI)
'''
pass
def getCreationFactories():
'''public List<Resource> getCreationFactories(final String domURI, final String resTypeURI)
public List<Resource> getCreationFactories(final Resource svcRes, final String resTypeURI)
'''
pass
def getAPIResourceCollection():
'''public List<Resource> getAPIResourceCollection(final Resource svcRes, final String resTypeURI, final Property apiProp)
'''
pass
def getUsageURI():
'''public List<String> getUsageURI(final Resource oslcOp)
'''
pass
def getQueryBaseURI():
'''public String getQueryBaseURI(final Resource queryCapabilityRes)
'''
pass
def getCreationURI():
'''public String getCreationURI(final Resource cfRes)
'''
pass
def getNsPrefixMap():
'''public Map<String, String> getNsPrefixMap()
'''
pass
def getPrefixNsMap():
'''public Map<String, String> getPrefixNsMap()
'''
pass
