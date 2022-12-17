def getWSDLParser():
    '''returns Parser\n\n
    getWSDLParser()\n
    '''
def ():
    '''returns Service\n\n
    ()\n
    (final QName serviceName)\n
    (final EngineConfiguration engineConfiguration, final AxisClient axisClient)\n
    (final EngineConfiguration config)\n
    (final URL wsdlDoc, final QName serviceName)\n
    (final Parser parser, final QName serviceName)\n
    (final String wsdlLocation, final QName serviceName)\n
    (final InputStream wsdlInputStream, final QName serviceName)\n
    '''
def getPort():
    '''returns Remote\n\n
    getPort(final QName portName, final Class proxyInterface)\n
    getPort(final Class proxyInterface)\n
    getPort(final String endpoint, final Class proxyInterface)\n
    '''
def getHandlerRegistry():
    '''returns HandlerRegistry\n\n
    getHandlerRegistry()\n
    '''
def getWSDLDocumentLocation():
    '''returns URL\n\n
    getWSDLDocumentLocation()\n
    '''
def getServiceName():
    '''returns QName\n\n
    getServiceName()\n
    '''
def getPorts():
    '''returns Iterator\n\n
    getPorts()\n
    '''
def setTypeMappingRegistry():
    '''returns None\n\n
    setTypeMappingRegistry(final TypeMappingRegistry registry)\n
    '''
def getTypeMappingRegistry():
    '''returns TypeMappingRegistry\n\n
    getTypeMappingRegistry()\n
    '''
def getReference():
    '''returns Reference\n\n
    getReference()\n
    '''
def setEngine():
    '''returns None\n\n
    setEngine(final AxisEngine engine)\n
    '''
def getEngine():
    '''returns AxisEngine\n\n
    getEngine()\n
    '''
def setEngineConfiguration():
    '''returns None\n\n
    setEngineConfiguration(final EngineConfiguration config)\n
    '''
def setMaintainSession():
    '''returns None\n\n
    setMaintainSession(final boolean yesno)\n
    '''
def getMaintainSession():
    '''returns boolean\n\n
    getMaintainSession()\n
    '''
def getCall():
    '''returns Call\n\n
    getCall()\n
    '''
def getCacheWSDL():
    '''returns boolean\n\n
    getCacheWSDL()\n
    '''
def setCacheWSDL():
    '''returns None\n\n
    setCacheWSDL(final boolean flag)\n
    '''
def setTypeMappingVersion():
    '''returns None\n\n
    setTypeMappingVersion(final String version)\n
    '''
def getHandlerChain():
    '''returns List\n\n
    getHandlerChain(final QName portName)\n
    '''
def setHandlerChain():
    '''returns None\n\n
    setHandlerChain(final QName portName, final List chain)\n
    '''
