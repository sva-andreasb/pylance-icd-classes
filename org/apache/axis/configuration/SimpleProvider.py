def SimpleProvider():
    '''    public SimpleProvider()
    public SimpleProvider(final EngineConfiguration defaultConfiguration)
    public SimpleProvider(final TypeMappingRegistry typeMappingRegistry)
    '''
def configureEngine():
    '''    public void configureEngine(final AxisEngine engine)
    '''
def writeEngineConfig():
    '''    public void writeEngineConfig(final AxisEngine engine)
    '''
def getGlobalOptions():
    '''    public Hashtable getGlobalOptions()
    '''
def setGlobalOptions():
    '''    public void setGlobalOptions(final Hashtable options)
    '''
def getGlobalRequest():
    '''    public Handler getGlobalRequest()
    '''
def setGlobalRequest():
    '''    public void setGlobalRequest(final Handler globalRequest)
    '''
def getGlobalResponse():
    '''    public Handler getGlobalResponse()
    '''
def setGlobalResponse():
    '''    public void setGlobalResponse(final Handler globalResponse)
    '''
def getTypeMappingRegistry():
    '''    public TypeMappingRegistry getTypeMappingRegistry()
    '''
def getTypeMapping():
    '''    public TypeMapping getTypeMapping(final String encodingStyle)
    '''
def getTransport():
    '''    public Handler getTransport(final QName qname)
    '''
def getService():
    '''    public SOAPService getService(final QName qname)
    '''
def getServiceByNamespaceURI():
    '''    public SOAPService getServiceByNamespaceURI(final String namespace)
    '''
def getHandler():
    '''    public Handler getHandler(final QName qname)
    '''
def deployService():
    '''    public void deployService(final QName qname, final SOAPService service)
    public void deployService(final String name, final SOAPService service)
    '''
def deployTransport():
    '''    public void deployTransport(final QName qname, final Handler transport)
    public void deployTransport(final String name, final Handler transport)
    '''
def getDeployedServices():
    '''    public Iterator getDeployedServices()
    '''
def setRoles():
    '''    public void setRoles(final List roles)
    '''
def addRole():
    '''    public void addRole(final String role)
    '''
def removeRole():
    '''    public void removeRole(final String role)
    '''
def getRoles():
    '''    public List getRoles()
    '''
