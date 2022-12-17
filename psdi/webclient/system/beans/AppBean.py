QUERY_NONE = "int  -1"
QUERY_ALL = "int  -2"
QUERY_KEY = "int  -3"
QUERY_ALL_BOOKMARKS = "int  -4"
QUICK_LINK = "String  \"QL\""
DIRECTPRINT_LINK = "String  \"DP\""
DIRECTPRINT_WATTACH_LINK = "String  \"PAD\""
LONG_OP_READY = "int  1"
LONG_OP_INPRG = "int  2"
def ():
    '''returns AppBean\n\n
    ()\n
    '''
def getQueryOption():
    '''returns int\n\n
    getQueryOption()\n
    '''
def setQueryOption():
    '''returns None\n\n
    setQueryOption(final int option)\n
    '''
def setupBean():
    '''returns None\n\n
    setupBean(final WebClientSession wcs)\n
    setupBean(final SessionContext sc)\n
    '''
def hasStartRecord():
    '''returns boolean\n\n
    hasStartRecord(final long uniqueId)\n
    '''
def initializeApp():
    '''returns None\n\n
    initializeApp()\n
    '''
def structureChangedEvent():
    '''returns None\n\n
    structureChangedEvent(final DataBean speaker)\n
    '''
def fireStructureChangedEvent():
    '''returns None\n\n
    fireStructureChangedEvent(final DataBean speaker)\n
    '''
def getMboSet():
    '''returns MboSetRemote\n\n
    getMboSet()\n
    '''
def autoInitiateWorkflow():
    '''returns None\n\n
    autoInitiateWorkflow()\n
    '''
def convertPortalParameters():
    '''returns None\n\n
    convertPortalParameters(final WebClientSession wcs)\n
    '''
def getPortalEvent():
    '''returns String\n\n
    getPortalEvent(final DataBean speaker)\n
    '''
def getCurrentRow():
    '''returns int\n\n
    getCurrentRow()\n
    '''
def saveYesNoCheck():
    '''returns boolean\n\n
    saveYesNoCheck()\n
    '''
def canSaveBasedOnLocks():
    '''returns boolean\n\n
    canSaveBasedOnLocks()\n
    '''
def saveYesNoInteractionCheck():
    '''returns boolean\n\n
    saveYesNoInteractionCheck()\n
    '''
def toBeSaved():
    '''returns boolean\n\n
    toBeSaved()\n
    '''
def getAppInfo():
    '''returns JSONObject\n\n
    getAppInfo()\n
    '''
def appinfo():
    '''returns int\n\n
    appinfo()\n
    '''
def NEXT():
    '''returns int\n\n
    NEXT()\n
    '''
def NAVHISTORY():
    '''returns int\n\n
    NAVHISTORY()\n
    '''
def SAVE():
    '''returns int\n\n
    SAVE()\n
    '''
def RUNREPORTS():
    '''returns int\n\n
    RUNREPORTS()\n
    '''
def RUNREPORTBYNAME():
    '''returns int\n\n
    RUNREPORTBYNAME()\n
    '''
def RUNAREPORT():
    '''returns int\n\n
    RUNAREPORT()\n
    '''
def PREVIOUS():
    '''returns int\n\n
    PREVIOUS()\n
    '''
def INSERT():
    '''returns int\n\n
    INSERT()\n
    '''
def DELETE():
    '''returns int\n\n
    DELETE()\n
    '''
def addrow():
    '''returns int\n\n
    addrow()\n
    '''
def toggledeleterow():
    '''returns int\n\n
    toggledeleterow()\n
    '''
def DUPLICATE():
    '''returns int\n\n
    DUPLICATE()\n
    '''
def CLEAR():
    '''returns int\n\n
    CLEAR()\n
    '''
def BOOKMARK():
    '''returns int\n\n
    BOOKMARK()\n
    '''
def RESULTS():
    '''returns int\n\n
    RESULTS()\n
    '''
def find():
    '''returns int\n\n
    find()\n
    '''
def returnwithvalue():
    '''returns int\n\n
    returnwithvalue()\n
    '''
