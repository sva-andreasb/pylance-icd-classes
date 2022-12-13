TIMEZONE_PM_WOGEN_PROCESS = "String  \"PMWOGEN\""
PLUSCAPPNAME = "String  \"PM\""
GENERATING_WORK = "String  \"PM.GeneratingWork\""
def PM():
    '''public PM(final MboSet ms)
    '''
def init():
    '''public void init()
    '''
def initFieldFlagsOnMbo():
    '''public void initFieldFlagsOnMbo(final String attrName)
    '''
def add():
    '''public void add()
    '''
def modify():
    '''public void modify()
    '''
def canDelete():
    '''public void canDelete()
    '''
def delete():
    '''public void delete(final long modifier)
    '''
def changeStatus():
    '''public void changeStatus(final String status, final boolean rollToAllChildren)
    public void changeStatus(final String status, final boolean rollToAllChildren, final Hashtable changedStatusPMs)
    '''
def updateUponCompletion():
    '''public void updateUponCompletion(final MboRemote completedWO)
    '''
def updateUponCancellation():
    '''public void updateUponCancellation(final MboRemote cancelledWO)
    '''
def updateForecastUponCancellation():
    '''public void updateForecastUponCancellation(final MboRemote cancelledWO)
    '''
def appValidate():
    '''public void appValidate()
    '''
def save():
    '''public void save()
    '''
def generateAutoKey():
    '''public void generateAutoKey()
    '''
def canGenerateWork():
    '''public void canGenerateWork()
    '''
def generateWork():
    '''public MboSetRemote generateWork(final boolean useFreqCrit, final int leadTime, final boolean forecast)
    public void generateWork(final boolean useFreqCrit, final int leadTime)
    public void generateWork(final String useFreqCritLeadTime)
    '''
def calculateWork():
    '''public MboSetRemote calculateWork(final boolean useFreqCrit, final Date generateUntil)
    '''
def calcWork():
    '''public MboSetRemote calcWork(final boolean useFreqCrit, final int leadTime)
    '''
def calculateTodaysDateWithObjectTimeZoneRule():
    '''public Date calculateTodaysDateWithObjectTimeZoneRule()
    '''
def checkSeason():
    '''public Date checkSeason(final Date origGenDate, final int totalLeadTime)
    '''
def setLinearAssetFieldsReadOnly():
    '''public void setLinearAssetFieldsReadOnly(final boolean readonlystate)
    '''
def clearLinearAssetFields():
    '''public void clearLinearAssetFields()
    '''
def getJobPlanToUse():
    '''public void getJobPlanToUse()
    '''
def validateAssetLoc():
    '''public void validateAssetLoc(boolean newAssetNum, boolean newLocation)
    '''
def updateTimeBasedNextDueDate():
    '''public void updateTimeBasedNextDueDate()
    '''
def checkDate():
    '''public Date checkDate()
    '''
def setPMCounter():
    '''public void setPMCounter(final int count)
    '''
def updateJpSeqInUse():
    '''public void updateJpSeqInUse()
    '''
def copyNextJobPlan():
    '''public void copyNextJobPlan()
    '''
def canViewJpSequence():
    '''public void canViewJpSequence()
    '''
def viewJpSequence():
    '''public MboSetRemote viewJpSequence()
    '''
def clearNextDueDate():
    '''public void clearNextDueDate()
    '''
def setNextDueDate():
    '''public void setNextDueDate()
    '''
def getGeneratedWonum():
    '''public String getGeneratedWonum(final int priority)
    '''
def duplicate():
    '''public MboRemote duplicate()
    '''
def isChangeByUserWhenSetFromLookup():
    '''public boolean isChangeByUserWhenSetFromLookup(final String lookupAttrName, final String attributeName)
    '''
def checkForOpenWO():
    '''public boolean checkForOpenWO()
    '''
def floatingPMHasOpenWOs():
    '''public boolean floatingPMHasOpenWOs()
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
def getChildren():
    '''public MboSetRemote getChildren()
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
def getMeterNextDueDate():
    '''public Date getMeterNextDueDate(final MboRemote pmMeter, final boolean assetMeter)
    '''
def addJobPlanDuration():
    '''public Date addJobPlanDuration(Date dueDate, final MboRemote retWOGen)
    '''
def getMeterNextDueDateNoForecast():
    '''public Date getMeterNextDueDateNoForecast(final MboRemote pmMeter, final boolean assetMeter)
    '''
def getTimeDate():
    '''public Date getTimeDate()
    '''
def validateMetersinMasterPM():
    '''public void validateMetersinMasterPM(final String assetnum, final String location, final String masterpm)
    '''
def getStatusListName():
    '''public String getStatusListName()
    '''
def checkFrequency():
    '''public Date checkFrequency(final int frequency, final Date nextDueDate, final int unit)
    '''
def validateTimeBasedFreq():
    '''public void validateTimeBasedFreq(final double frequency)
    '''
def setEarliestNextDueDate():
    '''public void setEarliestNextDueDate()
    '''
