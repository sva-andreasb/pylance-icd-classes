ATTR_CID = "String  \"cid\""
ATTR_HOST = "String  \"host\""
ATTR_JID = "String  \"jid\""
ATTR_PORT = "String  \"port\""
ATTR_PRIORITY = "String  \"priority\""
ATTR_TYPE = "String  \"type\""
def ():
    '''returns JingleS5BTransportCandidate\n\n
    (final String candidateId, final String host, final Jid jid, final int port, final int priority, final Type type)\n
    (final Bytestream.StreamHost streamHost, final int priority, final Type type)\n
    '''
def getCandidateId():
    '''returns String\n\n
    getCandidateId()\n
    '''
def getHost():
    '''returns String\n\n
    getHost()\n
    '''
def getJid():
    '''returns Jid\n\n
    getJid()\n
    '''
def getPort():
    '''returns int\n\n
    getPort()\n
    '''
def getPriority():
    '''returns int\n\n
    getPriority()\n
    '''
def getType():
    '''returns Type\n\n
    getType()\n
    '''
def toXML():
    '''returns CharSequence\n\n
    toXML(final String enclosingNamespace)\n
    '''
def getWeight():
    '''returns int\n\n
    getWeight()\n
    '''
def setCandidateId():
    '''returns Builder\n\n
    setCandidateId(final String cid)\n
    '''
def setHost():
    '''returns Builder\n\n
    setHost(final String host)\n
    '''
def setJid():
    '''returns Builder\n\n
    setJid(final String jid)\n
    '''
def setPort():
    '''returns Builder\n\n
    setPort(final int port)\n
    '''
def setPriority():
    '''returns Builder\n\n
    setPriority(final int priority)\n
    '''
def setType():
    '''returns Builder\n\n
    setType(final Type type)\n
    '''
def build():
    '''returns JingleS5BTransportCandidate\n\n
    build()\n
    '''
