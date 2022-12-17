def ():
    '''returns validateALNValueForDecimalUse\n\n
    (final MboSet ms)\n
    ()\n
    '''
def isNegativeAdjustment():
    '''returns boolean\n\n
    isNegativeAdjustment()\n
    '''
def setAdjustmentIsNegative():
    '''returns None\n\n
    setAdjustmentIsNegative(final boolean adjustmentIsNegative)\n
    '''
def modify():
    '''returns None\n\n
    modify()\n
    '''
def addModifiedReadingsForAvgCalc():
    '''returns None\n\n
    addModifiedReadingsForAvgCalc(final MboRemote reading)\n
    '''
def getOrigMRUpdate():
    '''returns Mbo\n\n
    getOrigMRUpdate()\n
    '''
def setOrigMRUpdate():
    '''returns None\n\n
    setOrigMRUpdate(final Mbo origMRUpdate)\n
    '''
def returnDeploymentInfo():
    '''returns Object[]\n\n
    returnDeploymentInfo()\n
    '''
def isReadingMostRecentReading():
    '''returns boolean\n\n
    isReadingMostRecentReading(final Date readingDate)\n
    '''
def setIsReadingUpdate():
    '''returns None\n\n
    setIsReadingUpdate(final boolean isUpdate)\n
    '''
def getIsReadingUpdate():
    '''returns boolean\n\n
    getIsReadingUpdate()\n
    '''
def getIsWOMeterProcess():
    '''returns boolean\n\n
    getIsWOMeterProcess()\n
    '''
def getSupressUniquenessErrorFlag():
    '''returns boolean\n\n
    getSupressUniquenessErrorFlag()\n
    '''
def getNextMeterReading():
    '''returns MboRemote\n\n
    getNextMeterReading(Date followingDate)\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def canDeleteForecast():
    '''returns boolean\n\n
    canDeleteForecast(final String message)\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    '''
def undelete():
    '''returns None\n\n
    undelete()\n
    '''
def meterInGroupToDeployedMeter():
    '''returns None\n\n
    meterInGroupToDeployedMeter(final MeterInGroupRemote meter, final boolean supressUniquenessError)\n
    meterInGroupToDeployedMeter(final MeterInGroupRemote meter, final boolean supressUniquenessError, final boolean supressDupSeqNumWarning)\n
    '''
def isCurrentlyBeingAddedOnMeterGroupChange():
    '''returns boolean\n\n
    isCurrentlyBeingAddedOnMeterGroupChange()\n
    '''
def setCurrentlyBeingAddedOnMeterGroupChange():
    '''returns None\n\n
    setCurrentlyBeingAddedOnMeterGroupChange(final boolean currentlyBeingAddedOnMeterGroupChange)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def getAvgCalcMethod():
    '''returns String\n\n
    getAvgCalcMethod()\n
    '''
def getReadingType():
    '''returns String\n\n
    getReadingType()\n
    '''
def getTheMeter():
    '''returns MeterRemote\n\n
    getTheMeter()\n
    '''
def setSkipAverageRefresh():
    '''returns None\n\n
    setSkipAverageRefresh(final boolean actReadInUpdateRangeAfterNewRead)\n
    '''
def getSkipAverageRefresh():
    '''returns boolean\n\n
    getSkipAverageRefresh()\n
    '''
def setTypeSpecificFlags():
    '''returns None\n\n
    setTypeSpecificFlags()\n
    '''
def enableDisable():
    '''returns None\n\n
    enableDisable()\n
    '''
def refreshPreviousReadingInfo():
    '''returns None\n\n
    refreshPreviousReadingInfo(final Date previousToDate)\n
    '''
def getPreviousMeterReading():
    '''returns MboRemote\n\n
    getPreviousMeterReading(Date previousToDate)\n
    '''
def getReadingValueAsDouble():
    '''returns double\n\n
    getReadingValueAsDouble(final Date dt)\n
    '''
def getMeterReadingForKnownDate():
    '''returns MboRemote\n\n
    getMeterReadingForKnownDate(final Date dt)\n
    '''
def setPreviousReadingInfoOnInit():
    '''returns None\n\n
    setPreviousReadingInfoOnInit()\n
    '''
def getValidateOrder():
    '''returns String[]\n\n
    getValidateOrder()\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def processNonContinuousReadings():
    '''returns None\n\n
    processNonContinuousReadings()\n
    '''
def addReading():
    '''returns MboRemote\n\n
    addReading()\n
    '''
def maintainWOMeter():
    '''returns None\n\n
    maintainWOMeter(final MboRemote reading)\n
    '''
def returnReadingForWOMeterProcessing():
    '''returns MboRemote\n\n
    returnReadingForWOMeterProcessing()\n
    '''
def resetMeter():
    '''returns None\n\n
    resetMeter()\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
def enterReadingOnMaterialIssue():
    '''returns boolean\n\n
    enterReadingOnMaterialIssue()\n
    '''
def validateALNEnteredDecimalValue():
    '''returns None\n\n
    validateALNEnteredDecimalValue(final String readingAttribute)\n
    '''
def pmForecastExistsForMeterOnPM():
    '''returns boolean\n\n
    pmForecastExistsForMeterOnPM()\n
    '''
def getDecimalRegex():
    '''returns String\n\n
    getDecimalRegex(final Locale locale)\n
    '''
