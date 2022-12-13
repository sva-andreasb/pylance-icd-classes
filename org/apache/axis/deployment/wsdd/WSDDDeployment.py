def deployHandler():
    '''    public void deployHandler(final WSDDHandler handler)
    '''
def deployTransport():
    '''    public void deployTransport(final WSDDTransport transport)
    '''
def deployService():
    '''    public void deployService(final WSDDService service)
    '''
def undeployHandler():
    '''    public void undeployHandler(final QName qname)
    '''
def undeployService():
    '''    public void undeployService(final QName qname)
    '''
def undeployTransport():
    '''    public void undeployTransport(final QName qname)
    '''
def deployTypeMapping():
    '''    public void deployTypeMapping(final WSDDTypeMapping typeMapping)
    '''
def WSDDDeployment():
    '''    public WSDDDeployment()
    public WSDDDeployment(final Element e)
    '''
def deployToRegistry():
    '''    public void deployToRegistry(final WSDDDeployment target)
    '''
def writeToContext():
    '''    public void writeToContext(final SerializationContext context)
    '''
def getGlobalConfiguration():
    '''    public WSDDGlobalConfiguration getGlobalConfiguration()
    '''
def setGlobalConfiguration():
    '''    public void setGlobalConfiguration(final WSDDGlobalConfiguration globalConfig)
    '''
def getTypeMappings():
    '''    public WSDDTypeMapping[] getTypeMappings()
    '''
def getServices():
    '''    public WSDDService[] getServices()
    '''
def getWSDDService():
    '''    public WSDDService getWSDDService(final QName qname)
    '''
def getHandler():
    '''    public Handler getHandler(final QName name)
    '''
def getTransport():
    '''    public Handler getTransport(final QName name)
    '''
def getService():
    '''    public SOAPService getService(final QName name)
    '''
def getServiceByNamespaceURI():
    '''    public SOAPService getServiceByNamespaceURI(final String namespace)
    '''
def configureEngine():
    '''    public void configureEngine(final AxisEngine engine)
    '''
def writeEngineConfig():
    '''    public void writeEngineConfig(final AxisEngine engine)
    '''
def getTypeMapping():
    '''    public TypeMapping getTypeMapping(final String encodingStyle)
    '''
def getTypeMappingRegistry():
    '''    public TypeMappingRegistry getTypeMappingRegistry()
    '''
def getGlobalRequest():
    '''    public Handler getGlobalRequest()
    '''
def getGlobalResponse():
    '''    public Handler getGlobalResponse()
    '''
def getGlobalOptions():
    '''    public Hashtable getGlobalOptions()
    '''
def getRoles():
    '''    public List getRoles()
    '''
def getDeployedServices():
    '''    public Iterator getDeployedServices()
    '''
def registerNamespaceForService():
    '''    public void registerNamespaceForService(final String namespace, final WSDDService service)
    '''
def removeNamespaceMapping():
    '''    public void removeNamespaceMapping(final String namespace)
    '''
def getEngine():
    '''    public AxisEngine getEngine()
    '''
def getDeployment():
    '''    public WSDDDeployment getDeployment()
    '''
def getHandlers():
    '''    public WSDDHandler[] getHandlers()
    '''
def getWSDDHandler():
    '''    public WSDDHandler getWSDDHandler(final QName qname)
    '''
def getTransports():
    '''    public WSDDTransport[] getTransports()
    '''
def getWSDDTransport():
    '''    public WSDDTransport getWSDDTransport(final QName qname)
    '''
