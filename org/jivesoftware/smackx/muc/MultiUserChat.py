def processStanza():
    '''public void processStanza(final Stanza packet)
    public void processStanza(final Stanza packet)
    public void processStanza(final Stanza packet)
    public void processStanza(final Stanza packet)
    public void processStanza(final Stanza packet)
    '''
def run():
    '''public void run()
    public void run()
    public void run()
    '''
def getRoom():
    '''public EntityBareJid getRoom()
    '''
def create():
    '''public synchronized MucCreateConfigFormHandle create(final Resourcepart nickname)
    '''
def createOrJoin():
    '''public synchronized MucCreateConfigFormHandle createOrJoin(final Resourcepart nickname)
    public MucCreateConfigFormHandle createOrJoin(final Resourcepart nickname, final String password, final DiscussionHistory history, final long timeout)
    public synchronized MucCreateConfigFormHandle createOrJoin(final MucEnterConfiguration mucEnterConfiguration)
    '''
def createOrJoinIfNecessary():
    '''public MucCreateConfigFormHandle createOrJoinIfNecessary(final Resourcepart nickname, final String password)
    '''
def join():
    '''public void join(final Resourcepart nickname)
    public void join(final Resourcepart nickname, final String password)
    public void join(final Resourcepart nickname, final String password, final DiscussionHistory history, final long timeout)
    public synchronized void join(final MucEnterConfiguration mucEnterConfiguration)
    '''
def isJoined():
    '''public boolean isJoined()
    '''
def leave():
    '''public synchronized void leave()
    '''
def leaveSync():
    '''public synchronized Presence leaveSync()
    '''
def getConfigFormManager():
    '''public MucConfigFormManager getConfigFormManager()
    public MucConfigFormManager getConfigFormManager()
    '''
def getConfigurationForm():
    '''public Form getConfigurationForm()
    '''
def sendConfigurationForm():
    '''public void sendConfigurationForm(final Form form)
    '''
def getRegistrationForm():
    '''public Form getRegistrationForm()
    '''
def sendRegistrationForm():
    '''public void sendRegistrationForm(final Form form)
    '''
def destroy():
    '''public void destroy(final String reason, final EntityBareJid alternateJID)
    '''
def invite():
    '''public void invite(final EntityBareJid user, final String reason)
    public void invite(final Message message, final EntityBareJid user, final String reason)
    '''
def addInvitationRejectionListener():
    '''public boolean addInvitationRejectionListener(final InvitationRejectionListener listener)
    '''
def removeInvitationRejectionListener():
    '''public boolean removeInvitationRejectionListener(final InvitationRejectionListener listener)
    '''
def addSubjectUpdatedListener():
    '''public boolean addSubjectUpdatedListener(final SubjectUpdatedListener listener)
    '''
def removeSubjectUpdatedListener():
    '''public boolean removeSubjectUpdatedListener(final SubjectUpdatedListener listener)
    '''
def addPresenceInterceptor():
    '''public void addPresenceInterceptor(final PresenceListener presenceInterceptor)
    '''
def removePresenceInterceptor():
    '''public void removePresenceInterceptor(final PresenceListener presenceInterceptor)
    '''
def getSubject():
    '''public String getSubject()
    '''
def getReservedNickname():
    '''public String getReservedNickname()
    '''
def getNickname():
    '''public Resourcepart getNickname()
    '''
def changeNickname():
    '''public synchronized void changeNickname(final Resourcepart nickname)
    '''
def changeAvailabilityStatus():
    '''public void changeAvailabilityStatus(final String status, final Presence.Mode mode)
    '''
def kickParticipant():
    '''public void kickParticipant(final Resourcepart nickname, final String reason)
    '''
def requestVoice():
    '''public void requestVoice()
    '''
def grantVoice():
    '''public void grantVoice(final Collection<Resourcepart> nicknames)
    public void grantVoice(final Resourcepart nickname)
    '''
