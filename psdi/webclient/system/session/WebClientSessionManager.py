UISESSIONID = "String  uisessionid""
DESIGN_MODE = "String  _DM_""
HTTPSESSION_KEY = "String  _WCSM_""
LOST_UISESSIONID = "String  lostcontext_uisessionid""
USER_REFRESH = "String  user_refresh""
MAX_UI_SESSION_PER_SESSION = "String  mxe.webclient.maxUISessionsPerHttpSession""
CSRFTOKEN = "String  csrftoken""
def getWebClientSessionManager():
'''public static WebClientSessionManager getWebClientSessionManager(final HttpSession session)
'''
pass
def WebClientSessionManager():
'''public WebClientSessionManager()
'''
pass
def hasSessions():
'''public boolean hasSessions()
'''
pass
def hasMultipleSessions():
'''public boolean hasMultipleSessions()
'''
pass
def getWebClientSession():
'''public WebClientSession getWebClientSession(final String uisessionid)
public WebClientSession getWebClientSession(final HttpServletRequest request)
'''
pass
def getWebClientSessionIds():
'''public String[] getWebClientSessionIds()
'''
pass
def removeWebClientSession():
'''public boolean removeWebClientSession(final WebClientSession wcs)
public boolean removeWebClientSession(final WebClientSession wcs, final boolean closeSession)
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
def preserveMXSession():
'''public void preserveMXSession()
'''
pass
def hasAvailableSessions():
'''public boolean hasAvailableSessions()
'''
pass
def getWebClientSessionCount():
'''public int getWebClientSessionCount()
'''
pass
def getSessionInvalidated():
'''public boolean getSessionInvalidated()
'''
pass
def setLostSessionId():
'''public void setLostSessionId(final String lostSessionId)
'''
pass
