TIMEZONE_PM_WOGEN_PROCESS = "String  \"PMWOGEN\""
PLUSCAPPNAME = "String  \"PM\""
GENERATING_WORK = "String  \"PM.GeneratingWork\""
def ():
    '''returns PM\n\n
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
def modify():
    '''returns None\n\n
    modify()\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long modifier)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String status, final boolean rollToAllChildren)\n
    changeStatus(final String status, final boolean rollToAllChildren, final Hashtable changedStatusPMs)\n
    '''
def updateUponCompletion():
    '''returns None\n\n
    updateUponCompletion(final MboRemote completedWO)\n
    '''
def updateUponCancellation():
    '''returns None\n\n
    updateUponCancellation(final MboRemote cancelledWO)\n
    '''
def updateForecastUponCancellation():
    '''returns None\n\n
    updateForecastUponCancellation(final MboRemote cancelledWO)\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
def generateAutoKey():
    '''returns None\n\n
    generateAutoKey()\n
    '''
def canGenerateWork():
    '''returns None\n\n
    canGenerateWork()\n
    '''
def generateWork():
    '''returns None\n\n
    generateWork(final boolean useFreqCrit, final int leadTime, final boolean forecast)\n
    generateWork(final boolean useFreqCrit, final int leadTime)\n
    generateWork(final String useFreqCritLeadTime)\n
    '''
def calculateWork():
    '''returns MboSetRemote\n\n
    calculateWork(final boolean useFreqCrit, final Date generateUntil)\n
    '''
def calcWork():
    '''returns MboSetRemote\n\n
    calcWork(final boolean useFreqCrit, final int leadTime)\n
    '''
def calculateTodaysDateWithObjectTimeZoneRule():
    '''returns Date\n\n
    calculateTodaysDateWithObjectTimeZoneRule()\n
    '''
def checkSeason():
    '''returns Date\n\n
    checkSeason(final Date origGenDate, final int totalLeadTime)\n
    '''
def setLinearAssetFieldsReadOnly():
    '''returns None\n\n
    setLinearAssetFieldsReadOnly(final boolean readonlystate)\n
    '''
def clearLinearAssetFields():
    '''returns None\n\n
    clearLinearAssetFields()\n
    '''
def getJobPlanToUse():
    '''returns None\n\n
    getJobPlanToUse()\n
    '''
def validateAssetLoc():
    '''returns None\n\n
    validateAssetLoc(boolean newAssetNum, boolean newLocation)\n
    '''
def updateTimeBasedNextDueDate():
    '''returns None\n\n
    updateTimeBasedNextDueDate()\n
    '''
def checkDate():
    '''returns Date\n\n
    checkDate()\n
    '''
def setPMCounter():
    '''returns None\n\n
    setPMCounter(final int count)\n
    '''
def updateJpSeqInUse():
    '''returns None\n\n
    updateJpSeqInUse()\n
    '''
def copyNextJobPlan():
    '''returns None\n\n
    copyNextJobPlan()\n
    '''
def canViewJpSequence():
    '''returns None\n\n
    canViewJpSequence()\n
    '''
def viewJpSequence():
    '''returns MboSetRemote\n\n
    viewJpSequence()\n
    '''
def clearNextDueDate():
    '''returns None\n\n
    clearNextDueDate()\n
    '''
def setNextDueDate():
    '''returns None\n\n
    setNextDueDate()\n
    '''
def getGeneratedWonum():
    '''returns String\n\n
    getGeneratedWonum(final int priority)\n
    '''
def duplicate():
    '''returns MboRemote\n\n
    duplicate()\n
    '''
def isChangeByUserWhenSetFromLookup():
    '''returns boolean\n\n
    isChangeByUserWhenSetFromLookup(final String lookupAttrName, final String attributeName)\n
    '''
def checkForOpenWO():
    '''returns boolean\n\n
    checkForOpenWO()\n
    '''
def floatingPMHasOpenWOs():
    '''returns boolean\n\n
    floatingPMHasOpenWOs()\n
    '''
def isTop():
    '''returns boolean\n\n
    isTop()\n
    '''
def hasChildren():
    '''returns boolean\n\n
    hasChildren()\n
    '''
def hasParents():
    '''returns boolean\n\n
    hasParents()\n
    '''
def getChildren():
    '''returns MboSetRemote\n\n
    getChildren()\n
    '''
def getParents():
    '''returns MboSetRemote\n\n
    getParents()\n
    '''
