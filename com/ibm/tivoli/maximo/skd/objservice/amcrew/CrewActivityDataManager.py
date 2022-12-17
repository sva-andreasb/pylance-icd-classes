CACHEKEY_ASSIGNMENTACTIVITYMAP = "String  \"CrewActivityDataManager-assignmentmap\""
def ():
    '''returns CrewActivityDataManager\n\n
    ()\n
    '''
def initializeActivity():
    '''returns None\n\n
    initializeActivity(final MXActivity activity, final String objectName, final MboRemote mboObject, final MXGanttModel model)\n
    '''
def populateActivities():
    '''returns None\n\n
    populateActivities(final HashMap<String, ArrayList<String>> queryMap)\n
    '''
def populateCrewActivities():
    '''returns None\n\n
    populateCrewActivities(final HashMap<String, ArrayList<String>> queryMap)\n
    '''
def getAmcrewLaborExcludeQuery():
    '''returns String\n\n
    getAmcrewLaborExcludeQuery(final int dbType)\n
    '''
def getAmcrewLaborRestrictQuery():
    '''returns String\n\n
    getAmcrewLaborRestrictQuery(final int dbType)\n
    '''
def getAmcrewAssetExcludeQuery():
    '''returns String\n\n
    getAmcrewAssetExcludeQuery(final int dbType)\n
    '''
def getAmcrewAssetRestrictQuery():
    '''returns String\n\n
    getAmcrewAssetRestrictQuery(final int dbType)\n
    '''
def populateCrewLabActivities():
    '''returns None\n\n
    populateCrewLabActivities(final HashMap<String, ArrayList<String>> queryMap)\n
    '''
def getOrgQuery():
    '''returns String\n\n
    getOrgQuery()\n
    '''
def getDateOnlyDBSqlString():
    '''returns String[]\n\n
    getDateOnlyDBSqlString(final int dbType)\n
    '''
def getSelectDateDBSqlString():
    '''returns String\n\n
    getSelectDateDBSqlString(final int dbType)\n
    '''
def getDateDBSqlString():
    '''returns String[]\n\n
    getDateDBSqlString(final int dbType)\n
    '''
def populateCrewLabposActivities():
    '''returns None\n\n
    populateCrewLabposActivities(final HashMap<String, ArrayList<String>> queryMap)\n
    '''
def populateActivityPropertyDetails():
    '''returns None\n\n
    populateActivityPropertyDetails()\n
    '''
def getCompleteQueryWhere():
    '''returns String\n\n
    getCompleteQueryWhere(final String objectName, final HashMap<String, ArrayList<String>> queryMap)\n
    '''
def getDefaultRestriction():
    '''returns String\n\n
    getDefaultRestriction(final String objectName)\n
    '''
def linkChildDummyNode():
    '''returns List<IlvActivity>\n\n
    linkChildDummyNode(final MXActivity activity, final MXGanttModel model, final SKDAppService.ActivityData activityData)\n
    '''
def loadActivity():
    '''returns None\n\n
    loadActivity(final MXActivity activity, final String objectName, final MboRemote mboObject)\n
    loadActivity(final MXActivity activity, final String objectName, final MXGanttModel model)\n
    '''
def activityRecordCount():
    '''returns int\n\n
    activityRecordCount(final HashMap<String, ArrayList<String>> queryMap)\n
    '''
def saveActivities():
    '''returns None\n\n
    saveActivities(final IlvGeneralActivity activity, final MXTransaction txn)\n
    '''
def applyAssignmentChanges():
    '''returns None\n\n
    applyAssignmentChanges(final IlvGeneralActivity activity, final MXTransaction txn)\n
    '''
def createAMCrewLabor():
    '''returns None\n\n
    createAMCrewLabor(final String position, final String laborCode, final String craft, final String skillLevel, final String vendor, final String contractNum, final String orgId, final MboRemote amCrew, final Date fromDateTime, final Date toDateTime, final MboSetRemote AssignSet)\n
    '''
