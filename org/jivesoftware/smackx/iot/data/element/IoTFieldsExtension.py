ELEMENT = "String  \"fields\""
NAMESPACE = "String  \"urn:xmpp:iot:sensordata\""
def ():
    '''returns IoTFieldsExtension\n\n
    (final int seqNr, final boolean done, final NodeElement node)\n
    (final int seqNr, final boolean done, final List<NodeElement> nodes)\n
    '''
def getSequenceNr():
    '''returns int\n\n
    getSequenceNr()\n
    '''
def isDone():
    '''returns boolean\n\n
    isDone()\n
    '''
def getNodes():
    '''returns List<NodeElement>\n\n
    getNodes()\n
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
    '''returns XmlStringBuilder\n\n
    toXML(final String enclosingNamespace)\n
    '''
