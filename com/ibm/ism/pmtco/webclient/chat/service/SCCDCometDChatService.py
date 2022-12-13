def SCCDCometDChatService():
    '''    public SCCDCometDChatService()
    '''
def getInstance():
    '''    public static synchronized SCCDCometDChatService getInstance()
    '''
def handleAbandonedChat():
    '''    public void handleAbandonedChat(final ServerSession client, final ServerMessage message)
    '''
def updateServerQueue():
    '''    public void updateServerQueue(final ServerSession client, final ServerMessage message)
    '''
def requestNextAgent():
    '''    public void requestNextAgent(final ServerSession client, final ServerMessage message)
    '''
def requestWaitQueueInfo():
    '''    public void requestWaitQueueInfo(final ServerSession client, final ServerMessage message)
    '''
def notifyAgentReady():
    '''    public void notifyAgentReady(final ServerSession client, final ServerMessage message)
    '''
def registerHost():
    '''    public void registerHost(final String URL)
    '''
def getOortCloud():
    '''    public ArrayList<String> getOortCloud(final String URL)
    '''
def configureCloud():
    '''    public void configureCloud(final ArrayList<String> comets)
    '''
def notifyLeaveChatDirect():
    '''    public void notifyLeaveChatDirect(final String clientID)
    '''
def chatSession():
    '''    public void chatSession(final ServerSession client, final ServerMessage message)
    '''
def getTimeMap():
    '''    public ConcurrentHashMap<String, Long> getTimeMap()
    '''
def isChatAgent():
    '''    public boolean isChatAgent(final String personID)
    '''
def canUserChatOnChannel():
    '''    public boolean canUserChatOnChannel(final String channelID, final String sessionPersonID)
    '''
def addUsersToChatChannel():
    '''    public void addUsersToChatChannel(final String channel, final String agentPersonID, final String userPersonID)
    '''
def run():
    '''    public void run()
    '''