def getTop():
    '''returns MboSetRemote\n\n
    getTop()\n
    '''
def getHierarchies():
    '''returns String[]\n\n
    getHierarchies()\n
    '''
def getMeterNextDueDate():
    '''returns Date\n\n
    getMeterNextDueDate(final MboRemote pmMeter, final boolean assetMeter)\n
    '''
def addJobPlanDuration():
    '''returns Date\n\n
    addJobPlanDuration(Date dueDate, final MboRemote retWOGen)\n
    '''
def getMeterNextDueDateNoForecast():
    '''returns Date\n\n
    getMeterNextDueDateNoForecast(final MboRemote pmMeter, final boolean assetMeter)\n
    '''
def getTimeDate():
    '''returns Date\n\n
    getTimeDate()\n
    '''
def validateMetersinMasterPM():
    '''returns None\n\n
    validateMetersinMasterPM(final String assetnum, final String location, final String masterpm)\n
    '''
def getStatusListName():
    '''returns String\n\n
    getStatusListName()\n
    '''
def checkFrequency():
    '''returns Date\n\n
    checkFrequency(final int frequency, final Date nextDueDate, final int unit)\n
    '''
def validateTimeBasedFreq():
    '''returns None\n\n
    validateTimeBasedFreq(final double frequency)\n
    '''
def setEarliestNextDueDate():
    '''returns None\n\n
    setEarliestNextDueDate()\n
    '''
def woCancel():
    '''returns None\n\n
    woCancel(final WORemote newWO)\n
    '''
def truncateHierarchy():
    '''returns boolean\n\n
    truncateHierarchy(final boolean forecast)\n
    '''
def includeInForecast():
    '''returns boolean\n\n
    includeInForecast()\n
    '''
def getDueDateForOpenWO():
    '''returns Date\n\n
    getDueDateForOpenWO(final MboRemote openWo)\n
    '''
def getDueDateForOpenWOWithoutFrequency():
    '''returns Date\n\n
    getDueDateForOpenWOWithoutFrequency(final MboRemote openWo)\n
    '''
def controlScheduleEarlyOnFreqConflictFlag():
    '''returns None\n\n
    controlScheduleEarlyOnFreqConflictFlag(final boolean reset)\n
    '''
def isFrequencyValidForEarlySchedConflict():
    '''returns boolean\n\n
    isFrequencyValidForEarlySchedConflict()\n
    isFrequencyValidForEarlySchedConflict(final long frequency)\n
    '''
def enableScheduleEarlyOnFreqConflict():
    '''returns None\n\n
    enableScheduleEarlyOnFreqConflict(final boolean enable, final boolean reset)\n
    '''
def getActiveDaysAddOn():
    '''returns Date\n\n
    getActiveDaysAddOn(final Date dtDate)\n
    '''
def generateForecast():
    '''returns None\n\n
    generateForecast(final String genDuration)\n
    generateForecast(final int genDuration)\n
    '''
def throwForecastWarning():
    '''returns None\n\n
    throwForecastWarning(final MXException exception)\n
    '''
def setPMForReForecast():
    '''returns int\n\n
    setPMForReForecast(final PM tempPM, final int genDuration)\n
    '''
def getReForecastingNextDate():
    '''returns Date\n\n
    getReForecastingNextDate(final Date fromDate)\n
    '''
def getLastPMForecastRecord():
    '''returns MboRemote\n\n
    getLastPMForecastRecord()\n
    '''
def getLastPMForecastDate():
    '''returns Date\n\n
    getLastPMForecastDate()\n
    '''
def getFirstPMForecastRecord():
    '''returns MboRemote\n\n
    getFirstPMForecastRecord()\n
    '''
def getFirstPMForecastDate():
    '''returns Date\n\n
    getFirstPMForecastDate()\n
    '''
def isFirstForecastRecord():
    '''returns boolean\n\n
    isFirstForecastRecord(final PMForecast pmForecast)\n
    '''
def canReforecastForUntilDate():
    '''returns None\n\n
    canReforecastForUntilDate(final Date lastForecastDate, final Date untilDate)\n
    '''
def deleteSetForecast():
    '''returns None\n\n
    deleteSetForecast()\n
    '''
def canDeletePMForecast():
    '''returns None\n\n
    canDeletePMForecast()\n
    '''
def deleteForecast():
    '''returns None\n\n
    deleteForecast()\n
    deleteForecast(final String nullValue)\n
    '''
def deletePMForecast():
    '''returns None\n\n
    deletePMForecast()\n
    '''
