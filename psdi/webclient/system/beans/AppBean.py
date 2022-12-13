QUERY_NONE = "int  -1"
QUERY_ALL = "int  -2"
QUERY_KEY = "int  -3"
QUERY_ALL_BOOKMARKS = "int  -4"
QUICK_LINK = "String  \"QL\""
DIRECTPRINT_LINK = "String  \"DP\""
DIRECTPRINT_WATTACH_LINK = "String  \"PAD\""
LONG_OP_READY = "int  1"
LONG_OP_INPRG = "int  2"
def AppBean():
    '''    public AppBean()
    '''
def getQueryOption():
    '''    public int getQueryOption()
    '''
def setQueryOption():
    '''    public void setQueryOption(final int option)
    '''
def setupBean():
    '''    public void setupBean(final WebClientSession wcs)
    public void setupBean(final SessionContext sc)
    '''
def hasStartRecord():
    '''    public boolean hasStartRecord(final long uniqueId)
    '''
def initializeApp():
    '''    public void initializeApp()
    '''
def structureChangedEvent():
    '''    public void structureChangedEvent(final DataBean speaker)
    '''
def fireStructureChangedEvent():
    '''    public void fireStructureChangedEvent(final DataBean speaker)
    '''
def reset():
    '''    public synchronized void reset()
    '''
def getMboSet():
    '''    public MboSetRemote getMboSet()
    '''
def save():
    '''    public synchronized void save()
    '''
def saveattachment():
    '''    public synchronized void saveattachment()
    '''
def autoInitiateWorkflow():
    '''    public void autoInitiateWorkflow()
    '''
def convertPortalParameters():
    '''    public void convertPortalParameters(final WebClientSession wcs)
    '''
def getPortalEvent():
    '''    public String getPortalEvent(final DataBean speaker)
    '''
def getCurrentRow():
    '''    public int getCurrentRow()
    '''
def isEmpty():
    '''    public synchronized boolean isEmpty()
    '''
def notExist():
    '''    public synchronized boolean notExist()
    '''
def saveYesNoCheck():
    '''    public boolean saveYesNoCheck()
    '''
def canSaveBasedOnLocks():
    '''    public boolean canSaveBasedOnLocks()
    '''
def saveYesNoInteractionCheck():
    '''    public boolean saveYesNoInteractionCheck()
    '''
def toBeSaved():
    '''    public boolean toBeSaved()
    '''
def getAppInfo():
    '''    public JSONObject getAppInfo()
    '''
def appinfo():
    '''    public int appinfo()
    '''
def NEXT():
    '''    public int NEXT()
    '''
def NAVHISTORY():
    '''    public int NAVHISTORY()
    '''
def SAVE():
    '''    public int SAVE()
    '''
def RUNREPORTS():
    '''    public int RUNREPORTS()
    '''
def RUNREPORTBYNAME():
    '''    public int RUNREPORTBYNAME()
    '''
def RUNAREPORT():
    '''    public int RUNAREPORT()
    '''
def PREVIOUS():
    '''    public int PREVIOUS()
    '''
def insert():
    '''    public synchronized void insert()
    '''
def INSERT():
    '''    public int INSERT()
    '''
def DELETE():
    '''    public int DELETE()
    '''
def addrow():
    '''    public int addrow()
    '''
def toggledeleterow():
    '''    public int toggledeleterow()
    '''
def DUPLICATE():
    '''    public int DUPLICATE()
    '''
def CLEAR():
    '''    public int CLEAR()
    '''
def BOOKMARK():
    '''    public int BOOKMARK()
    '''
def RESULTS():
    '''    public int RESULTS()
    '''
def find():
    '''    public int find()
    '''
def returnwithvalue():
    '''    public int returnwithvalue()
    '''
def returnnovalue():
    '''    public int returnnovalue()
    '''
def returntoapp():
    '''    public int returntoapp()
    '''
def getQuickFindRemote():
    '''    public MboSetRemote getQuickFindRemote()
    '''
def setDefaultQbe():
    '''    public void setDefaultQbe(final String attribute, final String expression)
    '''
def getResultsBean():
    '''    public ResultsBean getResultsBean()
    '''
def RECORDLOCK():
    '''    public int RECORDLOCK()
    '''
def RECUNLOCK():
    '''    public int RECUNLOCK()
    '''
def STRECLOCK():
    '''    public int STRECLOCK()
    '''
def getRecordLockProperties():
    '''    public JSONObject getRecordLockProperties()
    '''
def updateForRecordLock():
    '''    public void updateForRecordLock(final ControlInstance control)
    '''
def ROUTEWF():
    '''    public int ROUTEWF()
    '''
def STOPWF():
    '''    public int STOPWF()
    '''
def launchwf():
    '''    public int launchwf()
    '''
def SEARCHMORE():
    '''    public int SEARCHMORE()
    '''
def SEARCHWHER():
    '''    public int SEARCHWHER()
    '''
def SEARCHATTR():
    '''    public int SEARCHATTR()
    '''
def FLTRLASET():
    '''    public int FLTRLASET()
    '''
def setKPIId():
    '''    public void setKPIId(final long newId)
    '''
def getKPIId():
    '''    public long getKPIId()
    '''
def getKPIWhere():
    '''    public String getKPIWhere()
    '''
def getKPISelect():
    '''    public String getKPISelect()
    '''
def MODIFYSLAS():
    '''    public int MODIFYSLAS()
    '''
def moveToUniqueId():
    '''    public int moveToUniqueId(final long uniqueId)
    '''
def canExit():
    '''    public boolean canExit()
    '''
def getCurrentQueryName():
    '''    public String getCurrentQueryName()
    '''
def getCurrentQueryDescription():
    '''    public String getCurrentQueryDescription()
    '''
def HELPWF():
    '''    public int HELPWF()
    '''
def inboxwf():
    '''    public int inboxwf()
    '''
def ensureRecord():
    '''    public void ensureRecord()
    '''
def setFilterCleared():
    '''    public void setFilterCleared()
    '''
def clearfilter():
    '''    public int clearfilter()
    '''
def hasSaveAccess():
    '''    public boolean hasSaveAccess()
    '''
def submitPrintJob():
    '''    public int submitPrintJob()
    '''
def isUserWhereClauseThroughIntegration():
    '''    public boolean isUserWhereClauseThroughIntegration()
    '''
def setUserWhereClauseThroughIntegration():
    '''    public void setUserWhereClauseThroughIntegration(final boolean userWhereClauseThroughIntegration)
    '''
def hasSigOptionAccess():
    '''    public boolean hasSigOptionAccess(final int row, final String sigOption, final boolean checkAppLevel)
    public boolean hasSigOptionAccess(final int row, final String sigOption)
    '''
def refreshFieldErrors():
    '''    public void refreshFieldErrors()
    '''
def initQuickFIndRemote():
    '''    public MboSetRemote initQuickFIndRemote()
    '''
def hasModifications():
    '''    public boolean hasModifications()
    '''