def revokeVoice():
    '''public void revokeVoice(final Collection<Resourcepart> nicknames)
    public void revokeVoice(final Resourcepart nickname)
    '''
def banUsers():
    '''public void banUsers(final Collection<? extends Jid> jids)
    '''
def banUser():
    '''public void banUser(final Jid jid, final String reason)
    '''
def grantMembership():
    '''public void grantMembership(final Collection<? extends Jid> jids)
    public void grantMembership(final Jid jid)
    '''
def revokeMembership():
    '''public void revokeMembership(final Collection<? extends Jid> jids)
    public void revokeMembership(final Jid jid)
    '''
def grantModerator():
    '''public void grantModerator(final Collection<Resourcepart> nicknames)
    public void grantModerator(final Resourcepart nickname)
    '''
def revokeModerator():
    '''public void revokeModerator(final Collection<Resourcepart> nicknames)
    public void revokeModerator(final Resourcepart nickname)
    '''
def grantOwnership():
    '''public void grantOwnership(final Collection<? extends Jid> jids)
    public void grantOwnership(final Jid jid)
    '''
def revokeOwnership():
    '''public void revokeOwnership(final Collection<? extends Jid> jids)
    public void revokeOwnership(final Jid jid)
    '''
def grantAdmin():
    '''public void grantAdmin(final Collection<? extends Jid> jids)
    public void grantAdmin(final Jid jid)
    '''
def revokeAdmin():
    '''public void revokeAdmin(final Collection<? extends Jid> jids)
    public void revokeAdmin(final EntityJid jid)
    '''
def getOccupantsCount():
    '''public int getOccupantsCount()
    '''
def getOccupants():
    '''public List<EntityFullJid> getOccupants()
    '''
def getOccupantPresence():
    '''public Presence getOccupantPresence(final EntityFullJid user)
    '''
def getOccupant():
    '''public Occupant getOccupant(final EntityFullJid user)
    '''
def addParticipantListener():
    '''public boolean addParticipantListener(final PresenceListener listener)
    '''
def removeParticipantListener():
    '''public boolean removeParticipantListener(final PresenceListener listener)
    '''
def getOwners():
    '''public List<Affiliate> getOwners()
    '''
def getAdmins():
    '''public List<Affiliate> getAdmins()
    '''
def getMembers():
    '''public List<Affiliate> getMembers()
    '''
def getOutcasts():
    '''public List<Affiliate> getOutcasts()
    '''
def getModerators():
    '''public List<Occupant> getModerators()
    '''
def getParticipants():
    '''public List<Occupant> getParticipants()
    '''
def sendMessage():
    '''public void sendMessage(final String text)
    public void sendMessage(final Message message)
    '''
def createPrivateChat():
    '''public Chat createPrivateChat(final EntityFullJid occupant, final ChatMessageListener listener)
    '''
def createMessage():
    '''public Message createMessage()
    '''
def pollMessage():
    '''public Message pollMessage()
    '''
def nextMessage():
    '''public Message nextMessage()
    public Message nextMessage(final long timeout)
    '''
def addMessageListener():
    '''public boolean addMessageListener(final MessageListener listener)
    '''
def removeMessageListener():
    '''public boolean removeMessageListener(final MessageListener listener)
    '''
def changeSubject():
    '''public void changeSubject(final String subject)
    '''
def accept():
    '''public boolean accept(final Stanza packet)
    '''
def addUserStatusListener():
    '''public boolean addUserStatusListener(final UserStatusListener listener)
    '''
def removeUserStatusListener():
    '''public boolean removeUserStatusListener(final UserStatusListener listener)
    '''
def addParticipantStatusListener():
    '''public boolean addParticipantStatusListener(final ParticipantStatusListener listener)
    '''
def removeParticipantStatusListener():
    '''public boolean removeParticipantStatusListener(final ParticipantStatusListener listener)
    '''
def getXmppConnection():
    '''public XMPPConnection getXmppConnection()
    '''
def toString():
    '''public String toString()
    '''
def makeInstant():
    '''public void makeInstant()
    '''
