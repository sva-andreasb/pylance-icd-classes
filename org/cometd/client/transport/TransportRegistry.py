def ():
    '''returns TransportRegistry\n\n
    ()\n
    '''
def add():
    '''returns None\n\n
    add(final ClientTransport transport)\n
    '''
def getKnownTransports():
    '''returns Set<String>\n\n
    getKnownTransports()\n
    '''
def getAllowedTransports():
    '''returns List<String>\n\n
    getAllowedTransports()\n
    '''
def negotiate():
    '''returns List<ClientTransport>\n\n
    negotiate(final Object[] requestedTransports, final String bayeuxVersion)\n
    '''
def getTransport():
    '''returns ClientTransport\n\n
    getTransport(final String transport)\n
    '''
