def AgentSession():
'''public AgentSession(final EntityBareJid workgroupJID, final XMPPConnection connection)
'''
pass
def processStanza():
'''public void processStanza(final Stanza packet)
'''
pass
def handleIQRequest():
'''public IQ handleIQRequest(final IQ iqRequest)
public IQ handleIQRequest(final IQ iqRequest)
'''
pass
def close():
'''public void close()
'''
pass
def getAgentRoster():
'''public AgentRoster getAgentRoster()
'''
pass
def getMaxChats():
'''public int getMaxChats()
'''
pass
def isOnline():
'''public boolean isOnline()
'''
pass
def setMetaData():
'''public void setMetaData(final String key, final String val)
'''
pass
def removeMetaData():
'''public void removeMetaData(final String key)
'''
pass
def getMetaData():
'''public List<String> getMetaData(final String key)
'''
pass
def setOnline():
'''public void setOnline(final boolean online)
'''
pass
def setStatus():
'''public void setStatus(final Presence.Mode presenceMode, final int maxChats)
public void setStatus(Presence.Mode presenceMode, final int maxChats, final String status)
public void setStatus(Presence.Mode presenceMode, final String status)
'''
pass
def dequeueUser():
'''public void dequeueUser(final EntityJid userID)
'''
pass
def getTranscripts():
'''public Transcripts getTranscripts(final Jid userID)
'''
pass
def getTranscript():
'''public Transcript getTranscript(final String sessionID)
'''
pass
def getTranscriptSearchForm():
'''public Form getTranscriptSearchForm()
'''
pass
def searchTranscripts():
'''public ReportedData searchTranscripts(final Form completedForm)
'''
pass
def getOccupantsInfo():
'''public OccupantsInfo getOccupantsInfo(final String roomID)
'''
pass
def getWorkgroupJID():
'''public Jid getWorkgroupJID()
'''
pass
def getAgent():
'''public Agent getAgent()
'''
pass
def getQueue():
'''public WorkgroupQueue getQueue(final String queueName)
public WorkgroupQueue getQueue(final Resourcepart queueName)
'''
pass
def getQueues():
'''public Iterator<WorkgroupQueue> getQueues()
'''
pass
def addQueueUsersListener():
'''public void addQueueUsersListener(final QueueUsersListener listener)
'''
pass
def removeQueueUsersListener():
'''public void removeQueueUsersListener(final QueueUsersListener listener)
'''
pass
def addOfferListener():
'''public void addOfferListener(final OfferListener offerListener)
'''
pass
def removeOfferListener():
'''public void removeOfferListener(final OfferListener offerListener)
'''
pass
def addInvitationListener():
'''public void addInvitationListener(final WorkgroupInvitationListener invitationListener)
'''
pass
def removeInvitationListener():
'''public void removeInvitationListener(final WorkgroupInvitationListener invitationListener)
'''
pass
def setNote():
'''public void setNote(final String sessionID, final String note)
'''
pass
def getNote():
'''public ChatNotes getNote(final String sessionID)
'''
pass
def getAgentHistory():
'''public AgentChatHistory getAgentHistory(final EntityBareJid jid, final int maxSessions, final Date startDate)
'''
pass
def getSearchSettings():
'''public SearchSettings getSearchSettings()
'''
pass
def getMacros():
'''public MacroGroup getMacros(final boolean global)
'''
pass
def saveMacros():
'''public void saveMacros(final MacroGroup group)
'''
pass
def getChatMetadata():
'''public Map<String, List<String>> getChatMetadata(final String sessionID)
'''
pass
def sendRoomInvitation():
'''public void sendRoomInvitation(final RoomInvitation.Type type, final Jid invitee, final String sessionID, final String reason)
'''
pass
def sendRoomTransfer():
'''public void sendRoomTransfer(final RoomTransfer.Type type, final String invitee, final String sessionID, final String reason)
'''
pass
def getGenericSettings():
'''public GenericSettings getGenericSettings(final XMPPConnection con, final String query)
'''
pass
def hasMonitorPrivileges():
'''public boolean hasMonitorPrivileges(final XMPPConnection con)
'''
pass
def makeRoomOwner():
'''public void makeRoomOwner(final XMPPConnection con, final String sessionID)
'''
pass
