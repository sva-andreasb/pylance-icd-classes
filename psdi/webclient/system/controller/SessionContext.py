def SessionContext():
'''public SessionContext(final WebClientSession masterInstance)
'''
pass
def getMasterInstance():
'''public WebClientSession getMasterInstance()
'''
pass
def getMXSession():
'''public MXSession getMXSession()
'''
pass
def getCurrentApp():
'''public AppInstance getCurrentApp()
'''
pass
def getCurrentAppId():
'''public String getCurrentAppId()
'''
pass
def getCurrentPageId():
'''public String getCurrentPageId()
'''
pass
def setCurrentEvent():
'''public void setCurrentEvent(final WebClientEvent event)
'''
pass
def getCurrentEvent():
'''public WebClientEvent getCurrentEvent()
'''
pass
def getCurrentEventHandler():
'''public ControlHandler getCurrentEventHandler()
'''
pass
def getLoginEvent():
'''public WebClientEvent getLoginEvent()
'''
pass
def getLocale():
'''public Locale getLocale()
'''
pass
def getTimeZone():
'''public TimeZone getTimeZone()
'''
pass
def getUserInfo():
'''public UserInfo getUserInfo()
'''
pass
def getWorkflowDirector():
'''public WorkflowDirector getWorkflowDirector()
'''
pass
def getPreviousApp():
'''public AppInstance getPreviousApp()
'''
pass
def pop():
'''public AppInstance pop()
'''
pass
def getRequest():
'''public HttpServletRequest getRequest()
'''
pass
def getResponse():
'''public HttpServletResponse getResponse()
'''
pass
def queueRefreshEvent():
'''public void queueRefreshEvent()
'''
pass
def queueEvent():
'''public void queueEvent(final WebClientEvent event)
'''
pass
def runLongOp():
'''public boolean runLongOp(final DataBean dataSrc, final String method)
public boolean runLongOp(final DataBean dataSrc, final WebClientEvent event)
'''
pass
def haslongOpStarted():
'''public boolean haslongOpStarted()
'''
pass
def haslongOpCompleted():
'''public boolean haslongOpCompleted()
'''
pass
def getSpellSessionAdapter():
'''public SpellingSessionAdapter getSpellSessionAdapter()
'''
pass
def setSpellSessionAdapter():
'''public void setSpellSessionAdapter(final SpellingSessionAdapter spellSessionAdapter)
'''
pass
def hasWarnings():
'''public boolean hasWarnings()
'''
pass
def getWarnings():
'''public ArrayList<MXException> getWarnings()
'''
pass
def showLongOpStatus():
'''public void showLongOpStatus()
'''
pass