def deleteForecastForPMHierarchy():
    '''returns None\n\n
    deleteForecastForPMHierarchy()\n
    '''
def deleteForecastForHierarchyChange():
    '''returns None\n\n
    deleteForecastForHierarchyChange()\n
    '''
def canDeleteForecast():
    '''returns boolean\n\n
    canDeleteForecast(final String message)\n
    canDeleteForecast(final String message, final MboValue fieldValue)\n
    '''
def canDisplayForecast():
    '''returns boolean\n\n
    canDisplayForecast()\n
    '''
def rolldownLockForecastFlagToChildren():
    '''returns None\n\n
    rolldownLockForecastFlagToChildren(final boolean torf)\n
    '''
def rolldownInclForecastFlagToChildren():
    '''returns None\n\n
    rolldownInclForecastFlagToChildren(final boolean torf)\n
    '''
def rolldownFieldValueToChildrens():
    '''returns None\n\n
    rolldownFieldValueToChildrens(final String fieldname, final String fieldvalue, final long accessModifier)\n
    '''
def canGenerateChildPMForecast():
    '''returns None\n\n
    canGenerateChildPMForecast()\n
    '''
def setCanDeleteForecastFlag():
    '''returns None\n\n
    setCanDeleteForecastFlag(final boolean flag)\n
    '''
def getCanDeleteForecastFlag():
    '''returns boolean\n\n
    getCanDeleteForecastFlag()\n
    '''
def reforecastSubsequentDates():
    '''returns None\n\n
    reforecastSubsequentDates()\n
    reforecastSubsequentDates(final PMForecast newDatePMForecast)\n
    reforecastSubsequentDates(final MboRemote newDatePMForecast, final MboSetRemote pmForecastSet)\n
    reforecastSubsequentDates(final String nullValue)\n
    '''
def setPMForReforecastSubsequentDates():
    '''returns None\n\n
    setPMForReforecastSubsequentDates(final Date newDate)\n
    '''
def getDurationToForecast():
    '''returns int\n\n
    getDurationToForecast(final MboRemote pmForecast, final MboSetRemote pmForecastSet)\n
    '''
def getCalendarTime():
    '''returns Calendar\n\n
    getCalendarTime(final Date date)\n
    '''
def getDurationBetweenTwoDates():
    '''returns int\n\n
    getDurationBetweenTwoDates(final Date toDate, final Date fromDate)\n
    '''
def canReforecast():
    '''returns boolean\n\n
    canReforecast()\n
    '''
def setUserChoiceForReforecast():
    '''returns None\n\n
    setUserChoiceForReforecast(final int userChoiceForReforecast)\n
    '''
def getUserChoiceForReforecast():
    '''returns int\n\n
    getUserChoiceForReforecast()\n
    '''
def canReforecastSubsequentDates():
    '''returns int\n\n
    canReforecastSubsequentDates(final PMForecast newDatePMForecast)\n
    '''
def clearReforecast():
    '''returns None\n\n
    clearReforecast()\n
    '''
def isReforecastPending():
    '''returns boolean\n\n
    isReforecastPending()\n
    '''
def editOnlyFirstPMForecastRecord():
    '''returns boolean\n\n
    editOnlyFirstPMForecastRecord()\n
    '''
def throwOKCANCELMessage():
    '''returns boolean\n\n
    throwOKCANCELMessage(final String message)\n
    '''
def setOnSKDPMListTab():
    '''returns None\n\n
    setOnSKDPMListTab(final boolean listTab)\n
    '''
def onSKDPMListTab():
    '''returns boolean\n\n
    onSKDPMListTab()\n
    '''
def resetlastPMForecastRecord():
    '''returns None\n\n
    resetlastPMForecastRecord()\n
    '''
def setDeleteForecastFlag():
    '''returns None\n\n
    setDeleteForecastFlag(final boolean flag)\n
    '''
def getDeleteForecastFlag():
    '''returns boolean\n\n
    getDeleteForecastFlag()\n
    '''
def editPMDeleteForecast():
    '''returns None\n\n
    editPMDeleteForecast()\n
    editPMDeleteForecast(final MboValue fieldValue)\n
    '''
def canUpdateForecastJobPlans():
    '''returns boolean\n\n
    canUpdateForecastJobPlans()\n
    '''
def updateForecastJobPlans():
    '''returns None\n\n
    updateForecastJobPlans()\n
    '''
