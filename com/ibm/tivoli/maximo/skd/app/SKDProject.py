def SKDProject():
    '''public SKDProject(final MboSet ms)
    '''
def setAssetLocWhere():
    '''public void setAssetLocWhere(final String key, final String where)
    '''
def getAssetLocWhere():
    '''public String getAssetLocWhere(final String key)
    '''
def init():
    '''public void init()
    '''
def updateProjectData():
    '''public void updateProjectData()
    '''
def save():
    '''public void save()
    '''
def add():
    '''public void add()
    '''
def setCalendarDates():
    '''public void setCalendarDates()
    '''
def originalAppName():
    '''public String originalAppName(final String appName)
    '''
def dupSchedulerProject():
    '''public void dupSchedulerProject(final MboRemote selectedproject)
    '''
def duplicate():
    '''public MboRemote duplicate()
    '''
def delete():
    '''public void delete(final long accessModifier)
    '''
def canDelete():
    '''public void canDelete()
    '''
def modify():
    '''public void modify()
    '''
def setFromAsync():
    '''public void setFromAsync(final boolean flag)
    '''
def getFromAsync():
    '''public boolean getFromAsync()
    '''
def isProjectDataModified():
    '''public boolean isProjectDataModified()
    '''
def appValidate():
    '''public void appValidate()
    '''
def startScheduleCompliance():
    '''public void startScheduleCompliance()
    public void startScheduleCompliance(final MboSetRemote skdActivitySet, final SKDProjectRemote skdProject, final Date compstart, final Date compend)
    '''
def endScheduleCompliance():
    '''public void endScheduleCompliance(final SKDProjectRemote skdProject, final Date compend)
    '''
def setNextDueDate():
    '''public void setNextDueDate()
    '''
def updateNextStartAndEndDate():
    '''public void updateNextStartAndEndDate()
    '''
def updateTimeBasedNextDueDate():
    '''public void updateTimeBasedNextDueDate()
    '''
def getStatusListName():
    '''public String getStatusListName()
    '''
def publish():
    '''public void publish()
    '''
def createBaseLine():
    '''public MboRemote createBaseLine(final String baseLineName, final String baseLineDescription, final String baseLineMemo, final String inputName, final String scenarioType)
    '''
def getBaseLineUniqueId():
    '''public long getBaseLineUniqueId()
    '''
def getDefaultScenarioUniqueId():
    '''public long getDefaultScenarioUniqueId(final String SKDProjectName)
    '''
def setDefaultScenario():
    '''public void setDefaultScenario(final SKDProjectRemote SKDProject)
    '''
def canPublish():
    '''public void canPublish()
    '''
def canCreateScenario():
    '''public void canCreateScenario()
    '''
def canCreateSnapShot():
    '''public void canCreateSnapShot()
    '''
def setPublishFlag():
    '''public void setPublishFlag(final boolean publish)
    '''
def getPublishFlag():
    '''public boolean getPublishFlag()
    '''
def setScenarioFlag():
    '''public void setScenarioFlag(final boolean scenario)
    '''
def getScenarioFlag():
    '''public boolean getScenarioFlag()
    '''
def setScenarioProjectString():
    '''public void setScenarioProjectString(final MboRemote skdProject)
    '''
def getScenarioString():
    '''public String getScenarioString(final MboRemote skdProject)
    '''
def getQuickQueryQbe():
    '''public HashMap<Long, Hashtable<String, String>> getQuickQueryQbe()
    '''
def putQuickQueryQbe():
    '''public void putQuickQueryQbe(final long skdqueryid, final Hashtable<String, String> savedQbeAttributesQuickQuery)
    '''
def getEWOQuickQueryQbe():
    '''public HashMap<Long, Hashtable<String, String>> getEWOQuickQueryQbe()
    '''
def putEWOQuickQueryQbe():
    '''public void putEWOQuickQueryQbe(final long skdprojectid, final Hashtable<String, String> savedQbeAttributesQuickQuery)
    '''
