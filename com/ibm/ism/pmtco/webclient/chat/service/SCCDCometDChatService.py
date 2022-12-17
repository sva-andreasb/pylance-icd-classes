def ():
    '''returns SCCDCometDChatService\n\n
    ()\n
    '''
def handleAbandonedChat():
    '''returns None\n\n
    handleAbandonedChat(final ServerSession client, final ServerMessage message)\n
    '''
def updateServerQueue():
    '''returns None\n\n
    updateServerQueue(final ServerSession client, final ServerMessage message)\n
    '''
def requestNextAgent():
    '''returns None\n\n
    requestNextAgent(final ServerSession client, final ServerMessage message)\n
    '''
def requestWaitQueueInfo():
    '''returns None\n\n
    requestWaitQueueInfo(final ServerSession client, final ServerMessage message)\n
    '''
def notifyAgentReady():
    '''returns None\n\n
    notifyAgentReady(final ServerSession client, final ServerMessage message)\n
    '''
def registerHost():
    '''returns None\n\n
    registerHost(final String URL)\n
    '''
def getOortCloud():
    '''returns ArrayList<String>\n\n
    getOortCloud(final String URL)\n
    '''
def configureCloud():
    '''returns None\n\n
    configureCloud(final ArrayList<String> comets)\n
    '''
def notifyLeaveChatDirect():
    '''returns None\n\n
    notifyLeaveChatDirect(final String clientID)\n
    '''
def chatSession():
    '''returns None\n\n
    chatSession(final ServerSession client, final ServerMessage message)\n
    '''
def isChatAgent():
    '''returns boolean\n\n
    isChatAgent(final String personID)\n
    '''
def canUserChatOnChannel():
    '''returns boolean\n\n
    canUserChatOnChannel(final String channelID, final String sessionPersonID)\n
    '''
def addUsersToChatChannel():
    '''returns None\n\n
    addUsersToChatChannel(final String channel, final String agentPersonID, final String userPersonID)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
