def Workgroup():
'''public Workgroup(final EntityBareJid workgroupJID, final XMPPConnection connection)
'''
pass
def joinedQueue():
'''public void joinedQueue()
'''
pass
def departedQueue():
'''public void departedQueue()
'''
pass
def queuePositionUpdated():
'''public void queuePositionUpdated(final int currentPosition)
'''
pass
def queueWaitTimeUpdated():
'''public void queueWaitTimeUpdated(final int secondsRemaining)
'''
pass
def invitationReceived():
'''public void invitationReceived(final XMPPConnection conn, final MultiUserChat room, final EntityJid inviter, final String reason, final String password, final Message message, final MUCUser.Invite invitation)
'''
pass
def processStanza():
'''public void processStanza(final Stanza packet)
'''
pass
def getWorkgroupJID():
'''public EntityBareJid getWorkgroupJID()
'''
pass
def isInQueue():
'''public boolean isInQueue()
'''
pass
def isAvailable():
'''public boolean isAvailable()
'''
pass
def getQueuePosition():
'''public int getQueuePosition()
'''
pass
def getQueueRemainingTime():
'''public int getQueueRemainingTime()
'''
pass
def joinQueue():
'''public void joinQueue()
public void joinQueue(final Form answerForm)
public void joinQueue(final Form answerForm, final Jid userID)
public void joinQueue(final Map<String, Object> metadata, final Jid userID)
'''
pass
def departQueue():
'''public void departQueue()
'''
pass
def addQueueListener():
'''public void addQueueListener(final QueueListener queueListener)
'''
pass
def removeQueueListener():
'''public void removeQueueListener(final QueueListener queueListener)
public void removeQueueListener(final WorkgroupInvitationListener invitationListener)
'''
pass
def addInvitationListener():
'''public void addInvitationListener(final WorkgroupInvitationListener invitationListener)
'''
pass
def getChatSetting():
'''public ChatSetting getChatSetting(final String key)
'''
pass
def getChatSettings():
'''public ChatSettings getChatSettings(final int type)
public ChatSettings getChatSettings()
'''
pass
def isEmailAvailable():
'''public boolean isEmailAvailable()
'''
pass
def getOfflineSettings():
'''public OfflineSettings getOfflineSettings()
'''
pass
def getSoundSettings():
'''public SoundSettings getSoundSettings()
'''
pass
def getWorkgroupProperties():
'''public WorkgroupProperties getWorkgroupProperties()
public WorkgroupProperties getWorkgroupProperties(final String jid)
'''
pass
def getWorkgroupForm():
'''public Form getWorkgroupForm()
'''
pass
