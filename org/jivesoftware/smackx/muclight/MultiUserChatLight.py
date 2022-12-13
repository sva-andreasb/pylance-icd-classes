NAMESPACE = "String  \"urn:xmpp:muclight:0\""
AFFILIATIONS = "String  \"#affiliations\""
INFO = "String  \"#info\""
CONFIGURATION = "String  \"#configuration\""
CREATE = "String  \"#create\""
DESTROY = "String  \"#destroy\""
BLOCKING = "String  \"#blocking\""
def processStanza():
    '''    public void processStanza(final Stanza packet)
    '''
def getRoom():
    '''    public EntityJid getRoom()
    '''
def sendMessage():
    '''    public void sendMessage(final String text)
    public void sendMessage(final Message message)
    '''
def createPrivateChat():
    '''    public Chat createPrivateChat(final EntityJid occupant, final ChatMessageListener listener)
    '''
def createMessage():
    '''    public Message createMessage()
    '''
def pollMessage():
    '''    public Message pollMessage()
    '''
def nextMessage():
    '''    public Message nextMessage()
    public Message nextMessage(final long timeout)
    '''
def addMessageListener():
    '''    public boolean addMessageListener(final MessageListener listener)
    '''
def removeMessageListener():
    '''    public boolean removeMessageListener(final MessageListener listener)
    '''
def toString():
    '''    public String toString()
    '''
def create():
    '''    public void create(final String roomName, final String subject, final HashMap<String, String> customConfigs, final List<Jid> occupants)
    public void create(final String roomName, final List<Jid> occupants)
    '''
def leave():
    '''    public void leave()
    '''
def getFullInfo():
    '''    public MUCLightRoomInfo getFullInfo(final String version)
    public MUCLightRoomInfo getFullInfo()
    '''
def getConfiguration():
    '''    public MUCLightRoomConfiguration getConfiguration(final String version)
    public MUCLightRoomConfiguration getConfiguration()
    '''
def getAffiliations():
    '''    public HashMap<Jid, MUCLightAffiliation> getAffiliations(final String version)
    public HashMap<Jid, MUCLightAffiliation> getAffiliations()
    '''
def changeAffiliations():
    '''    public void changeAffiliations(final HashMap<Jid, MUCLightAffiliation> affiliations)
    '''
def destroy():
    '''    public void destroy()
    '''
def changeSubject():
    '''    public void changeSubject(final String subject)
    '''
def changeRoomName():
    '''    public void changeRoomName(final String roomName)
    '''
def setRoomConfigs():
    '''    public void setRoomConfigs(final HashMap<String, String> customConfigs)
    public void setRoomConfigs(final String roomName, final HashMap<String, String> customConfigs)
    '''
