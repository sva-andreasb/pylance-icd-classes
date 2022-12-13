def AgentService_ServiceLocator():
    '''    public AgentService_ServiceLocator()
    public AgentService_ServiceLocator(final EngineConfiguration config)
    public AgentService_ServiceLocator(final String wsdlLoc, final QName sName)
    '''
def getagentServiceAddress():
    '''    public String getagentServiceAddress()
    '''
def getagentServiceWSDDServiceName():
    '''    public String getagentServiceWSDDServiceName()
    '''
def setagentServiceWSDDServiceName():
    '''    public void setagentServiceWSDDServiceName(final String name)
    '''
def getagentService():
    '''    public AgentService_PortType getagentService()
    public AgentService_PortType getagentService(final URL portAddress)
    '''
def setagentServiceEndpointAddress():
    '''    public void setagentServiceEndpointAddress(final String address)
    '''
def getPort():
    '''    public Remote getPort(final Class serviceEndpointInterface)
    public Remote getPort(final QName portName, final Class serviceEndpointInterface)
    '''
def getServiceName():
    '''    public QName getServiceName()
    '''
def getPorts():
    '''    public Iterator getPorts()
    '''
def setEndpointAddress():
    '''    public void setEndpointAddress(final String portName, final String address)
    public void setEndpointAddress(final QName portName, final String address)
    '''
