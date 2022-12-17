def deployHandler():
    '''returns None\n\n
    deployHandler(final WSDDHandler handler)\n
    '''
def deployTransport():
    '''returns None\n\n
    deployTransport(final WSDDTransport transport)\n
    '''
def deployService():
    '''returns None\n\n
    deployService(final WSDDService service)\n
    '''
def undeployHandler():
    '''returns None\n\n
    undeployHandler(final QName qname)\n
    '''
def undeployService():
    '''returns None\n\n
    undeployService(final QName qname)\n
    '''
def undeployTransport():
    '''returns None\n\n
    undeployTransport(final QName qname)\n
    '''
def deployTypeMapping():
    '''returns None\n\n
    deployTypeMapping(final WSDDTypeMapping typeMapping)\n
    '''
def ():
    '''returns WSDDDeployment\n\n
    ()\n
    (final Element e)\n
    '''
def deployToRegistry():
    '''returns None\n\n
    deployToRegistry(final WSDDDeployment target)\n
    '''
def writeToContext():
    '''returns None\n\n
    writeToContext(final SerializationContext context)\n
    '''
def getGlobalConfiguration():
    '''returns WSDDGlobalConfiguration\n\n
    getGlobalConfiguration()\n
    '''
def setGlobalConfiguration():
    '''returns None\n\n
    setGlobalConfiguration(final WSDDGlobalConfiguration globalConfig)\n
    '''
def getTypeMappings():
    '''returns WSDDTypeMapping[]\n\n
    getTypeMappings()\n
    '''
def getServices():
    '''returns WSDDService[]\n\n
    getServices()\n
    '''
def getWSDDService():
    '''returns WSDDService\n\n
    getWSDDService(final QName qname)\n
    '''
def getHandler():
    '''returns Handler\n\n
    getHandler(final QName name)\n
    '''
def getTransport():
    '''returns Handler\n\n
    getTransport(final QName name)\n
    '''
def getService():
    '''returns SOAPService\n\n
    getService(final QName name)\n
    '''
def getServiceByNamespaceURI():
    '''returns SOAPService\n\n
    getServiceByNamespaceURI(final String namespace)\n
    '''
def configureEngine():
    '''returns None\n\n
    configureEngine(final AxisEngine engine)\n
    '''
def writeEngineConfig():
    '''returns None\n\n
    writeEngineConfig(final AxisEngine engine)\n
    '''
def getTypeMapping():
    '''returns TypeMapping\n\n
    getTypeMapping(final String encodingStyle)\n
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
def getRoles():
    '''returns List\n\n
    getRoles()\n
    '''
def getDeployedServices():
    '''returns Iterator\n\n
    getDeployedServices()\n
    '''
def registerNamespaceForService():
    '''returns None\n\n
    registerNamespaceForService(final String namespace, final WSDDService service)\n
    '''
def removeNamespaceMapping():
    '''returns None\n\n
    removeNamespaceMapping(final String namespace)\n
    '''
def getEngine():
    '''returns AxisEngine\n\n
    getEngine()\n
    '''
def getDeployment():
    '''returns WSDDDeployment\n\n
    getDeployment()\n
    '''
def getHandlers():
    '''returns WSDDHandler[]\n\n
    getHandlers()\n
    '''
def getWSDDHandler():
    '''returns WSDDHandler\n\n
    getWSDDHandler(final QName qname)\n
    '''
def getTransports():
    '''returns WSDDTransport[]\n\n
    getTransports()\n
    '''
def getWSDDTransport():
    '''returns WSDDTransport\n\n
    getWSDDTransport(final QName qname)\n
    '''
