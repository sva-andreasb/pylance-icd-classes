NAMESPACE = "String  urn:xmpp:muclight:0""
AFFILIATIONS = "String  #affiliations""
INFO = "String  #info""
CONFIGURATION = "String  #configuration""
CREATE = "String  #create""
DESTROY = "String  #destroy""
BLOCKING = "String  #blocking""
def processStanza():
'''public void processStanza(final Stanza packet)
'''
pass
def getRoom():
'''public EntityJid getRoom()
'''
pass
def sendMessage():
'''public void sendMessage(final String text)
public void sendMessage(final Message message)
'''
pass
def createPrivateChat():
'''public Chat createPrivateChat(final EntityJid occupant, final ChatMessageListener listener)
'''
pass
def createMessage():
'''public Message createMessage()
'''
pass
def pollMessage():
'''public Message pollMessage()
'''
pass
def nextMessage():
'''public Message nextMessage()
public Message nextMessage(final long timeout)
'''
pass
def addMessageListener():
'''public boolean addMessageListener(final MessageListener listener)
'''
pass
def removeMessageListener():
'''public boolean removeMessageListener(final MessageListener listener)
'''
pass
def toString():
'''public String toString()
'''
pass
def create():
'''public void create(final String roomName, final String subject, final HashMap<String, String> customConfigs, final List<Jid> occupants)
public void create(final String roomName, final List<Jid> occupants)
'''
pass
def leave():
'''public void leave()
'''
pass
def getFullInfo():
'''public MUCLightRoomInfo getFullInfo(final String version)
public MUCLightRoomInfo getFullInfo()
'''
pass
def getConfiguration():
'''public MUCLightRoomConfiguration getConfiguration(final String version)
public MUCLightRoomConfiguration getConfiguration()
'''
pass
def getAffiliations():
'''public HashMap<Jid, MUCLightAffiliation> getAffiliations(final String version)
public HashMap<Jid, MUCLightAffiliation> getAffiliations()
'''
pass
def changeAffiliations():
'''public void changeAffiliations(final HashMap<Jid, MUCLightAffiliation> affiliations)
'''
pass
def destroy():
'''public void destroy()
'''
pass
def changeSubject():
'''public void changeSubject(final String subject)
'''
pass
def changeRoomName():
'''public void changeRoomName(final String roomName)
'''
pass
def setRoomConfigs():
'''public void setRoomConfigs(final HashMap<String, String> customConfigs)
public void setRoomConfigs(final String roomName, final HashMap<String, String> customConfigs)
'''
pass
