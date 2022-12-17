def ():
    '''returns JobPlan\n\n
    (final MboSet ms)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def initFieldFlagsOnMbo():
    '''returns None\n\n
    initFieldFlagsOnMbo(final String attrName)\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def generateAutoKey():
    '''returns None\n\n
    generateAutoKey()\n
    '''
def duplicate():
    '''returns MboRemote\n\n
    duplicate()\n
    '''
def getTotals():
    '''returns Vector\n\n
    getTotals(final String siteid)\n
    '''
def copySparePartsToJPMatSet():
    '''returns None\n\n
    copySparePartsToJPMatSet(final MboSetRemote sparePartSet)\n
    '''
def createJPTaskFromWOTask():
    '''returns Mbo\n\n
    createJPTaskFromWOTask(final Mbo fromWO, final Mbo fromWOTask, final MboSet jpTasks)\n
    '''
def createJPTaskFromWOChild():
    '''returns Mbo\n\n
    createJPTaskFromWOChild(final Mbo fromWO, final Mbo fromWOChild, final MboSet jpTasks)\n
    '''
def createJPLaborFromWOLabor():
    '''returns Mbo\n\n
    createJPLaborFromWOLabor(final Mbo fromWO, final Mbo fromWOLabor, final MboSet jpLabors)\n
    '''
def createJPMaterialFromWOMaterial():
    '''returns Mbo\n\n
    createJPMaterialFromWOMaterial(final Mbo fromWO, final Mbo fromWOMaterial, final MboSet jpMaterials)\n
    '''
def createJPServiceFromWPService():
    '''returns Mbo\n\n
    createJPServiceFromWPService(final Mbo fromWO, final Mbo fromWPService, final MboSet jpServiceSet)\n
    '''
def createJPToolFromWOTool():
    '''returns Mbo\n\n
    createJPToolFromWOTool(final Mbo fromWO, final Mbo fromWOTool, final MboSet jpTools)\n
    '''
def createJPAssetFromWOAsset():
    '''returns None\n\n
    createJPAssetFromWOAsset(final Mbo fromWO, final MboSet jpAssets)\n
    '''
