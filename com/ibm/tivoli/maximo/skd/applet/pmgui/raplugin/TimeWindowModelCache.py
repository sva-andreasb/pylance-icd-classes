COPYRIGHT = "String  \"\n\nLicensed Materials - Property of IBM\n5725-E24\n(C)Copyright IBM Corporation 2007, 2013.\nAll Rights Reserved.\nUS Government Users Restricted Rights - Use, duplication \nor disclosure restricted by GSA ADP Schedule Contract with IBM Corp.\n\n\""
def TimeWindowModelCache():
    '''    public TimeWindowModelCache()
    '''
def canProcessActivity():
    '''    public boolean canProcessActivity(final IlvGeneralActivity activity, final IlvGanttModel ganttModel)
    '''
def isDisabled():
    '''    public boolean isDisabled()
    '''
def getDisabledMsg():
    '''    public String getDisabledMsg()
    '''
def clear():
    '''    public void clear()
    '''
def getCachedModel():
    '''    public TimeWindowModel getCachedModel(final IlvGeneralActivity activity)
    '''
def preloadCache():
    '''    public void preloadCache(final IlvGanttModel ganttModel)
    '''
def getModel():
    '''    public TimeWindowModel getModel(final IlvGeneralActivity activity, final IlvGanttModel ganttModel)
    '''
def getEmptyModel():
    '''    public TimeWindowModel getEmptyModel()
    '''
def updateCacheFromGanttModel():
    '''    public int updateCacheFromGanttModel(final IlvGanttModel ganttModel)
    '''
def updateCacheFromActivityList():
    '''    public int updateCacheFromActivityList(final IlvActivity[] list)
    '''
def updateCacheFromActivity():
    '''    public int updateCacheFromActivity(final IlvGeneralActivity activity)
    '''
def updateModelFromGanttModel():
    '''    public int updateModelFromGanttModel(final TimeWindowModel twModel, final IlvGanttModel ganttModel)
    '''
def updateModelFromActivityList():
    '''    public int updateModelFromActivityList(final TimeWindowModel twModel, final IlvActivity[] list)
    '''
def updateModelFromActivity():
    '''    public int updateModelFromActivity(final TimeWindowModel twModel, final IlvGeneralActivity activity)
    public int updateModelFromActivity(final TimeWindowModel twModel, final IlvGeneralActivity activity, final Date startTime, final Date endTime)
    '''
def clearAllModelsFromActivity():
    '''    public int clearAllModelsFromActivity(final IlvGeneralActivity activity)
    '''
def clearModelFromActivity():
    '''    public int clearModelFromActivity(final TimeWindowModel twModel, final IlvGeneralActivity activity)
    '''
def saveState():
    '''    public void saveState()
    '''
def getState():
    '''    public TimeWindowState getState()
    '''
def markAsDirty():
    '''    public void markAsDirty(final TimeWindowModel excludeModel)
    public void markAsDirty()
    '''
def isConstraintViolated():
    '''    public boolean isConstraintViolated(final IlvGeneralActivity activity)
    '''
def setConstraintViolated():
    '''    public void setConstraintViolated(final IlvGeneralActivity activity)
    '''
def clearConstraintViolated():
    '''    public void clearConstraintViolated(final IlvGeneralActivity activity)
    '''
def determineConstraintVolation():
    '''    public void determineConstraintVolation(final IlvGeneralActivity activity, final TimeWindowModel twModel)
    public void determineConstraintVolation(final IlvGeneralActivity activity, final IlvGanttModel ganttModel)
    public void determineConstraintVolation(final IlvActivity[] activityList, final IlvGanttModel ganttModel)
    public void determineConstraintVolation(final IlvGanttModel ganttModel)
    '''
def isDebugOn():
    '''    public boolean isDebugOn()
    '''
