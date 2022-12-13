def SimpleProvider():
'''public SimpleProvider()
public SimpleProvider(final EngineConfiguration defaultConfiguration)
public SimpleProvider(final TypeMappingRegistry typeMappingRegistry)
'''
pass
def configureEngine():
'''public void configureEngine(final AxisEngine engine)
'''
pass
def writeEngineConfig():
'''public void writeEngineConfig(final AxisEngine engine)
'''
pass
def getGlobalOptions():
'''public Hashtable getGlobalOptions()
'''
pass
def setGlobalOptions():
'''public void setGlobalOptions(final Hashtable options)
'''
pass
def getGlobalRequest():
'''public Handler getGlobalRequest()
'''
pass
def setGlobalRequest():
'''public void setGlobalRequest(final Handler globalRequest)
'''
pass
def getGlobalResponse():
'''public Handler getGlobalResponse()
'''
pass
def setGlobalResponse():
'''public void setGlobalResponse(final Handler globalResponse)
'''
pass
def getTypeMappingRegistry():
'''public TypeMappingRegistry getTypeMappingRegistry()
'''
pass
def getTypeMapping():
'''public TypeMapping getTypeMapping(final String encodingStyle)
'''
pass
def getTransport():
'''public Handler getTransport(final QName qname)
'''
pass
def getService():
'''public SOAPService getService(final QName qname)
'''
pass
def getServiceByNamespaceURI():
'''public SOAPService getServiceByNamespaceURI(final String namespace)
'''
pass
def getHandler():
'''public Handler getHandler(final QName qname)
'''
pass
def deployService():
'''public void deployService(final QName qname, final SOAPService service)
public void deployService(final String name, final SOAPService service)
'''
pass
def deployTransport():
'''public void deployTransport(final QName qname, final Handler transport)
public void deployTransport(final String name, final Handler transport)
'''
pass
def getDeployedServices():
'''public Iterator getDeployedServices()
'''
pass
def setRoles():
'''public void setRoles(final List roles)
'''
pass
def addRole():
'''public void addRole(final String role)
'''
pass
def removeRole():
'''public void removeRole(final String role)
'''
pass
def getRoles():
'''public List getRoles()
'''
pass
