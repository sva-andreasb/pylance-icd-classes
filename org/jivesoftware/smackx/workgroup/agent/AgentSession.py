def ():
    '''returns AgentSession\n\n
    (final EntityBareJid workgroupJID, final XMPPConnection connection)\n
    '''
def processStanza():
    '''returns None\n\n
    processStanza(final Stanza packet)\n
    '''
def handleIQRequest():
    '''returns IQ\n\n
    handleIQRequest(final IQ iqRequest)\n
    handleIQRequest(final IQ iqRequest)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def getAgentRoster():
    '''returns AgentRoster\n\n
    getAgentRoster()\n
    '''
def getMaxChats():
    '''returns int\n\n
    getMaxChats()\n
    '''
def isOnline():
    '''returns boolean\n\n
    isOnline()\n
    '''
def setMetaData():
    '''returns None\n\n
    setMetaData(final String key, final String val)\n
    '''
def removeMetaData():
    '''returns None\n\n
    removeMetaData(final String key)\n
    '''
def getMetaData():
    '''returns List<String>\n\n
    getMetaData(final String key)\n
    '''
def setOnline():
    '''returns None\n\n
    setOnline(final boolean online)\n
    '''
def setStatus():
    '''returns None\n\n
    setStatus(final Presence.Mode presenceMode, final int maxChats)\n
    setStatus(Presence.Mode presenceMode, final int maxChats, final String status)\n
    setStatus(Presence.Mode presenceMode, final String status)\n
    '''
def dequeueUser():
    '''returns None\n\n
    dequeueUser(final EntityJid userID)\n
    '''
def getTranscripts():
    '''returns Transcripts\n\n
    getTranscripts(final Jid userID)\n
    '''
def getTranscript():
    '''returns Transcript\n\n
    getTranscript(final String sessionID)\n
    '''
def getTranscriptSearchForm():
    '''returns Form\n\n
    getTranscriptSearchForm()\n
    '''
def searchTranscripts():
    '''returns ReportedData\n\n
    searchTranscripts(final Form completedForm)\n
    '''
def getOccupantsInfo():
    '''returns OccupantsInfo\n\n
    getOccupantsInfo(final String roomID)\n
    '''
def getWorkgroupJID():
    '''returns Jid\n\n
    getWorkgroupJID()\n
    '''
def getAgent():
    '''returns Agent\n\n
    getAgent()\n
    '''
def getQueue():
    '''returns WorkgroupQueue\n\n
    getQueue(final String queueName)\n
    getQueue(final Resourcepart queueName)\n
    '''
def getQueues():
    '''returns Iterator<WorkgroupQueue>\n\n
    getQueues()\n
    '''
def addQueueUsersListener():
    '''returns None\n\n
    addQueueUsersListener(final QueueUsersListener listener)\n
    '''
def removeQueueUsersListener():
    '''returns None\n\n
    removeQueueUsersListener(final QueueUsersListener listener)\n
    '''
def addOfferListener():
    '''returns None\n\n
    addOfferListener(final OfferListener offerListener)\n
    '''
def removeOfferListener():
    '''returns None\n\n
    removeOfferListener(final OfferListener offerListener)\n
    '''
def addInvitationListener():
    '''returns None\n\n
    addInvitationListener(final WorkgroupInvitationListener invitationListener)\n
    '''
def removeInvitationListener():
    '''returns None\n\n
    removeInvitationListener(final WorkgroupInvitationListener invitationListener)\n
    '''
def setNote():
    '''returns None\n\n
    setNote(final String sessionID, final String note)\n
    '''
def getNote():
    '''returns ChatNotes\n\n
    getNote(final String sessionID)\n
    '''
def getAgentHistory():
    '''returns AgentChatHistory\n\n
    getAgentHistory(final EntityBareJid jid, final int maxSessions, final Date startDate)\n
    '''
def getSearchSettings():
    '''returns SearchSettings\n\n
    getSearchSettings()\n
    '''
def getMacros():
    '''returns MacroGroup\n\n
    getMacros(final boolean global)\n
    '''
def saveMacros():
    '''returns None\n\n
    saveMacros(final MacroGroup group)\n
    '''
def sendRoomInvitation():
    '''returns None\n\n
    sendRoomInvitation(final RoomInvitation.Type type, final Jid invitee, final String sessionID, final String reason)\n
    '''
def sendRoomTransfer():
    '''returns None\n\n
    sendRoomTransfer(final RoomTransfer.Type type, final String invitee, final String sessionID, final String reason)\n
    '''
def getGenericSettings():
    '''returns GenericSettings\n\n
    getGenericSettings(final XMPPConnection con, final String query)\n
    '''
def hasMonitorPrivileges():
    '''returns boolean\n\n
    hasMonitorPrivileges(final XMPPConnection con)\n
    '''
def makeRoomOwner():
    '''returns None\n\n
    makeRoomOwner(final XMPPConnection con, final String sessionID)\n
    '''