def returnnovalue():
    '''returns int\n\n
    returnnovalue()\n
    '''
def returntoapp():
    '''returns int\n\n
    returntoapp()\n
    '''
def getQuickFindRemote():
    '''returns MboSetRemote\n\n
    getQuickFindRemote()\n
    '''
def setDefaultQbe():
    '''returns None\n\n
    setDefaultQbe(final String attribute, final String expression)\n
    '''
def getResultsBean():
    '''returns ResultsBean\n\n
    getResultsBean()\n
    '''
def RECORDLOCK():
    '''returns int\n\n
    RECORDLOCK()\n
    '''
def RECUNLOCK():
    '''returns int\n\n
    RECUNLOCK()\n
    '''
def STRECLOCK():
    '''returns int\n\n
    STRECLOCK()\n
    '''
def getRecordLockProperties():
    '''returns JSONObject\n\n
    getRecordLockProperties()\n
    '''
def updateForRecordLock():
    '''returns None\n\n
    updateForRecordLock(final ControlInstance control)\n
    '''
def ROUTEWF():
    '''returns int\n\n
    ROUTEWF()\n
    '''
def STOPWF():
    '''returns int\n\n
    STOPWF()\n
    '''
def launchwf():
    '''returns int\n\n
    launchwf()\n
    '''
def SEARCHMORE():
    '''returns int\n\n
    SEARCHMORE()\n
    '''
def SEARCHWHER():
    '''returns int\n\n
    SEARCHWHER()\n
    '''
def SEARCHATTR():
    '''returns int\n\n
    SEARCHATTR()\n
    '''
def FLTRLASET():
    '''returns int\n\n
    FLTRLASET()\n
    '''
def setKPIId():
    '''returns None\n\n
    setKPIId(final long newId)\n
    '''
def getKPIId():
    '''returns long\n\n
    getKPIId()\n
    '''
def getKPIWhere():
    '''returns String\n\n
    getKPIWhere()\n
    '''
def getKPISelect():
    '''returns String\n\n
    getKPISelect()\n
    '''
def MODIFYSLAS():
    '''returns int\n\n
    MODIFYSLAS()\n
    '''
def moveToUniqueId():
    '''returns int\n\n
    moveToUniqueId(final long uniqueId)\n
    '''
def canExit():
    '''returns boolean\n\n
    canExit()\n
    '''
def getCurrentQueryName():
    '''returns String\n\n
    getCurrentQueryName()\n
    '''
def getCurrentQueryDescription():
    '''returns String\n\n
    getCurrentQueryDescription()\n
    '''
def HELPWF():
    '''returns int\n\n
    HELPWF()\n
    '''
def inboxwf():
    '''returns int\n\n
    inboxwf()\n
    '''
def ensureRecord():
    '''returns None\n\n
    ensureRecord()\n
    '''
def setFilterCleared():
    '''returns None\n\n
    setFilterCleared()\n
    '''
def clearfilter():
    '''returns int\n\n
    clearfilter()\n
    '''
def hasSaveAccess():
    '''returns boolean\n\n
    hasSaveAccess()\n
    '''
def submitPrintJob():
    '''returns int\n\n
    submitPrintJob()\n
    '''
def isUserWhereClauseThroughIntegration():
    '''returns boolean\n\n
    isUserWhereClauseThroughIntegration()\n
    '''
def setUserWhereClauseThroughIntegration():
    '''returns None\n\n
    setUserWhereClauseThroughIntegration(final boolean userWhereClauseThroughIntegration)\n
    '''
def hasSigOptionAccess():
    '''returns boolean\n\n
    hasSigOptionAccess(final int row, final String sigOption, final boolean checkAppLevel)\n
    hasSigOptionAccess(final int row, final String sigOption)\n
    '''
def refreshFieldErrors():
    '''returns None\n\n
    refreshFieldErrors()\n
    '''
def initQuickFIndRemote():
    '''returns MboSetRemote\n\n
    initQuickFIndRemote()\n
    '''
def hasModifications():
    '''returns boolean\n\n
    hasModifications()\n
    '''
