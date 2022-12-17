def ():
    '''returns AsyncProcessRunOptimization\n\n
    (final MboSet ms)\n
    (final UserInfo userInfo, final SKDProject project, final OptimizationServiceRemote optimizationService, final String odmApplicationName, final OptimizationInputProcessParameters inputProcessParameters, final OptimizationOutputProcessParameters outputProcessParameters)\n
    '''
def setAssetLocWhere():
    '''returns None\n\n
    setAssetLocWhere(final String key, final String where)\n
    '''
def getAssetLocWhere():
    '''returns String\n\n
    getAssetLocWhere(final String key)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def updateProjectData():
    '''returns None\n\n
    updateProjectData()\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def setCalendarDates():
    '''returns None\n\n
    setCalendarDates()\n
    '''
def originalAppName():
    '''returns String\n\n
    originalAppName(final String appName)\n
    '''
def dupSchedulerProject():
    '''returns None\n\n
    dupSchedulerProject(final MboRemote selectedproject)\n
    '''
def duplicate():
    '''returns MboRemote\n\n
    duplicate()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def modify():
    '''returns None\n\n
    modify()\n
    '''
def setFromAsync():
    '''returns None\n\n
    setFromAsync(final boolean flag)\n
    '''
def getFromAsync():
    '''returns boolean\n\n
    getFromAsync()\n
    '''
def isProjectDataModified():
    '''returns boolean\n\n
    isProjectDataModified()\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def startScheduleCompliance():
    '''returns None\n\n
    startScheduleCompliance()\n
    startScheduleCompliance(final MboSetRemote skdActivitySet, final SKDProjectRemote skdProject, final Date compstart, final Date compend)\n
    '''
def endScheduleCompliance():
    '''returns None\n\n
    endScheduleCompliance(final SKDProjectRemote skdProject, final Date compend)\n
    '''
def setNextDueDate():
    '''returns None\n\n
    setNextDueDate()\n
    '''
def updateNextStartAndEndDate():
    '''returns None\n\n
    updateNextStartAndEndDate()\n
    '''
def updateTimeBasedNextDueDate():
    '''returns None\n\n
    updateTimeBasedNextDueDate()\n
    '''
def getStatusListName():
    '''returns String\n\n
    getStatusListName()\n
    '''
def publish():
    '''returns None\n\n
    publish()\n
    '''
def createBaseLine():
    '''returns MboRemote\n\n
    createBaseLine(final String baseLineName, final String baseLineDescription, final String baseLineMemo, final String inputName, final String scenarioType)\n
    '''
def getBaseLineUniqueId():
    '''returns long\n\n
    getBaseLineUniqueId()\n
    '''
def getDefaultScenarioUniqueId():
    '''returns long\n\n
    getDefaultScenarioUniqueId(final String SKDProjectName)\n
    '''
def setDefaultScenario():
    '''returns None\n\n
    setDefaultScenario(final SKDProjectRemote SKDProject)\n
    '''
def canPublish():
    '''returns None\n\n
    canPublish()\n
    '''
def canCreateScenario():
    '''returns None\n\n
    canCreateScenario()\n
    '''
def canCreateSnapShot():
    '''returns None\n\n
    canCreateSnapShot()\n
    '''
def setPublishFlag():
    '''returns None\n\n
    setPublishFlag(final boolean publish)\n
    '''
def getPublishFlag():
    '''returns boolean\n\n
    getPublishFlag()\n
    '''
def setScenarioFlag():
    '''returns None\n\n
    setScenarioFlag(final boolean scenario)\n
    '''
def getScenarioFlag():
    '''returns boolean\n\n
    getScenarioFlag()\n
    '''
def setScenarioProjectString():
    '''returns None\n\n
    setScenarioProjectString(final MboRemote skdProject)\n
    '''
def getScenarioString():
    '''returns String\n\n
    getScenarioString(final MboRemote skdProject)\n
    '''
def putQuickQueryQbe():
    '''returns None\n\n
    putQuickQueryQbe(final long skdqueryid, final Hashtable<String, String> savedQbeAttributesQuickQuery)\n
    '''
def putEWOQuickQueryQbe():
    '''returns None\n\n
    putEWOQuickQueryQbe(final long skdprojectid, final Hashtable<String, String> savedQbeAttributesQuickQuery)\n
    '''
