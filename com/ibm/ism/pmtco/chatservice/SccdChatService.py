def SccdChatService():
'''public SccdChatService()
public SccdChatService(final MXServer mxServer)
'''
pass
def restart():
'''public void restart()
'''
pass
def init():
'''public void init()
'''
pass
def createSRWithTemplate():
'''public SRRemote createSRWithTemplate(final TKTemplateRemote template, final String originator)
'''
pass
def createServiceRequest():
'''public SRRemote createServiceRequest(final SolutionRemote solution, final String originator)
'''
pass
def destroy():
'''public void destroy()
'''
pass
def setChatOwner():
'''public void setChatOwner(final String ticketUid, final String agent)
'''
pass
def addCommLog():
'''public void addCommLog(final String ticketUid, final String userId, final String agentId, final List<Map<String, Object>> chatHistory, final String ticketclass, final String agentClientId, final String userClientId)
'''
pass
def addChatUser():
'''public void addChatUser(final String ticketUID, final String clientID, final String personID, final String tkClass, final String ticketID, final boolean isNewSR, final String queueID, final String nodeUrl)
'''
pass
def getQueueCounts():
'''public Map<String, Object> getQueueCounts()
'''
pass
def getOldestUser():
'''public ConcurrentHashMap<String, String> getOldestUser(final String[] queues)
'''
pass
def setUserAgentInfo():
'''public int setUserAgentInfo(final String agentPersonID, final String agentClientID, final String chatChannel, final String useruuid, final String nodeUrl)
'''
pass
def getSessionInfo():
'''public ConcurrentHashMap<String, String> getSessionInfo(final String clientID)
'''
pass
def deleteChat():
'''public void deleteChat(final String channel, final boolean timedOut)
'''
pass
def deleteAbandonedChat():
'''public void deleteAbandonedChat(final String clientid, final String ticketUid)
'''
pass
def deleteServiceRequest():
'''public void deleteServiceRequest(final String ticketUid)
'''
pass
def updateChatStatus():
'''public void updateChatStatus(final String status, final String clientID)
'''
pass
def getEntryByChannel():
'''public ConcurrentHashMap<String, String> getEntryByChannel(final String chatChannel)
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
def releaseChatRequest():
'''public void releaseChatRequest(final String useruuid)
'''
pass
def cleanUpChats():
'''public void cleanUpChats(final String nodeurl)
'''
pass
def getAgentDisplayName():
'''public String getAgentDisplayName(final String agentID)
'''
pass
def getRequestPersonID():
'''public String getRequestPersonID()
'''
pass
def isChatAgent():
'''public boolean isChatAgent(final String personID)
'''
pass
def getAgentChatQueues():
'''public String[] getAgentChatQueues(final String personID)
'''
pass
def isUserAssignedToChannel():
'''public boolean isUserAssignedToChannel(final String channelID, final String sessionPersonID)
'''
pass
