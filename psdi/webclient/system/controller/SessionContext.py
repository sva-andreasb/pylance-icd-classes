def ():
    '''returns SessionContext\n\n
    (final WebClientSession masterInstance)\n
    '''
def getMasterInstance():
    '''returns WebClientSession\n\n
    getMasterInstance()\n
    '''
def getMXSession():
    '''returns MXSession\n\n
    getMXSession()\n
    '''
def getCurrentApp():
    '''returns AppInstance\n\n
    getCurrentApp()\n
    '''
def getCurrentAppId():
    '''returns String\n\n
    getCurrentAppId()\n
    '''
def getCurrentPageId():
    '''returns String\n\n
    getCurrentPageId()\n
    '''
def setCurrentEvent():
    '''returns None\n\n
    setCurrentEvent(final WebClientEvent event)\n
    '''
def getCurrentEvent():
    '''returns WebClientEvent\n\n
    getCurrentEvent()\n
    '''
def getCurrentEventHandler():
    '''returns ControlHandler\n\n
    getCurrentEventHandler()\n
    '''
def getLoginEvent():
    '''returns WebClientEvent\n\n
    getLoginEvent()\n
    '''
def getLocale():
    '''returns Locale\n\n
    getLocale()\n
    '''
def getTimeZone():
    '''returns TimeZone\n\n
    getTimeZone()\n
    '''
def getUserInfo():
    '''returns UserInfo\n\n
    getUserInfo()\n
    '''
def getWorkflowDirector():
    '''returns WorkflowDirector\n\n
    getWorkflowDirector()\n
    '''
def getPreviousApp():
    '''returns AppInstance\n\n
    getPreviousApp()\n
    '''
def pop():
    '''returns AppInstance\n\n
    pop()\n
    '''
def getRequest():
    '''returns HttpServletRequest\n\n
    getRequest()\n
    '''
def getResponse():
    '''returns HttpServletResponse\n\n
    getResponse()\n
    '''
def queueRefreshEvent():
    '''returns None\n\n
    queueRefreshEvent()\n
    '''
def queueEvent():
    '''returns None\n\n
    queueEvent(final WebClientEvent event)\n
    '''
def runLongOp():
    '''returns boolean\n\n
    runLongOp(final DataBean dataSrc, final String method)\n
    runLongOp(final DataBean dataSrc, final WebClientEvent event)\n
    '''
def haslongOpStarted():
    '''returns boolean\n\n
    haslongOpStarted()\n
    '''
def haslongOpCompleted():
    '''returns boolean\n\n
    haslongOpCompleted()\n
    '''
def getSpellSessionAdapter():
    '''returns SpellingSessionAdapter\n\n
    getSpellSessionAdapter()\n
    '''
def setSpellSessionAdapter():
    '''returns None\n\n
    setSpellSessionAdapter(final SpellingSessionAdapter spellSessionAdapter)\n
    '''
def hasWarnings():
    '''returns boolean\n\n
    hasWarnings()\n
    '''
def getWarnings():
    '''returns ArrayList<MXException>\n\n
    getWarnings()\n
    '''
def showLongOpStatus():
    '''returns None\n\n
    showLongOpStatus()\n
    '''
