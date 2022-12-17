def ():
    '''returns SimpleProvider\n\n
    ()\n
    (final EngineConfiguration defaultConfiguration)\n
    (final TypeMappingRegistry typeMappingRegistry)\n
    '''
def configureEngine():
    '''returns None\n\n
    configureEngine(final AxisEngine engine)\n
    '''
def writeEngineConfig():
    '''returns None\n\n
    writeEngineConfig(final AxisEngine engine)\n
    '''
def getGlobalOptions():
    '''returns Hashtable\n\n
    getGlobalOptions()\n
    '''
def setGlobalOptions():
    '''returns None\n\n
    setGlobalOptions(final Hashtable options)\n
    '''
def getGlobalRequest():
    '''returns Handler\n\n
    getGlobalRequest()\n
    '''
def setGlobalRequest():
    '''returns None\n\n
    setGlobalRequest(final Handler globalRequest)\n
    '''
def getGlobalResponse():
    '''returns Handler\n\n
    getGlobalResponse()\n
    '''
def setGlobalResponse():
    '''returns None\n\n
    setGlobalResponse(final Handler globalResponse)\n
    '''
def getTypeMappingRegistry():
    '''returns TypeMappingRegistry\n\n
    getTypeMappingRegistry()\n
    '''
def getTypeMapping():
    '''returns TypeMapping\n\n
    getTypeMapping(final String encodingStyle)\n
    '''
def getTransport():
    '''returns Handler\n\n
    getTransport(final QName qname)\n
    '''
def getService():
    '''returns SOAPService\n\n
    getService(final QName qname)\n
    '''
def getServiceByNamespaceURI():
    '''returns SOAPService\n\n
    getServiceByNamespaceURI(final String namespace)\n
    '''
def getHandler():
    '''returns Handler\n\n
    getHandler(final QName qname)\n
    '''
def deployService():
    '''returns None\n\n
    deployService(final QName qname, final SOAPService service)\n
    deployService(final String name, final SOAPService service)\n
    '''
def deployTransport():
    '''returns None\n\n
    deployTransport(final QName qname, final Handler transport)\n
    deployTransport(final String name, final Handler transport)\n
    '''
def getDeployedServices():
    '''returns Iterator\n\n
    getDeployedServices()\n
    '''
def setRoles():
    '''returns None\n\n
    setRoles(final List roles)\n
    '''
def addRole():
    '''returns None\n\n
    addRole(final String role)\n
    '''
def removeRole():
    '''returns None\n\n
    removeRole(final String role)\n
    '''
def getRoles():
    '''returns List\n\n
    getRoles()\n
    '''
