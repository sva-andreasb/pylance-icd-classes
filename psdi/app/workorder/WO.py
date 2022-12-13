crewDurStatic = "String  \"Static\""
crewDurDynamic = "String  \"Dynamic\""
crewDurCrewPos = "String  \"PLUSDCRW\""
APPLYASSETLOC = "String  \"WO.ApplyingAssetLoc\""
def isChangeInHierarchy():
    '''public boolean isChangeInHierarchy()
    '''
def setChangeInHierarchy():
    '''public void setChangeInHierarchy(final boolean changeInHierarchy)
    '''
def getPreviousParent():
    '''public String getPreviousParent()
    '''
def setPreviousParent():
    '''public void setPreviousParent(final String previousParent)
    '''
def WO():
    '''public WO(final MboSet ms)
    '''
def getProcess():
    '''public String getProcess()
    '''
def getStatusListName():
    '''public String getStatusListName()
    '''
def init():
    '''public void init()
    '''
def isCharacteristic():
    '''public boolean isCharacteristic()
    '''
def canEditRelatedSet():
    '''public void canEditRelatedSet(final String relationName)
    '''
def setRelatedMboEditibility():
    '''public void setRelatedMboEditibility(final String relationName)
    '''
def initRelationship():
    '''public void initRelationship(final String relationName, final MboSetRemote mboSet)
    '''
def modify():
    '''public void modify()
    '''
def add():
    '''public void add()
    '''
def updateServiceAddress():
    '''public void updateServiceAddress()
    '''
def createJobEntry():
    '''public MboRemote createJobEntry()
    '''
def createAssignRepLoc():
    '''public void createAssignRepLoc()
    '''
def getCrewMemberCount():
    '''public int getCrewMemberCount(final Date desiredDate)
    '''
def copyDoclinksToWO():
    '''public void copyDoclinksToWO()
    public void copyDoclinksToWO(final WO wo)
    '''
def inChildSubSet():
    '''public boolean inChildSubSet()
    '''
def canDelete():
    '''public void canDelete()
    '''
def getSimilarWorkOrders():
    '''public WOSetRemote getSimilarWorkOrders()
    '''
def getAlreadyReportedSet():
    '''public WOSetRemote getAlreadyReportedSet()
    '''
def getLocForAsset():
    '''public void getLocForAsset()
    '''
def applyAssetLoc():
    '''public void applyAssetLoc()
    public void applyAssetLoc(final boolean calcSafetyPlan)
    '''
def copyJobPlanToWorkPlan():
    '''public void copyJobPlanToWorkPlan()
    '''
def copyJobPlanToWorkPlanNoNestedJP():
    '''public void copyJobPlanToWorkPlanNoNestedJP()
    '''
def clearWorkPlanInfo():
    '''public void clearWorkPlanInfo()
    '''
def calculateConstaintDates():
    '''public void calculateConstaintDates(final MboValue startOffset, final MboValue finishOffset, final MboValue woDur)
    '''
def getWoTaskLookup():
    '''public Map<String, Mbo> getWoTaskLookup()
    '''
def getAddingFirstJobTask():
    '''public boolean getAddingFirstJobTask()
    '''
def getCopyingJobTasks():
    '''public boolean getCopyingJobTasks()
    '''
def getCopyingWorkPlanAssignments():
    '''public boolean getCopyingWorkPlanAssignments()
    '''
def applyingJobPlan():
    '''public boolean applyingJobPlan()
    '''
def setParentValuesForNestedjpWO():
    '''public void setParentValuesForNestedjpWO(final MboRemote newChild, final MboRemote parent)
    '''
def generateTaskID():
    '''public void generateTaskID()
    '''
def copySafetyPlanToWoSafetyPlan():
    '''public void copySafetyPlanToWoSafetyPlan()
    '''
def setJobPlanFieldFlag():
    '''public void setJobPlanFieldFlag()
    '''
def startWFOnWoReqSave():
    '''public boolean startWFOnWoReqSave()
    '''
def updateForMovedAsset():
    '''public void updateForMovedAsset(final MboRemote movedAsset)
    '''
def incrEstLabCost():
    '''public void incrEstLabCost(final double incrAmount, final boolean isExternal)
    '''
def incrEstLabHours():
    '''public void incrEstLabHours(final double incrAmount, final boolean isExternal)
    '''
def incrEstToolCost():
    '''public void incrEstToolCost(final double incrAmount)
    '''
def incrEstMatCost():
    '''public void incrEstMatCost(final double incrAmount)
    '''
def incrEstServCost():
    '''public void incrEstServCost(final double incrAmount)
    '''
def incrActMatCost():
    '''public void incrActMatCost(final double incrAmount, final boolean isOutsideCost)
    '''
def incrActLabCost():
    '''public void incrActLabCost(final double incrAmount, final boolean isOutsideCost)
    '''
def incrActLabHrs():
    '''public void incrActLabHrs(final double incrAmount, final boolean isExternal)
    '''
def incrActToolCost():
    '''public void incrActToolCost(final double incrAmount, final boolean isOutsideCost)
    '''