def setScenarioType():
    '''public void setScenarioType(final int type)
    public void setScenarioType(final String type)
    '''
def getScenarioType():
    '''public int getScenarioType()
    '''
def getScenarioTypeStr():
    '''public String getScenarioTypeStr()
    '''
def addSKDProjectScenario():
    '''public void addSKDProjectScenario(final String inputObj, final String ODMAppName, final String scenarioName, final String inputName, final long inputObjId)
    '''
def deleteUncommitData():
    '''public void deleteUncommitData()
    '''
def deleteData():
    '''public void deleteData(final Connection conn, final String objectName, final String msgStr, final long projectId)
    '''
def hasDatesBeenUpdated():
    '''public boolean hasDatesBeenUpdated()
    '''
def runOptimization():
    '''public boolean runOptimization(final UserInfo userInfo, final boolean async)
    public boolean runOptimization(final UserInfo userInfo, final long skdOdmeRunIdIn, final boolean async)
    '''
def populateOriginDestMatrix():
    '''public boolean populateOriginDestMatrix()
    '''
def needRefreshProject():
    '''public boolean needRefreshProject()
    '''
def ShiftWorkperiod():
    '''public MboRemote ShiftWorkperiod(final Date workdate, final String Orgid, final String Calnum, final String shiftnum)
    '''
def ShiftWorkingTime():
    '''public boolean ShiftWorkingTime(final Date workdate, final String Orgid, final String Calnum, final String shiftnum)
    '''
def setProjectAssignDate():
    '''public void setProjectAssignDate(final boolean next)
    '''
def gotoAssignDate():
    '''public void gotoAssignDate(final String gotoday)
    '''
def createCronTaskInstance():
    '''public void createCronTaskInstance(final boolean oneTimeCron)
    public void createCronTaskInstance(final boolean oneTimeCron, String cronTaskName)
    '''
def getProjectScenario():
    '''public SKDProjectScenarioRemote getProjectScenario(final String cronTaskName)
    '''
def removeCronTaskInstance():
    '''public void removeCronTaskInstance(final boolean oneTimeCron)
    public void removeCronTaskInstance(final boolean oneTimeCron, String cronTaskName)
    '''
def dynamicScheduling():
    '''public int dynamicScheduling()
    '''
def assignLaborCrewFromSuggestSet():
    '''public void assignLaborCrewFromSuggestSet(final MboSetRemote emWOAvailResSet)
    '''
def updateActivityDates():
    '''public void updateActivityDates()
    '''
def getProjectsList():
    '''public MboSetRemote getProjectsList(final MboSetRemote resultSet, final String userName)
    '''
def canCommit():
    '''public void canCommit(final String personId)
    '''
def copyPersonsToCommPerson():
    '''public void copyPersonsToCommPerson(final MboSetRemote personSet)
    '''
def copyGroupsToCommGroup():
    '''public void copyGroupsToCommGroup(final MboSetRemote groupSet)
    '''
def roll():
    '''public int roll()
    '''
def setRollDates():
    '''public int setRollDates()
    '''
def isOptimizationInprogress():
    '''public boolean isOptimizationInprogress()
    '''
def getCurrentSkdODMERunId():
    '''public long getCurrentSkdODMERunId()
    '''
def setCurrentSkdODMERunId():
    '''public long setCurrentSkdODMERunId(final long skdODMERunID)
    '''
def getPopulateDataObjectsWhere():
    '''public String getPopulateDataObjectsWhere()
    '''
def getMaxSequenceName():
    '''public String getMaxSequenceName(final String tbname)
    '''
def AsyncProcessRunOptimization():
    '''public AsyncProcessRunOptimization(final UserInfo userInfo, final SKDProject project, final OptimizationServiceRemote optimizationService, final String odmApplicationName, final OptimizationInputProcessParameters inputProcessParameters, final OptimizationOutputProcessParameters outputProcessParameters)
    '''
def run():
    '''public void run()
    '''
