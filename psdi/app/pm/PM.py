TIMEZONE_PM_WOGEN_PROCESS = "String  PMWOGEN""
PLUSCAPPNAME = "String  PM""
GENERATING_WORK = "String  PM.GeneratingWork""
def PM():
'''public PM(final MboSet ms)
'''
pass
def init():
'''public void init()
'''
pass
def initFieldFlagsOnMbo():
'''public void initFieldFlagsOnMbo(final String attrName)
'''
pass
def add():
'''public void add()
'''
pass
def modify():
'''public void modify()
'''
pass
def canDelete():
'''public void canDelete()
'''
pass
def delete():
'''public void delete(final long modifier)
'''
pass
def changeStatus():
'''public void changeStatus(final String status, final boolean rollToAllChildren)
public void changeStatus(final String status, final boolean rollToAllChildren, final Hashtable changedStatusPMs)
'''
pass
def updateUponCompletion():
'''public void updateUponCompletion(final MboRemote completedWO)
'''
pass
def updateUponCancellation():
'''public void updateUponCancellation(final MboRemote cancelledWO)
'''
pass
def updateForecastUponCancellation():
'''public void updateForecastUponCancellation(final MboRemote cancelledWO)
'''
pass
def appValidate():
'''public void appValidate()
'''
pass
def save():
'''public void save()
'''
pass
def generateAutoKey():
'''public void generateAutoKey()
'''
pass
def canGenerateWork():
'''public void canGenerateWork()
'''
pass
def generateWork():
'''public MboSetRemote generateWork(final boolean useFreqCrit, final int leadTime, final boolean forecast)
public void generateWork(final boolean useFreqCrit, final int leadTime)
public void generateWork(final String useFreqCritLeadTime)
'''
pass
def calculateWork():
'''public MboSetRemote calculateWork(final boolean useFreqCrit, final Date generateUntil)
'''
pass
def calcWork():
'''public MboSetRemote calcWork(final boolean useFreqCrit, final int leadTime)
'''
pass
def calculateTodaysDateWithObjectTimeZoneRule():
'''public Date calculateTodaysDateWithObjectTimeZoneRule()
'''
pass
def checkSeason():
'''public Date checkSeason(final Date origGenDate, final int totalLeadTime)
'''
pass
def setLinearAssetFieldsReadOnly():
'''public void setLinearAssetFieldsReadOnly(final boolean readonlystate)
'''
pass
def clearLinearAssetFields():
'''public void clearLinearAssetFields()
'''
pass
def getJobPlanToUse():
'''public void getJobPlanToUse()
'''
pass
def validateAssetLoc():
'''public void validateAssetLoc(boolean newAssetNum, boolean newLocation)
'''
pass
def updateTimeBasedNextDueDate():
'''public void updateTimeBasedNextDueDate()
'''
pass
def checkDate():
'''public Date checkDate()
'''
pass
def setPMCounter():
'''public void setPMCounter(final int count)
'''
pass
def updateJpSeqInUse():
'''public void updateJpSeqInUse()
'''
pass
def copyNextJobPlan():
'''public void copyNextJobPlan()
'''
pass
def canViewJpSequence():
'''public void canViewJpSequence()
'''
pass
def viewJpSequence():
'''public MboSetRemote viewJpSequence()
'''
pass
def clearNextDueDate():
'''public void clearNextDueDate()
'''
pass
def setNextDueDate():
'''public void setNextDueDate()
'''
pass
def getGeneratedWonum():
'''public String getGeneratedWonum(final int priority)
'''
pass
def duplicate():
'''public MboRemote duplicate()
'''
pass
def isChangeByUserWhenSetFromLookup():
'''public boolean isChangeByUserWhenSetFromLookup(final String lookupAttrName, final String attributeName)
'''
pass
def checkForOpenWO():
'''public boolean checkForOpenWO()
'''
pass
def floatingPMHasOpenWOs():
'''public boolean floatingPMHasOpenWOs()
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
def getChildren():
'''public MboSetRemote getChildren()
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
def getMeterNextDueDate():
'''public Date getMeterNextDueDate(final MboRemote pmMeter, final boolean assetMeter)
'''
pass
def addJobPlanDuration():
'''public Date addJobPlanDuration(Date dueDate, final MboRemote retWOGen)
'''
pass
def getMeterNextDueDateNoForecast():
'''public Date getMeterNextDueDateNoForecast(final MboRemote pmMeter, final boolean assetMeter)
'''
pass
def getTimeDate():
'''public Date getTimeDate()
'''
pass
def validateMetersinMasterPM():
'''public void validateMetersinMasterPM(final String assetnum, final String location, final String masterpm)
'''
pass
def getStatusListName():
'''public String getStatusListName()
'''
pass
def checkFrequency():
'''public Date checkFrequency(final int frequency, final Date nextDueDate, final int unit)
'''
pass
def validateTimeBasedFreq():
'''public void validateTimeBasedFreq(final double frequency)
'''
pass
def setEarliestNextDueDate():
'''public void setEarliestNextDueDate()
'''
pass
def woCancel():
'''public void woCancel(final WORemote newWO)
'''
pass
def truncateHierarchy():
'''public boolean truncateHierarchy(final boolean forecast)
'''
pass
def includeInForecast():
'''public boolean includeInForecast()
'''
pass
def getDueDateForOpenWO():
'''public Date getDueDateForOpenWO(final MboRemote openWo)
'''
pass
def getDueDateForOpenWOWithoutFrequency():
'''public Date getDueDateForOpenWOWithoutFrequency(final MboRemote openWo)
'''
pass
def controlScheduleEarlyOnFreqConflictFlag():
'''public void controlScheduleEarlyOnFreqConflictFlag(final boolean reset)
'''
pass
def isFrequencyValidForEarlySchedConflict():
'''public boolean isFrequencyValidForEarlySchedConflict()
public boolean isFrequencyValidForEarlySchedConflict(final long frequency)
'''
pass
def enableScheduleEarlyOnFreqConflict():
'''public void enableScheduleEarlyOnFreqConflict(final boolean enable, final boolean reset)
'''
pass
def getActiveDaysAddOn():
'''public Date getActiveDaysAddOn(final Date dtDate)
'''
pass
def generateForecast():
'''public void generateForecast(final String genDuration)
public void generateForecast(final int genDuration)
'''
pass
def throwForecastWarning():
'''public void throwForecastWarning(final MXException exception)
'''
pass
def setPMForReForecast():
'''public int setPMForReForecast(final PM tempPM, final int genDuration)
'''
pass
def getReForecastingNextDate():
'''public Date getReForecastingNextDate(final Date fromDate)
'''
pass
def getLastPMForecastRecord():
'''public MboRemote getLastPMForecastRecord()
'''
pass
def getLastPMForecastDate():
'''public Date getLastPMForecastDate()
'''
pass
def getFirstPMForecastRecord():
'''public MboRemote getFirstPMForecastRecord()
'''
pass
def getFirstPMForecastDate():
'''public Date getFirstPMForecastDate()
'''
pass
def isFirstForecastRecord():
'''public boolean isFirstForecastRecord(final PMForecast pmForecast)
'''
pass
def canReforecastForUntilDate():
'''public void canReforecastForUntilDate(final Date lastForecastDate, final Date untilDate)
'''
pass
def deleteSetForecast():
'''public void deleteSetForecast()
'''
pass
def canDeletePMForecast():
'''public void canDeletePMForecast()
'''
pass
def deleteForecast():
'''public void deleteForecast()
public void deleteForecast(final String nullValue)
'''
pass
def deletePMForecast():
'''public void deletePMForecast()
'''
pass
def deleteForecastForPMHierarchy():
'''public void deleteForecastForPMHierarchy()
'''
pass
def deleteForecastForHierarchyChange():
'''public void deleteForecastForHierarchyChange()
'''
pass
def canDeleteForecast():
'''public boolean canDeleteForecast(final String message)
public boolean canDeleteForecast(final String message, final MboValue fieldValue)
'''
pass
def canDisplayForecast():
'''public boolean canDisplayForecast()
'''
pass
def rolldownLockForecastFlagToChildren():
'''public void rolldownLockForecastFlagToChildren(final boolean torf)
'''
pass
def rolldownInclForecastFlagToChildren():
'''public void rolldownInclForecastFlagToChildren(final boolean torf)
'''
pass
def rolldownFieldValueToChildrens():
'''public void rolldownFieldValueToChildrens(final String fieldname, final String fieldvalue, final long accessModifier)
'''
pass
def canGenerateChildPMForecast():
'''public void canGenerateChildPMForecast()
'''
pass
def setCanDeleteForecastFlag():
'''public void setCanDeleteForecastFlag(final boolean flag)
'''
pass
def getCanDeleteForecastFlag():
'''public boolean getCanDeleteForecastFlag()
'''
pass
def reforecastSubsequentDates():
'''public void reforecastSubsequentDates()
public void reforecastSubsequentDates(final PMForecast newDatePMForecast)
public void reforecastSubsequentDates(final MboRemote newDatePMForecast, final MboSetRemote pmForecastSet)
public void reforecastSubsequentDates(final String nullValue)
'''
pass
def setPMForReforecastSubsequentDates():
'''public void setPMForReforecastSubsequentDates(final Date newDate)
'''
pass
def getDurationToForecast():
'''public int getDurationToForecast(final MboRemote pmForecast, final MboSetRemote pmForecastSet)
'''
pass
def getCalendarTime():
'''public Calendar getCalendarTime(final Date date)
'''
pass
def getDurationBetweenTwoDates():
'''public int getDurationBetweenTwoDates(final Date toDate, final Date fromDate)
'''
pass
def canReforecast():
'''public boolean canReforecast()
'''
pass
def setUserChoiceForReforecast():
'''public void setUserChoiceForReforecast(final int userChoiceForReforecast)
'''
pass
def getUserChoiceForReforecast():
'''public int getUserChoiceForReforecast()
'''
pass
def canReforecastSubsequentDates():
'''public int canReforecastSubsequentDates(final PMForecast newDatePMForecast)
'''
pass
def clearReforecast():
'''public void clearReforecast()
'''
pass
def isReforecastPending():
'''public boolean isReforecastPending()
'''
pass
def editOnlyFirstPMForecastRecord():
'''public boolean editOnlyFirstPMForecastRecord()
'''
pass
def throwOKCANCELMessage():
'''public boolean throwOKCANCELMessage(final String message)
'''
pass
def setOnSKDPMListTab():
'''public void setOnSKDPMListTab(final boolean listTab)
'''
pass
def onSKDPMListTab():
'''public boolean onSKDPMListTab()
'''
pass
def resetlastPMForecastRecord():
'''public void resetlastPMForecastRecord()
'''
pass
def setDeleteForecastFlag():
'''public void setDeleteForecastFlag(final boolean flag)
'''
pass
def getDeleteForecastFlag():
'''public boolean getDeleteForecastFlag()
'''
pass
def editPMDeleteForecast():
'''public void editPMDeleteForecast()
public void editPMDeleteForecast(final MboValue fieldValue)
'''
pass
def canUpdateForecastJobPlans():
'''public boolean canUpdateForecastJobPlans()
'''
pass
def updateForecastJobPlans():
'''public void updateForecastJobPlans()
'''
pass
def addPlusCPMExtDate():
'''public void addPlusCPMExtDate(final boolean setPrevDate, final Date extdate, final boolean hasToSave, final String comments, final String commentsLD)
public void addPlusCPMExtDate(final boolean setPrevDate, final Date extdate, final boolean hasToSave, final String comments)
'''
pass
def canAddPMExtDate():
'''public boolean canAddPMExtDate()
'''
pass
def getAsset():
'''public AssetRemote getAsset()
'''
pass
def getLocation():
'''public LocationRemote getLocation()
'''
pass
def canOverride():
'''public void canOverride()
'''
pass
def getWorkType():
'''public String getWorkType()
'''
pass
def getWorkTypeCal():
'''public String getWorkTypeCal()
'''
pass
def isCalibrationInstalled():
'''public boolean isCalibrationInstalled()
'''
pass
def regenerateForecast():
'''public int regenerateForecast(final String message)
'''
pass
def forecastDateBeforeToday():
'''public boolean forecastDateBeforeToday(final MboRemote pmforecast)
'''
pass
def checkForecastForGenWork():
'''public void checkForecastForGenWork()
'''
pass
def canGenerateForecastWork():
'''public int canGenerateForecastWork(final boolean useFreqCrit)
'''
pass
def lockUnlockForecast():
'''public void lockUnlockForecast(final boolean lockForecast)
'''
pass
def checkJPSeq():
'''public boolean checkJPSeq()
'''
pass
def AddPMForecastJPRecord():
'''public void AddPMForecastJPRecord(final String rootancestor, final MboRemote cancelledWO)
'''
pass
def canLockUnlockChildPMForecast():
'''public void canLockUnlockChildPMForecast()
'''
pass
def hasForecast():
'''public boolean hasForecast()
'''
pass
def clearPmDeleteForecastVector():
'''public void clearPmDeleteForecastVector()
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
def getTargStartDate():
'''public Date getTargStartDate(final Date date, final String calledFromFlag)
'''
pass
def getPMNextDate():
'''public Date getPMNextDate(final Date date, final String calledFromFlag)
'''
pass
def getPMLastCompDate():
'''public Date getPMLastCompDate(final Date date, final String calledFromFlag)
'''
pass
def getPMLastStartDate():
'''public Date getPMLastStartDate(final Date date, final String calledFromFlag)
'''
pass
def getPMDueDate():
'''public Date getPMDueDate(final Date date, final String calledFromFlag)
'''
pass
def getPMExtDate():
'''public Date getPMExtDate(final Date date, final String calledFromFlag)
'''
pass
def getPMForecastDate():
'''public Date getPMForecastDate(final Date date, final String calledFromFlag)
'''
pass
def getDateWithTimeZone():
'''public Date getDateWithTimeZone(final Date date)
'''
pass
def getDateWithServerTimeZone():
'''public Date getDateWithServerTimeZone(Date date)
'''
pass
def getDateWithObjectTimeZone():
'''public Date getDateWithObjectTimeZone(Date date)
'''
pass
def storeResourceDataForForecast():
'''public void storeResourceDataForForecast()
'''
pass
def getResourcesForForecastSegement():
'''public void getResourcesForForecastSegement(final MboRemote jobplan, final MboRemote pmforecastJP)
'''
pass
def getGeneratedWonumAndWorkOrderId():
'''public Object[] getGeneratedWonumAndWorkOrderId(final int priority)
'''
pass
def getJPNumWithDate():
'''public String getJPNumWithDate(final Date date, final String jpnum)
'''
pass
def getWOSavedInDB():
'''public MboRemote getWOSavedInDB(final MboRemote woGenerated)
'''
pass