def woCancel():
    '''public void woCancel(final WORemote newWO)
    '''
def truncateHierarchy():
    '''public boolean truncateHierarchy(final boolean forecast)
    '''
def includeInForecast():
    '''public boolean includeInForecast()
    '''
def getDueDateForOpenWO():
    '''public Date getDueDateForOpenWO(final MboRemote openWo)
    '''
def getDueDateForOpenWOWithoutFrequency():
    '''public Date getDueDateForOpenWOWithoutFrequency(final MboRemote openWo)
    '''
def controlScheduleEarlyOnFreqConflictFlag():
    '''public void controlScheduleEarlyOnFreqConflictFlag(final boolean reset)
    '''
def isFrequencyValidForEarlySchedConflict():
    '''public boolean isFrequencyValidForEarlySchedConflict()
    public boolean isFrequencyValidForEarlySchedConflict(final long frequency)
    '''
def enableScheduleEarlyOnFreqConflict():
    '''public void enableScheduleEarlyOnFreqConflict(final boolean enable, final boolean reset)
    '''
def getActiveDaysAddOn():
    '''public Date getActiveDaysAddOn(final Date dtDate)
    '''
def generateForecast():
    '''public void generateForecast(final String genDuration)
    public void generateForecast(final int genDuration)
    '''
def throwForecastWarning():
    '''public void throwForecastWarning(final MXException exception)
    '''
def setPMForReForecast():
    '''public int setPMForReForecast(final PM tempPM, final int genDuration)
    '''
def getReForecastingNextDate():
    '''public Date getReForecastingNextDate(final Date fromDate)
    '''
def getLastPMForecastRecord():
    '''public MboRemote getLastPMForecastRecord()
    '''
def getLastPMForecastDate():
    '''public Date getLastPMForecastDate()
    '''
def getFirstPMForecastRecord():
    '''public MboRemote getFirstPMForecastRecord()
    '''
def getFirstPMForecastDate():
    '''public Date getFirstPMForecastDate()
    '''
def isFirstForecastRecord():
    '''public boolean isFirstForecastRecord(final PMForecast pmForecast)
    '''
def canReforecastForUntilDate():
    '''public void canReforecastForUntilDate(final Date lastForecastDate, final Date untilDate)
    '''
def deleteSetForecast():
    '''public void deleteSetForecast()
    '''
def canDeletePMForecast():
    '''public void canDeletePMForecast()
    '''
def deleteForecast():
    '''public void deleteForecast()
    public void deleteForecast(final String nullValue)
    '''
def deletePMForecast():
    '''public void deletePMForecast()
    '''
def deleteForecastForPMHierarchy():
    '''public void deleteForecastForPMHierarchy()
    '''
def deleteForecastForHierarchyChange():
    '''public void deleteForecastForHierarchyChange()
    '''
def canDeleteForecast():
    '''public boolean canDeleteForecast(final String message)
    public boolean canDeleteForecast(final String message, final MboValue fieldValue)
    '''
def canDisplayForecast():
    '''public boolean canDisplayForecast()
    '''
def rolldownLockForecastFlagToChildren():
    '''public void rolldownLockForecastFlagToChildren(final boolean torf)
    '''
def rolldownInclForecastFlagToChildren():
    '''public void rolldownInclForecastFlagToChildren(final boolean torf)
    '''
def rolldownFieldValueToChildrens():
    '''public void rolldownFieldValueToChildrens(final String fieldname, final String fieldvalue, final long accessModifier)
    '''
def canGenerateChildPMForecast():
    '''public void canGenerateChildPMForecast()
    '''
def setCanDeleteForecastFlag():
    '''public void setCanDeleteForecastFlag(final boolean flag)
    '''
def getCanDeleteForecastFlag():
    '''public boolean getCanDeleteForecastFlag()
    '''
def reforecastSubsequentDates():
    '''public void reforecastSubsequentDates()
    public void reforecastSubsequentDates(final PMForecast newDatePMForecast)
    public void reforecastSubsequentDates(final MboRemote newDatePMForecast, final MboSetRemote pmForecastSet)
    public void reforecastSubsequentDates(final String nullValue)
    '''
def setPMForReforecastSubsequentDates():
    '''public void setPMForReforecastSubsequentDates(final Date newDate)
    '''
def getDurationToForecast():
    '''public int getDurationToForecast(final MboRemote pmForecast, final MboSetRemote pmForecastSet)
    '''
def getCalendarTime():
    '''public Calendar getCalendarTime(final Date date)
    '''
def getDurationBetweenTwoDates():
    '''public int getDurationBetweenTwoDates(final Date toDate, final Date fromDate)
    '''
def canReforecast():
    '''public boolean canReforecast()
    '''
def setUserChoiceForReforecast():
    '''public void setUserChoiceForReforecast(final int userChoiceForReforecast)
    '''
def getUserChoiceForReforecast():
    '''public int getUserChoiceForReforecast()
    '''