def addPlusCPMExtDate():
    '''returns None\n\n
    addPlusCPMExtDate(final boolean setPrevDate, final Date extdate, final boolean hasToSave, final String comments, final String commentsLD)\n
    addPlusCPMExtDate(final boolean setPrevDate, final Date extdate, final boolean hasToSave, final String comments)\n
    '''
def canAddPMExtDate():
    '''returns boolean\n\n
    canAddPMExtDate()\n
    '''
def getAsset():
    '''returns AssetRemote\n\n
    getAsset()\n
    '''
def getLocation():
    '''returns LocationRemote\n\n
    getLocation()\n
    '''
def canOverride():
    '''returns None\n\n
    canOverride()\n
    '''
def getWorkType():
    '''returns String\n\n
    getWorkType()\n
    '''
def getWorkTypeCal():
    '''returns String\n\n
    getWorkTypeCal()\n
    '''
def isCalibrationInstalled():
    '''returns boolean\n\n
    isCalibrationInstalled()\n
    '''
def regenerateForecast():
    '''returns int\n\n
    regenerateForecast(final String message)\n
    '''
def forecastDateBeforeToday():
    '''returns boolean\n\n
    forecastDateBeforeToday(final MboRemote pmforecast)\n
    '''
def checkForecastForGenWork():
    '''returns None\n\n
    checkForecastForGenWork()\n
    '''
def canGenerateForecastWork():
    '''returns int\n\n
    canGenerateForecastWork(final boolean useFreqCrit)\n
    '''
def lockUnlockForecast():
    '''returns None\n\n
    lockUnlockForecast(final boolean lockForecast)\n
    '''
def checkJPSeq():
    '''returns boolean\n\n
    checkJPSeq()\n
    '''
def AddPMForecastJPRecord():
    '''returns None\n\n
    AddPMForecastJPRecord(final String rootancestor, final MboRemote cancelledWO)\n
    '''
def canLockUnlockChildPMForecast():
    '''returns None\n\n
    canLockUnlockChildPMForecast()\n
    '''
def hasForecast():
    '''returns boolean\n\n
    hasForecast()\n
    '''
def clearPmDeleteForecastVector():
    '''returns None\n\n
    clearPmDeleteForecastVector()\n
    '''
def isListSelected():
    '''returns boolean\n\n
    isListSelected()\n
    '''
def setListSelected():
    '''returns None\n\n
    setListSelected(final boolean isListSelected)\n
    '''
def getTargStartDate():
    '''returns Date\n\n
    getTargStartDate(final Date date, final String calledFromFlag)\n
    '''
def getPMNextDate():
    '''returns Date\n\n
    getPMNextDate(final Date date, final String calledFromFlag)\n
    '''
def getPMLastCompDate():
    '''returns Date\n\n
    getPMLastCompDate(final Date date, final String calledFromFlag)\n
    '''
def getPMLastStartDate():
    '''returns Date\n\n
    getPMLastStartDate(final Date date, final String calledFromFlag)\n
    '''
def getPMDueDate():
    '''returns Date\n\n
    getPMDueDate(final Date date, final String calledFromFlag)\n
    '''
def getPMExtDate():
    '''returns Date\n\n
    getPMExtDate(final Date date, final String calledFromFlag)\n
    '''
def getPMForecastDate():
    '''returns Date\n\n
    getPMForecastDate(final Date date, final String calledFromFlag)\n
    '''
def getDateWithTimeZone():
    '''returns Date\n\n
    getDateWithTimeZone(final Date date)\n
    '''
def getDateWithServerTimeZone():
    '''returns Date\n\n
    getDateWithServerTimeZone(Date date)\n
    '''
def getDateWithObjectTimeZone():
    '''returns Date\n\n
    getDateWithObjectTimeZone(Date date)\n
    '''
def storeResourceDataForForecast():
    '''returns None\n\n
    storeResourceDataForForecast()\n
    '''
def getResourcesForForecastSegement():
    '''returns None\n\n
    getResourcesForForecastSegement(final MboRemote jobplan, final MboRemote pmforecastJP)\n
    '''
def getGeneratedWonumAndWorkOrderId():
    '''returns Object[]\n\n
    getGeneratedWonumAndWorkOrderId(final int priority)\n
    '''
def getJPNumWithDate():
    '''returns String\n\n
    getJPNumWithDate(final Date date, final String jpnum)\n
    '''
def getWOSavedInDB():
    '''returns MboRemote\n\n
    getWOSavedInDB(final MboRemote woGenerated)\n
    '''
