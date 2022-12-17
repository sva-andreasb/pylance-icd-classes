def ():
    '''returns ReportAdHoc\n\n
    (final MboSet ms)\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    '''
def addAllAttributes():
    '''returns None\n\n
    addAllAttributes()\n
    '''
def removeAllAttributes():
    '''returns None\n\n
    removeAllAttributes()\n
    '''
def toggleAttribute():
    '''returns None\n\n
    toggleAttribute(final String attributeName, final boolean toBeAdded)\n
    toggleAttribute(final MboRemote attribute, final boolean toBeAdded)\n
    '''
def addToExpressionList():
    '''returns None\n\n
    addToExpressionList()\n
    '''
def addToSummaryList():
    '''returns None\n\n
    addToSummaryList()\n
    '''
def addAttrToExpr():
    '''returns None\n\n
    addAttrToExpr(final MboRemote attribute, final boolean toBeAdded)\n
    '''
def setSelectedCalcCategory():
    '''returns None\n\n
    setSelectedCalcCategory(final String category)\n
    '''
def getSelectedCalcCategory():
    '''returns String\n\n
    getSelectedCalcCategory()\n
    '''
def addAttrToSum():
    '''returns None\n\n
    addAttrToSum(final MboRemote attribute)\n
    '''
def initializeObjectStructureInfo():
    '''returns None\n\n
    initializeObjectStructureInfo()\n
    '''
def isParentSelected():
    '''returns boolean\n\n
    isParentSelected(final int objectID)\n
    '''
def isParentSelectedCalc():
    '''returns boolean\n\n
    isParentSelectedCalc(final int objectID)\n
    '''
def objectDependencyCheck():
    '''returns None\n\n
    objectDependencyCheck(final int id)\n
    '''
def getObjectName():
    '''returns String\n\n
    getObjectName(final int objectID)\n
    '''
def getValidAttributes():
    '''returns Set<String>\n\n
    getValidAttributes(final int objectID)\n
    '''
def updateAvailableAttributes():
    '''returns None\n\n
    updateAvailableAttributes()\n
    '''
def updateAvailableAttributesCalc():
    '''returns None\n\n
    updateAvailableAttributesCalc()\n
    '''
def updateAvailableAttributesSum():
    '''returns None\n\n
    updateAvailableAttributesSum()\n
    '''
def getAvailableAttributesSet():
    '''returns MboSetRemote\n\n
    getAvailableAttributesSet()\n
    '''
def getAvailableAttributesSetCalc():
    '''returns MboSetRemote\n\n
    getAvailableAttributesSetCalc()\n
    '''
def reorderColumns():
    '''returns None\n\n
    reorderColumns()\n
    '''
def reorderCalculations():
    '''returns None\n\n
    reorderCalculations()\n
    '''
def reorderSummaries():
    '''returns None\n\n
    reorderSummaries()\n
    '''
def suggestUniqueName():
    '''returns String\n\n
    suggestUniqueName()\n
    suggestUniqueName(String reportName)\n
    '''
def disableScheduleFields():
    '''returns None\n\n
    disableScheduleFields(final boolean disable)\n
    '''
def createReport():
    '''returns None\n\n
    createReport()\n
    '''
def getReportNum():
    '''returns int\n\n
    getReportNum()\n
    '''
def getReportXML():
    '''returns String\n\n
    getReportXML()\n
    '''
def getPresentationForThisDialog():
    '''returns String\n\n
    getPresentationForThisDialog()\n
    '''
def setDefaultObjectID():
    '''returns None\n\n
    setDefaultObjectID()\n
    '''
def setSelectedObjectID():
    '''returns None\n\n
    setSelectedObjectID(final int objectID)\n
    '''
def getSelectedObjectID():
    '''returns int\n\n
    getSelectedObjectID()\n
    '''
def setSelectedObjectIDCalc():
    '''returns None\n\n
    setSelectedObjectIDCalc(final int objectID)\n
    '''
def getSelectedObjectIDCalc():
    '''returns int\n\n
    getSelectedObjectIDCalc()\n
    '''
def setSelectedObjectIDSum():
    '''returns None\n\n
    setSelectedObjectIDSum(final int objectID)\n
    '''
def getSelectedObjectIDSum():
    '''returns int\n\n
    getSelectedObjectIDSum()\n
    '''
def clearFields():
    '''returns None\n\n
    clearFields(final String fieldType)\n
    '''
def getLevelCount():
    '''returns int\n\n
    getLevelCount(final String fieldType)\n
    '''
def isGroupOrSortField():
    '''returns boolean\n\n
    isGroupOrSortField(final MboRemote attribute, final String fieldType)\n
    '''
def hasDuplicateReportTitle():
    '''returns boolean\n\n
    hasDuplicateReportTitle()\n
    '''
def getDuplicateReportName():
    '''returns String\n\n
    getDuplicateReportName()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def initFieldFlagsOnMbo():
    '''returns None\n\n
    initFieldFlagsOnMbo(final String attrName)\n
    '''
def sigopGranted():
    '''returns boolean\n\n
    sigopGranted(final String app, final String optionname)\n
    '''
def getCategory():
    '''returns String\n\n
    getCategory(final int objectID)\n
    '''
def setObjectOnlyDefaults():
    '''returns None\n\n
    setObjectOnlyDefaults()\n
    '''
def setSelectedAttributes():
    '''returns None\n\n
    setSelectedAttributes()\n
    '''
def copyChildrenForInit():
    '''returns None\n\n
    copyChildrenForInit()\n
    '''
def copyChildrenForSave():
    '''returns None\n\n
    copyChildrenForSave()\n
    '''
def createReportName():
    '''returns String\n\n
    createReportName()\n
    '''
def clearCalcTempFields():
    '''returns None\n\n
    clearCalcTempFields()\n
    '''
def setLabelSyncFlag():
    '''returns None\n\n
    setLabelSyncFlag()\n
    '''
def setTransientBROSInfo():
    '''returns None\n\n
    setTransientBROSInfo(final String brosID, final Hashtable reportParams, final String csrfToken)\n
    '''
