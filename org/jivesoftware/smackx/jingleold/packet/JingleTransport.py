NODENAME = "String  \"candidate\""
NAMESPACE = "String  \"http://www.xmpp.org/extensions/xep-0177.html#ns\""
def ():
    '''returns Candidate\n\n
    ()\n
    (final JingleTransportCandidate candidate)\n
    (final JingleTransport tr)\n
    ()\n
    (final TransportCandidate candidate)\n
    ()\n
    ()\n
    (final TransportCandidate tc)\n
    ()\n
    ()\n
    (final TransportCandidate tc)\n
    '''
def addCandidate():
    '''returns None\n\n
    addCandidate(final JingleTransportCandidate candidate)\n
    addCandidate(final JingleTransportCandidate candidate)\n
    addCandidate(final JingleTransportCandidate candidate)\n
    '''
def getCandidates():
    '''returns Iterator<JingleTransportCandidate>\n\n
    getCandidates()\n
    '''
def getCandidatesList():
    '''returns List<JingleTransportCandidate>\n\n
    getCandidatesList()\n
    getCandidatesList()\n
    getCandidatesList()\n
    '''
def getCandidatesCount():
    '''returns int\n\n
    getCandidatesCount()\n
    '''
def getElementName():
    '''returns String\n\n
    getElementName()\n
    '''
def getNamespace():
    '''returns String\n\n
    getNamespace()\n
    '''
def toXML():
    '''returns String\n\n
    toXML(final String enclosingNamespace)\n
    toXML()\n
    '''
def getMediaTransport():
    '''returns TransportCandidate\n\n
    getMediaTransport()\n
    '''
def setMediaTransport():
    '''returns None\n\n
    setMediaTransport(final TransportCandidate cand)\n
    '''
