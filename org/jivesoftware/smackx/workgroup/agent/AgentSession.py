def AgentSession():
    '''public AgentSession(final EntityBareJid workgroupJID, final XMPPConnection connection)
    '''
def processStanza():
    '''public void processStanza(final Stanza packet)
    '''
def handleIQRequest():
    '''public IQ handleIQRequest(final IQ iqRequest)
    public IQ handleIQRequest(final IQ iqRequest)
    '''
def close():
    '''public void close()
    '''
def getAgentRoster():
    '''public AgentRoster getAgentRoster()
    '''
def getMaxChats():
    '''public int getMaxChats()
    '''
def isOnline():
    '''public boolean isOnline()
    '''
def setMetaData():
    '''public void setMetaData(final String key, final String val)
    '''
def removeMetaData():
    '''public void removeMetaData(final String key)
    '''
def getMetaData():
    '''public List<String> getMetaData(final String key)
    '''
def setOnline():
    '''public void setOnline(final boolean online)
    '''
def setStatus():
    '''public void setStatus(final Presence.Mode presenceMode, final int maxChats)
    public void setStatus(Presence.Mode presenceMode, final int maxChats, final String status)
    public void setStatus(Presence.Mode presenceMode, final String status)
    '''
def dequeueUser():
    '''public void dequeueUser(final EntityJid userID)
    '''
def getTranscripts():
    '''public Transcripts getTranscripts(final Jid userID)
    '''
def getTranscript():
    '''public Transcript getTranscript(final String sessionID)
    '''
def getTranscriptSearchForm():
    '''public Form getTranscriptSearchForm()
    '''
def searchTranscripts():
    '''public ReportedData searchTranscripts(final Form completedForm)
    '''
def getOccupantsInfo():
    '''public OccupantsInfo getOccupantsInfo(final String roomID)
    '''
def getWorkgroupJID():
    '''public Jid getWorkgroupJID()
    '''
def getAgent():
    '''public Agent getAgent()
    '''
def getQueue():
    '''public WorkgroupQueue getQueue(final String queueName)
    public WorkgroupQueue getQueue(final Resourcepart queueName)
    '''
def getQueues():
    '''public Iterator<WorkgroupQueue> getQueues()
    '''
def addQueueUsersListener():
    '''public void addQueueUsersListener(final QueueUsersListener listener)
    '''
def removeQueueUsersListener():
    '''public void removeQueueUsersListener(final QueueUsersListener listener)
    '''
def addOfferListener():
    '''public void addOfferListener(final OfferListener offerListener)
    '''
def removeOfferListener():
    '''public void removeOfferListener(final OfferListener offerListener)
    '''
def addInvitationListener():
    '''public void addInvitationListener(final WorkgroupInvitationListener invitationListener)
    '''
def removeInvitationListener():
    '''public void removeInvitationListener(final WorkgroupInvitationListener invitationListener)
    '''
def setNote():
    '''public void setNote(final String sessionID, final String note)
    '''
def getNote():
    '''public ChatNotes getNote(final String sessionID)
    '''
def getAgentHistory():
    '''public AgentChatHistory getAgentHistory(final EntityBareJid jid, final int maxSessions, final Date startDate)
    '''
def getSearchSettings():
    '''public SearchSettings getSearchSettings()
    '''
def getMacros():
    '''public MacroGroup getMacros(final boolean global)
    '''
def saveMacros():
    '''public void saveMacros(final MacroGroup group)
    '''
def getChatMetadata():
    '''public Map<String, List<String>> getChatMetadata(final String sessionID)
    '''
def sendRoomInvitation():
    '''public void sendRoomInvitation(final RoomInvitation.Type type, final Jid invitee, final String sessionID, final String reason)
    '''
def sendRoomTransfer():
    '''public void sendRoomTransfer(final RoomTransfer.Type type, final String invitee, final String sessionID, final String reason)
    '''
def getGenericSettings():
    '''public GenericSettings getGenericSettings(final XMPPConnection con, final String query)
    '''
def hasMonitorPrivileges():
    '''public boolean hasMonitorPrivileges(final XMPPConnection con)
    '''
def makeRoomOwner():
    '''public void makeRoomOwner(final XMPPConnection con, final String sessionID)
    '''
