MESSAGE_GROUP = "String  instantmessaging""
IM_SERVER_HOST_MX_PROPERTY = "String  mxe.imi.serverhostname""
def getIMSessionHandler():
'''public static synchronized IMSessionHandler getIMSessionHandler(final HttpSession httpSession)
'''
pass
def hasIMSessionHandler():
'''public static synchronized boolean hasIMSessionHandler(final HttpSession session)
'''
pass
def validate():
'''public synchronized boolean validate()
'''
pass
def refreshIMServerHostname():
'''public synchronized boolean refreshIMServerHostname()
'''
pass
def refreshIMConnectionTimeout():
'''public synchronized boolean refreshIMConnectionTimeout()
'''
pass
def openIMSession():
'''public synchronized boolean openIMSession()
public synchronized boolean openIMSession(final IMUser.IMUserStatus imUserStatus)
'''
pass
def closeIMSession():
'''public synchronized boolean closeIMSession(final boolean saveFlag, final WebClientSession webClientSession)
public synchronized boolean closeIMSession(final boolean saveFlag, final HttpServletRequest request)
'''
pass
def changeUserStatus():
'''public synchronized void changeUserStatus(final IMUser.IMUserStatus imUserStatus)
'''
pass
def getUserInfo():
'''public static synchronized UserInfo getUserInfo(final HttpSession httpSession)
'''
pass
def getImDriverName():
'''public synchronized String getImDriverName()
'''
pass
def getIMServerHostname():
'''public synchronized String getIMServerHostname()
'''
pass
def getIMConnectionTimeout():
'''public synchronized String getIMConnectionTimeout()
'''
pass
def getPartnerInfo():
'''public synchronized PartnerInfo getPartnerInfo(final HttpServletRequest httpRequest)
'''
pass
def isIMSessionOpened():
'''public synchronized boolean isIMSessionOpened()
'''
pass
def userStatusChanged():
'''public void userStatusChanged(final IMUserStatusEvent userStatusEvent)
'''
pass
def resolve():
'''public synchronized IMUser resolve(final String userDisplayName)
'''
pass
def isUserAvailable():
'''public boolean isUserAvailable(final String userId)
'''
pass
def getChatHelper():
'''public synchronized ChatHelper getChatHelper(final HttpServletRequest httpRequest, final String sessionId, final long chatIdentifier, final String partnerIMId)
'''
pass
def isPartnerChatting():
'''public synchronized boolean isPartnerChatting(final String partnerIMId)
'''
pass
def chatClosed():
'''public void chatClosed(final String sessionId)
'''
pass
def valueBound():
'''public void valueBound(final HttpSessionBindingEvent arg0)
'''
pass
def valueUnbound():
'''public void valueUnbound(final HttpSessionBindingEvent arg0)
'''
pass
def serverConnected():
'''public void serverConnected(final MXEvent evt)
'''
pass
def serverConnectionError():
'''public void serverConnectionError(final MXEvent evt)
'''
pass
def serverDisconnected():
'''public void serverDisconnected(final MXEvent evt)
'''
pass
def wasChatHelperAborted():
'''public static synchronized boolean wasChatHelperAborted(final String sessionId)
'''
pass
def wasChatTranscriptSavedBeforeAbortion():
'''public static synchronized boolean wasChatTranscriptSavedBeforeAbortion(final String sessionId)
'''
pass
def resetActivityFlag():
'''public void resetActivityFlag()
'''
pass
def logInfo():
'''public static void logInfo(final String logMessage)
'''
pass
def logDebug():
'''public static void logDebug(final String logMessage)
'''
pass
def logError():
'''public static void logError(final Throwable throwable)
public static void logError(final String logMessage, final Throwable throwable)
'''
pass
