def processStanza():
    '''returns None\n\n
    processStanza(final Stanza packet)\n
    processStanza(final Stanza packet)\n
    processStanza(final Stanza packet)\n
    processStanza(final Stanza packet)\n
    processStanza(final Stanza packet)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    run()\n
    '''
def getRoom():
    '''returns EntityBareJid\n\n
    getRoom()\n
    '''
def createOrJoin():
    '''returns MucCreateConfigFormHandle\n\n
    createOrJoin(final Resourcepart nickname, final String password, final DiscussionHistory history, final long timeout)\n
    '''
def createOrJoinIfNecessary():
    '''returns MucCreateConfigFormHandle\n\n
    createOrJoinIfNecessary(final Resourcepart nickname, final String password)\n
    '''
def join():
    '''returns None\n\n
    join(final Resourcepart nickname)\n
    join(final Resourcepart nickname, final String password)\n
    join(final Resourcepart nickname, final String password, final DiscussionHistory history, final long timeout)\n
    '''
def isJoined():
    '''returns boolean\n\n
    isJoined()\n
    '''
def getConfigFormManager():
    '''returns MucConfigFormManager\n\n
    getConfigFormManager()\n
    getConfigFormManager()\n
    '''
def getConfigurationForm():
    '''returns Form\n\n
    getConfigurationForm()\n
    '''
def sendConfigurationForm():
    '''returns None\n\n
    sendConfigurationForm(final Form form)\n
    '''
def getRegistrationForm():
    '''returns Form\n\n
    getRegistrationForm()\n
    '''
def sendRegistrationForm():
    '''returns None\n\n
    sendRegistrationForm(final Form form)\n
    '''
def destroy():
    '''returns None\n\n
    destroy(final String reason, final EntityBareJid alternateJID)\n
    '''
def invite():
    '''returns None\n\n
    invite(final EntityBareJid user, final String reason)\n
    invite(final Message message, final EntityBareJid user, final String reason)\n
    '''
def addInvitationRejectionListener():
    '''returns boolean\n\n
    addInvitationRejectionListener(final InvitationRejectionListener listener)\n
    '''
def removeInvitationRejectionListener():
    '''returns boolean\n\n
    removeInvitationRejectionListener(final InvitationRejectionListener listener)\n
    '''
def addSubjectUpdatedListener():
    '''returns boolean\n\n
    addSubjectUpdatedListener(final SubjectUpdatedListener listener)\n
    '''
def removeSubjectUpdatedListener():
    '''returns boolean\n\n
    removeSubjectUpdatedListener(final SubjectUpdatedListener listener)\n
    '''
def addPresenceInterceptor():
    '''returns None\n\n
    addPresenceInterceptor(final PresenceListener presenceInterceptor)\n
    '''
def removePresenceInterceptor():
    '''returns None\n\n
    removePresenceInterceptor(final PresenceListener presenceInterceptor)\n
    '''
def getSubject():
    '''returns String\n\n
    getSubject()\n
    '''
def getReservedNickname():
    '''returns String\n\n
    getReservedNickname()\n
    '''
def getNickname():
    '''returns Resourcepart\n\n
    getNickname()\n
    '''
def changeAvailabilityStatus():
    '''returns None\n\n
    changeAvailabilityStatus(final String status, final Presence.Mode mode)\n
    '''
def kickParticipant():
    '''returns None\n\n
    kickParticipant(final Resourcepart nickname, final String reason)\n
    '''
def requestVoice():
    '''returns None\n\n
    requestVoice()\n
    '''
def grantVoice():
    '''returns None\n\n
    grantVoice(final Collection<Resourcepart> nicknames)\n
    grantVoice(final Resourcepart nickname)\n
    '''
def revokeVoice():
    '''returns None\n\n
    revokeVoice(final Collection<Resourcepart> nicknames)\n
    revokeVoice(final Resourcepart nickname)\n
    '''
def banUsers():
    '''returns None\n\n
    banUsers(final Collection<? extends Jid> jids)\n
    '''
def banUser():
    '''returns None\n\n
    banUser(final Jid jid, final String reason)\n
    '''
def grantMembership():
    '''returns None\n\n
    grantMembership(final Collection<? extends Jid> jids)\n
    grantMembership(final Jid jid)\n
    '''
