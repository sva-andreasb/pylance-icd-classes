def ():
    '''returns Workgroup\n\n
    (final EntityBareJid workgroupJID, final XMPPConnection connection)\n
    '''
def joinedQueue():
    '''returns None\n\n
    joinedQueue()\n
    '''
def departedQueue():
    '''returns None\n\n
    departedQueue()\n
    '''
def queuePositionUpdated():
    '''returns None\n\n
    queuePositionUpdated(final int currentPosition)\n
    '''
def queueWaitTimeUpdated():
    '''returns None\n\n
    queueWaitTimeUpdated(final int secondsRemaining)\n
    '''
def invitationReceived():
    '''returns None\n\n
    invitationReceived(final XMPPConnection conn, final MultiUserChat room, final EntityJid inviter, final String reason, final String password, final Message message, final MUCUser.Invite invitation)\n
    '''
def processStanza():
    '''returns None\n\n
    processStanza(final Stanza packet)\n
    '''
def getWorkgroupJID():
    '''returns EntityBareJid\n\n
    getWorkgroupJID()\n
    '''
def isInQueue():
    '''returns boolean\n\n
    isInQueue()\n
    '''
def isAvailable():
    '''returns boolean\n\n
    isAvailable()\n
    '''
def getQueuePosition():
    '''returns int\n\n
    getQueuePosition()\n
    '''
def getQueueRemainingTime():
    '''returns int\n\n
    getQueueRemainingTime()\n
    '''
def joinQueue():
    '''returns None\n\n
    joinQueue()\n
    joinQueue(final Form answerForm)\n
    joinQueue(final Form answerForm, final Jid userID)\n
    joinQueue(final Map<String, Object> metadata, final Jid userID)\n
    '''
def departQueue():
    '''returns None\n\n
    departQueue()\n
    '''
def addQueueListener():
    '''returns None\n\n
    addQueueListener(final QueueListener queueListener)\n
    '''
def removeQueueListener():
    '''returns None\n\n
    removeQueueListener(final QueueListener queueListener)\n
    removeQueueListener(final WorkgroupInvitationListener invitationListener)\n
    '''
def addInvitationListener():
    '''returns None\n\n
    addInvitationListener(final WorkgroupInvitationListener invitationListener)\n
    '''
def getChatSetting():
    '''returns ChatSetting\n\n
    getChatSetting(final String key)\n
    '''
def getChatSettings():
    '''returns ChatSettings\n\n
    getChatSettings(final int type)\n
    getChatSettings()\n
    '''
def isEmailAvailable():
    '''returns boolean\n\n
    isEmailAvailable()\n
    '''
def getOfflineSettings():
    '''returns OfflineSettings\n\n
    getOfflineSettings()\n
    '''
def getSoundSettings():
    '''returns SoundSettings\n\n
    getSoundSettings()\n
    '''
def getWorkgroupProperties():
    '''returns WorkgroupProperties\n\n
    getWorkgroupProperties()\n
    getWorkgroupProperties(final String jid)\n
    '''
def getWorkgroupForm():
    '''returns Form\n\n
    getWorkgroupForm()\n
    '''