def createJPTaskRelFromWOTaskRel():
    '''returns Mbo\n\n
    createJPTaskRelFromWOTaskRel(final Mbo fromWO, final Mbo fromWOTaskRel, final MboSet jptaskRelations, final Map<String, Mbo> woTaskLookup)\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def validateJPKey():
    '''returns None\n\n
    validateJPKey()\n
    '''
def getMboSet():
    '''returns MboSetRemote\n\n
    getMboSet(final String name)\n
    '''
def deleteJobTaskComponents():
    '''returns None\n\n
    deleteJobTaskComponents(final int jptask, String taskorg, String tasksite)\n
    '''
def undeleteJobTaskComponents():
    '''returns None\n\n
    undeleteJobTaskComponents(final int jptask, String taskorg, String tasksite)\n
    '''
def updatePredecessorFields():
    '''returns None\n\n
    updatePredecessorFields()\n
    '''
def componentAdded():
    '''returns None\n\n
    componentAdded()\n
    '''
def getStatusListName():
    '''returns String\n\n
    getStatusListName()\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String status, Date date, final String memo, final long accessModifier)\n
    '''
def canChangeStatus():
    '''returns None\n\n
    canChangeStatus(final JobPlanRemote jobplan, String currentStatus, String desiredStatus)\n
    '''
def nestedJobPlans():
    '''returns boolean\n\n
    nestedJobPlans(final JobPlanRemote jobplan, String currentStatus, String desiredStatus)\n
    '''
def doChangeStatus():
    '''returns None\n\n
    doChangeStatus(final JobPlanRemote jobplan, String currentStatus, String desiredStatus, final Date date, final String memo)\n
    '''
def getJobPlanComponentSet():
    '''returns MboSetRemote\n\n
    getJobPlanComponentSet(final String maxRelName, final String orgid, final String siteid)\n
    '''
def clearClassification():
    '''returns None\n\n
    clearClassification()\n
    '''
def validateProcessFlow():
    '''returns None\n\n
    validateProcessFlow()\n
    '''
def validateNetwork():
    '''returns None\n\n
    validateNetwork(final Hashtable<String, LinkedList> htSuccessors, final LinkedList<String> startingNodes, final boolean printDebugMsgs)\n
    '''
def findMatchingTasks():
    '''returns Stack<MboRemote>\n\n
    findMatchingTasks(final MboSetRemote taskSet, final String orgid, final String siteid, final String jptask)\n
    '''
def suspendChildrensProcessFlow():
    '''returns None\n\n
    suspendChildrensProcessFlow(final boolean torf)\n
    '''
def setChildrensFlowControl():
    '''returns None\n\n
    setChildrensFlowControl(final boolean torf)\n
    '''
def changeChildrensFieldValue():
    '''returns None\n\n
    changeChildrensFieldValue(final String fieldname, final String fieldvalue, final long accessModifier)\n
    '''
def propagateRevisionStatus():
    '''returns None\n\n
    propagateRevisionStatus(final JobPlanRemote newRevision)\n
    '''
def propagateRevisionNumber():
    '''returns None\n\n
    propagateRevisionNumber(final JobPlanRemote newRevision)\n
    '''
def revise():
    '''returns MboRemote\n\n
    revise(final String revDescription)\n
    '''
def canRevise():
    '''returns None\n\n
    canRevise()\n
    '''
def setReadOnlyFields():
    '''returns None\n\n
    setReadOnlyFields()\n
    '''
def isRevEnabled():
    '''returns boolean\n\n
    isRevEnabled()\n
    '''
def isRevisionStatusNotAllowed():
    '''returns boolean\n\n
    isRevisionStatusNotAllowed()\n
    '''
def setStatusHistoryFields():
    '''returns None\n\n
    setStatusHistoryFields(final JobPlan jp, final Date date, final String memo)\n
    '''
def active():
    '''returns None\n\n
    active(final MboRemote jobplan, final String currentMaxStatus, final String desiredStatus, final Date date)\n
    '''
def getNextRevNum():
    '''returns int\n\n
    getNextRevNum()\n
    '''
def getMaxValidStatusRevNum():
    '''returns int\n\n
    getMaxValidStatusRevNum()\n
    '''
def getSpecificStringOfSites():
    '''returns String\n\n
    getSpecificStringOfSites(final MboSetRemote jobPlanSubSets)\n
    '''
def copyCrewTypeToWpLaborSet():
    '''returns None\n\n
    copyCrewTypeToWpLaborSet(final MboSetRemote crewTypeSet)\n
    '''
def getHistoryFlag():
    '''returns boolean\n\n
    getHistoryFlag()\n
    '''
def canDeleteAttachedDocs():
    '''returns None\n\n
    canDeleteAttachedDocs()\n
    '''
def initRelationship():
    '''returns None\n\n
    initRelationship(final String relationName, final MboSetRemote mboSet)\n
    '''
def setRelatedMboEditibility():
    '''returns None\n\n
    setRelatedMboEditibility(final String relationName, final MboSetRemote relatedSet)\n
    '''
def setRevisedStatus():
    '''returns None\n\n
    setRevisedStatus(final boolean value)\n
    '''
def getRevisedStatus():
    '''returns boolean\n\n
    getRevisedStatus()\n
    '''
def setListPage():
    '''returns None\n\n
    setListPage(final boolean value)\n
    '''
def getListPage():
    '''returns boolean\n\n
    getListPage()\n
    '''
def isDuringDUPLICATE():
    '''returns boolean\n\n
    isDuringDUPLICATE()\n
    '''
def setDuringDUPLICATE():
    '''returns None\n\n
    setDuringDUPLICATE(final boolean value)\n
    '''
