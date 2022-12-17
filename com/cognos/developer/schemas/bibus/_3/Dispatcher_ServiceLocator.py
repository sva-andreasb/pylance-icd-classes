def ():
    '''returns Dispatcher_ServiceLocator\n\n
    ()\n
    (final EngineConfiguration config)\n
    (final String wsdlLoc, final QName sName)\n
    '''
def getdispatcherAddress():
    '''returns String\n\n
    getdispatcherAddress()\n
    '''
def getdispatcherWSDDServiceName():
    '''returns String\n\n
    getdispatcherWSDDServiceName()\n
    '''
def setdispatcherWSDDServiceName():
    '''returns None\n\n
    setdispatcherWSDDServiceName(final String name)\n
    '''
def getdispatcher():
    '''returns Dispatcher_PortType\n\n
    getdispatcher()\n
    getdispatcher(final URL portAddress)\n
    '''
def setdispatcherEndpointAddress():
    '''returns None\n\n
    setdispatcherEndpointAddress(final String address)\n
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
