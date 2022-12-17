UISESSIONID = "String  \"uisessionid\""
DESIGN_MODE = "String  \"_DM_\""
HTTPSESSION_KEY = "String  \"_WCSM_\""
LOST_UISESSIONID = "String  \"lostcontext_uisessionid\""
USER_REFRESH = "String  \"user_refresh\""
MAX_UI_SESSION_PER_SESSION = "String  \"mxe.webclient.maxUISessionsPerHttpSession\""
CSRFTOKEN = "String  \"csrftoken\""
def ():
    '''returns WebClientSessionManager\n\n
    ()\n
    '''
def hasSessions():
    '''returns boolean\n\n
    hasSessions()\n
    '''
def hasMultipleSessions():
    '''returns boolean\n\n
    hasMultipleSessions()\n
    '''
def getWebClientSession():
    '''returns WebClientSession\n\n
    getWebClientSession(final String uisessionid)\n
    getWebClientSession(final HttpServletRequest request)\n
    '''
def getWebClientSessionIds():
    '''returns String[]\n\n
    getWebClientSessionIds()\n
    '''
def removeWebClientSession():
    '''returns boolean\n\n
    removeWebClientSession(final WebClientSession wcs)\n
    removeWebClientSession(final WebClientSession wcs, final boolean closeSession)\n
    '''
def valueBound():
    '''returns None\n\n
    valueBound(final HttpSessionBindingEvent arg0)\n
    '''
def valueUnbound():
    '''returns None\n\n
    valueUnbound(final HttpSessionBindingEvent arg0)\n
    '''
def preserveMXSession():
    '''returns None\n\n
    preserveMXSession()\n
    '''
def hasAvailableSessions():
    '''returns boolean\n\n
    hasAvailableSessions()\n
    '''
def getWebClientSessionCount():
    '''returns int\n\n
    getWebClientSessionCount()\n
    '''
def getSessionInvalidated():
    '''returns boolean\n\n
    getSessionInvalidated()\n
    '''
def setLostSessionId():
    '''returns None\n\n
    setLostSessionId(final String lostSessionId)\n
    '''
