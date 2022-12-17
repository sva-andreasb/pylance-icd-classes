NAMESPACE = "String  \"urn:xmpp:jingle:1\""
ACTION_ATTRIBUTE_NAME = "String  \"action\""
INITIATOR_ATTRIBUTE_NAME = "String  \"initiator\""
RESPONDER_ATTRIBUTE_NAME = "String  \"responder\""
SESSION_ID_ATTRIBUTE_NAME = "String  \"sid\""
ELEMENT = "String  \"jingle\""
def getInitiator():
    '''returns FullJid\n\n
    getInitiator()\n
    '''
def getResponder():
    '''returns FullJid\n\n
    getResponder()\n
    '''
def getSid():
    '''returns String\n\n
    getSid()\n
    '''
def getAction():
    '''returns JingleAction\n\n
    getAction()\n
    '''
def getReason():
    '''returns JingleReason\n\n
    getReason()\n
    '''
def getContents():
    '''returns List<JingleContent>\n\n
    getContents()\n
    '''
def getSoleContentOrThrow():
    '''returns JingleContent\n\n
    getSoleContentOrThrow()\n
    '''
def setSessionId():
    '''returns Builder\n\n
    setSessionId(final String sessionId)\n
    '''
def setAction():
    '''returns Builder\n\n
    setAction(final JingleAction action)\n
    '''
def setInitiator():
    '''returns Builder\n\n
    setInitiator(final FullJid initator)\n
    '''
def setResponder():
    '''returns Builder\n\n
    setResponder(final FullJid responder)\n
    '''
def addJingleContent():
    '''returns Builder\n\n
    addJingleContent(final JingleContent content)\n
    '''
def setReason():
    '''returns Builder\n\n
    setReason(final JingleReason.Reason reason)\n
    setReason(final JingleReason reason)\n
    '''
def build():
    '''returns Jingle\n\n
    build()\n
    '''