def incrActServCost():
    '''public void incrActServCost(final double incrAmount)
    '''
def haveReceivedDirectIssue():
    '''public void haveReceivedDirectIssue(final MboRemote poMbo, final MboRemote poLineMbo)
    '''
def getValidateOrder():
    '''public String[] getValidateOrder()
    '''
def isCanceled():
    '''public boolean isCanceled()
    '''
def generateAutoKey():
    '''public void generateAutoKey()
    '''
def isAssetChargeStore():
    '''public boolean isAssetChargeStore()
    '''
def canChargeStore():
    '''public boolean canChargeStore()
    '''
def calcGLAccount():
    '''public void calcGLAccount()
    '''
def getSubWorkOrders():
    '''public MboSetRemote getSubWorkOrders()
    '''
def canApplyRoute():
    '''public void canApplyRoute()
    public void canApplyRoute(final long accessModifier)
    public void canApplyRoute(final String routeID)
    public void canApplyRoute(final String routeID, final long accessModifier)
    '''
def applyRoute():
    '''public void applyRoute(final String routeID, final String storeLoc)
    public void applyRoute(final String routeID, final String storeLoc, final String storeLocSite)
    public void applyRoute(final String routeID, final String storeLoc, final String storeLocSite, final long accessModifier)
    public void applyRoute(final String routeID, final String storeLoc, final String storeLocSite, final long accessModifier, final MboSetRemote infoSet)
    '''
def getGrandTotals():
    '''public Vector getGrandTotals()
    '''
def getDuplicated():
    '''public boolean getDuplicated()
    '''
def setDuplicated():
    '''public void setDuplicated(final boolean duplicated)
    '''
def duplicate():
    '''public MboRemote duplicate()
    '''
def canGenFollowUpWo():
    '''public void canGenFollowUpWo()
    '''
def genFollowUpWo():
    '''public MboRemote genFollowUpWo()
    '''
def setSafetyPlanFieldFlag():
    '''public void setSafetyPlanFieldFlag()
    '''
def getServiceTotal():
    '''public double getServiceTotal()
    '''
def isTop():
    '''public boolean isTop()
    '''
def hasChildren():
    '''public boolean hasChildren()
    '''
def hasParents():
    '''public boolean hasParents()
    '''
def hasSafetyPlan():
    '''public boolean hasSafetyPlan()
    '''
def getChildren():
    '''public MboSetRemote getChildren()
    '''
def getChildNoTask():
    '''public MboSetRemote getChildNoTask()
    '''
def getTasksOnly():
    '''public MboSetRemote getTasksOnly()
    '''
def getParents():
    '''public MboSetRemote getParents()
    '''
def getTop():
    '''public MboSetRemote getTop()
    '''
def getHierarchies():
    '''public String[] getHierarchies()
    '''
def copySparePartsToWpMatSet():
    '''public void copySparePartsToWpMatSet(final MboSetRemote sparePartSet)
    '''
def copySparePartsToMatUseSet():
    '''public void copySparePartsToMatUseSet(final MboSetRemote sparePartSet)
    '''
def copyInvresvItemsToMatUseSet():
    '''public void copyInvresvItemsToMatUseSet(final MboSetRemote InvresvItemSet)
    '''
def copyPlanToolToToolTransSet():
    '''public void copyPlanToolToToolTransSet(final MboSetRemote planToolSet)
    '''
def copyPlanLaborToLabTransSet():
    '''public void copyPlanLaborToLabTransSet(final MboSetRemote planLaborSet)
    '''
def applyHazardToWoHazardSet():
    '''public void applyHazardToWoHazardSet(final MboRemote spRelatedasset, final MboSetRemote hazardSet)
    '''
def enterQuickReportingMode():
    '''public void enterQuickReportingMode()
    '''
def isQuickReportingMode():
    '''public boolean isQuickReportingMode()
    '''
def isApproved():
    '''public boolean isApproved()
    '''
def getTaskForWonum():
    '''public String getTaskForWonum(final String wonum)
    '''
def getWOforTask():
    '''public MboRemote getWOforTask(final String task)
    '''
def getWOforWonum():
    '''public WORemote getWOforWonum(final String wonum)
    '''
def getWOClassDescription():
    '''public String getWOClassDescription(final MboRemote theMboRemote)
    '''
def changeWorkOrderParent():
    '''public void changeWorkOrderParent(final MboRemote woparent)
    '''
def changeStatus():
    '''public void changeStatus(final String status, final Date date, final String memo, final long accessModifier)
    public void changeStatus(final String status, final Date date, final String memo, final long accessModifier, final boolean comingFromReceiving)
    '''
def changeChildrenStatus():
    '''public void changeChildrenStatus()
    '''
def getParentMbo():
    '''public WO getParentMbo()
    '''
def getWoFromCombined():
    '''public WORemote getWoFromCombined(final String findWonum)
    '''
def canRemoveSafetyPlan():
    '''public void canRemoveSafetyPlan()
    '''