def setScenarioType():
    '''returns None\n\n
    setScenarioType(final int type)\n
    setScenarioType(final String type)\n
    '''
def getScenarioType():
    '''returns int\n\n
    getScenarioType()\n
    '''
def getScenarioTypeStr():
    '''returns String\n\n
    getScenarioTypeStr()\n
    '''
def addSKDProjectScenario():
    '''returns None\n\n
    addSKDProjectScenario(final String inputObj, final String ODMAppName, final String scenarioName, final String inputName, final long inputObjId)\n
    '''
def deleteUncommitData():
    '''returns None\n\n
    deleteUncommitData()\n
    '''
def deleteData():
    '''returns None\n\n
    deleteData(final Connection conn, final String objectName, final String msgStr, final long projectId)\n
    '''
def hasDatesBeenUpdated():
    '''returns boolean\n\n
    hasDatesBeenUpdated()\n
    '''
def runOptimization():
    '''returns boolean\n\n
    runOptimization(final UserInfo userInfo, final boolean async)\n
    runOptimization(final UserInfo userInfo, final long skdOdmeRunIdIn, final boolean async)\n
    '''
def populateOriginDestMatrix():
    '''returns boolean\n\n
    populateOriginDestMatrix()\n
    '''
def needRefreshProject():
    '''returns boolean\n\n
    needRefreshProject()\n
    '''
def ShiftWorkperiod():
    '''returns MboRemote\n\n
    ShiftWorkperiod(final Date workdate, final String Orgid, final String Calnum, final String shiftnum)\n
    '''
def ShiftWorkingTime():
    '''returns boolean\n\n
    ShiftWorkingTime(final Date workdate, final String Orgid, final String Calnum, final String shiftnum)\n
    '''
def setProjectAssignDate():
    '''returns None\n\n
    setProjectAssignDate(final boolean next)\n
    '''
def gotoAssignDate():
    '''returns None\n\n
    gotoAssignDate(final String gotoday)\n
    '''
def createCronTaskInstance():
    '''returns None\n\n
    createCronTaskInstance(final boolean oneTimeCron)\n
    createCronTaskInstance(final boolean oneTimeCron, String cronTaskName)\n
    '''
def getProjectScenario():
    '''returns SKDProjectScenarioRemote\n\n
    getProjectScenario(final String cronTaskName)\n
    '''
def removeCronTaskInstance():
    '''returns None\n\n
    removeCronTaskInstance(final boolean oneTimeCron)\n
    removeCronTaskInstance(final boolean oneTimeCron, String cronTaskName)\n
    '''
def dynamicScheduling():
    '''returns int\n\n
    dynamicScheduling()\n
    '''
def assignLaborCrewFromSuggestSet():
    '''returns None\n\n
    assignLaborCrewFromSuggestSet(final MboSetRemote emWOAvailResSet)\n
    '''
def updateActivityDates():
    '''returns None\n\n
    updateActivityDates()\n
    '''
def getProjectsList():
    '''returns MboSetRemote\n\n
    getProjectsList(final MboSetRemote resultSet, final String userName)\n
    '''
def canCommit():
    '''returns None\n\n
    canCommit(final String personId)\n
    '''
def copyPersonsToCommPerson():
    '''returns None\n\n
    copyPersonsToCommPerson(final MboSetRemote personSet)\n
    '''
def copyGroupsToCommGroup():
    '''returns None\n\n
    copyGroupsToCommGroup(final MboSetRemote groupSet)\n
    '''
def roll():
    '''returns int\n\n
    roll()\n
    '''
def setRollDates():
    '''returns int\n\n
    setRollDates()\n
    '''
def isOptimizationInprogress():
    '''returns boolean\n\n
    isOptimizationInprogress()\n
    '''
def getCurrentSkdODMERunId():
    '''returns long\n\n
    getCurrentSkdODMERunId()\n
    '''
def setCurrentSkdODMERunId():
    '''returns long\n\n
    setCurrentSkdODMERunId(final long skdODMERunID)\n
    '''
def getPopulateDataObjectsWhere():
    '''returns String\n\n
    getPopulateDataObjectsWhere()\n
    '''
def getMaxSequenceName():
    '''returns String\n\n
    getMaxSequenceName(final String tbname)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
