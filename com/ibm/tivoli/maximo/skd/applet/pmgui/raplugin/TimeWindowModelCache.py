COPYRIGHT = "String  \n\nLicensed Materials - Property of IBM\n5725-E24\n(C)Copyright IBM Corporation 2007, 2013.\nAll Rights Reserved.\nUS Government Users Restricted Rights - Use, duplication \nor disclosure restricted by GSA ADP Schedule Contract with IBM Corp.\n\n""
def TimeWindowModelCache():
'''public TimeWindowModelCache()
'''
pass
def canProcessActivity():
'''public boolean canProcessActivity(final IlvGeneralActivity activity, final IlvGanttModel ganttModel)
'''
pass
def isDisabled():
'''public boolean isDisabled()
'''
pass
def getDisabledMsg():
'''public String getDisabledMsg()
'''
pass
def clear():
'''public void clear()
'''
pass
def getCachedModel():
'''public TimeWindowModel getCachedModel(final IlvGeneralActivity activity)
'''
pass
def preloadCache():
'''public void preloadCache(final IlvGanttModel ganttModel)
'''
pass
def getModel():
'''public TimeWindowModel getModel(final IlvGeneralActivity activity, final IlvGanttModel ganttModel)
'''
pass
def getEmptyModel():
'''public TimeWindowModel getEmptyModel()
'''
pass
def updateCacheFromGanttModel():
'''public int updateCacheFromGanttModel(final IlvGanttModel ganttModel)
'''
pass
def updateCacheFromActivityList():
'''public int updateCacheFromActivityList(final IlvActivity[] list)
'''
pass
def updateCacheFromActivity():
'''public int updateCacheFromActivity(final IlvGeneralActivity activity)
'''
pass
def updateModelFromGanttModel():
'''public int updateModelFromGanttModel(final TimeWindowModel twModel, final IlvGanttModel ganttModel)
'''
pass
def updateModelFromActivityList():
'''public int updateModelFromActivityList(final TimeWindowModel twModel, final IlvActivity[] list)
'''
pass
def updateModelFromActivity():
'''public int updateModelFromActivity(final TimeWindowModel twModel, final IlvGeneralActivity activity)
public int updateModelFromActivity(final TimeWindowModel twModel, final IlvGeneralActivity activity, final Date startTime, final Date endTime)
'''
pass
def clearAllModelsFromActivity():
'''public int clearAllModelsFromActivity(final IlvGeneralActivity activity)
'''
pass
def clearModelFromActivity():
'''public int clearModelFromActivity(final TimeWindowModel twModel, final IlvGeneralActivity activity)
'''
pass
def saveState():
'''public void saveState()
'''
pass
def getState():
'''public TimeWindowState getState()
'''
pass
def markAsDirty():
'''public void markAsDirty(final TimeWindowModel excludeModel)
public void markAsDirty()
'''
pass
def isConstraintViolated():
'''public boolean isConstraintViolated(final IlvGeneralActivity activity)
'''
pass
def setConstraintViolated():
'''public void setConstraintViolated(final IlvGeneralActivity activity)
'''
pass
def clearConstraintViolated():
'''public void clearConstraintViolated(final IlvGeneralActivity activity)
'''
pass
def determineConstraintVolation():
'''public void determineConstraintVolation(final IlvGeneralActivity activity, final TimeWindowModel twModel)
public void determineConstraintVolation(final IlvGeneralActivity activity, final IlvGanttModel ganttModel)
public void determineConstraintVolation(final IlvActivity[] activityList, final IlvGanttModel ganttModel)
public void determineConstraintVolation(final IlvGanttModel ganttModel)
'''
pass
def isDebugOn():
'''public boolean isDebugOn()
'''
pass