def removeSafetyPlan():
    '''public void removeSafetyPlan()
    '''
def canReportDowntime():
    '''public void canReportDowntime()
    '''
def getOwnSet():
    '''public MboSetRemote getOwnSet()
    '''
def setAttrFromWoGen():
    '''public void setAttrFromWoGen(final MboRemote woGen)
    '''
def getECommHelperRemote():
    '''public ECommHelperRemote getECommHelperRemote()
    '''
def editHistory():
    '''public void editHistory()
    '''
def isWOInEditHist():
    '''public boolean isWOInEditHist()
    '''
def propagateKeyValue():
    '''public void propagateKeyValue(final String keyName, final String keyValue)
    '''
def getPM():
    '''public PMRemote getPM()
    '''
def getAsset():
    '''public AssetRemote getAsset()
    '''
def delete():
    '''public void delete()
    public void delete(final long accessModifier)
    '''
def undelete():
    '''public void undelete()
    '''
def getFailListForReport():
    '''public MboSetRemote getFailListForReport()
    '''
def copyFailListToReportSet():
    '''public void copyFailListToReportSet(final MboSetRemote failListSet)
    '''
def copyLaborToWpLaborSet():
    '''public void copyLaborToWpLaborSet(final MboSetRemote laborSet)
    '''
def copyCraftRateToWpLaborSet():
    '''public void copyCraftRateToWpLaborSet(final MboSetRemote craftRateSet)
    '''
def copyLaborToLabTransSet():
    '''public void copyLaborToLabTransSet(final MboSetRemote laborSet)
    '''
def copyItemToWpMatSet():
    '''public void copyItemToWpMatSet(final MboSetRemote itemSet)
    '''
def copyServiceItemsToWpSerSet():
    '''public void copyServiceItemsToWpSerSet(final MboSetRemote serviceItemSet)
    '''
def copyItemToMatUseTransSet():
    '''public void copyItemToMatUseTransSet(final MboSetRemote itemSet)
    '''
def copyToolToWpToolSet():
    '''public void copyToolToWpToolSet(final MboSetRemote toolSet)
    '''
def copyMatUseTransToToolTransSet():
    '''public void copyMatUseTransToToolTransSet(final MboSetRemote matUseTransSet)
    '''
def copyToolToToolTransSet():
    '''public void copyToolToToolTransSet(final MboSetRemote toolSet)
    '''
def copyMRLineToPlanMaterialSet():
    '''public void copyMRLineToPlanMaterialSet(final MboSetRemote mrLineSet)
    '''
def getMboSet():
    '''public MboSetRemote getMboSet(String name)
    '''
def getPOTotal():
    '''public double getPOTotal()
    '''
def getPRTotal():
    '''public double getPRTotal()
    '''
def makeSelectedChildren():
    '''public void makeSelectedChildren(final MboSetRemote selectSet)
    public void makeSelectedChildren(final MboSetRemote selectSet, String dialogLabel)
    '''
def canRemoveWorkPlan():
    '''public void canRemoveWorkPlan()
    '''
def removeWorkPlan():
    '''public boolean removeWorkPlan()
    '''
def hasActuals():
    '''public boolean hasActuals()
    '''
def hasPlanMoveModify():
    '''public boolean hasPlanMoveModify()
    '''
def removeFailureReport():
    '''public void removeFailureReport()
    '''
def promptForDowntimeReport():
    '''public boolean promptForDowntimeReport(final String newStatus)
    '''
def promptForFailureReport():
    '''public boolean promptForFailureReport(final String newStatus)
    '''
def createJPFromWO():
    '''public MboRemote createJPFromWO(final String jpnum, final String description, final String longdescription)
    public MboRemote createJPFromWO(final Date date, final String jpnum, final String description, final String longdescription)
    '''
def createJPHeaderFromWO():
    '''public Mbo createJPHeaderFromWO(final String jpnum, final String description, final String longdescription)
    '''
def createWorkorder():
    '''public MboRemote createWorkorder()
    public MboRemote createWorkorder(final String jpnum)
    public MboRemote createWorkorder(final MboSetRemote workorderSet)
    public MboRemote createWorkorder(final MboSetRemote workorderSet, final String jpnum, final boolean saveSet)
    '''
def createChange():
    '''public MboRemote createChange()
    public MboRemote createChange(final String jpnum)
    '''
def createRelease():
    '''public MboRemote createRelease()
    public MboRemote createRelease(final String jpnum)
    '''
def createServiceRequest():
    '''public MboRemote createServiceRequest()
    public MboRemote createServiceRequest(final String tickettemplateid)
    '''
def createProblem():
    '''public MboRemote createProblem()
    public MboRemote createProblem(final String tickettemplateid)
    '''
def createIncident():
    '''public MboRemote createIncident()
    public MboRemote createIncident(final String tickettemplateid)
    '''
def orphan():
    '''public void orphan()
    '''
def handleChildren():
    '''public void handleChildren()
    '''
def handleTasks():
    '''public void handleTasks()
    '''
def handleUndeleteTasks():
    '''public void handleUndeleteTasks()
    '''
