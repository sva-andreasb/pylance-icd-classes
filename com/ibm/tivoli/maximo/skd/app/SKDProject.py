def SKDProject():
'''public SKDProject(final MboSet ms)
'''
pass
def setAssetLocWhere():
'''public void setAssetLocWhere(final String key, final String where)
'''
pass
def getAssetLocWhere():
'''public String getAssetLocWhere(final String key)
'''
pass
def init():
'''public void init()
'''
pass
def updateProjectData():
'''public void updateProjectData()
'''
pass
def save():
'''public void save()
'''
pass
def add():
'''public void add()
'''
pass
def setCalendarDates():
'''public void setCalendarDates()
'''
pass
def originalAppName():
'''public String originalAppName(final String appName)
'''
pass
def dupSchedulerProject():
'''public void dupSchedulerProject(final MboRemote selectedproject)
'''
pass
def duplicate():
'''public MboRemote duplicate()
'''
pass
def delete():
'''public void delete(final long accessModifier)
'''
pass
def canDelete():
'''public void canDelete()
'''
pass
def modify():
'''public void modify()
'''
pass
def setFromAsync():
'''public void setFromAsync(final boolean flag)
'''
pass
def getFromAsync():
'''public boolean getFromAsync()
'''
pass
def isProjectDataModified():
'''public boolean isProjectDataModified()
'''
pass
def appValidate():
'''public void appValidate()
'''
pass
def startScheduleCompliance():
'''public void startScheduleCompliance()
public void startScheduleCompliance(final MboSetRemote skdActivitySet, final SKDProjectRemote skdProject, final Date compstart, final Date compend)
'''
pass
def endScheduleCompliance():
'''public void endScheduleCompliance(final SKDProjectRemote skdProject, final Date compend)
'''
pass
def setNextDueDate():
'''public void setNextDueDate()
'''
pass
def updateNextStartAndEndDate():
'''public void updateNextStartAndEndDate()
'''
pass
def updateTimeBasedNextDueDate():
'''public void updateTimeBasedNextDueDate()
'''
pass
def getStatusListName():
'''public String getStatusListName()
'''
pass
def publish():
'''public void publish()
'''
pass
def createBaseLine():
'''public MboRemote createBaseLine(final String baseLineName, final String baseLineDescription, final String baseLineMemo, final String inputName, final String scenarioType)
'''
pass
def getBaseLineUniqueId():
'''public long getBaseLineUniqueId()
'''
pass
def getDefaultScenarioUniqueId():
'''public long getDefaultScenarioUniqueId(final String SKDProjectName)
'''
pass
def setDefaultScenario():
'''public void setDefaultScenario(final SKDProjectRemote SKDProject)
'''
pass
def canPublish():
'''public void canPublish()
'''
pass
def canCreateScenario():
'''public void canCreateScenario()
'''
pass
def canCreateSnapShot():
'''public void canCreateSnapShot()
'''
pass
def setPublishFlag():
'''public void setPublishFlag(final boolean publish)
'''
pass
def getPublishFlag():
'''public boolean getPublishFlag()
'''
pass
def setScenarioFlag():
'''public void setScenarioFlag(final boolean scenario)
'''
pass
def getScenarioFlag():
'''public boolean getScenarioFlag()
'''
pass
def setScenarioProjectString():
'''public void setScenarioProjectString(final MboRemote skdProject)
'''
pass
def getScenarioString():
'''public String getScenarioString(final MboRemote skdProject)
'''
pass
def getQuickQueryQbe():
'''public HashMap<Long, Hashtable<String, String>> getQuickQueryQbe()
'''
pass
def putQuickQueryQbe():
'''public void putQuickQueryQbe(final long skdqueryid, final Hashtable<String, String> savedQbeAttributesQuickQuery)
'''
pass
def getEWOQuickQueryQbe():
'''public HashMap<Long, Hashtable<String, String>> getEWOQuickQueryQbe()
'''
pass
def putEWOQuickQueryQbe():
'''public void putEWOQuickQueryQbe(final long skdprojectid, final Hashtable<String, String> savedQbeAttributesQuickQuery)
'''
pass
def setScenarioType():
'''public void setScenarioType(final int type)
public void setScenarioType(final String type)
'''
pass
def getScenarioType():
'''public int getScenarioType()
'''
pass
def getScenarioTypeStr():
'''public String getScenarioTypeStr()
'''
pass
def addSKDProjectScenario():
'''public void addSKDProjectScenario(final String inputObj, final String ODMAppName, final String scenarioName, final String inputName, final long inputObjId)
'''
pass
def deleteUncommitData():
'''public void deleteUncommitData()
'''
pass
def deleteData():
'''public void deleteData(final Connection conn, final String objectName, final String msgStr, final long projectId)
'''
pass
def hasDatesBeenUpdated():
'''public boolean hasDatesBeenUpdated()
'''
pass
def runOptimization():
'''public boolean runOptimization(final UserInfo userInfo, final boolean async)
public boolean runOptimization(final UserInfo userInfo, final long skdOdmeRunIdIn, final boolean async)
'''
pass
def populateOriginDestMatrix():
'''public boolean populateOriginDestMatrix()
'''
pass
def needRefreshProject():
'''public boolean needRefreshProject()
'''
pass
def ShiftWorkperiod():
'''public MboRemote ShiftWorkperiod(final Date workdate, final String Orgid, final String Calnum, final String shiftnum)
'''
pass
def ShiftWorkingTime():
'''public boolean ShiftWorkingTime(final Date workdate, final String Orgid, final String Calnum, final String shiftnum)
'''
pass
def setProjectAssignDate():
'''public void setProjectAssignDate(final boolean next)
'''
pass
def gotoAssignDate():
'''public void gotoAssignDate(final String gotoday)
'''
pass
def createCronTaskInstance():
'''public void createCronTaskInstance(final boolean oneTimeCron)
public void createCronTaskInstance(final boolean oneTimeCron, String cronTaskName)
'''
pass
def getProjectScenario():
'''public SKDProjectScenarioRemote getProjectScenario(final String cronTaskName)
'''
pass
def removeCronTaskInstance():
'''public void removeCronTaskInstance(final boolean oneTimeCron)
public void removeCronTaskInstance(final boolean oneTimeCron, String cronTaskName)
'''
pass
def dynamicScheduling():
'''public int dynamicScheduling()
'''
pass
def assignLaborCrewFromSuggestSet():
'''public void assignLaborCrewFromSuggestSet(final MboSetRemote emWOAvailResSet)
'''
pass
def updateActivityDates():
'''public void updateActivityDates()
'''
pass
def getProjectsList():
'''public MboSetRemote getProjectsList(final MboSetRemote resultSet, final String userName)
'''
pass
def canCommit():
'''public void canCommit(final String personId)
'''
pass
def copyPersonsToCommPerson():
'''public void copyPersonsToCommPerson(final MboSetRemote personSet)
'''
pass
def copyGroupsToCommGroup():
'''public void copyGroupsToCommGroup(final MboSetRemote groupSet)
'''
pass
def roll():
'''public int roll()
'''
pass
def setRollDates():
'''public int setRollDates()
'''
pass
def isOptimizationInprogress():
'''public boolean isOptimizationInprogress()
'''
pass
def getCurrentSkdODMERunId():
'''public long getCurrentSkdODMERunId()
'''
pass
def setCurrentSkdODMERunId():
'''public long setCurrentSkdODMERunId(final long skdODMERunID)
'''
pass
def getPopulateDataObjectsWhere():
'''public String getPopulateDataObjectsWhere()
'''
pass
def getMaxSequenceName():
'''public String getMaxSequenceName(final String tbname)
'''
pass
def AsyncProcessRunOptimization():
'''public AsyncProcessRunOptimization(final UserInfo userInfo, final SKDProject project, final OptimizationServiceRemote optimizationService, final String odmApplicationName, final OptimizationInputProcessParameters inputProcessParameters, final OptimizationOutputProcessParameters outputProcessParameters)
'''
pass
def run():
'''public void run()
'''
pass
