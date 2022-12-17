def ():
    '''returns SccdChatService\n\n
    ()\n
    (final MXServer mxServer)\n
    '''
def restart():
    '''returns None\n\n
    restart()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def createSRWithTemplate():
    '''returns SRRemote\n\n
    createSRWithTemplate(final TKTemplateRemote template, final String originator)\n
    '''
def createServiceRequest():
    '''returns SRRemote\n\n
    createServiceRequest(final SolutionRemote solution, final String originator)\n
    '''
def destroy():
    '''returns None\n\n
    destroy()\n
    '''
def setChatOwner():
    '''returns None\n\n
    setChatOwner(final String ticketUid, final String agent)\n
    '''
def addCommLog():
    '''returns None\n\n
    addCommLog(final String ticketUid, final String userId, final String agentId, final List<Map<String, Object>> chatHistory, final String ticketclass, final String agentClientId, final String userClientId)\n
    '''
def addChatUser():
    '''returns None\n\n
    addChatUser(final String ticketUID, final String clientID, final String personID, final String tkClass, final String ticketID, final boolean isNewSR, final String queueID, final String nodeUrl)\n
    '''
def setUserAgentInfo():
    '''returns int\n\n
    setUserAgentInfo(final String agentPersonID, final String agentClientID, final String chatChannel, final String useruuid, final String nodeUrl)\n
    '''
def deleteChat():
    '''returns None\n\n
    deleteChat(final String channel, final boolean timedOut)\n
    '''
def deleteAbandonedChat():
    '''returns None\n\n
    deleteAbandonedChat(final String clientid, final String ticketUid)\n
    '''
def deleteServiceRequest():
    '''returns None\n\n
    deleteServiceRequest(final String ticketUid)\n
    '''
def updateChatStatus():
    '''returns None\n\n
    updateChatStatus(final String status, final String clientID)\n
    '''
def registerHost():
    '''returns None\n\n
    registerHost(final String URL)\n
    '''
def getOortCloud():
    '''returns ArrayList<String>\n\n
    getOortCloud(final String URL)\n
    '''
def releaseChatRequest():
    '''returns None\n\n
    releaseChatRequest(final String useruuid)\n
    '''
def cleanUpChats():
    '''returns None\n\n
    cleanUpChats(final String nodeurl)\n
    '''
def getAgentDisplayName():
    '''returns String\n\n
    getAgentDisplayName(final String agentID)\n
    '''
def getRequestPersonID():
    '''returns String\n\n
    getRequestPersonID()\n
    '''
def isChatAgent():
    '''returns boolean\n\n
    isChatAgent(final String personID)\n
    '''
def getAgentChatQueues():
    '''returns String[]\n\n
    getAgentChatQueues(final String personID)\n
    '''
def isUserAssignedToChannel():
    '''returns boolean\n\n
    isUserAssignedToChannel(final String channelID, final String sessionPersonID)\n
    '''
