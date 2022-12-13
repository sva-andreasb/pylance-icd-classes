def getWSDLParser():
'''public Parser getWSDLParser()
'''
pass
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
pass
def getPort():
'''public Remote getPort(final QName portName, final Class proxyInterface)
public Remote getPort(final Class proxyInterface)
public Remote getPort(final String endpoint, final Class proxyInterface)
'''
pass
def getHandlerRegistry():
'''public HandlerRegistry getHandlerRegistry()
'''
pass
def getWSDLDocumentLocation():
'''public URL getWSDLDocumentLocation()
'''
pass
def getServiceName():
'''public QName getServiceName()
'''
pass
def getPorts():
'''public Iterator getPorts()
'''
pass
def setTypeMappingRegistry():
'''public void setTypeMappingRegistry(final TypeMappingRegistry registry)
'''
pass
def getTypeMappingRegistry():
'''public TypeMappingRegistry getTypeMappingRegistry()
'''
pass
def getReference():
'''public Reference getReference()
'''
pass
def setEngine():
'''public void setEngine(final AxisEngine engine)
'''
pass
def getEngine():
'''public AxisEngine getEngine()
'''
pass
def setEngineConfiguration():
'''public void setEngineConfiguration(final EngineConfiguration config)
'''
pass
def setMaintainSession():
'''public void setMaintainSession(final boolean yesno)
'''
pass
def getMaintainSession():
'''public boolean getMaintainSession()
'''
pass
def getCall():
'''public Call getCall()
'''
pass
def getCacheWSDL():
'''public boolean getCacheWSDL()
'''
pass
def setCacheWSDL():
'''public void setCacheWSDL(final boolean flag)
'''
pass
def setTypeMappingVersion():
'''public void setTypeMappingVersion(final String version)
'''
pass
def getHandlerChain():
'''public List getHandlerChain(final QName portName)
'''
pass
def setHandlerChain():
'''public void setHandlerChain(final QName portName, final List chain)
'''
pass
