QUERY_NONE = "int  -1"
QUERY_ALL = "int  -2"
QUERY_KEY = "int  -3"
QUERY_ALL_BOOKMARKS = "int  -4"
QUICK_LINK = "String  QL""
DIRECTPRINT_LINK = "String  DP""
DIRECTPRINT_WATTACH_LINK = "String  PAD""
LONG_OP_READY = "int  1"
LONG_OP_INPRG = "int  2"
def AppBean():
'''public AppBean()
'''
pass
def getQueryOption():
'''public int getQueryOption()
'''
pass
def setQueryOption():
'''public void setQueryOption(final int option)
'''
pass
def setupBean():
'''public void setupBean(final WebClientSession wcs)
public void setupBean(final SessionContext sc)
'''
pass
def hasStartRecord():
'''public boolean hasStartRecord(final long uniqueId)
'''
pass
def initializeApp():
'''public void initializeApp()
'''
pass
def structureChangedEvent():
'''public void structureChangedEvent(final DataBean speaker)
'''
pass
def fireStructureChangedEvent():
'''public void fireStructureChangedEvent(final DataBean speaker)
'''
pass
def reset():
'''public synchronized void reset()
'''
pass
def getMboSet():
'''public MboSetRemote getMboSet()
'''
pass
def save():
'''public synchronized void save()
'''
pass
def saveattachment():
'''public synchronized void saveattachment()
'''
pass
def autoInitiateWorkflow():
'''public void autoInitiateWorkflow()
'''
pass
def convertPortalParameters():
'''public void convertPortalParameters(final WebClientSession wcs)
'''
pass
def getPortalEvent():
'''public String getPortalEvent(final DataBean speaker)
'''
pass
def getCurrentRow():
'''public int getCurrentRow()
'''
pass
def isEmpty():
'''public synchronized boolean isEmpty()
'''
pass
def notExist():
'''public synchronized boolean notExist()
'''
pass
def saveYesNoCheck():
'''public boolean saveYesNoCheck()
'''
pass
def canSaveBasedOnLocks():
'''public boolean canSaveBasedOnLocks()
'''
pass
def saveYesNoInteractionCheck():
'''public boolean saveYesNoInteractionCheck()
'''
pass
def toBeSaved():
'''public boolean toBeSaved()
'''
pass
def getAppInfo():
'''public JSONObject getAppInfo()
'''
pass
def appinfo():
'''public int appinfo()
'''
pass
def NEXT():
'''public int NEXT()
'''
pass
def NAVHISTORY():
'''public int NAVHISTORY()
'''
pass
def SAVE():
'''public int SAVE()
'''
pass
def RUNREPORTS():
'''public int RUNREPORTS()
'''
pass
def RUNREPORTBYNAME():
'''public int RUNREPORTBYNAME()
'''
pass
def RUNAREPORT():
'''public int RUNAREPORT()
'''
pass
def PREVIOUS():
'''public int PREVIOUS()
'''
pass
def insert():
'''public synchronized void insert()
'''
pass
def INSERT():
'''public int INSERT()
'''
pass
def DELETE():
'''public int DELETE()
'''
pass
def addrow():
'''public int addrow()
'''
pass
def toggledeleterow():
'''public int toggledeleterow()
'''
pass
def DUPLICATE():
'''public int DUPLICATE()
'''
pass
def CLEAR():
'''public int CLEAR()
'''
pass
def BOOKMARK():
'''public int BOOKMARK()
'''
pass
def RESULTS():
'''public int RESULTS()
'''
pass
def find():
'''public int find()
'''
pass
def returnwithvalue():
'''public int returnwithvalue()
'''
pass
def returnnovalue():
'''public int returnnovalue()
'''
pass
def returntoapp():
'''public int returntoapp()
'''
pass
def getQuickFindRemote():
'''public MboSetRemote getQuickFindRemote()
'''
pass
def setDefaultQbe():
'''public void setDefaultQbe(final String attribute, final String expression)
'''
pass
def getResultsBean():
'''public ResultsBean getResultsBean()
'''
pass
def RECORDLOCK():
'''public int RECORDLOCK()
'''
pass
def RECUNLOCK():
'''public int RECUNLOCK()
'''
pass
def STRECLOCK():
'''public int STRECLOCK()
'''
pass
def getRecordLockProperties():
'''public JSONObject getRecordLockProperties()
'''
pass
def updateForRecordLock():
'''public void updateForRecordLock(final ControlInstance control)
'''
pass
def ROUTEWF():
'''public int ROUTEWF()
'''
pass
def STOPWF():
'''public int STOPWF()
'''
pass
def launchwf():
'''public int launchwf()
'''
pass
def SEARCHMORE():
'''public int SEARCHMORE()
'''
pass
def SEARCHWHER():
'''public int SEARCHWHER()
'''
pass
def SEARCHATTR():
'''public int SEARCHATTR()
'''
pass
def FLTRLASET():
'''public int FLTRLASET()
'''
pass
def setKPIId():
'''public void setKPIId(final long newId)
'''
pass
def getKPIId():
'''public long getKPIId()
'''
pass
def getKPIWhere():
'''public String getKPIWhere()
'''
pass
def getKPISelect():
'''public String getKPISelect()
'''
pass
def MODIFYSLAS():
'''public int MODIFYSLAS()
'''
pass
def moveToUniqueId():
'''public int moveToUniqueId(final long uniqueId)
'''
pass
def canExit():
'''public boolean canExit()
'''
pass
def getCurrentQueryName():
'''public String getCurrentQueryName()
'''
pass
def getCurrentQueryDescription():
'''public String getCurrentQueryDescription()
'''
pass
def HELPWF():
'''public int HELPWF()
'''
pass
def inboxwf():
'''public int inboxwf()
'''
pass
def ensureRecord():
'''public void ensureRecord()
'''
pass
def setFilterCleared():
'''public void setFilterCleared()
'''
pass
def clearfilter():
'''public int clearfilter()
'''
pass
def hasSaveAccess():
'''public boolean hasSaveAccess()
'''
pass
def submitPrintJob():
'''public int submitPrintJob()
'''
pass
def isUserWhereClauseThroughIntegration():
'''public boolean isUserWhereClauseThroughIntegration()
'''
pass
def setUserWhereClauseThroughIntegration():
'''public void setUserWhereClauseThroughIntegration(final boolean userWhereClauseThroughIntegration)
'''
pass
def hasSigOptionAccess():
'''public boolean hasSigOptionAccess(final int row, final String sigOption, final boolean checkAppLevel)
public boolean hasSigOptionAccess(final int row, final String sigOption)
'''
pass
def refreshFieldErrors():
'''public void refreshFieldErrors()
'''
pass
def initQuickFIndRemote():
'''public MboSetRemote initQuickFIndRemote()
'''
pass
def hasModifications():
'''public boolean hasModifications()
'''
pass
