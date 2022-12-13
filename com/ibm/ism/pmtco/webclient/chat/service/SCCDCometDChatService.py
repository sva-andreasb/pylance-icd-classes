def SCCDCometDChatService():
'''public SCCDCometDChatService()
'''
pass
def getInstance():
'''public static synchronized SCCDCometDChatService getInstance()
'''
pass
def handleAbandonedChat():
'''public void handleAbandonedChat(final ServerSession client, final ServerMessage message)
'''
pass
def updateServerQueue():
'''public void updateServerQueue(final ServerSession client, final ServerMessage message)
'''
pass
def requestNextAgent():
'''public void requestNextAgent(final ServerSession client, final ServerMessage message)
'''
pass
def requestWaitQueueInfo():
'''public void requestWaitQueueInfo(final ServerSession client, final ServerMessage message)
'''
pass
def notifyAgentReady():
'''public void notifyAgentReady(final ServerSession client, final ServerMessage message)
'''
pass
def registerHost():
'''public void registerHost(final String URL)
'''
pass
def getOortCloud():
'''public ArrayList<String> getOortCloud(final String URL)
'''
pass
def configureCloud():
'''public void configureCloud(final ArrayList<String> comets)
'''
pass
def notifyLeaveChatDirect():
'''public void notifyLeaveChatDirect(final String clientID)
'''
pass
def chatSession():
'''public void chatSession(final ServerSession client, final ServerMessage message)
'''
pass
def getTimeMap():
'''public ConcurrentHashMap<String, Long> getTimeMap()
'''
pass
def isChatAgent():
'''public boolean isChatAgent(final String personID)
'''
pass
def canUserChatOnChannel():
'''public boolean canUserChatOnChannel(final String channelID, final String sessionPersonID)
'''
pass
def addUsersToChatChannel():
'''public void addUsersToChatChannel(final String channel, final String agentPersonID, final String userPersonID)
'''
pass
def run():
'''public void run()
'''
pass
