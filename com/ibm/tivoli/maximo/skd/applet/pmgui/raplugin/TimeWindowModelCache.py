COPYRIGHT = "String  \"\n\nLicensed Materials - Property of IBM\n5725-E24\n(C)Copyright IBM Corporation 2007, 2013.\nAll Rights Reserved.\nUS Government Users Restricted Rights - Use, duplication \nor disclosure restricted by GSA ADP Schedule Contract with IBM Corp.\n\n\""
def ():
    '''returns TimeWindowModelCache\n\n
    ()\n
    '''
def canProcessActivity():
    '''returns boolean\n\n
    canProcessActivity(final IlvGeneralActivity activity, final IlvGanttModel ganttModel)\n
    '''
def isDisabled():
    '''returns boolean\n\n
    isDisabled()\n
    '''
def getDisabledMsg():
    '''returns String\n\n
    getDisabledMsg()\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def getCachedModel():
    '''returns TimeWindowModel\n\n
    getCachedModel(final IlvGeneralActivity activity)\n
    '''
def preloadCache():
    '''returns None\n\n
    preloadCache(final IlvGanttModel ganttModel)\n
    '''
def getModel():
    '''returns TimeWindowModel\n\n
    getModel(final IlvGeneralActivity activity, final IlvGanttModel ganttModel)\n
    '''
def getEmptyModel():
    '''returns TimeWindowModel\n\n
    getEmptyModel()\n
    '''
def updateCacheFromGanttModel():
    '''returns int\n\n
    updateCacheFromGanttModel(final IlvGanttModel ganttModel)\n
    '''
def updateCacheFromActivityList():
    '''returns int\n\n
    updateCacheFromActivityList(final IlvActivity[] list)\n
    '''
def updateCacheFromActivity():
    '''returns int\n\n
    updateCacheFromActivity(final IlvGeneralActivity activity)\n
    '''
def updateModelFromGanttModel():
    '''returns int\n\n
    updateModelFromGanttModel(final TimeWindowModel twModel, final IlvGanttModel ganttModel)\n
    '''
def updateModelFromActivityList():
    '''returns int\n\n
    updateModelFromActivityList(final TimeWindowModel twModel, final IlvActivity[] list)\n
    '''
def updateModelFromActivity():
    '''returns int\n\n
    updateModelFromActivity(final TimeWindowModel twModel, final IlvGeneralActivity activity)\n
    updateModelFromActivity(final TimeWindowModel twModel, final IlvGeneralActivity activity, final Date startTime, final Date endTime)\n
    '''
def clearAllModelsFromActivity():
    '''returns int\n\n
    clearAllModelsFromActivity(final IlvGeneralActivity activity)\n
    '''
def clearModelFromActivity():
    '''returns int\n\n
    clearModelFromActivity(final TimeWindowModel twModel, final IlvGeneralActivity activity)\n
    '''
def saveState():
    '''returns None\n\n
    saveState()\n
    '''
def getState():
    '''returns TimeWindowState\n\n
    getState()\n
    '''
def markAsDirty():
    '''returns None\n\n
    markAsDirty(final TimeWindowModel excludeModel)\n
    markAsDirty()\n
    '''
def isConstraintViolated():
    '''returns boolean\n\n
    isConstraintViolated(final IlvGeneralActivity activity)\n
    '''
def setConstraintViolated():
    '''returns None\n\n
    setConstraintViolated(final IlvGeneralActivity activity)\n
    '''
def clearConstraintViolated():
    '''returns None\n\n
    clearConstraintViolated(final IlvGeneralActivity activity)\n
    '''
def determineConstraintVolation():
    '''returns None\n\n
    determineConstraintVolation(final IlvGeneralActivity activity, final TimeWindowModel twModel)\n
    determineConstraintVolation(final IlvGeneralActivity activity, final IlvGanttModel ganttModel)\n
    determineConstraintVolation(final IlvActivity[] activityList, final IlvGanttModel ganttModel)\n
    determineConstraintVolation(final IlvGanttModel ganttModel)\n
    '''
def isDebugOn():
    '''returns boolean\n\n
    isDebugOn()\n
    '''