def handleUndeleteChildren():
    '''public void handleUndeleteChildren()
    '''
def deleteChildren():
    '''public void deleteChildren(final boolean task)
    '''
def undeleteChildren():
    '''public void undeleteChildren(final boolean task)
    '''
def isWoAcceptsChargesEditable():
    '''public boolean isWoAcceptsChargesEditable()
    '''
def getTaskIdsThatAcceptCharges():
    '''public String getTaskIdsThatAcceptCharges()
    '''
def pmAlertStatus():
    '''public MboSetRemote pmAlertStatus(final String status)
    '''
def pmAlert():
    '''public MboSetRemote pmAlert()
    '''
def getStatus():
    '''public String getStatus(final String status)
    '''
def woCancel():
    '''public boolean woCancel()
    '''
def canEnterMeterReadings():
    '''public void canEnterMeterReadings()
    '''
def startTimer():
    '''public void startTimer()
    public void startTimer(final Date startdatetime, final Long anywhererefid, final String transtype)
    '''
def stopTimer():
    '''public void stopTimer()
    public MboRemote stopTimer(final Date finishdatetime, final boolean noStopTimerPopup)
    public MboRemote stopTimer(final Date finishdatetime, final Date startDateTime, final boolean noStopTimerPopup)
    '''
def getStopTimerLabtrans():
    '''public MboRemote getStopTimerLabtrans()
    '''
def needPopupOnStopTimer():
    '''public boolean needPopupOnStopTimer()
    '''
def updateWorkview():
    '''public void updateWorkview()
    '''
def clearClassification():
    '''public void clearClassification()
    '''
def applyOwner():
    '''public void applyOwner(final String ownerID)
    '''
def applyOwnerGroup():
    '''public void applyOwnerGroup(final String ownergroupID)
    '''
def applyAssignedOwnerGroup():
    '''public void applyAssignedOwnerGroup(final String ownergroupID)
    '''
def ownership():
    '''public void ownership()
    '''
def copyAssetSpecToAutoAttrUpdateSet():
    '''public void copyAssetSpecToAutoAttrUpdateSet(final MboSetRemote assetspecset, final MboRemote woasset)
    '''
def copyLocSpecToAutoAttrUpdateSet():
    '''public void copyLocSpecToAutoAttrUpdateSet(final MboSetRemote locspecset, final MboRemote woasset)
    '''
def copyCISpecToAutoAttrUpdateSet():
    '''public void copyCISpecToAutoAttrUpdateSet(final MboSetRemote cispecset, final MboRemote woasset)
    '''
def applyToAllAssetLoc():
    '''public void applyToAllAssetLoc(final MboRemote attrupdate)
    '''
def copyAssets():
    '''public void copyAssets(final MboSetRemote assetset)
    '''
def copyLocations():
    '''public void copyLocations(final MboSetRemote locationset)
    '''
def moveModifyAssets():
    '''public void moveModifyAssets()
    public boolean moveModifyAssets(final boolean checkonly)
    '''
def moveAllAssets():
    '''public void moveAllAssets()
    '''
def modifyAllAssetLocationAttributes():
    '''public void modifyAllAssetLocationAttributes()
    '''
def removeUserCust():
    '''public void removeUserCust()
    public void removeUserCust(final boolean removeAssetUserCustPlans, final boolean removeLocUserCustPlans)
    public void removeUserCust(final boolean removeAssetUserCustPlans, final boolean removeLocUserCustPlans, final MboRemote multiassetlocci)
    '''
def restoreUserCust():
    '''public void restoreUserCust()
    public void restoreUserCust(final MboRemote multiassetlocci)
    '''
def clearMoveandDeleteAttrUpdate():
    '''public void clearMoveandDeleteAttrUpdate()
    '''
def clearMoveAssetFields():
    '''public void clearMoveAssetFields()
    '''
def updateWarrantyContracts():
    '''public void updateWarrantyContracts()
    '''
def getServiceContractInClause():
    '''public String getServiceContractInClause()
    '''
def getWODate():
    '''public Date getWODate()
    '''
def userVerifiedRemoveSafetyPlan():
    '''public boolean userVerifiedRemoveSafetyPlan()
    '''
def getSafetyPlanID():
    '''public String getSafetyPlanID()
    '''
def copyTicketToRelatedRecSet():
    '''public void copyTicketToRelatedRecSet(final MboSetRemote TicketSet)
    public void copyTicketToRelatedRecSet(final MboSetRemote TicketSet, final boolean copyToParent)
    '''
def copyTicketParentToRelatedRecSet():
    '''public void copyTicketParentToRelatedRecSet(final MboSetRemote TicketSet)
    '''
def copyWOToRelatedRecSet():
    '''public void copyWOToRelatedRecSet(final MboSetRemote woSet)
    public void copyWOToRelatedRecSet(final MboSetRemote woSet, final boolean copyToParent)
    '''
def copyWOParentToRelatedRecSet():
    '''public void copyWOParentToRelatedRecSet(final MboSetRemote woSet)
    '''
