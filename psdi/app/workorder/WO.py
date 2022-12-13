crewDurStatic = "String  Static""
crewDurDynamic = "String  Dynamic""
crewDurCrewPos = "String  PLUSDCRW""
APPLYASSETLOC = "String  WO.ApplyingAssetLoc""
def isChangeInHierarchy():
'''public boolean isChangeInHierarchy()
'''
pass
def setChangeInHierarchy():
'''public void setChangeInHierarchy(final boolean changeInHierarchy)
'''
pass
def getPreviousParent():
'''public String getPreviousParent()
'''
pass
def setPreviousParent():
'''public void setPreviousParent(final String previousParent)
'''
pass
def WO():
'''public WO(final MboSet ms)
'''
pass
def getProcess():
'''public String getProcess()
'''
pass
def getStatusListName():
'''public String getStatusListName()
'''
pass
def init():
'''public void init()
'''
pass
def isCharacteristic():
'''public boolean isCharacteristic()
'''
pass
def canEditRelatedSet():
'''public void canEditRelatedSet(final String relationName)
'''
pass
def setRelatedMboEditibility():
'''public void setRelatedMboEditibility(final String relationName)
'''
pass
def initRelationship():
'''public void initRelationship(final String relationName, final MboSetRemote mboSet)
'''
pass
def modify():
'''public void modify()
'''
pass
def add():
'''public void add()
'''
pass
def updateServiceAddress():
'''public void updateServiceAddress()
'''
pass
def createJobEntry():
'''public MboRemote createJobEntry()
'''
pass
def createAssignRepLoc():
'''public void createAssignRepLoc()
'''
pass
def getCrewMemberCount():
'''public int getCrewMemberCount(final Date desiredDate)
'''
pass
def copyDoclinksToWO():
'''public void copyDoclinksToWO()
public void copyDoclinksToWO(final WO wo)
'''
pass
def inChildSubSet():
'''public boolean inChildSubSet()
'''
pass
def canDelete():
'''public void canDelete()
'''
pass
def getSimilarWorkOrders():
'''public WOSetRemote getSimilarWorkOrders()
'''
pass
def getAlreadyReportedSet():
'''public WOSetRemote getAlreadyReportedSet()
'''
pass
def getLocForAsset():
'''public void getLocForAsset()
'''
pass
def applyAssetLoc():
'''public void applyAssetLoc()
public void applyAssetLoc(final boolean calcSafetyPlan)
'''
pass
def copyJobPlanToWorkPlan():
'''public void copyJobPlanToWorkPlan()
'''
pass
def copyJobPlanToWorkPlanNoNestedJP():
'''public void copyJobPlanToWorkPlanNoNestedJP()
'''
pass
def clearWorkPlanInfo():
'''public void clearWorkPlanInfo()
'''
pass
def calculateConstaintDates():
'''public void calculateConstaintDates(final MboValue startOffset, final MboValue finishOffset, final MboValue woDur)
'''
pass
def getWoTaskLookup():
'''public Map<String, Mbo> getWoTaskLookup()
'''
pass
def getAddingFirstJobTask():
'''public boolean getAddingFirstJobTask()
'''
pass
def getCopyingJobTasks():
'''public boolean getCopyingJobTasks()
'''
pass
def getCopyingWorkPlanAssignments():
'''public boolean getCopyingWorkPlanAssignments()
'''
pass
def applyingJobPlan():
'''public boolean applyingJobPlan()
'''
pass
def setParentValuesForNestedjpWO():
'''public void setParentValuesForNestedjpWO(final MboRemote newChild, final MboRemote parent)
'''
pass
def generateTaskID():
'''public void generateTaskID()
'''
pass
def copySafetyPlanToWoSafetyPlan():
'''public void copySafetyPlanToWoSafetyPlan()
'''
pass
def setJobPlanFieldFlag():
'''public void setJobPlanFieldFlag()
'''
pass
def startWFOnWoReqSave():
'''public boolean startWFOnWoReqSave()
'''
pass
def updateForMovedAsset():
'''public void updateForMovedAsset(final MboRemote movedAsset)
'''
pass
def incrEstLabCost():
'''public void incrEstLabCost(final double incrAmount, final boolean isExternal)
'''
pass
def incrEstLabHours():
'''public void incrEstLabHours(final double incrAmount, final boolean isExternal)
'''
pass
def incrEstToolCost():
'''public void incrEstToolCost(final double incrAmount)
'''
pass
def incrEstMatCost():
'''public void incrEstMatCost(final double incrAmount)
'''
pass
def incrEstServCost():
'''public void incrEstServCost(final double incrAmount)
'''
pass
def incrActMatCost():
'''public void incrActMatCost(final double incrAmount, final boolean isOutsideCost)
'''
pass
def incrActLabCost():
'''public void incrActLabCost(final double incrAmount, final boolean isOutsideCost)
'''
pass
def incrActLabHrs():
'''public void incrActLabHrs(final double incrAmount, final boolean isExternal)
'''
pass
def incrActToolCost():
'''public void incrActToolCost(final double incrAmount, final boolean isOutsideCost)
'''
pass
def incrActServCost():
'''public void incrActServCost(final double incrAmount)
'''
pass
def haveReceivedDirectIssue():
'''public void haveReceivedDirectIssue(final MboRemote poMbo, final MboRemote poLineMbo)
'''
pass
def getValidateOrder():
'''public String[] getValidateOrder()
'''
pass
def isCanceled():
'''public boolean isCanceled()
'''
pass
def generateAutoKey():
'''public void generateAutoKey()
'''
pass
def isAssetChargeStore():
'''public boolean isAssetChargeStore()
'''
pass
def canChargeStore():
'''public boolean canChargeStore()
'''
pass
def calcGLAccount():
'''public void calcGLAccount()
'''
pass
def getSubWorkOrders():
'''public MboSetRemote getSubWorkOrders()
'''
pass
def canApplyRoute():
'''public void canApplyRoute()
public void canApplyRoute(final long accessModifier)
public void canApplyRoute(final String routeID)
public void canApplyRoute(final String routeID, final long accessModifier)
'''
pass
def applyRoute():
'''public void applyRoute(final String routeID, final String storeLoc)
public void applyRoute(final String routeID, final String storeLoc, final String storeLocSite)
public void applyRoute(final String routeID, final String storeLoc, final String storeLocSite, final long accessModifier)
public void applyRoute(final String routeID, final String storeLoc, final String storeLocSite, final long accessModifier, final MboSetRemote infoSet)
'''
pass
def getGrandTotals():
'''public Vector getGrandTotals()
'''
pass
def getDuplicated():
'''public boolean getDuplicated()
'''
pass
def setDuplicated():
'''public void setDuplicated(final boolean duplicated)
'''
pass
def duplicate():
'''public MboRemote duplicate()
'''
pass
def canGenFollowUpWo():
'''public void canGenFollowUpWo()
'''
pass
def genFollowUpWo():
'''public MboRemote genFollowUpWo()
'''
pass
def setSafetyPlanFieldFlag():
'''public void setSafetyPlanFieldFlag()
'''
pass
def getServiceTotal():
'''public double getServiceTotal()
'''
pass
def isTop():
'''public boolean isTop()
'''
pass
def hasChildren():
'''public boolean hasChildren()
'''
pass
def hasParents():
'''public boolean hasParents()
'''
pass
def hasSafetyPlan():
'''public boolean hasSafetyPlan()
'''
pass
def getChildren():
'''public MboSetRemote getChildren()
'''
pass
def getChildNoTask():
'''public MboSetRemote getChildNoTask()
'''
pass
def getTasksOnly():
'''public MboSetRemote getTasksOnly()
'''
pass
def getParents():
'''public MboSetRemote getParents()
'''
pass
def getTop():
'''public MboSetRemote getTop()
'''
pass
def getHierarchies():
'''public String[] getHierarchies()
'''
pass
def copySparePartsToWpMatSet():
'''public void copySparePartsToWpMatSet(final MboSetRemote sparePartSet)
'''
pass
def copySparePartsToMatUseSet():
'''public void copySparePartsToMatUseSet(final MboSetRemote sparePartSet)
'''
pass
def copyInvresvItemsToMatUseSet():
'''public void copyInvresvItemsToMatUseSet(final MboSetRemote InvresvItemSet)
'''
pass
def copyPlanToolToToolTransSet():
'''public void copyPlanToolToToolTransSet(final MboSetRemote planToolSet)
'''
pass
def copyPlanLaborToLabTransSet():
'''public void copyPlanLaborToLabTransSet(final MboSetRemote planLaborSet)
'''
pass
def applyHazardToWoHazardSet():
'''public void applyHazardToWoHazardSet(final MboRemote spRelatedasset, final MboSetRemote hazardSet)
'''
pass
def enterQuickReportingMode():
'''public void enterQuickReportingMode()
'''
pass
def isQuickReportingMode():
'''public boolean isQuickReportingMode()
'''
pass
def isApproved():
'''public boolean isApproved()
'''
pass
def getTaskForWonum():
'''public String getTaskForWonum(final String wonum)
'''
pass
def getWOforTask():
'''public MboRemote getWOforTask(final String task)
'''
pass
def getWOforWonum():
'''public WORemote getWOforWonum(final String wonum)
'''
pass
def getWOClassDescription():
'''public String getWOClassDescription(final MboRemote theMboRemote)
'''
pass
def changeWorkOrderParent():
'''public void changeWorkOrderParent(final MboRemote woparent)
'''
pass
def changeStatus():
'''public void changeStatus(final String status, final Date date, final String memo, final long accessModifier)
public void changeStatus(final String status, final Date date, final String memo, final long accessModifier, final boolean comingFromReceiving)
'''
pass
def changeChildrenStatus():
'''public void changeChildrenStatus()
'''
pass
def getParentMbo():
'''public WO getParentMbo()
'''
pass
def getWoFromCombined():
'''public WORemote getWoFromCombined(final String findWonum)
'''
pass
def canRemoveSafetyPlan():
'''public void canRemoveSafetyPlan()
'''
pass
def removeSafetyPlan():
'''public void removeSafetyPlan()
'''
pass
def canReportDowntime():
'''public void canReportDowntime()
'''
pass
def getOwnSet():
'''public MboSetRemote getOwnSet()
'''
pass
def setAttrFromWoGen():
'''public void setAttrFromWoGen(final MboRemote woGen)
'''
pass
def getECommHelperRemote():
'''public ECommHelperRemote getECommHelperRemote()
'''
pass
def editHistory():
'''public void editHistory()
'''
pass
def isWOInEditHist():
'''public boolean isWOInEditHist()
'''
pass
def propagateKeyValue():
'''public void propagateKeyValue(final String keyName, final String keyValue)
'''
pass
def getPM():
'''public PMRemote getPM()
'''
pass
def getAsset():
'''public AssetRemote getAsset()
'''
pass
def delete():
'''public void delete()
public void delete(final long accessModifier)
'''
pass
def undelete():
'''public void undelete()
'''
pass
def getFailListForReport():
'''public MboSetRemote getFailListForReport()
'''
pass
def copyFailListToReportSet():
'''public void copyFailListToReportSet(final MboSetRemote failListSet)
'''
pass
def copyLaborToWpLaborSet():
'''public void copyLaborToWpLaborSet(final MboSetRemote laborSet)
'''
pass
def copyCraftRateToWpLaborSet():
'''public void copyCraftRateToWpLaborSet(final MboSetRemote craftRateSet)
'''
pass
def copyLaborToLabTransSet():
'''public void copyLaborToLabTransSet(final MboSetRemote laborSet)
'''
pass
def copyItemToWpMatSet():
'''public void copyItemToWpMatSet(final MboSetRemote itemSet)
'''
pass
def copyServiceItemsToWpSerSet():
'''public void copyServiceItemsToWpSerSet(final MboSetRemote serviceItemSet)
'''
pass
def copyItemToMatUseTransSet():
'''public void copyItemToMatUseTransSet(final MboSetRemote itemSet)
'''
pass
def copyToolToWpToolSet():
'''public void copyToolToWpToolSet(final MboSetRemote toolSet)
'''
pass
def copyMatUseTransToToolTransSet():
'''public void copyMatUseTransToToolTransSet(final MboSetRemote matUseTransSet)
'''
pass
def copyToolToToolTransSet():
'''public void copyToolToToolTransSet(final MboSetRemote toolSet)
'''
pass
def copyMRLineToPlanMaterialSet():
'''public void copyMRLineToPlanMaterialSet(final MboSetRemote mrLineSet)
'''
pass
def getMboSet():
'''public MboSetRemote getMboSet(String name)
'''
pass
def getPOTotal():
'''public double getPOTotal()
'''
pass
def getPRTotal():
'''public double getPRTotal()
'''
pass
def makeSelectedChildren():
'''public void makeSelectedChildren(final MboSetRemote selectSet)
public void makeSelectedChildren(final MboSetRemote selectSet, String dialogLabel)
'''
pass
def canRemoveWorkPlan():
'''public void canRemoveWorkPlan()
'''
pass
def removeWorkPlan():
'''public boolean removeWorkPlan()
'''
pass
def hasActuals():
'''public boolean hasActuals()
'''
pass
def hasPlanMoveModify():
'''public boolean hasPlanMoveModify()
'''
pass
def removeFailureReport():
'''public void removeFailureReport()
'''
pass
def promptForDowntimeReport():
'''public boolean promptForDowntimeReport(final String newStatus)
'''
pass
def promptForFailureReport():
'''public boolean promptForFailureReport(final String newStatus)
'''
pass
def createJPFromWO():
'''public MboRemote createJPFromWO(final String jpnum, final String description, final String longdescription)
public MboRemote createJPFromWO(final Date date, final String jpnum, final String description, final String longdescription)
'''
pass
def createJPHeaderFromWO():
'''public Mbo createJPHeaderFromWO(final String jpnum, final String description, final String longdescription)
'''
pass
def createWorkorder():
'''public MboRemote createWorkorder()
public MboRemote createWorkorder(final String jpnum)
public MboRemote createWorkorder(final MboSetRemote workorderSet)
public MboRemote createWorkorder(final MboSetRemote workorderSet, final String jpnum, final boolean saveSet)
'''
pass
def createChange():
'''public MboRemote createChange()
public MboRemote createChange(final String jpnum)
'''
pass
def createRelease():
'''public MboRemote createRelease()
public MboRemote createRelease(final String jpnum)
'''
pass
def createServiceRequest():
'''public MboRemote createServiceRequest()
public MboRemote createServiceRequest(final String tickettemplateid)
'''
pass
def createProblem():
'''public MboRemote createProblem()
public MboRemote createProblem(final String tickettemplateid)
'''
pass
def createIncident():
'''public MboRemote createIncident()
public MboRemote createIncident(final String tickettemplateid)
'''
pass
def orphan():
'''public void orphan()
'''
pass
def handleChildren():
'''public void handleChildren()
'''
pass
def handleTasks():
'''public void handleTasks()
'''
pass
def handleUndeleteTasks():
'''public void handleUndeleteTasks()
'''
pass
def handleUndeleteChildren():
'''public void handleUndeleteChildren()
'''
pass
def deleteChildren():
'''public void deleteChildren(final boolean task)
'''
pass
def undeleteChildren():
'''public void undeleteChildren(final boolean task)
'''
pass
def isWoAcceptsChargesEditable():
'''public boolean isWoAcceptsChargesEditable()
'''
pass
def getTaskIdsThatAcceptCharges():
'''public String getTaskIdsThatAcceptCharges()
'''
pass
def pmAlertStatus():
'''public MboSetRemote pmAlertStatus(final String status)
'''
pass
def pmAlert():
'''public MboSetRemote pmAlert()
'''
pass
def getStatus():
'''public String getStatus(final String status)
'''
pass
def woCancel():
'''public boolean woCancel()
'''
pass
def canEnterMeterReadings():
'''public void canEnterMeterReadings()
'''
pass
def startTimer():
'''public void startTimer()
public void startTimer(final Date startdatetime, final Long anywhererefid, final String transtype)
'''
pass
def stopTimer():
'''public void stopTimer()
public MboRemote stopTimer(final Date finishdatetime, final boolean noStopTimerPopup)
public MboRemote stopTimer(final Date finishdatetime, final Date startDateTime, final boolean noStopTimerPopup)
'''
pass
def getStopTimerLabtrans():
'''public MboRemote getStopTimerLabtrans()
'''
pass
def needPopupOnStopTimer():
'''public boolean needPopupOnStopTimer()
'''
pass
def updateWorkview():
'''public void updateWorkview()
'''
pass
def clearClassification():
'''public void clearClassification()
'''
pass
def applyOwner():
'''public void applyOwner(final String ownerID)
'''
pass
def applyOwnerGroup():
'''public void applyOwnerGroup(final String ownergroupID)
'''
pass
def applyAssignedOwnerGroup():
'''public void applyAssignedOwnerGroup(final String ownergroupID)
'''
pass
def ownership():
'''public void ownership()
'''
pass
def copyAssetSpecToAutoAttrUpdateSet():
'''public void copyAssetSpecToAutoAttrUpdateSet(final MboSetRemote assetspecset, final MboRemote woasset)
'''
pass
def copyLocSpecToAutoAttrUpdateSet():
'''public void copyLocSpecToAutoAttrUpdateSet(final MboSetRemote locspecset, final MboRemote woasset)
'''
pass
def copyCISpecToAutoAttrUpdateSet():
'''public void copyCISpecToAutoAttrUpdateSet(final MboSetRemote cispecset, final MboRemote woasset)
'''
pass
def applyToAllAssetLoc():
'''public void applyToAllAssetLoc(final MboRemote attrupdate)
'''
pass
def copyAssets():
'''public void copyAssets(final MboSetRemote assetset)
'''
pass
def copyLocations():
'''public void copyLocations(final MboSetRemote locationset)
'''
pass
def moveModifyAssets():
'''public void moveModifyAssets()
public boolean moveModifyAssets(final boolean checkonly)
'''
pass
def moveAllAssets():
'''public void moveAllAssets()
'''
pass
def modifyAllAssetLocationAttributes():
'''public void modifyAllAssetLocationAttributes()
'''
pass
def removeUserCust():
'''public void removeUserCust()
public void removeUserCust(final boolean removeAssetUserCustPlans, final boolean removeLocUserCustPlans)
public void removeUserCust(final boolean removeAssetUserCustPlans, final boolean removeLocUserCustPlans, final MboRemote multiassetlocci)
'''
pass
def restoreUserCust():
'''public void restoreUserCust()
public void restoreUserCust(final MboRemote multiassetlocci)
'''
pass
def clearMoveandDeleteAttrUpdate():
'''public void clearMoveandDeleteAttrUpdate()
'''
pass
def clearMoveAssetFields():
'''public void clearMoveAssetFields()
'''
pass
def updateWarrantyContracts():
'''public void updateWarrantyContracts()
'''
pass
def getServiceContractInClause():
'''public String getServiceContractInClause()
'''
pass
def getWODate():
'''public Date getWODate()
'''
pass
def userVerifiedRemoveSafetyPlan():
'''public boolean userVerifiedRemoveSafetyPlan()
'''
pass
def getSafetyPlanID():
'''public String getSafetyPlanID()
'''
pass
def copyTicketToRelatedRecSet():
'''public void copyTicketToRelatedRecSet(final MboSetRemote TicketSet)
public void copyTicketToRelatedRecSet(final MboSetRemote TicketSet, final boolean copyToParent)
'''
pass
def copyTicketParentToRelatedRecSet():
'''public void copyTicketParentToRelatedRecSet(final MboSetRemote TicketSet)
'''
pass
def copyWOToRelatedRecSet():
'''public void copyWOToRelatedRecSet(final MboSetRemote woSet)
public void copyWOToRelatedRecSet(final MboSetRemote woSet, final boolean copyToParent)
'''
pass
def copyWOParentToRelatedRecSet():
'''public void copyWOParentToRelatedRecSet(final MboSetRemote woSet)
'''
pass
def copyParentValuesToRelatedRec():
'''public void copyParentValuesToRelatedRec(final MboRemote relatedMbo)
'''
pass
def updateOriginator():
'''public void updateOriginator()
'''
pass
def getWOObjectName():
'''public String getWOObjectName()
'''
pass
def getRecordMboName():
'''public String getRecordMboName()
'''
pass
def setHashForSelectedRecord():
'''public void setHashForSelectedRecord(final HashSet hs)
'''
pass
def getHashForSelectedRecord():
'''public HashSet getHashForSelectedRecord()
'''
pass
def clearHashForSelectedRecord():
'''public void clearHashForSelectedRecord()
'''
pass
def relateWorkorders():
'''public MboSetRemote relateWorkorders(final MboSetRemote woSet)
'''
pass
def relateTickets():
'''public MboSetRemote relateTickets(final MboSetRemote ticketSet)
'''
pass
def copyAssetsToMultiAsset():
'''public void copyAssetsToMultiAsset(final AssetSetRemote assetSetRemote)
'''
pass
def copyLocationsToMultiAsset():
'''public void copyLocationsToMultiAsset(final MboSetRemote locationSetRemote)
'''
pass
def checkNestedJobPlans():
'''public boolean checkNestedJobPlans()
'''
pass
def setRemoveWorkPlan():
'''public void setRemoveWorkPlan(final boolean removeChildFlag)
'''
pass
def getRemoveWorkPlan():
'''public boolean getRemoveWorkPlan()
'''
pass
def copyCIsToMultiAsset():
'''public void copyCIsToMultiAsset(final MboSetRemote ciSetRemote)
'''
pass
def copyRouteStopsToMultiAsset():
'''public void copyRouteStopsToMultiAsset(final MboSetRemote routestopSetRemote)
'''
pass
def copyCollectDetailsToMultiAsset():
'''public void copyCollectDetailsToMultiAsset(final MboSetRemote routestopSetRemote)
'''
pass
def appValidate():
'''public void appValidate()
'''
pass
def setmultiassetrecord():
'''public void setmultiassetrecord()
'''
pass
def copyWOFieldsToMultiAsset():
'''public void copyWOFieldsToMultiAsset(final MultiAssetLocCIRemote multiAssetMbo)
'''
pass
def isLicensePresent():
'''public static boolean isLicensePresent(final String lic)
'''
pass
def getFlowControlState():
'''public int getFlowControlState()
public int getFlowControlState(final WO wo, final String status)
'''
pass
def isFlowControlComplete():
'''public boolean isFlowControlComplete()
public boolean isFlowControlComplete(final WO wo, final String status)
'''
pass
def getStartStatusForWorkType():
'''public String getStartStatusForWorkType()
public String getStartStatusForWorkType(final WO wo)
'''
pass
def getCompleteStatusForWorkType():
'''public String getCompleteStatusForWorkType()
public String getCompleteStatusForWorkType(final WO wo)
'''
pass
def getPredecessors():
'''public Vector getPredecessors()
'''
pass
def getSuccessors():
'''public Vector getSuccessors()
'''
pass
def getChildrenThatHaveNoPredecessors():
'''public Vector getChildrenThatHaveNoPredecessors()
'''
pass
def suspendChildrensProcessFlow():
'''public void suspendChildrensProcessFlow(final boolean torf)
'''
pass
def setChildrensFlowControl():
'''public void setChildrensFlowControl(final boolean torf)
'''
pass
def changeChildrensFieldValue():
'''public void changeChildrensFieldValue(final String fieldname, final String fieldvalue, final long accessModifier)
'''
pass
def executeProcessFlowControlAction():
'''public void executeProcessFlowControlAction()
'''
pass
def changeStatusProcessFlowControl():
'''public void changeStatusProcessFlowControl()
'''
pass
def startSuccessors():
'''public boolean startSuccessors(final Mbo mbo, final Vector successors, final Date date, final String memo, final long accessModifier)
'''
pass
def adjustSuccVectors():
'''public void adjustSuccVectors(final Vector existingSuccs, final Vector newSuccs)
'''
pass
def areAllPredecessorsComplete():
'''public boolean areAllPredecessorsComplete()
public boolean areAllPredecessorsComplete(final WO wo)
public boolean areAllPredecessorsComplete(final String targetStatus, final boolean fully)
public boolean areAllPredecessorsComplete(final WO wo, final String targetStatus, final boolean fully)
'''
pass
def areAllPredecessorsSufficientlyComplete():
'''public boolean areAllPredecessorsSufficientlyComplete(final WO wo, final String targetStatus)
'''
pass
def getContemplatedAction():
'''public int getContemplatedAction(final WO wo, final String targetStatus)
'''
pass
def isSufficientlyFlowControlComplete():
'''public boolean isSufficientlyFlowControlComplete(final WO wo, final String reltypeToSuccessor, final int contemplatedAction)
public boolean isSufficientlyFlowControlComplete(final WO wo, final String status, final String reltypeToSuccessor, final int contemplatedAction)
'''
pass
def getChildPFCOrder():
'''public Vector getChildPFCOrder(final boolean getChildrenWOs, final boolean appendSiteid)
'''
pass
def findPredecessorPosition():
'''public int findPredecessorPosition(final Vector vector2Search, final String wonum, final Hashtable htNetwork)
'''
pass
def bulkReschedule():
'''public void bulkReschedule(final boolean resched, final Date reschedDate, final boolean fromListTab)
public void bulkReschedule(final boolean resched, final Date reschedDate)
'''
pass
def getRescheduled():
'''public int getRescheduled()
'''
pass
def getUnassigned():
'''public int getUnassigned()
'''
pass
def unassignWOAssignments():
'''public void unassignWOAssignments(AssignmentSet assignSet, final Date reschedDate)
'''
pass
def unassignAssignments():
'''public void unassignAssignments(final AssignmentSet assignSet, final Date reschedDate)
'''
pass
def rescheduleAssignments():
'''public void rescheduleAssignments(AssignmentSet assignSet, final Date reschedDate, final boolean fromListTab)
public void rescheduleAssignments(final AssignmentSet assignSet, final Date reschedDate)
'''
pass
def getLCRSqlFormatHashMap():
'''public HashMap getLCRSqlFormatHashMap(final AssignmentSet assignSet)
'''
pass
def calculateScheduleFinishDate():
'''public Date calculateScheduleFinishDate(final WO wo, final Date schedStartDate)
'''
pass
def setWOScheduleDates():
'''public void setWOScheduleDates(final WO wo, Date schedStartDate)
public void setWOScheduleDates(final WO wo, Date schedStartDate, final double duration)
'''
pass
def restoreSplitAssignments():
'''public AssignmentSet restoreSplitAssignments(AssignmentSet assignSet)
'''
pass
def getToplevelParentAssign():
'''public Assignment getToplevelParentAssign(Assignment assign, final AssignmentSet assignSet, final HashMap assignIndexMap)
'''
pass
def removeCompleteStartedAssigns():
'''public AssignmentSet removeCompleteStartedAssigns(final AssignmentSet assignSet, final HashMap assignIndexMap)
'''
pass
def applyToAllUser():
'''public void applyToAllUser(final MboRemote woModUser)
'''
pass
def setPrimaryLinearAssetFieldsReadOnly():
'''public void setPrimaryLinearAssetFieldsReadOnly(MultiAssetLocCIRemote multiAssetMbo, final boolean readonlystate)
'''
pass
def clearPrimaryLinearAssetFields():
'''public void clearPrimaryLinearAssetFields(final MultiAssetLocCIRemote multiAssetMbo)
'''
pass
def copyLinearAssetFieldsFromRouteStop():
'''public void copyLinearAssetFieldsFromRouteStop(final MboRemote toMbo, final MboRemote routestop)
'''
pass
def setRemoveWorkPlanFlag():
'''public void setRemoveWorkPlanFlag(final boolean removeWorkplan)
'''
pass
def getRemoveWorkPlanFlag():
'''public boolean getRemoveWorkPlanFlag()
'''
pass
def getTopOwner():
'''public MboRemote getTopOwner()
'''
pass
def checkCompStatus():
'''public void checkCompStatus()
'''
pass
def doClassificationCreateTicketViews():
'''public void doClassificationCreateTicketViews(final MboRemote newMbo)
'''
pass
def doClassificationCreateWOViews():
'''public void doClassificationCreateWOViews(final MboRemote newMbo)
'''
pass
def doClassificationCreateWOSpecFromJobPlan():
'''public void doClassificationCreateWOSpecFromJobPlan(final MboRemote newMbo, final MboRemote sourceMbo)
'''
pass
def CheckOrigIsFollowup():
'''public void CheckOrigIsFollowup()
'''
pass
def clearSkipCopyFields():
'''public void clearSkipCopyFields()
'''
pass
def routeStopExists():
'''public boolean routeStopExists()
'''
pass
def isListSelected():
'''public boolean isListSelected()
'''
pass
def setListSelected():
'''public void setListSelected(final boolean isListSelected)
'''
pass
def getCopydocMboSet():
'''public MboSetRemote getCopydocMboSet(String name)
'''
pass
def setAvailibilityStatus():
'''public MTLStatus setAvailibilityStatus(final boolean changeStatus)
'''
pass
def setStoreroomStatus():
'''public MTLStatus setStoreroomStatus(final boolean changeStatus)
'''
pass
def setDirectIssueStatus():
'''public MTLStatus setDirectIssueStatus()
'''
pass
def setChildrenStatus():
'''public MTLStatus setChildrenStatus(final MTLStatus storeroomStatus, final MTLStatus directIssueStatus, final boolean changeStatus)
'''
pass
def setMaterialAvailStatus():
'''public MTLStatus setMaterialAvailStatus()
'''
pass
def smartFillForAllSites():
'''public MboSetRemote smartFillForAllSites(final String attribute, final String value, final boolean exact)
'''
pass
def smartFindForAllSites():
'''public MboSetRemote smartFindForAllSites(final String attribute, final String value, final boolean exact)
'''
pass
def isRevEnabled():
'''public boolean isRevEnabled()
'''
pass
def isCalibrationInstalled():
'''public boolean isCalibrationInstalled()
'''
pass
def isFromMobile():
'''public boolean isFromMobile()
'''
pass
def setFromMobile():
'''public void setFromMobile(final boolean isFromMobile)
'''
pass
def setCompleteWOFromEveryplace():
'''public void setCompleteWOFromEveryplace(boolean completeWOFromEveryplace)
'''
pass
def manageCircleEffect():
'''public void manageCircleEffect(final MboRemote thisToolTrans)
'''
pass
def getWorkTypeCal():
'''public String getWorkTypeCal()
'''
pass
def getTranslatedWorkTypeCal():
'''public String getTranslatedWorkTypeCal()
'''
pass
def getJobRevNum():
'''public String getJobRevNum(final Mbo PlusCWO)
'''
pass
def isValidJPRevNum():
'''public boolean isValidJPRevNum(final String jpNum, final String revNum)
'''
pass
def getWorkType():
'''public String getWorkType()
'''
pass
def checkRequiredDatasheets():
'''public boolean checkRequiredDatasheets()
'''
pass
def duplicateWODS():
'''public MboRemote duplicateWODS(final MboRemote newWO)
'''
pass
def canEditRelatedSetCal():
'''public void canEditRelatedSetCal(final String relationName)
'''
pass
def canEditAsFoundAsLeftFields():
'''public boolean canEditAsFoundAsLeftFields()
'''
pass
def copyJobPlanToWorkPlanCal():
'''public void copyJobPlanToWorkPlanCal()
'''
pass
def copyDSPlanToWO():
'''public void copyDSPlanToWO(final Mbo ds)
'''
pass
def updatePreviousAsLeftValues():
'''public void updatePreviousAsLeftValues()
'''
pass
def isTolWarning():
'''public boolean isTolWarning()
'''
pass
def canEditAsset():
'''public boolean canEditAsset()
'''
pass
def changeStatusCal():
'''public void changeStatusCal(final String status, final Date date, final String memo, final long accessModifier, final boolean comingFromReceiving)
'''
pass
def managePlusCNextDate():
'''public void managePlusCNextDate()
'''
pass
def getLoopRotAsset():
'''public MboRemote getLoopRotAsset(final MboRemote toolMbo)
'''
pass
def validateRotatingAsset():
'''public boolean validateRotatingAsset(final MboRemote toolMbo)
'''
pass
def generateWORelRecord():
'''public void generateWORelRecord(final WORemote oldWO)
'''
pass
def checkWorkPackStatus():
'''public void checkWorkPackStatus()
'''
pass
def parentMbo():
'''public MboRemote parentMbo(final String wonum)
'''
pass
def updateHierarchyWPStatus():
'''public MboRemote updateHierarchyWPStatus(final MboRemote parentMbo, final MboRemote mainMbo, final String previousParentValue, final Boolean parentChanged)
'''
pass
def refreshWorkPackHierarchy():
'''public void refreshWorkPackHierarchy()
public void refreshWorkPackHierarchy(final WORemote mbo)
'''
pass
def setPMWOCancelUserListResponse():
'''public void setPMWOCancelUserListResponse(final boolean response)
'''
pass
def getPMWOCancelUserListResponse():
'''public boolean getPMWOCancelUserListResponse()
'''
pass
def canDeleteAttachedDocs():
'''public void canDeleteAttachedDocs()
'''
pass
def getWOServiceAddress():
'''public WOServiceAddressRemote getWOServiceAddress()
'''
pass
def hasServiceAddress():
'''public boolean hasServiceAddress()
'''
pass
def getServiceAddress():
'''public WOServiceAddressRemote getServiceAddress()
'''
pass
def getLatitudeY():
'''public Double getLatitudeY()
'''
pass
def getLongitudeX():
'''public Double getLongitudeX()
'''
pass
def getAddressString():
'''public String getAddressString()
'''
pass
def saveGISData():
'''public void saveGISData(final String address, final String lat, final String lng)
'''
pass
def isGISDataReadonly():
'''public boolean isGISDataReadonly()
'''
pass
def updateChildrensServiceAddress():
'''public void updateChildrensServiceAddress(final WO currentWO)
'''
pass
def getAmCrewLabor():
'''public MboRemote getAmCrewLabor(final String laborCode, final String laborOrg)
'''
pass
def getAmCrew():
'''public MboRemote getAmCrew(final String crew, final String laborOrg)
'''
pass
def getAmCrewLaborSet():
'''public MboSetRemote getAmCrewLaborSet(final String crew, final String laborOrg)
'''
pass
def isMobileCrew():
'''public boolean isMobileCrew(final String laborCode, final String laborOrg)
'''
pass
def isCrew():
'''public boolean isCrew(final String laborCode, final String laborOrg)
'''
pass
def createToolTransEveryplace():
'''public void createToolTransEveryplace(final MboRemote labTransMbo)
'''
pass
def getAmCrewToolSet():
'''public MboSetRemote getAmCrewToolSet(final String crew)
'''
pass
def getAutoLocateObject():
'''public MboRemote getAutoLocateObject()
public MboRemote getAutoLocateObject(final AutoLocatable nextInChain)
'''
pass
def hasCoords():
'''public Boolean hasCoords()
'''
pass
def setClearLBSLocation():
'''public void setClearLBSLocation(final boolean setLocation)
'''
pass
def setPMWOCancelUserMainAndChildren():
'''public void setPMWOCancelUserMainAndChildren(final int response)
'''
pass
def getPMWOCancelUserMainAndChildren():
'''public int getPMWOCancelUserMainAndChildren()
'''
pass
def setWoOwnerDuringStatusChange():
'''public void setWoOwnerDuringStatusChange(final MboRemote parentWO)
'''
pass
def getWoOwnerDuringStatusChange():
'''public MboRemote getWoOwnerDuringStatusChange()
'''
pass
def checkForActiveLabTrans():
'''public boolean checkForActiveLabTrans()
'''
pass
def copyCrewTypeToWpLaborSet():
'''public void copyCrewTypeToWpLaborSet(final MboSetRemote crewTypeSet)
'''
pass
def setStoreroomStatusWOGen():
'''public MTLStatus setStoreroomStatusWOGen(final boolean changeStatus)
'''
pass
def setDirectIssueStatusWOGen():
'''public MTLStatus setDirectIssueStatusWOGen()
'''
pass
def checkSynonymStatusDate():
'''public void checkSynonymStatusDate(final String status, Date date)
'''
pass
def getTargStartDate():
'''public Date getTargStartDate(final Date date, final String calledFromFlag)
'''
pass
def getPMNextDate():
'''public Date getPMNextDate(final Date date, final String calledFromFlag)
'''
pass
def getPMExtDate():
'''public Date getPMExtDate(final Date date, final String calledFromFlag)
'''
pass
def getSharedMatUseTransSet():
'''public MboSetRemote getSharedMatUseTransSet(final MboRemote wpm)
'''
pass
def isFullyIssued():
'''public boolean isFullyIssued(final MboRemote wpm)
'''
pass
def ProcessParentInVector():
'''public void ProcessParentInVector(final MboRemote currentParent)
'''
pass
def isPartiallyIssued():
'''public boolean isPartiallyIssued(final MboRemote wpm)
'''
pass
def hasUndeleteFRCompleted():
'''public boolean hasUndeleteFRCompleted()
'''
pass
def fireEvent():
'''public synchronized void fireEvent(final String type)
'''
pass
def getAvailableLabor():
'''public MboSetRemote getAvailableLabor()
'''
pass
def setChangeStatusSet():
'''public void setChangeStatusSet(final MboSetRemote changeStatusSet)
'''
pass
def getChangeStatusSet():
'''public MboSetRemote getChangeStatusSet()
'''
pass
def canCreateRelatedRecord():
'''public boolean canCreateRelatedRecord()
'''
pass
def setTopWOInWOGen():
'''public void setTopWOInWOGen(final MboRemote topWO)
'''
pass
def getTopWOInWOGen():
'''public MboRemote getTopWOInWOGen()
'''
pass
def getUnCommittedWOs():
'''public Vector getUnCommittedWOs()
'''
pass
def storeUnCommittedWOs():
'''public void storeUnCommittedWOs(final MboRemote childWO)
'''
pass
def setAsyncChangeStatus():
'''public void setAsyncChangeStatus()
'''
pass
def isAsyncStatusChange():
'''public boolean isAsyncStatusChange()
'''
pass
def setAppDefaultValue():
'''public void setAppDefaultValue()
'''
pass
def initMXYesNoHash():
'''public void initMXYesNoHash(final HashMap<String, MXApplicationYesNoCancelException> hash)
'''
pass
def getMXYesNoHash():
'''public HashMap<String, MXApplicationYesNoCancelException> getMXYesNoHash()
'''
pass
def setMustApplyDJP():
'''public void setMustApplyDJP(final boolean mustApplyDJP)
'''
pass
def mustApplyDJP():
'''public boolean mustApplyDJP()
'''
pass
def calculateDynamicJobPlan():
'''public void calculateDynamicJobPlan()
'''
pass
def mustApplyLinearCalculation():
'''public boolean mustApplyLinearCalculation()
'''
pass
def calculateTotalWorkUnitsFor():
'''public void calculateTotalWorkUnitsFor(final MboRemote multiAssetLocCI, final String unitOfWork)
'''
pass
def calculateTotalWorkUnits():
'''public void calculateTotalWorkUnits()
'''
pass
def isCalculationAppliedSuccessfully():
'''public boolean isCalculationAppliedSuccessfully()
'''
pass
def getWorkLog():
'''public MboSetRemote getWorkLog()
'''
pass
def getWoHazardPrecHashMap():
'''public Map getWoHazardPrecHashMap()
'''
pass
def incrementWoHazardPrecHashMap():
'''public void incrementWoHazardPrecHashMap(final String precautionid)
'''
pass
def decrementWoHazardPrecHashMap():
'''public void decrementWoHazardPrecHashMap(final String precautionid)
'''
pass
def compareJPTask():
'''public compareJPTask()
'''
pass
def compare():
'''public int compare(final MboRemote m1, final MboRemote m2)
'''
pass
