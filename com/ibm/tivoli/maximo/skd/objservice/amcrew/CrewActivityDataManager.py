CACHEKEY_ASSIGNMENTACTIVITYMAP = "String  \"CrewActivityDataManager-assignmentmap\""
def CrewActivityDataManager():
    '''    public CrewActivityDataManager()
    '''
def initializeActivity():
    '''    public void initializeActivity(final MXActivity activity, final String objectName, final MboRemote mboObject, final MXGanttModel model)
    '''
def populateActivities():
    '''    public void populateActivities(final HashMap<String, ArrayList<String>> queryMap)
    '''
def populateCrewActivities():
    '''    public void populateCrewActivities(final HashMap<String, ArrayList<String>> queryMap)
    '''
def getAmcrewLaborExcludeQuery():
    '''    public String getAmcrewLaborExcludeQuery(final int dbType)
    '''
def getAmcrewLaborRestrictQuery():
    '''    public String getAmcrewLaborRestrictQuery(final int dbType)
    '''
def getAmcrewAssetExcludeQuery():
    '''    public String getAmcrewAssetExcludeQuery(final int dbType)
    '''
def getAmcrewAssetRestrictQuery():
    '''    public String getAmcrewAssetRestrictQuery(final int dbType)
    '''
def populateCrewLabActivities():
    '''    public void populateCrewLabActivities(final HashMap<String, ArrayList<String>> queryMap)
    '''
def getOrgQuery():
    '''    public String getOrgQuery()
    '''
def getDateOnlyDBSqlString():
    '''    public String[] getDateOnlyDBSqlString(final int dbType)
    '''
def getSelectDateDBSqlString():
    '''    public String getSelectDateDBSqlString(final int dbType)
    '''
def getDateDBSqlString():
    '''    public String[] getDateDBSqlString(final int dbType)
    '''
def populateCrewLabposActivities():
    '''    public void populateCrewLabposActivities(final HashMap<String, ArrayList<String>> queryMap)
    '''
def populateActivityPropertyDetails():
    '''    public void populateActivityPropertyDetails()
    '''
def getCompleteQueryWhere():
    '''    public String getCompleteQueryWhere(final String objectName, final HashMap<String, ArrayList<String>> queryMap)
    '''
def getDefaultRestriction():
    '''    public String getDefaultRestriction(final String objectName)
    '''
def linkChildDummyNode():
    '''    public List<IlvActivity> linkChildDummyNode(final MXActivity activity, final MXGanttModel model, final SKDAppService.ActivityData activityData)
    '''
def loadActivity():
    '''    public void loadActivity(final MXActivity activity, final String objectName, final MboRemote mboObject)
    public void loadActivity(final MXActivity activity, final String objectName, final MXGanttModel model)
    '''
def activityRecordCount():
    '''    public int activityRecordCount(final HashMap<String, ArrayList<String>> queryMap)
    '''
def saveActivities():
    '''    public void saveActivities(final IlvGeneralActivity activity, final MXTransaction txn)
    '''
def applyAssignmentChanges():
    '''    public void applyAssignmentChanges(final IlvGeneralActivity activity, final MXTransaction txn)
    '''
def createAMCrewLabor():
    '''    public void createAMCrewLabor(final String position, final String laborCode, final String craft, final String skillLevel, final String vendor, final String contractNum, final String orgId, final MboRemote amCrew, final Date fromDateTime, final Date toDateTime, final MboSetRemote AssignSet)
    '''
def replaceAMCrewLabor():
    '''    public void replaceAMCrewLabor(final String position, final String laborCode, final String toLaborCode, final String craft, final String skillLevel, final String vendor, final String contractNum, final String orgId, final MboRemote amCrew, final Date fromDateTime, final Date toDateTime, final MboSetRemote AssignSet)
    '''
def removeAMCrewLabor():
    '''    public void removeAMCrewLabor(final String laborCode, final String craft, final String skillLevel, final String vendor, final String contractNum, final String orgId, final MboRemote amCrew, final Date endDateTime, final Date returnDateTime, final MboSetRemote AssignSet)
    '''
def createAMCrewTool():
    '''    public void createAMCrewTool(final String amcrew, final String toolSeq, final String assetNum, final String siteid, final String itemNum, final String setid, final MboRemote amCrew, final Date fromDateTime, final Date toDateTime, final MboSetRemote AssignSet)
    '''
def replaceAMCrewTool():
    '''    public void replaceAMCrewTool(final String amcrew, final String toolSeq, final String assetNum, final String toAssetNum, final String siteid, final String itemNum, final String setid, final MboRemote amCrew, final Date fromDateTime, final Date toDateTime, final MboSetRemote AssignSet)
    '''
def removeAMCrewTool():
    '''    public void removeAMCrewTool(final String amcrew, final String toolSeq, final String assetNum, final String siteid, final String itemNum, final String setid, final MboRemote amCrew, final Date origEndDateTime, final Date returnDateTime, final MboSetRemote AssignSet)
    '''
def applyActivityChange():
    '''    public void applyActivityChange(final MboRemote activityMboRemote, final MXTransaction txn)
    '''
def populateCrewToolSqActivities():
    '''    public void populateCrewToolSqActivities(final HashMap<String, ArrayList<String>> queryMap)
    '''
def populateCrewToolActivities():
    '''    public void populateCrewToolActivities(final HashMap<String, ArrayList<String>> queryMap)
    '''
def loadAdditionalActivities():
    '''    public void loadAdditionalActivities(final MXGanttModel model, final SKDAppService.ActivityData activityData)
    '''
def loadWorkAndNonWorkActivities():
    '''    public void loadWorkAndNonWorkActivities(final MXGanttModel model, final SKDAppService.ActivityData activityData)
    '''
def getAMCrew():
    '''    public String getAMCrew()
    '''
def setAMCrew():
    '''    public void setAMCrew(final String amcrew)
    '''
def getOrgId():
    '''    public String getOrgId()
    '''
def setOrgId():
    '''    public void setOrgId(final String orgId)
    '''
def getCalnum():
    '''    public String getCalnum()
    '''
def setCalnum():
    '''    public void setCalnum(final String calnum)
    '''
def getShiftnum():
    '''    public String getShiftnum()
    '''
def setShiftnum():
    '''    public void setShiftnum(final String shiftnum)
    '''
def getAssignDate():
    '''    public Date getAssignDate()
    '''
def setAssignDate():
    '''    public void setAssignDate(final Date assignDate)
    '''
def getAssignSeqNo():
    '''    public int getAssignSeqNo()
    '''
def setAssignSeqNo():
    '''    public void setAssignSeqNo(final int assignSeqNo)
    '''
def getRemarks():
    '''    public String getRemarks()
    '''
def setRemarks():
    '''    public void setRemarks(final String remarks)
    '''
