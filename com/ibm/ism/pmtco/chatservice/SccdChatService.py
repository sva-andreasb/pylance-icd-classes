def SccdChatService():
    '''    public SccdChatService()
    public SccdChatService(final MXServer mxServer)
    '''
def restart():
    '''    public void restart()
    '''
def init():
    '''    public void init()
    '''
def createSRWithTemplate():
    '''    public SRRemote createSRWithTemplate(final TKTemplateRemote template, final String originator)
    '''
def createServiceRequest():
    '''    public SRRemote createServiceRequest(final SolutionRemote solution, final String originator)
    '''
def destroy():
    '''    public void destroy()
    '''
def setChatOwner():
    '''    public void setChatOwner(final String ticketUid, final String agent)
    '''
def addCommLog():
    '''    public void addCommLog(final String ticketUid, final String userId, final String agentId, final List<Map<String, Object>> chatHistory, final String ticketclass, final String agentClientId, final String userClientId)
    '''
def addChatUser():
    '''    public void addChatUser(final String ticketUID, final String clientID, final String personID, final String tkClass, final String ticketID, final boolean isNewSR, final String queueID, final String nodeUrl)
    '''
def getQueueCounts():
    '''    public Map<String, Object> getQueueCounts()
    '''
def getOldestUser():
    '''    public ConcurrentHashMap<String, String> getOldestUser(final String[] queues)
    '''
def setUserAgentInfo():
    '''    public int setUserAgentInfo(final String agentPersonID, final String agentClientID, final String chatChannel, final String useruuid, final String nodeUrl)
    '''
def getSessionInfo():
    '''    public ConcurrentHashMap<String, String> getSessionInfo(final String clientID)
    '''
def deleteChat():
    '''    public void deleteChat(final String channel, final boolean timedOut)
    '''
def deleteAbandonedChat():
    '''    public void deleteAbandonedChat(final String clientid, final String ticketUid)
    '''
def deleteServiceRequest():
    '''    public void deleteServiceRequest(final String ticketUid)
    '''
def updateChatStatus():
    '''    public void updateChatStatus(final String status, final String clientID)
    '''
def getEntryByChannel():
    '''    public ConcurrentHashMap<String, String> getEntryByChannel(final String chatChannel)
    '''
def registerHost():
    '''    public void registerHost(final String URL)
    '''
def getOortCloud():
    '''    public ArrayList<String> getOortCloud(final String URL)
    '''
def releaseChatRequest():
    '''    public void releaseChatRequest(final String useruuid)
    '''
def cleanUpChats():
    '''    public void cleanUpChats(final String nodeurl)
    '''
def getAgentDisplayName():
    '''    public String getAgentDisplayName(final String agentID)
    '''
def getRequestPersonID():
    '''    public String getRequestPersonID()
    '''
def isChatAgent():
    '''    public boolean isChatAgent(final String personID)
    '''
def getAgentChatQueues():
    '''    public String[] getAgentChatQueues(final String personID)
    '''
def isUserAssignedToChannel():
    '''    public boolean isUserAssignedToChannel(final String channelID, final String sessionPersonID)
    '''