def copyParentValuesToRelatedRec():
    '''public void copyParentValuesToRelatedRec(final MboRemote relatedMbo)
    '''
def updateOriginator():
    '''public void updateOriginator()
    '''
def getWOObjectName():
    '''public String getWOObjectName()
    '''
def getRecordMboName():
    '''public String getRecordMboName()
    '''
def setHashForSelectedRecord():
    '''public void setHashForSelectedRecord(final HashSet hs)
    '''
def getHashForSelectedRecord():
    '''public HashSet getHashForSelectedRecord()
    '''
def clearHashForSelectedRecord():
    '''public void clearHashForSelectedRecord()
    '''
def relateWorkorders():
    '''public MboSetRemote relateWorkorders(final MboSetRemote woSet)
    '''
def relateTickets():
    '''public MboSetRemote relateTickets(final MboSetRemote ticketSet)
    '''
def copyAssetsToMultiAsset():
    '''public void copyAssetsToMultiAsset(final AssetSetRemote assetSetRemote)
    '''
def copyLocationsToMultiAsset():
    '''public void copyLocationsToMultiAsset(final MboSetRemote locationSetRemote)
    '''
def checkNestedJobPlans():
    '''public boolean checkNestedJobPlans()
    '''
def setRemoveWorkPlan():
    '''public void setRemoveWorkPlan(final boolean removeChildFlag)
    '''
def getRemoveWorkPlan():
    '''public boolean getRemoveWorkPlan()
    '''
def copyCIsToMultiAsset():
    '''public void copyCIsToMultiAsset(final MboSetRemote ciSetRemote)
    '''
def copyRouteStopsToMultiAsset():
    '''public void copyRouteStopsToMultiAsset(final MboSetRemote routestopSetRemote)
    '''
def copyCollectDetailsToMultiAsset():
    '''public void copyCollectDetailsToMultiAsset(final MboSetRemote routestopSetRemote)
    '''
def appValidate():
    '''public void appValidate()
    '''
def setmultiassetrecord():
    '''public void setmultiassetrecord()
    '''
def copyWOFieldsToMultiAsset():
    '''public void copyWOFieldsToMultiAsset(final MultiAssetLocCIRemote multiAssetMbo)
    '''
def isLicensePresent():
    '''public static boolean isLicensePresent(final String lic)
    '''
def getFlowControlState():
    '''public int getFlowControlState()
    public int getFlowControlState(final WO wo, final String status)
    '''
def isFlowControlComplete():
    '''public boolean isFlowControlComplete()
    public boolean isFlowControlComplete(final WO wo, final String status)
    '''
def getStartStatusForWorkType():
    '''public String getStartStatusForWorkType()
    public String getStartStatusForWorkType(final WO wo)
    '''
def getCompleteStatusForWorkType():
    '''public String getCompleteStatusForWorkType()
    public String getCompleteStatusForWorkType(final WO wo)
    '''
def getPredecessors():
    '''public Vector getPredecessors()
    '''
def getSuccessors():
    '''public Vector getSuccessors()
    '''
def getChildrenThatHaveNoPredecessors():
    '''public Vector getChildrenThatHaveNoPredecessors()
    '''
def suspendChildrensProcessFlow():
    '''public void suspendChildrensProcessFlow(final boolean torf)
    '''
def setChildrensFlowControl():
    '''public void setChildrensFlowControl(final boolean torf)
    '''
def changeChildrensFieldValue():
    '''public void changeChildrensFieldValue(final String fieldname, final String fieldvalue, final long accessModifier)
    '''
def executeProcessFlowControlAction():
    '''public void executeProcessFlowControlAction()
    '''
def changeStatusProcessFlowControl():
    '''public void changeStatusProcessFlowControl()
    '''
def startSuccessors():
    '''public boolean startSuccessors(final Mbo mbo, final Vector successors, final Date date, final String memo, final long accessModifier)
    '''
def adjustSuccVectors():
    '''public void adjustSuccVectors(final Vector existingSuccs, final Vector newSuccs)
    '''
def areAllPredecessorsComplete():
    '''public boolean areAllPredecessorsComplete()
    public boolean areAllPredecessorsComplete(final WO wo)
    public boolean areAllPredecessorsComplete(final String targetStatus, final boolean fully)
    public boolean areAllPredecessorsComplete(final WO wo, final String targetStatus, final boolean fully)
    '''
def areAllPredecessorsSufficientlyComplete():
    '''public boolean areAllPredecessorsSufficientlyComplete(final WO wo, final String targetStatus)
    '''
def getContemplatedAction():
    '''public int getContemplatedAction(final WO wo, final String targetStatus)
    '''
def isSufficientlyFlowControlComplete():
    '''public boolean isSufficientlyFlowControlComplete(final WO wo, final String reltypeToSuccessor, final int contemplatedAction)
    public boolean isSufficientlyFlowControlComplete(final WO wo, final String status, final String reltypeToSuccessor, final int contemplatedAction)
    '''
def getChildPFCOrder():
    '''public Vector getChildPFCOrder(final boolean getChildrenWOs, final boolean appendSiteid)
    '''
