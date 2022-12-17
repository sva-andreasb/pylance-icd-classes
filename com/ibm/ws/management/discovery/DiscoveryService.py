def ():
    '''returns DiscoveryService\n\n
    (final ServerInfo info, final Endpoint endpoint, final PeerAdv advertisement)\n
    '''
def addDiscoveryListener():
    '''returns None\n\n
    addDiscoveryListener(final DiscoveryListener listener)\n
    '''
def removeDiscoveryListener():
    '''returns None\n\n
    removeDiscoveryListener(final DiscoveryListener listener)\n
    '''
def sendQuery():
    '''returns long\n\n
    sendQuery(final EndpointAddress destination, final ServerInfo target)\n
    '''
def processQuery():
    '''returns DiscoveryResponseMsg\n\n
    processQuery(final XMLDocument queryDocument)\n
    '''
def pushResponse():
    '''returns None\n\n
    pushResponse(final XMLDocument responseDocument)\n
    '''
def respond():
    '''returns None\n\n
    respond(final EndpointAddress destination, final DiscoveryResponseMsg response)\n
    '''
def demux():
    '''returns None\n\n
    demux(final Message message)\n
    '''
