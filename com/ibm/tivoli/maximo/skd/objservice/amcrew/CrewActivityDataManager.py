CACHEKEY_ASSIGNMENTACTIVITYMAP = "String  CrewActivityDataManager-assignmentmap""
def CrewActivityDataManager():
'''public CrewActivityDataManager()
'''
pass
def initializeActivity():
'''public void initializeActivity(final MXActivity activity, final String objectName, final MboRemote mboObject, final MXGanttModel model)
'''
pass
def populateActivities():
'''public void populateActivities(final HashMap<String, ArrayList<String>> queryMap)
'''
pass
def populateCrewActivities():
'''public void populateCrewActivities(final HashMap<String, ArrayList<String>> queryMap)
'''
pass
def getAmcrewLaborExcludeQuery():
'''public String getAmcrewLaborExcludeQuery(final int dbType)
'''
pass
def getAmcrewLaborRestrictQuery():
'''public String getAmcrewLaborRestrictQuery(final int dbType)
'''
pass
def getAmcrewAssetExcludeQuery():
'''public String getAmcrewAssetExcludeQuery(final int dbType)
'''
pass
def getAmcrewAssetRestrictQuery():
'''public String getAmcrewAssetRestrictQuery(final int dbType)
'''
pass
def populateCrewLabActivities():
'''public void populateCrewLabActivities(final HashMap<String, ArrayList<String>> queryMap)
'''
pass
def getOrgQuery():
'''public String getOrgQuery()
'''
pass
def getDateOnlyDBSqlString():
'''public String[] getDateOnlyDBSqlString(final int dbType)
'''
pass
def getSelectDateDBSqlString():
'''public String getSelectDateDBSqlString(final int dbType)
'''
pass
def getDateDBSqlString():
'''public String[] getDateDBSqlString(final int dbType)
'''
pass
def populateCrewLabposActivities():
'''public void populateCrewLabposActivities(final HashMap<String, ArrayList<String>> queryMap)
'''
pass
def populateActivityPropertyDetails():
'''public void populateActivityPropertyDetails()
'''
pass
def getCompleteQueryWhere():
'''public String getCompleteQueryWhere(final String objectName, final HashMap<String, ArrayList<String>> queryMap)
'''
pass
def getDefaultRestriction():
'''public String getDefaultRestriction(final String objectName)
'''
pass
def linkChildDummyNode():
'''public List<IlvActivity> linkChildDummyNode(final MXActivity activity, final MXGanttModel model, final SKDAppService.ActivityData activityData)
'''
pass
def loadActivity():
'''public void loadActivity(final MXActivity activity, final String objectName, final MboRemote mboObject)
public void loadActivity(final MXActivity activity, final String objectName, final MXGanttModel model)
'''
pass
def activityRecordCount():
'''public int activityRecordCount(final HashMap<String, ArrayList<String>> queryMap)
'''
pass
def saveActivities():
'''public void saveActivities(final IlvGeneralActivity activity, final MXTransaction txn)
'''
pass
def applyAssignmentChanges():
'''public void applyAssignmentChanges(final IlvGeneralActivity activity, final MXTransaction txn)
'''
pass
def createAMCrewLabor():
'''public void createAMCrewLabor(final String position, final String laborCode, final String craft, final String skillLevel, final String vendor, final String contractNum, final String orgId, final MboRemote amCrew, final Date fromDateTime, final Date toDateTime, final MboSetRemote AssignSet)
'''
pass
def replaceAMCrewLabor():
'''public void replaceAMCrewLabor(final String position, final String laborCode, final String toLaborCode, final String craft, final String skillLevel, final String vendor, final String contractNum, final String orgId, final MboRemote amCrew, final Date fromDateTime, final Date toDateTime, final MboSetRemote AssignSet)
'''
pass
def removeAMCrewLabor():
'''public void removeAMCrewLabor(final String laborCode, final String craft, final String skillLevel, final String vendor, final String contractNum, final String orgId, final MboRemote amCrew, final Date endDateTime, final Date returnDateTime, final MboSetRemote AssignSet)
'''
pass
def createAMCrewTool():
'''public void createAMCrewTool(final String amcrew, final String toolSeq, final String assetNum, final String siteid, final String itemNum, final String setid, final MboRemote amCrew, final Date fromDateTime, final Date toDateTime, final MboSetRemote AssignSet)
'''
pass
def replaceAMCrewTool():
'''public void replaceAMCrewTool(final String amcrew, final String toolSeq, final String assetNum, final String toAssetNum, final String siteid, final String itemNum, final String setid, final MboRemote amCrew, final Date fromDateTime, final Date toDateTime, final MboSetRemote AssignSet)
'''
pass
def removeAMCrewTool():
'''public void removeAMCrewTool(final String amcrew, final String toolSeq, final String assetNum, final String siteid, final String itemNum, final String setid, final MboRemote amCrew, final Date origEndDateTime, final Date returnDateTime, final MboSetRemote AssignSet)
'''
pass
def applyActivityChange():
'''public void applyActivityChange(final MboRemote activityMboRemote, final MXTransaction txn)
'''
pass
def populateCrewToolSqActivities():
'''public void populateCrewToolSqActivities(final HashMap<String, ArrayList<String>> queryMap)
'''
pass
def populateCrewToolActivities():
'''public void populateCrewToolActivities(final HashMap<String, ArrayList<String>> queryMap)
'''
pass
def loadAdditionalActivities():
'''public void loadAdditionalActivities(final MXGanttModel model, final SKDAppService.ActivityData activityData)
'''
pass
def loadWorkAndNonWorkActivities():
'''public void loadWorkAndNonWorkActivities(final MXGanttModel model, final SKDAppService.ActivityData activityData)
'''
pass
def getAMCrew():
'''public String getAMCrew()
'''
pass
def setAMCrew():
'''public void setAMCrew(final String amcrew)
'''
pass
def getOrgId():
'''public String getOrgId()
'''
pass
def setOrgId():
'''public void setOrgId(final String orgId)
'''
pass
def getCalnum():
'''public String getCalnum()
'''
pass
def setCalnum():
'''public void setCalnum(final String calnum)
'''
pass
def getShiftnum():
'''public String getShiftnum()
'''
pass
def setShiftnum():
'''public void setShiftnum(final String shiftnum)
'''
pass
def getAssignDate():
'''public Date getAssignDate()
'''
pass
def setAssignDate():
'''public void setAssignDate(final Date assignDate)
'''
pass
def getAssignSeqNo():
'''public int getAssignSeqNo()
'''
pass
def setAssignSeqNo():
'''public void setAssignSeqNo(final int assignSeqNo)
'''
pass
def getRemarks():
'''public String getRemarks()
'''
pass
def setRemarks():
'''public void setRemarks(final String remarks)
'''
pass
