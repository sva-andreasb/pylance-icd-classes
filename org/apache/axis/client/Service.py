def getWSDLParser():
    '''public Parser getWSDLParser()
    '''
def Service():
    '''public Service()
    public Service(final QName serviceName)
    public Service(final EngineConfiguration engineConfiguration, final AxisClient axisClient)
    public Service(final EngineConfiguration config)
    public Service(final URL wsdlDoc, final QName serviceName)
    public Service(final Parser parser, final QName serviceName)
    public Service(final String wsdlLocation, final QName serviceName)
    public Service(final InputStream wsdlInputStream, final QName serviceName)
    '''
def getPort():
    '''public Remote getPort(final QName portName, final Class proxyInterface)
    public Remote getPort(final Class proxyInterface)
    public Remote getPort(final String endpoint, final Class proxyInterface)
    '''
def getHandlerRegistry():
    '''public HandlerRegistry getHandlerRegistry()
    '''
def getWSDLDocumentLocation():
    '''public URL getWSDLDocumentLocation()
    '''
def getServiceName():
    '''public QName getServiceName()
    '''
def getPorts():
    '''public Iterator getPorts()
    '''
def setTypeMappingRegistry():
    '''public void setTypeMappingRegistry(final TypeMappingRegistry registry)
    '''
def getTypeMappingRegistry():
    '''public TypeMappingRegistry getTypeMappingRegistry()
    '''
def getReference():
    '''public Reference getReference()
    '''
def setEngine():
    '''public void setEngine(final AxisEngine engine)
    '''
def getEngine():
    '''public AxisEngine getEngine()
    '''
def setEngineConfiguration():
    '''public void setEngineConfiguration(final EngineConfiguration config)
    '''
def setMaintainSession():
    '''public void setMaintainSession(final boolean yesno)
    '''
def getMaintainSession():
    '''public boolean getMaintainSession()
    '''
def getCall():
    '''public Call getCall()
    '''
def getCacheWSDL():
    '''public boolean getCacheWSDL()
    '''
def setCacheWSDL():
    '''public void setCacheWSDL(final boolean flag)
    '''
def setTypeMappingVersion():
    '''public void setTypeMappingVersion(final String version)
    '''
def getHandlerChain():
    '''public List getHandlerChain(final QName portName)
    '''
def setHandlerChain():
    '''public void setHandlerChain(final QName portName, final List chain)
    '''
