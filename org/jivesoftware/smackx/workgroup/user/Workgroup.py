def Workgroup():
    '''public Workgroup(final EntityBareJid workgroupJID, final XMPPConnection connection)
    '''
def joinedQueue():
    '''public void joinedQueue()
    '''
def departedQueue():
    '''public void departedQueue()
    '''
def queuePositionUpdated():
    '''public void queuePositionUpdated(final int currentPosition)
    '''
def queueWaitTimeUpdated():
    '''public void queueWaitTimeUpdated(final int secondsRemaining)
    '''
def invitationReceived():
    '''public void invitationReceived(final XMPPConnection conn, final MultiUserChat room, final EntityJid inviter, final String reason, final String password, final Message message, final MUCUser.Invite invitation)
    '''
def processStanza():
    '''public void processStanza(final Stanza packet)
    '''
def getWorkgroupJID():
    '''public EntityBareJid getWorkgroupJID()
    '''
def isInQueue():
    '''public boolean isInQueue()
    '''
def isAvailable():
    '''public boolean isAvailable()
    '''
def getQueuePosition():
    '''public int getQueuePosition()
    '''
def getQueueRemainingTime():
    '''public int getQueueRemainingTime()
    '''
def joinQueue():
    '''public void joinQueue()
    public void joinQueue(final Form answerForm)
    public void joinQueue(final Form answerForm, final Jid userID)
    public void joinQueue(final Map<String, Object> metadata, final Jid userID)
    '''
def departQueue():
    '''public void departQueue()
    '''
def addQueueListener():
    '''public void addQueueListener(final QueueListener queueListener)
    '''
def removeQueueListener():
    '''public void removeQueueListener(final QueueListener queueListener)
    public void removeQueueListener(final WorkgroupInvitationListener invitationListener)
    '''
def addInvitationListener():
    '''public void addInvitationListener(final WorkgroupInvitationListener invitationListener)
    '''
def getChatSetting():
    '''public ChatSetting getChatSetting(final String key)
    '''
def getChatSettings():
    '''public ChatSettings getChatSettings(final int type)
    public ChatSettings getChatSettings()
    '''
def isEmailAvailable():
    '''public boolean isEmailAvailable()
    '''
def getOfflineSettings():
    '''public OfflineSettings getOfflineSettings()
    '''
def getSoundSettings():
    '''public SoundSettings getSoundSettings()
    '''
def getWorkgroupProperties():
    '''public WorkgroupProperties getWorkgroupProperties()
    public WorkgroupProperties getWorkgroupProperties(final String jid)
    '''
def getWorkgroupForm():
    '''public Form getWorkgroupForm()
    '''