def findPredecessorPosition():
    '''public int findPredecessorPosition(final Vector vector2Search, final String wonum, final Hashtable htNetwork)
    '''
def bulkReschedule():
    '''public void bulkReschedule(final boolean resched, final Date reschedDate, final boolean fromListTab)
    public void bulkReschedule(final boolean resched, final Date reschedDate)
    '''
def getRescheduled():
    '''public int getRescheduled()
    '''
def getUnassigned():
    '''public int getUnassigned()
    '''
def unassignWOAssignments():
    '''public void unassignWOAssignments(AssignmentSet assignSet, final Date reschedDate)
    '''
def unassignAssignments():
    '''public void unassignAssignments(final AssignmentSet assignSet, final Date reschedDate)
    '''
def rescheduleAssignments():
    '''public void rescheduleAssignments(AssignmentSet assignSet, final Date reschedDate, final boolean fromListTab)
    public void rescheduleAssignments(final AssignmentSet assignSet, final Date reschedDate)
    '''
def getLCRSqlFormatHashMap():
    '''public HashMap getLCRSqlFormatHashMap(final AssignmentSet assignSet)
    '''
def calculateScheduleFinishDate():
    '''public Date calculateScheduleFinishDate(final WO wo, final Date schedStartDate)
    '''
def setWOScheduleDates():
    '''public void setWOScheduleDates(final WO wo, Date schedStartDate)
    public void setWOScheduleDates(final WO wo, Date schedStartDate, final double duration)
    '''
def restoreSplitAssignments():
    '''public AssignmentSet restoreSplitAssignments(AssignmentSet assignSet)
    '''
def getToplevelParentAssign():
    '''public Assignment getToplevelParentAssign(Assignment assign, final AssignmentSet assignSet, final HashMap assignIndexMap)
    '''
def removeCompleteStartedAssigns():
    '''public AssignmentSet removeCompleteStartedAssigns(final AssignmentSet assignSet, final HashMap assignIndexMap)
    '''
def applyToAllUser():
    '''public void applyToAllUser(final MboRemote woModUser)
    '''
def setPrimaryLinearAssetFieldsReadOnly():
    '''public void setPrimaryLinearAssetFieldsReadOnly(MultiAssetLocCIRemote multiAssetMbo, final boolean readonlystate)
    '''
def clearPrimaryLinearAssetFields():
    '''public void clearPrimaryLinearAssetFields(final MultiAssetLocCIRemote multiAssetMbo)
    '''
def copyLinearAssetFieldsFromRouteStop():
    '''public void copyLinearAssetFieldsFromRouteStop(final MboRemote toMbo, final MboRemote routestop)
    '''
def setRemoveWorkPlanFlag():
    '''public void setRemoveWorkPlanFlag(final boolean removeWorkplan)
    '''
def getRemoveWorkPlanFlag():
    '''public boolean getRemoveWorkPlanFlag()
    '''
def getTopOwner():
    '''public MboRemote getTopOwner()
    '''
def checkCompStatus():
    '''public void checkCompStatus()
    '''
def doClassificationCreateTicketViews():
    '''public void doClassificationCreateTicketViews(final MboRemote newMbo)
    '''
def doClassificationCreateWOViews():
    '''public void doClassificationCreateWOViews(final MboRemote newMbo)
    '''
def doClassificationCreateWOSpecFromJobPlan():
    '''public void doClassificationCreateWOSpecFromJobPlan(final MboRemote newMbo, final MboRemote sourceMbo)
    '''
def CheckOrigIsFollowup():
    '''public void CheckOrigIsFollowup()
    '''
def clearSkipCopyFields():
    '''public void clearSkipCopyFields()
    '''
def routeStopExists():
    '''public boolean routeStopExists()
    '''
def isListSelected():
    '''public boolean isListSelected()
    '''
def setListSelected():
    '''public void setListSelected(final boolean isListSelected)
    '''
def getCopydocMboSet():
    '''public MboSetRemote getCopydocMboSet(String name)
    '''
def setAvailibilityStatus():
    '''public MTLStatus setAvailibilityStatus(final boolean changeStatus)
    '''
def setStoreroomStatus():
    '''public MTLStatus setStoreroomStatus(final boolean changeStatus)
    '''
def setDirectIssueStatus():
    '''public MTLStatus setDirectIssueStatus()
    '''
def setChildrenStatus():
    '''public MTLStatus setChildrenStatus(final MTLStatus storeroomStatus, final MTLStatus directIssueStatus, final boolean changeStatus)
    '''
def setMaterialAvailStatus():
    '''public MTLStatus setMaterialAvailStatus()
    '''
def smartFillForAllSites():
    '''public MboSetRemote smartFillForAllSites(final String attribute, final String value, final boolean exact)
    '''
def smartFindForAllSites():
    '''public MboSetRemote smartFindForAllSites(final String attribute, final String value, final boolean exact)
    '''
def isRevEnabled():
    '''public boolean isRevEnabled()
    '''