def canReforecastSubsequentDates():
    '''public int canReforecastSubsequentDates(final PMForecast newDatePMForecast)
    '''
def clearReforecast():
    '''public void clearReforecast()
    '''
def isReforecastPending():
    '''public boolean isReforecastPending()
    '''
def editOnlyFirstPMForecastRecord():
    '''public boolean editOnlyFirstPMForecastRecord()
    '''
def throwOKCANCELMessage():
    '''public boolean throwOKCANCELMessage(final String message)
    '''
def setOnSKDPMListTab():
    '''public void setOnSKDPMListTab(final boolean listTab)
    '''
def onSKDPMListTab():
    '''public boolean onSKDPMListTab()
    '''
def resetlastPMForecastRecord():
    '''public void resetlastPMForecastRecord()
    '''
def setDeleteForecastFlag():
    '''public void setDeleteForecastFlag(final boolean flag)
    '''
def getDeleteForecastFlag():
    '''public boolean getDeleteForecastFlag()
    '''
def editPMDeleteForecast():
    '''public void editPMDeleteForecast()
    public void editPMDeleteForecast(final MboValue fieldValue)
    '''
def canUpdateForecastJobPlans():
    '''public boolean canUpdateForecastJobPlans()
    '''
def updateForecastJobPlans():
    '''public void updateForecastJobPlans()
    '''
def addPlusCPMExtDate():
    '''public void addPlusCPMExtDate(final boolean setPrevDate, final Date extdate, final boolean hasToSave, final String comments, final String commentsLD)
    public void addPlusCPMExtDate(final boolean setPrevDate, final Date extdate, final boolean hasToSave, final String comments)
    '''
def canAddPMExtDate():
    '''public boolean canAddPMExtDate()
    '''
def getAsset():
    '''public AssetRemote getAsset()
    '''
def getLocation():
    '''public LocationRemote getLocation()
    '''
def canOverride():
    '''public void canOverride()
    '''
def getWorkType():
    '''public String getWorkType()
    '''
def getWorkTypeCal():
    '''public String getWorkTypeCal()
    '''
def isCalibrationInstalled():
    '''public boolean isCalibrationInstalled()
    '''
def regenerateForecast():
    '''public int regenerateForecast(final String message)
    '''
def forecastDateBeforeToday():
    '''public boolean forecastDateBeforeToday(final MboRemote pmforecast)
    '''
def checkForecastForGenWork():
    '''public void checkForecastForGenWork()
    '''
def canGenerateForecastWork():
    '''public int canGenerateForecastWork(final boolean useFreqCrit)
    '''
def lockUnlockForecast():
    '''public void lockUnlockForecast(final boolean lockForecast)
    '''
def checkJPSeq():
    '''public boolean checkJPSeq()
    '''
def AddPMForecastJPRecord():
    '''public void AddPMForecastJPRecord(final String rootancestor, final MboRemote cancelledWO)
    '''
def canLockUnlockChildPMForecast():
    '''public void canLockUnlockChildPMForecast()
    '''
def hasForecast():
    '''public boolean hasForecast()
    '''
def clearPmDeleteForecastVector():
    '''public void clearPmDeleteForecastVector()
    '''
def isListSelected():
    '''public boolean isListSelected()
    '''
def setListSelected():
    '''public void setListSelected(final boolean isListSelected)
    '''
def getTargStartDate():
    '''public Date getTargStartDate(final Date date, final String calledFromFlag)
    '''
def getPMNextDate():
    '''public Date getPMNextDate(final Date date, final String calledFromFlag)
    '''
def getPMLastCompDate():
    '''public Date getPMLastCompDate(final Date date, final String calledFromFlag)
    '''
def getPMLastStartDate():
    '''public Date getPMLastStartDate(final Date date, final String calledFromFlag)
    '''
def getPMDueDate():
    '''public Date getPMDueDate(final Date date, final String calledFromFlag)
    '''
def getPMExtDate():
    '''public Date getPMExtDate(final Date date, final String calledFromFlag)
    '''
def getPMForecastDate():
    '''public Date getPMForecastDate(final Date date, final String calledFromFlag)
    '''
def getDateWithTimeZone():
    '''public Date getDateWithTimeZone(final Date date)
    '''
def getDateWithServerTimeZone():
    '''public Date getDateWithServerTimeZone(Date date)
    '''
def getDateWithObjectTimeZone():
    '''public Date getDateWithObjectTimeZone(Date date)
    '''
def storeResourceDataForForecast():
    '''public void storeResourceDataForForecast()
    '''
def getResourcesForForecastSegement():
    '''public void getResourcesForForecastSegement(final MboRemote jobplan, final MboRemote pmforecastJP)
    '''
def getGeneratedWonumAndWorkOrderId():
    '''public Object[] getGeneratedWonumAndWorkOrderId(final int priority)
    '''
def getJPNumWithDate():
    '''public String getJPNumWithDate(final Date date, final String jpnum)
    '''
def getWOSavedInDB():
    '''public MboRemote getWOSavedInDB(final MboRemote woGenerated)
    '''
