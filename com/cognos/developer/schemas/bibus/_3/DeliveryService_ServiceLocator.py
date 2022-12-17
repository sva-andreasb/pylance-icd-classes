def ():
    '''returns DeliveryService_ServiceLocator\n\n
    ()\n
    (final EngineConfiguration config)\n
    (final String wsdlLoc, final QName sName)\n
    '''
def getdeliveryServiceAddress():
    '''returns String\n\n
    getdeliveryServiceAddress()\n
    '''
def getdeliveryServiceWSDDServiceName():
    '''returns String\n\n
    getdeliveryServiceWSDDServiceName()\n
    '''
def setdeliveryServiceWSDDServiceName():
    '''returns None\n\n
    setdeliveryServiceWSDDServiceName(final String name)\n
    '''
def getdeliveryService():
    '''returns DeliveryService_PortType\n\n
    getdeliveryService()\n
    getdeliveryService(final URL portAddress)\n
    '''
def setdeliveryServiceEndpointAddress():
    '''returns None\n\n
    setdeliveryServiceEndpointAddress(final String address)\n
    '''
def getPort():
    '''returns Remote\n\n
    getPort(final Class serviceEndpointInterface)\n
    getPort(final QName portName, final Class serviceEndpointInterface)\n
    '''
def getServiceName():
    '''returns QName\n\n
    getServiceName()\n
    '''
def getPorts():
    '''returns Iterator\n\n
    getPorts()\n
    '''
def setEndpointAddress():
    '''returns None\n\n
    setEndpointAddress(final String portName, final String address)\n
    setEndpointAddress(final QName portName, final String address)\n
    '''