def revokeMembership():
    '''returns None\n\n
    revokeMembership(final Collection<? extends Jid> jids)\n
    revokeMembership(final Jid jid)\n
    '''
def grantModerator():
    '''returns None\n\n
    grantModerator(final Collection<Resourcepart> nicknames)\n
    grantModerator(final Resourcepart nickname)\n
    '''
def revokeModerator():
    '''returns None\n\n
    revokeModerator(final Collection<Resourcepart> nicknames)\n
    revokeModerator(final Resourcepart nickname)\n
    '''
def grantOwnership():
    '''returns None\n\n
    grantOwnership(final Collection<? extends Jid> jids)\n
    grantOwnership(final Jid jid)\n
    '''
def revokeOwnership():
    '''returns None\n\n
    revokeOwnership(final Collection<? extends Jid> jids)\n
    revokeOwnership(final Jid jid)\n
    '''
def grantAdmin():
    '''returns None\n\n
    grantAdmin(final Collection<? extends Jid> jids)\n
    grantAdmin(final Jid jid)\n
    '''
def revokeAdmin():
    '''returns None\n\n
    revokeAdmin(final Collection<? extends Jid> jids)\n
    revokeAdmin(final EntityJid jid)\n
    '''
def getOccupantsCount():
    '''returns int\n\n
    getOccupantsCount()\n
    '''
def getOccupants():
    '''returns List<EntityFullJid>\n\n
    getOccupants()\n
    '''
def getOccupantPresence():
    '''returns Presence\n\n
    getOccupantPresence(final EntityFullJid user)\n
    '''
def getOccupant():
    '''returns Occupant\n\n
    getOccupant(final EntityFullJid user)\n
    '''
def addParticipantListener():
    '''returns boolean\n\n
    addParticipantListener(final PresenceListener listener)\n
    '''
def removeParticipantListener():
    '''returns boolean\n\n
    removeParticipantListener(final PresenceListener listener)\n
    '''
def getOwners():
    '''returns List<Affiliate>\n\n
    getOwners()\n
    '''
def getAdmins():
    '''returns List<Affiliate>\n\n
    getAdmins()\n
    '''
def getMembers():
    '''returns List<Affiliate>\n\n
    getMembers()\n
    '''
def getOutcasts():
    '''returns List<Affiliate>\n\n
    getOutcasts()\n
    '''
def getModerators():
    '''returns List<Occupant>\n\n
    getModerators()\n
    '''
def getParticipants():
    '''returns List<Occupant>\n\n
    getParticipants()\n
    '''
def sendMessage():
    '''returns None\n\n
    sendMessage(final String text)\n
    sendMessage(final Message message)\n
    '''
def createPrivateChat():
    '''returns Chat\n\n
    createPrivateChat(final EntityFullJid occupant, final ChatMessageListener listener)\n
    '''
def createMessage():
    '''returns Message\n\n
    createMessage()\n
    '''
def pollMessage():
    '''returns Message\n\n
    pollMessage()\n
    '''
def nextMessage():
    '''returns Message\n\n
    nextMessage()\n
    nextMessage(final long timeout)\n
    '''
def addMessageListener():
    '''returns boolean\n\n
    addMessageListener(final MessageListener listener)\n
    '''
def removeMessageListener():
    '''returns boolean\n\n
    removeMessageListener(final MessageListener listener)\n
    '''
def changeSubject():
    '''returns None\n\n
    changeSubject(final String subject)\n
    '''
def accept():
    '''returns boolean\n\n
    accept(final Stanza packet)\n
    '''
def addUserStatusListener():
    '''returns boolean\n\n
    addUserStatusListener(final UserStatusListener listener)\n
    '''
def removeUserStatusListener():
    '''returns boolean\n\n
    removeUserStatusListener(final UserStatusListener listener)\n
    '''
def addParticipantStatusListener():
    '''returns boolean\n\n
    addParticipantStatusListener(final ParticipantStatusListener listener)\n
    '''
def removeParticipantStatusListener():
    '''returns boolean\n\n
    removeParticipantStatusListener(final ParticipantStatusListener listener)\n
    '''
def getXmppConnection():
    '''returns XMPPConnection\n\n
    getXmppConnection()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def makeInstant():
    '''returns None\n\n
    makeInstant()\n
    '''