def isCalibrationInstalled():
    '''public boolean isCalibrationInstalled()
    '''
def isFromMobile():
    '''public boolean isFromMobile()
    '''
def setFromMobile():
    '''public void setFromMobile(final boolean isFromMobile)
    '''
def setCompleteWOFromEveryplace():
    '''public void setCompleteWOFromEveryplace(boolean completeWOFromEveryplace)
    '''
def manageCircleEffect():
    '''public void manageCircleEffect(final MboRemote thisToolTrans)
    '''
def getWorkTypeCal():
    '''public String getWorkTypeCal()
    '''
def getTranslatedWorkTypeCal():
    '''public String getTranslatedWorkTypeCal()
    '''
def getJobRevNum():
    '''public String getJobRevNum(final Mbo PlusCWO)
    '''
def isValidJPRevNum():
    '''public boolean isValidJPRevNum(final String jpNum, final String revNum)
    '''
def getWorkType():
    '''public String getWorkType()
    '''
def checkRequiredDatasheets():
    '''public boolean checkRequiredDatasheets()
    '''
def duplicateWODS():
    '''public MboRemote duplicateWODS(final MboRemote newWO)
    '''
def canEditRelatedSetCal():
    '''public void canEditRelatedSetCal(final String relationName)
    '''
def canEditAsFoundAsLeftFields():
    '''public boolean canEditAsFoundAsLeftFields()
    '''
def copyJobPlanToWorkPlanCal():
    '''public void copyJobPlanToWorkPlanCal()
    '''
def copyDSPlanToWO():
    '''public void copyDSPlanToWO(final Mbo ds)
    '''
def updatePreviousAsLeftValues():
    '''public void updatePreviousAsLeftValues()
    '''
def isTolWarning():
    '''public boolean isTolWarning()
    '''
def canEditAsset():
    '''public boolean canEditAsset()
    '''
def changeStatusCal():
    '''public void changeStatusCal(final String status, final Date date, final String memo, final long accessModifier, final boolean comingFromReceiving)
    '''
def managePlusCNextDate():
    '''public void managePlusCNextDate()
    '''
def getLoopRotAsset():
    '''public MboRemote getLoopRotAsset(final MboRemote toolMbo)
    '''
def validateRotatingAsset():
    '''public boolean validateRotatingAsset(final MboRemote toolMbo)
    '''
def generateWORelRecord():
    '''public void generateWORelRecord(final WORemote oldWO)
    '''
def checkWorkPackStatus():
    '''public void checkWorkPackStatus()
    '''
def parentMbo():
    '''public MboRemote parentMbo(final String wonum)
    '''
def updateHierarchyWPStatus():
    '''public MboRemote updateHierarchyWPStatus(final MboRemote parentMbo, final MboRemote mainMbo, final String previousParentValue, final Boolean parentChanged)
    '''
def refreshWorkPackHierarchy():
    '''public void refreshWorkPackHierarchy()
    public void refreshWorkPackHierarchy(final WORemote mbo)
    '''
def setPMWOCancelUserListResponse():
    '''public void setPMWOCancelUserListResponse(final boolean response)
    '''
def getPMWOCancelUserListResponse():
    '''public boolean getPMWOCancelUserListResponse()
    '''
def canDeleteAttachedDocs():
    '''public void canDeleteAttachedDocs()
    '''
def getWOServiceAddress():
    '''public WOServiceAddressRemote getWOServiceAddress()
    '''
def hasServiceAddress():
    '''public boolean hasServiceAddress()
    '''
def getServiceAddress():
    '''public WOServiceAddressRemote getServiceAddress()
    '''
def getLatitudeY():
    '''public Double getLatitudeY()
    '''
def getLongitudeX():
    '''public Double getLongitudeX()
    '''
def getAddressString():
    '''public String getAddressString()
    '''
def saveGISData():
    '''public void saveGISData(final String address, final String lat, final String lng)
    '''
def isGISDataReadonly():
    '''public boolean isGISDataReadonly()
    '''
def updateChildrensServiceAddress():
    '''public void updateChildrensServiceAddress(final WO currentWO)
    '''
def getAmCrewLabor():
    '''public MboRemote getAmCrewLabor(final String laborCode, final String laborOrg)
    '''
def getAmCrew():
    '''public MboRemote getAmCrew(final String crew, final String laborOrg)
    '''
def getAmCrewLaborSet():
    '''public MboSetRemote getAmCrewLaborSet(final String crew, final String laborOrg)
    '''
def isMobileCrew():
    '''public boolean isMobileCrew(final String laborCode, final String laborOrg)
    '''
def isCrew():
    '''public boolean isCrew(final String laborCode, final String laborOrg)
    '''
def createToolTransEveryplace():
    '''public void createToolTransEveryplace(final MboRemote labTransMbo)
    '''
def getAmCrewToolSet():
    '''public MboSetRemote getAmCrewToolSet(final String crew)
    '''
def getAutoLocateObject():
    '''public MboRemote getAutoLocateObject()
    public MboRemote getAutoLocateObject(final AutoLocatable nextInChain)
    '''
