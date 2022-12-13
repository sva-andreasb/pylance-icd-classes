def processStanza():
'''public void processStanza(final Stanza packet)
public void processStanza(final Stanza packet)
public void processStanza(final Stanza packet)
public void processStanza(final Stanza packet)
public void processStanza(final Stanza packet)
'''
pass
def run():
'''public void run()
public void run()
public void run()
'''
pass
def getRoom():
'''public EntityBareJid getRoom()
'''
pass
def create():
'''public synchronized MucCreateConfigFormHandle create(final Resourcepart nickname)
'''
pass
def createOrJoin():
'''public synchronized MucCreateConfigFormHandle createOrJoin(final Resourcepart nickname)
public MucCreateConfigFormHandle createOrJoin(final Resourcepart nickname, final String password, final DiscussionHistory history, final long timeout)
public synchronized MucCreateConfigFormHandle createOrJoin(final MucEnterConfiguration mucEnterConfiguration)
'''
pass
def createOrJoinIfNecessary():
'''public MucCreateConfigFormHandle createOrJoinIfNecessary(final Resourcepart nickname, final String password)
'''
pass
def join():
'''public void join(final Resourcepart nickname)
public void join(final Resourcepart nickname, final String password)
public void join(final Resourcepart nickname, final String password, final DiscussionHistory history, final long timeout)
public synchronized void join(final MucEnterConfiguration mucEnterConfiguration)
'''
pass
def isJoined():
'''public boolean isJoined()
'''
pass
def leave():
'''public synchronized void leave()
'''
pass
def leaveSync():
'''public synchronized Presence leaveSync()
'''
pass
def getConfigFormManager():
'''public MucConfigFormManager getConfigFormManager()
public MucConfigFormManager getConfigFormManager()
'''
pass
def getConfigurationForm():
'''public Form getConfigurationForm()
'''
pass
def sendConfigurationForm():
'''public void sendConfigurationForm(final Form form)
'''
pass
def getRegistrationForm():
'''public Form getRegistrationForm()
'''
pass
def sendRegistrationForm():
'''public void sendRegistrationForm(final Form form)
'''
pass
def destroy():
'''public void destroy(final String reason, final EntityBareJid alternateJID)
'''
pass
def invite():
'''public void invite(final EntityBareJid user, final String reason)
public void invite(final Message message, final EntityBareJid user, final String reason)
'''
pass
def addInvitationRejectionListener():
'''public boolean addInvitationRejectionListener(final InvitationRejectionListener listener)
'''
pass
def removeInvitationRejectionListener():
'''public boolean removeInvitationRejectionListener(final InvitationRejectionListener listener)
'''
pass
def addSubjectUpdatedListener():
'''public boolean addSubjectUpdatedListener(final SubjectUpdatedListener listener)
'''
pass
def removeSubjectUpdatedListener():
'''public boolean removeSubjectUpdatedListener(final SubjectUpdatedListener listener)
'''
pass
def addPresenceInterceptor():
'''public void addPresenceInterceptor(final PresenceListener presenceInterceptor)
'''
pass
def removePresenceInterceptor():
'''public void removePresenceInterceptor(final PresenceListener presenceInterceptor)
'''
pass
def getSubject():
'''public String getSubject()
'''
pass
def getReservedNickname():
'''public String getReservedNickname()
'''
pass
def getNickname():
'''public Resourcepart getNickname()
'''
pass
def changeNickname():
'''public synchronized void changeNickname(final Resourcepart nickname)
'''
pass
def changeAvailabilityStatus():
'''public void changeAvailabilityStatus(final String status, final Presence.Mode mode)
'''
pass
def kickParticipant():
'''public void kickParticipant(final Resourcepart nickname, final String reason)
'''
pass
def requestVoice():
'''public void requestVoice()
'''
pass
def grantVoice():
'''public void grantVoice(final Collection<Resourcepart> nicknames)
public void grantVoice(final Resourcepart nickname)
'''
pass
def revokeVoice():
'''public void revokeVoice(final Collection<Resourcepart> nicknames)
public void revokeVoice(final Resourcepart nickname)
'''
pass
def banUsers():
'''public void banUsers(final Collection<? extends Jid> jids)
'''
pass
def banUser():
'''public void banUser(final Jid jid, final String reason)
'''
pass
def grantMembership():
'''public void grantMembership(final Collection<? extends Jid> jids)
public void grantMembership(final Jid jid)
'''
pass
def revokeMembership():
'''public void revokeMembership(final Collection<? extends Jid> jids)
public void revokeMembership(final Jid jid)
'''
pass
def grantModerator():
'''public void grantModerator(final Collection<Resourcepart> nicknames)
public void grantModerator(final Resourcepart nickname)
'''
pass
def revokeModerator():
'''public void revokeModerator(final Collection<Resourcepart> nicknames)
public void revokeModerator(final Resourcepart nickname)
'''
pass
def grantOwnership():
'''public void grantOwnership(final Collection<? extends Jid> jids)
public void grantOwnership(final Jid jid)
'''
pass
def revokeOwnership():
'''public void revokeOwnership(final Collection<? extends Jid> jids)
public void revokeOwnership(final Jid jid)
'''
pass
def grantAdmin():
'''public void grantAdmin(final Collection<? extends Jid> jids)
public void grantAdmin(final Jid jid)
'''
pass
def revokeAdmin():
'''public void revokeAdmin(final Collection<? extends Jid> jids)
public void revokeAdmin(final EntityJid jid)
'''
pass
def getOccupantsCount():
'''public int getOccupantsCount()
'''
pass
def getOccupants():
'''public List<EntityFullJid> getOccupants()
'''
pass
def getOccupantPresence():
'''public Presence getOccupantPresence(final EntityFullJid user)
'''
pass
def getOccupant():
'''public Occupant getOccupant(final EntityFullJid user)
'''
pass
def addParticipantListener():
'''public boolean addParticipantListener(final PresenceListener listener)
'''
pass
def removeParticipantListener():
'''public boolean removeParticipantListener(final PresenceListener listener)
'''
pass
def getOwners():
'''public List<Affiliate> getOwners()
'''
pass
def getAdmins():
'''public List<Affiliate> getAdmins()
'''
pass
def getMembers():
'''public List<Affiliate> getMembers()
'''
pass
def getOutcasts():
'''public List<Affiliate> getOutcasts()
'''
pass
def getModerators():
'''public List<Occupant> getModerators()
'''
pass
def getParticipants():
'''public List<Occupant> getParticipants()
'''
pass
def sendMessage():
'''public void sendMessage(final String text)
public void sendMessage(final Message message)
'''
pass
def createPrivateChat():
'''public Chat createPrivateChat(final EntityFullJid occupant, final ChatMessageListener listener)
'''
pass
def createMessage():
'''public Message createMessage()
'''
pass
def pollMessage():
'''public Message pollMessage()
'''
pass
def nextMessage():
'''public Message nextMessage()
public Message nextMessage(final long timeout)
'''
pass
def addMessageListener():
'''public boolean addMessageListener(final MessageListener listener)
'''
pass
def removeMessageListener():
'''public boolean removeMessageListener(final MessageListener listener)
'''
pass
def changeSubject():
'''public void changeSubject(final String subject)
'''
pass
def accept():
'''public boolean accept(final Stanza packet)
'''
pass
def addUserStatusListener():
'''public boolean addUserStatusListener(final UserStatusListener listener)
'''
pass
def removeUserStatusListener():
'''public boolean removeUserStatusListener(final UserStatusListener listener)
'''
pass
def addParticipantStatusListener():
'''public boolean addParticipantStatusListener(final ParticipantStatusListener listener)
'''
pass
def removeParticipantStatusListener():
'''public boolean removeParticipantStatusListener(final ParticipantStatusListener listener)
'''
pass
def getXmppConnection():
'''public XMPPConnection getXmppConnection()
'''
pass
def toString():
'''public String toString()
'''
pass
def makeInstant():
'''public void makeInstant()
'''
pass
