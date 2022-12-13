def SessionContext():
    '''public SessionContext(final WebClientSession masterInstance)
    '''
def getMasterInstance():
    '''public WebClientSession getMasterInstance()
    '''
def getMXSession():
    '''public MXSession getMXSession()
    '''
def getCurrentApp():
    '''public AppInstance getCurrentApp()
    '''
def getCurrentAppId():
    '''public String getCurrentAppId()
    '''
def getCurrentPageId():
    '''public String getCurrentPageId()
    '''
def setCurrentEvent():
    '''public void setCurrentEvent(final WebClientEvent event)
    '''
def getCurrentEvent():
    '''public WebClientEvent getCurrentEvent()
    '''
def getCurrentEventHandler():
    '''public ControlHandler getCurrentEventHandler()
    '''
def getLoginEvent():
    '''public WebClientEvent getLoginEvent()
    '''
def getLocale():
    '''public Locale getLocale()
    '''
def getTimeZone():
    '''public TimeZone getTimeZone()
    '''
def getUserInfo():
    '''public UserInfo getUserInfo()
    '''
def getWorkflowDirector():
    '''public WorkflowDirector getWorkflowDirector()
    '''
def getPreviousApp():
    '''public AppInstance getPreviousApp()
    '''
def pop():
    '''public AppInstance pop()
    '''
def getRequest():
    '''public HttpServletRequest getRequest()
    '''
def getResponse():
    '''public HttpServletResponse getResponse()
    '''
def queueRefreshEvent():
    '''public void queueRefreshEvent()
    '''
def queueEvent():
    '''public void queueEvent(final WebClientEvent event)
    '''
def runLongOp():
    '''public boolean runLongOp(final DataBean dataSrc, final String method)
    public boolean runLongOp(final DataBean dataSrc, final WebClientEvent event)
    '''
def haslongOpStarted():
    '''public boolean haslongOpStarted()
    '''
def haslongOpCompleted():
    '''public boolean haslongOpCompleted()
    '''
def getSpellSessionAdapter():
    '''public SpellingSessionAdapter getSpellSessionAdapter()
    '''
def setSpellSessionAdapter():
    '''public void setSpellSessionAdapter(final SpellingSessionAdapter spellSessionAdapter)
    '''
def hasWarnings():
    '''public boolean hasWarnings()
    '''
def getWarnings():
    '''public ArrayList<MXException> getWarnings()
    '''
def showLongOpStatus():
    '''public void showLongOpStatus()
    '''
