def ():
    '''returns FileProvider\n\n
    (final String filename)\n
    (final String basepath, final String filename)\n
    (final InputStream is)\n
    '''
def setInputStream():
    '''returns None\n\n
    setInputStream(final InputStream is)\n
    '''
def getDeployment():
    '''returns WSDDDeployment\n\n
    getDeployment()\n
    '''
def setDeployment():
    '''returns None\n\n
    setDeployment(final WSDDDeployment deployment)\n
    '''
def setSearchClasspath():
    '''returns None\n\n
    setSearchClasspath(final boolean searchClasspath)\n
    '''
def configureEngine():
    '''returns None\n\n
    configureEngine(final AxisEngine engine)\n
    '''
def writeEngineConfig():
    '''returns None\n\n
    writeEngineConfig(final AxisEngine engine)\n
    '''
def getHandler():
    '''returns Handler\n\n
    getHandler(final QName qname)\n
    '''
def getService():
    '''returns SOAPService\n\n
    getService(final QName qname)\n
    '''
def getServiceByNamespaceURI():
    '''returns SOAPService\n\n
    getServiceByNamespaceURI(final String namespace)\n
    '''
def getTransport():
    '''returns Handler\n\n
    getTransport(final QName qname)\n
    '''
def getTypeMappingRegistry():
    '''returns TypeMappingRegistry\n\n
    getTypeMappingRegistry()\n
    '''
def getGlobalRequest():
    '''returns Handler\n\n
    getGlobalRequest()\n
    '''
def getGlobalResponse():
    '''returns Handler\n\n
    getGlobalResponse()\n
    '''
def getGlobalOptions():
    '''returns Hashtable\n\n
    getGlobalOptions()\n
    '''
def getDeployedServices():
    '''returns Iterator\n\n
    getDeployedServices()\n
    '''
def getRoles():
    '''returns List\n\n
    getRoles()\n
    '''
