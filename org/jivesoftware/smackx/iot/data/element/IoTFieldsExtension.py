ELEMENT = "String  \"fields\""
NAMESPACE = "String  \"urn:xmpp:iot:sensordata\""
def IoTFieldsExtension():
    '''public IoTFieldsExtension(final int seqNr, final boolean done, final NodeElement node)
    public IoTFieldsExtension(final int seqNr, final boolean done, final List<NodeElement> nodes)
    '''
def getSequenceNr():
    '''public int getSequenceNr()
    '''
def isDone():
    '''public boolean isDone()
    '''
def getNodes():
    '''public List<NodeElement> getNodes()
    '''
def getElementName():
    '''public String getElementName()
    '''
def getNamespace():
    '''public String getNamespace()
    '''
def toXML():
    '''public XmlStringBuilder toXML(final String enclosingNamespace)
    '''
def buildFor():
    '''public static IoTFieldsExtension buildFor(final int seqNr, final boolean done, final NodeInfo nodeInfo, final List<? extends IoTDataField> data)
    '''
def from():
    '''public static IoTFieldsExtension from(final Message message)
    '''
