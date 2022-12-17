NODENAME = "String  \"content\""
CREATOR = "String  \"creator\""
NAME = "String  \"name\""
def ():
    '''returns JingleContent\n\n
    (final String creator, final String name)\n
    '''
def getCreator():
    '''returns String\n\n
    getCreator()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getElementName():
    '''returns String\n\n
    getElementName()\n
    '''
def getNamespace():
    '''returns String\n\n
    getNamespace()\n
    '''
def setDescription():
    '''returns None\n\n
    setDescription(final JingleDescription description)\n
    '''
def getDescription():
    '''returns JingleDescription\n\n
    getDescription()\n
    '''
def addJingleTransport():
    '''returns None\n\n
    addJingleTransport(final JingleTransport transport)\n
    '''
def addTransports():
    '''returns None\n\n
    addTransports(final List<JingleTransport> transports)\n
    '''
def getJingleTransports():
    '''returns Iterator<JingleTransport>\n\n
    getJingleTransports()\n
    '''
def getJingleTransportsList():
    '''returns List<JingleTransport>\n\n
    getJingleTransportsList()\n
    '''
def getJingleTransportsCount():
    '''returns int\n\n
    getJingleTransportsCount()\n
    '''
def toXML():
    '''returns String\n\n
    toXML(final String enclosingNamespace)\n
    '''
