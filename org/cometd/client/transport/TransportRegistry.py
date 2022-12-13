def TransportRegistry():
    '''    public TransportRegistry()
    '''
def add():
    '''    public void add(final ClientTransport transport)
    '''
def getKnownTransports():
    '''    public Set<String> getKnownTransports()
    '''
def getAllowedTransports():
    '''    public List<String> getAllowedTransports()
    '''
def negotiate():
    '''    public List<ClientTransport> negotiate(final Object[] requestedTransports, final String bayeuxVersion)
    '''
def getTransport():
    '''    public ClientTransport getTransport(final String transport)
    '''
