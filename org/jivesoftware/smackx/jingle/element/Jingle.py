NAMESPACE = "String  \"urn:xmpp:jingle:1\""
ACTION_ATTRIBUTE_NAME = "String  \"action\""
INITIATOR_ATTRIBUTE_NAME = "String  \"initiator\""
RESPONDER_ATTRIBUTE_NAME = "String  \"responder\""
SESSION_ID_ATTRIBUTE_NAME = "String  \"sid\""
ELEMENT = "String  \"jingle\""
def getInitiator():
    '''    public FullJid getInitiator()
    '''
def getResponder():
    '''    public FullJid getResponder()
    '''
def getSid():
    '''    public String getSid()
    '''
def getAction():
    '''    public JingleAction getAction()
    '''
def getReason():
    '''    public JingleReason getReason()
    '''
def getContents():
    '''    public List<JingleContent> getContents()
    '''
def getSoleContentOrThrow():
    '''    public JingleContent getSoleContentOrThrow()
    '''
def getBuilder():
    '''    public static Builder getBuilder()
    '''
def setSessionId():
    '''    public Builder setSessionId(final String sessionId)
    '''
def setAction():
    '''    public Builder setAction(final JingleAction action)
    '''
def setInitiator():
    '''    public Builder setInitiator(final FullJid initator)
    '''
def setResponder():
    '''    public Builder setResponder(final FullJid responder)
    '''
def addJingleContent():
    '''    public Builder addJingleContent(final JingleContent content)
    '''
def setReason():
    '''    public Builder setReason(final JingleReason.Reason reason)
    public Builder setReason(final JingleReason reason)
    '''
def build():
    '''    public Jingle build()
    '''
