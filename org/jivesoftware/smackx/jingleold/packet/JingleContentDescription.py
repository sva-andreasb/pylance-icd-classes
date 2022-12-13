NODENAME = "String  \"payload-type\""
NAMESPACE = "String  \"urn:xmpp:tmp:jingle:apps:rtp\""
def JingleContentDescription():
    '''public JingleContentDescription()
    '''
def getElementName():
    '''public String getElementName()
    public static String getElementName()
    '''
def addJinglePayloadType():
    '''public void addJinglePayloadType(final JinglePayloadType pt)
    '''
def addAudioPayloadTypes():
    '''public void addAudioPayloadTypes(final List<PayloadType.Audio> pts)
    '''
def getJinglePayloadTypes():
    '''public Iterator<JinglePayloadType> getJinglePayloadTypes()
    '''
def getJinglePayloadTypesList():
    '''public ArrayList<JinglePayloadType> getJinglePayloadTypesList()
    '''
def getJinglePayloadTypesCount():
    '''public int getJinglePayloadTypesCount()
    '''
def toXML():
    '''public String toXML(final String enclosingNamespace)
    public String toXML()
    '''
def Audio():
    '''public Audio()
    public Audio(final JinglePayloadType pt)
    public Audio(final PayloadType.Audio audio)
    '''
def getNamespace():
    '''public String getNamespace()
    '''
def JinglePayloadType():
    '''public JinglePayloadType(final PayloadType payload)
    public JinglePayloadType()
    '''
def getPayloadType():
    '''public PayloadType getPayloadType()
    '''
def setPayload():
    '''public void setPayload(final PayloadType payload)
    '''
