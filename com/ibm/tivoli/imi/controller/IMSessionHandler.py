MESSAGE_GROUP = "String  \"instantmessaging\""
IM_SERVER_HOST_MX_PROPERTY = "String  \"mxe.imi.serverhostname\""
def getIMSessionHandler():
    '''    public static synchronized IMSessionHandler getIMSessionHandler(final HttpSession httpSession)
    '''
def hasIMSessionHandler():
    '''    public static synchronized boolean hasIMSessionHandler(final HttpSession session)
    '''
def validate():
    '''    public synchronized boolean validate()
    '''
def refreshIMServerHostname():
    '''    public synchronized boolean refreshIMServerHostname()
    '''
def refreshIMConnectionTimeout():
    '''    public synchronized boolean refreshIMConnectionTimeout()
    '''
def openIMSession():
    '''    public synchronized boolean openIMSession()
    public synchronized boolean openIMSession(final IMUser.IMUserStatus imUserStatus)
    '''
def closeIMSession():
    '''    public synchronized boolean closeIMSession(final boolean saveFlag, final WebClientSession webClientSession)
    public synchronized boolean closeIMSession(final boolean saveFlag, final HttpServletRequest request)
    '''
def changeUserStatus():
    '''    public synchronized void changeUserStatus(final IMUser.IMUserStatus imUserStatus)
    '''
def getUserInfo():
    '''    public static synchronized UserInfo getUserInfo(final HttpSession httpSession)
    '''
def getImDriverName():
    '''    public synchronized String getImDriverName()
    '''
def getIMServerHostname():
    '''    public synchronized String getIMServerHostname()
    '''
def getIMConnectionTimeout():
    '''    public synchronized String getIMConnectionTimeout()
    '''
def getPartnerInfo():
    '''    public synchronized PartnerInfo getPartnerInfo(final HttpServletRequest httpRequest)
    '''
def isIMSessionOpened():
    '''    public synchronized boolean isIMSessionOpened()
    '''
def userStatusChanged():
    '''    public void userStatusChanged(final IMUserStatusEvent userStatusEvent)
    '''
def resolve():
    '''    public synchronized IMUser resolve(final String userDisplayName)
    '''
def isUserAvailable():
    '''    public boolean isUserAvailable(final String userId)
    '''
def getChatHelper():
    '''    public synchronized ChatHelper getChatHelper(final HttpServletRequest httpRequest, final String sessionId, final long chatIdentifier, final String partnerIMId)
    '''
def isPartnerChatting():
    '''    public synchronized boolean isPartnerChatting(final String partnerIMId)
    '''
def chatClosed():
    '''    public void chatClosed(final String sessionId)
    '''
def valueBound():
    '''    public void valueBound(final HttpSessionBindingEvent arg0)
    '''
def valueUnbound():
    '''    public void valueUnbound(final HttpSessionBindingEvent arg0)
    '''
def serverConnected():
    '''    public void serverConnected(final MXEvent evt)
    '''
def serverConnectionError():
    '''    public void serverConnectionError(final MXEvent evt)
    '''
def serverDisconnected():
    '''    public void serverDisconnected(final MXEvent evt)
    '''
def wasChatHelperAborted():
    '''    public static synchronized boolean wasChatHelperAborted(final String sessionId)
    '''
def wasChatTranscriptSavedBeforeAbortion():
    '''    public static synchronized boolean wasChatTranscriptSavedBeforeAbortion(final String sessionId)
    '''
def resetActivityFlag():
    '''    public void resetActivityFlag()
    '''
def logInfo():
    '''    public static void logInfo(final String logMessage)
    '''
def logDebug():
    '''    public static void logDebug(final String logMessage)
    '''
def logError():
    '''    public static void logError(final Throwable throwable)
    public static void logError(final String logMessage, final Throwable throwable)
    '''