def replaceAMCrewLabor():
    '''returns None\n\n
    replaceAMCrewLabor(final String position, final String laborCode, final String toLaborCode, final String craft, final String skillLevel, final String vendor, final String contractNum, final String orgId, final MboRemote amCrew, final Date fromDateTime, final Date toDateTime, final MboSetRemote AssignSet)\n
    '''
def removeAMCrewLabor():
    '''returns None\n\n
    removeAMCrewLabor(final String laborCode, final String craft, final String skillLevel, final String vendor, final String contractNum, final String orgId, final MboRemote amCrew, final Date endDateTime, final Date returnDateTime, final MboSetRemote AssignSet)\n
    '''
def createAMCrewTool():
    '''returns None\n\n
    createAMCrewTool(final String amcrew, final String toolSeq, final String assetNum, final String siteid, final String itemNum, final String setid, final MboRemote amCrew, final Date fromDateTime, final Date toDateTime, final MboSetRemote AssignSet)\n
    '''
def replaceAMCrewTool():
    '''returns None\n\n
    replaceAMCrewTool(final String amcrew, final String toolSeq, final String assetNum, final String toAssetNum, final String siteid, final String itemNum, final String setid, final MboRemote amCrew, final Date fromDateTime, final Date toDateTime, final MboSetRemote AssignSet)\n
    '''
def removeAMCrewTool():
    '''returns None\n\n
    removeAMCrewTool(final String amcrew, final String toolSeq, final String assetNum, final String siteid, final String itemNum, final String setid, final MboRemote amCrew, final Date origEndDateTime, final Date returnDateTime, final MboSetRemote AssignSet)\n
    '''
def applyActivityChange():
    '''returns None\n\n
    applyActivityChange(final MboRemote activityMboRemote, final MXTransaction txn)\n
    '''
def populateCrewToolSqActivities():
    '''returns None\n\n
    populateCrewToolSqActivities(final HashMap<String, ArrayList<String>> queryMap)\n
    '''
def populateCrewToolActivities():
    '''returns None\n\n
    populateCrewToolActivities(final HashMap<String, ArrayList<String>> queryMap)\n
    '''
def loadAdditionalActivities():
    '''returns None\n\n
    loadAdditionalActivities(final MXGanttModel model, final SKDAppService.ActivityData activityData)\n
    '''
def loadWorkAndNonWorkActivities():
    '''returns None\n\n
    loadWorkAndNonWorkActivities(final MXGanttModel model, final SKDAppService.ActivityData activityData)\n
    '''
def getAMCrew():
    '''returns String\n\n
    getAMCrew()\n
    '''
def setAMCrew():
    '''returns None\n\n
    setAMCrew(final String amcrew)\n
    '''
def getOrgId():
    '''returns String\n\n
    getOrgId()\n
    '''
def setOrgId():
    '''returns None\n\n
    setOrgId(final String orgId)\n
    '''
def getCalnum():
    '''returns String\n\n
    getCalnum()\n
    '''
def setCalnum():
    '''returns None\n\n
    setCalnum(final String calnum)\n
    '''
def getShiftnum():
    '''returns String\n\n
    getShiftnum()\n
    '''
def setShiftnum():
    '''returns None\n\n
    setShiftnum(final String shiftnum)\n
    '''
def getAssignDate():
    '''returns Date\n\n
    getAssignDate()\n
    '''
def setAssignDate():
    '''returns None\n\n
    setAssignDate(final Date assignDate)\n
    '''
def getAssignSeqNo():
    '''returns int\n\n
    getAssignSeqNo()\n
    '''
def setAssignSeqNo():
    '''returns None\n\n
    setAssignSeqNo(final int assignSeqNo)\n
    '''
def getRemarks():
    '''returns String\n\n
    getRemarks()\n
    '''
def setRemarks():
    '''returns None\n\n
    setRemarks(final String remarks)\n
    '''