def hasCoords():
    '''public Boolean hasCoords()
    '''
def setClearLBSLocation():
    '''public void setClearLBSLocation(final boolean setLocation)
    '''
def setPMWOCancelUserMainAndChildren():
    '''public void setPMWOCancelUserMainAndChildren(final int response)
    '''
def getPMWOCancelUserMainAndChildren():
    '''public int getPMWOCancelUserMainAndChildren()
    '''
def setWoOwnerDuringStatusChange():
    '''public void setWoOwnerDuringStatusChange(final MboRemote parentWO)
    '''
def getWoOwnerDuringStatusChange():
    '''public MboRemote getWoOwnerDuringStatusChange()
    '''
def checkForActiveLabTrans():
    '''public boolean checkForActiveLabTrans()
    '''
def copyCrewTypeToWpLaborSet():
    '''public void copyCrewTypeToWpLaborSet(final MboSetRemote crewTypeSet)
    '''
def setStoreroomStatusWOGen():
    '''public MTLStatus setStoreroomStatusWOGen(final boolean changeStatus)
    '''
def setDirectIssueStatusWOGen():
    '''public MTLStatus setDirectIssueStatusWOGen()
    '''
def checkSynonymStatusDate():
    '''public void checkSynonymStatusDate(final String status, Date date)
    '''
def getTargStartDate():
    '''public Date getTargStartDate(final Date date, final String calledFromFlag)
    '''
def getPMNextDate():
    '''public Date getPMNextDate(final Date date, final String calledFromFlag)
    '''
def getPMExtDate():
    '''public Date getPMExtDate(final Date date, final String calledFromFlag)
    '''
def getSharedMatUseTransSet():
    '''public MboSetRemote getSharedMatUseTransSet(final MboRemote wpm)
    '''
def isFullyIssued():
    '''public boolean isFullyIssued(final MboRemote wpm)
    '''
def ProcessParentInVector():
    '''public void ProcessParentInVector(final MboRemote currentParent)
    '''
def isPartiallyIssued():
    '''public boolean isPartiallyIssued(final MboRemote wpm)
    '''
def hasUndeleteFRCompleted():
    '''public boolean hasUndeleteFRCompleted()
    '''
def fireEvent():
    '''public synchronized void fireEvent(final String type)
    '''
def getAvailableLabor():
    '''public MboSetRemote getAvailableLabor()
    '''
def setChangeStatusSet():
    '''public void setChangeStatusSet(final MboSetRemote changeStatusSet)
    '''
def getChangeStatusSet():
    '''public MboSetRemote getChangeStatusSet()
    '''
def canCreateRelatedRecord():
    '''public boolean canCreateRelatedRecord()
    '''
def setTopWOInWOGen():
    '''public void setTopWOInWOGen(final MboRemote topWO)
    '''
def getTopWOInWOGen():
    '''public MboRemote getTopWOInWOGen()
    '''
def getUnCommittedWOs():
    '''public Vector getUnCommittedWOs()
    '''
def storeUnCommittedWOs():
    '''public void storeUnCommittedWOs(final MboRemote childWO)
    '''
def setAsyncChangeStatus():
    '''public void setAsyncChangeStatus()
    '''
def isAsyncStatusChange():
    '''public boolean isAsyncStatusChange()
    '''
def setAppDefaultValue():
    '''public void setAppDefaultValue()
    '''
def initMXYesNoHash():
    '''public void initMXYesNoHash(final HashMap<String, MXApplicationYesNoCancelException> hash)
    '''
def getMXYesNoHash():
    '''public HashMap<String, MXApplicationYesNoCancelException> getMXYesNoHash()
    '''
def setMustApplyDJP():
    '''public void setMustApplyDJP(final boolean mustApplyDJP)
    '''
def mustApplyDJP():
    '''public boolean mustApplyDJP()
    '''
def calculateDynamicJobPlan():
    '''public void calculateDynamicJobPlan()
    '''
def mustApplyLinearCalculation():
    '''public boolean mustApplyLinearCalculation()
    '''
def calculateTotalWorkUnitsFor():
    '''public void calculateTotalWorkUnitsFor(final MboRemote multiAssetLocCI, final String unitOfWork)
    '''
def calculateTotalWorkUnits():
    '''public void calculateTotalWorkUnits()
    '''
def isCalculationAppliedSuccessfully():
    '''public boolean isCalculationAppliedSuccessfully()
    '''
def getWorkLog():
    '''public MboSetRemote getWorkLog()
    '''
def getWoHazardPrecHashMap():
    '''public Map getWoHazardPrecHashMap()
    '''
def incrementWoHazardPrecHashMap():
    '''public void incrementWoHazardPrecHashMap(final String precautionid)
    '''
def decrementWoHazardPrecHashMap():
    '''public void decrementWoHazardPrecHashMap(final String precautionid)
    '''
def compareJPTask():
    '''public compareJPTask()
    '''
def compare():
    '''public int compare(final MboRemote m1, final MboRemote m2)
    '''
