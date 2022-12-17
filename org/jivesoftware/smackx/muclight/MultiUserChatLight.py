NAMESPACE = "String  \"urn:xmpp:muclight:0\""
AFFILIATIONS = "String  \"#affiliations\""
INFO = "String  \"#info\""
CONFIGURATION = "String  \"#configuration\""
CREATE = "String  \"#create\""
DESTROY = "String  \"#destroy\""
BLOCKING = "String  \"#blocking\""
def processStanza():
    '''returns None\n\n
    processStanza(final Stanza packet)\n
    '''
def getRoom():
    '''returns EntityJid\n\n
    getRoom()\n
    '''
def sendMessage():
    '''returns None\n\n
    sendMessage(final String text)\n
    sendMessage(final Message message)\n
    '''
def createPrivateChat():
    '''returns Chat\n\n
    createPrivateChat(final EntityJid occupant, final ChatMessageListener listener)\n
    '''
def createMessage():
    '''returns Message\n\n
    createMessage()\n
    '''
def pollMessage():
    '''returns Message\n\n
    pollMessage()\n
    '''
def nextMessage():
    '''returns Message\n\n
    nextMessage()\n
    nextMessage(final long timeout)\n
    '''
def addMessageListener():
    '''returns boolean\n\n
    addMessageListener(final MessageListener listener)\n
    '''
def removeMessageListener():
    '''returns boolean\n\n
    removeMessageListener(final MessageListener listener)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def create():
    '''returns None\n\n
    create(final String roomName, final String subject, final HashMap<String, String> customConfigs, final List<Jid> occupants)\n
    create(final String roomName, final List<Jid> occupants)\n
    '''
def leave():
    '''returns None\n\n
    leave()\n
    '''
def getFullInfo():
    '''returns MUCLightRoomInfo\n\n
    getFullInfo(final String version)\n
    getFullInfo()\n
    '''
def getConfiguration():
    '''returns MUCLightRoomConfiguration\n\n
    getConfiguration(final String version)\n
    getConfiguration()\n
    '''
def changeAffiliations():
    '''returns None\n\n
    changeAffiliations(final HashMap<Jid, MUCLightAffiliation> affiliations)\n
    '''
def destroy():
    '''returns None\n\n
    destroy()\n
    '''
def changeSubject():
    '''returns None\n\n
    changeSubject(final String subject)\n
    '''
def changeRoomName():
    '''returns None\n\n
    changeRoomName(final String roomName)\n
    '''
def setRoomConfigs():
    '''returns None\n\n
    setRoomConfigs(final HashMap<String, String> customConfigs)\n
    setRoomConfigs(final String roomName, final HashMap<String, String> customConfigs)\n
    '''
