def ():
    '''returns AgentService_ServiceLocator\n\n
    ()\n
    (final EngineConfiguration config)\n
    (final String wsdlLoc, final QName sName)\n
    '''
def getagentServiceAddress():
    '''returns String\n\n
    getagentServiceAddress()\n
    '''
def getagentServiceWSDDServiceName():
    '''returns String\n\n
    getagentServiceWSDDServiceName()\n
    '''
def setagentServiceWSDDServiceName():
    '''returns None\n\n
    setagentServiceWSDDServiceName(final String name)\n
    '''
def getagentService():
    '''returns AgentService_PortType\n\n
    getagentService()\n
    getagentService(final URL portAddress)\n
    '''
def setagentServiceEndpointAddress():
    '''returns None\n\n
    setagentServiceEndpointAddress(final String address)\n
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
