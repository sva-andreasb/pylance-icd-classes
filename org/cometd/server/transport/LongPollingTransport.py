PREFIX = "String  \"long-polling\""
BROWSER_ID_OPTION = "String  \"browserId\""
MAX_SESSIONS_PER_BROWSER_OPTION = "String  \"maxSessionsPerBrowser\""
MULTI_SESSION_INTERVAL_OPTION = "String  \"multiSessionInterval\""
AUTOBATCH_OPTION = "String  \"autoBatch\""
ALLOW_MULTI_SESSIONS_NO_BROWSER_OPTION = "String  \"allowMultiSessionsNoBrowser\""
def handle():
    '''returns None\n\n
    handle(final HttpServletRequest request, final HttpServletResponse response)\n
    '''
def ():
    '''returns LongPollScheduler\n\n
    (final ServerSessionImpl session, final Continuation continuation, final ServerMessage.Mutable reply, final String browserId)\n
    '''
def cancel():
    '''returns None\n\n
    cancel()\n
    '''
def schedule():
    '''returns None\n\n
    schedule()\n
    '''
def getSession():
    '''returns ServerSessionImpl\n\n
    getSession()\n
    '''
def onComplete():
    '''returns None\n\n
    onComplete(final Continuation continuation)\n
    '''
def onTimeout():
    '''returns None\n\n
    onTimeout(final Continuation continuation)\n
    '''
