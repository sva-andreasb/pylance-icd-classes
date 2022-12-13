UISESSIONID = "String  \"uisessionid\""
DESIGN_MODE = "String  \"_DM_\""
HTTPSESSION_KEY = "String  \"_WCSM_\""
LOST_UISESSIONID = "String  \"lostcontext_uisessionid\""
USER_REFRESH = "String  \"user_refresh\""
MAX_UI_SESSION_PER_SESSION = "String  \"mxe.webclient.maxUISessionsPerHttpSession\""
CSRFTOKEN = "String  \"csrftoken\""
def getWebClientSessionManager():
    '''    public static WebClientSessionManager getWebClientSessionManager(final HttpSession session)
    '''
def WebClientSessionManager():
    '''    public WebClientSessionManager()
    '''
def hasSessions():
    '''    public boolean hasSessions()
    '''
def hasMultipleSessions():
    '''    public boolean hasMultipleSessions()
    '''
def getWebClientSession():
    '''    public WebClientSession getWebClientSession(final String uisessionid)
    public WebClientSession getWebClientSession(final HttpServletRequest request)
    '''
def getWebClientSessionIds():
    '''    public String[] getWebClientSessionIds()
    '''
def removeWebClientSession():
    '''    public boolean removeWebClientSession(final WebClientSession wcs)
    public boolean removeWebClientSession(final WebClientSession wcs, final boolean closeSession)
    '''
def valueBound():
    '''    public void valueBound(final HttpSessionBindingEvent arg0)
    '''
def valueUnbound():
    '''    public void valueUnbound(final HttpSessionBindingEvent arg0)
    '''
def preserveMXSession():
    '''    public void preserveMXSession()
    '''
def hasAvailableSessions():
    '''    public boolean hasAvailableSessions()
    '''
def getWebClientSessionCount():
    '''    public int getWebClientSessionCount()
    '''
def getSessionInvalidated():
    '''    public boolean getSessionInvalidated()
    '''
def setLostSessionId():
    '''    public void setLostSessionId(final String lostSessionId)
    '''
