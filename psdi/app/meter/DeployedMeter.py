def DeployedMeter():
    '''    public DeployedMeter(final MboSet ms)
    '''
def isNegativeAdjustment():
    '''    public boolean isNegativeAdjustment()
    '''
def setAdjustmentIsNegative():
    '''    public void setAdjustmentIsNegative(final boolean adjustmentIsNegative)
    '''
def modify():
    '''    public void modify()
    '''
def addModifiedReadingsForAvgCalc():
    '''    public void addModifiedReadingsForAvgCalc(final MboRemote reading)
    '''
def getOrigMRUpdate():
    '''    public Mbo getOrigMRUpdate()
    '''
def setOrigMRUpdate():
    '''    public void setOrigMRUpdate(final Mbo origMRUpdate)
    '''
def returnDeploymentInfo():
    '''    public Object[] returnDeploymentInfo()
    '''
def isReadingMostRecentReading():
    '''    public boolean isReadingMostRecentReading(final Date readingDate)
    '''
def setIsReadingUpdate():
    '''    public void setIsReadingUpdate(final boolean isUpdate)
    '''
def getIsReadingUpdate():
    '''    public boolean getIsReadingUpdate()
    '''
def getIsWOMeterProcess():
    '''    public boolean getIsWOMeterProcess()
    '''
def getSupressUniquenessErrorFlag():
    '''    public boolean getSupressUniquenessErrorFlag()
    '''
def getNextMeterReading():
    '''    public MboRemote getNextMeterReading(Date followingDate)
    '''
def add():
    '''    public void add()
    '''
def canDelete():
    '''    public void canDelete()
    '''
def canDeleteForecast():
    '''    public boolean canDeleteForecast(final String message)
    '''
def delete():
    '''    public void delete(final long accessModifier)
    '''
def undelete():
    '''    public void undelete()
    '''
def meterInGroupToDeployedMeter():
    '''    public void meterInGroupToDeployedMeter(final MeterInGroupRemote meter, final boolean supressUniquenessError)
    public void meterInGroupToDeployedMeter(final MeterInGroupRemote meter, final boolean supressUniquenessError, final boolean supressDupSeqNumWarning)
    '''
def isCurrentlyBeingAddedOnMeterGroupChange():
    '''    public boolean isCurrentlyBeingAddedOnMeterGroupChange()
    '''
def setCurrentlyBeingAddedOnMeterGroupChange():
    '''    public void setCurrentlyBeingAddedOnMeterGroupChange(final boolean currentlyBeingAddedOnMeterGroupChange)
    '''
def init():
    '''    public void init()
    '''
def getAvgCalcMethod():
    '''    public String getAvgCalcMethod()
    '''
def getReadingType():
    '''    public String getReadingType()
    '''
def getTheMeter():
    '''    public MeterRemote getTheMeter()
    '''
def setSkipAverageRefresh():
    '''    public void setSkipAverageRefresh(final boolean actReadInUpdateRangeAfterNewRead)
    '''
def getSkipAverageRefresh():
    '''    public boolean getSkipAverageRefresh()
    '''
def setTypeSpecificFlags():
    '''    public void setTypeSpecificFlags()
    '''
def enableDisable():
    '''    public void enableDisable()
    '''
def refreshPreviousReadingInfo():
    '''    public void refreshPreviousReadingInfo(final Date previousToDate)
    '''
def getPreviousMeterReading():
    '''    public MboRemote getPreviousMeterReading(Date previousToDate)
    '''
def getReadingValueAsDouble():
    '''    public double getReadingValueAsDouble(final Date dt)
    '''
def getMeterReadingForKnownDate():
    '''    public MboRemote getMeterReadingForKnownDate(final Date dt)
    '''
def setPreviousReadingInfoOnInit():
    '''    public void setPreviousReadingInfoOnInit()
    '''
def getValidateOrder():
    '''    public String[] getValidateOrder()
    '''
def appValidate():
    '''    public void appValidate()
    '''
def processNonContinuousReadings():
    '''    public void processNonContinuousReadings()
    '''
def addReading():
    '''    public MboRemote addReading()
    '''
def maintainWOMeter():
    '''    public void maintainWOMeter(final MboRemote reading)
    '''
def returnReadingForWOMeterProcessing():
    '''    public MboRemote returnReadingForWOMeterProcessing()
    '''
def resetMeter():
    '''    public void resetMeter()
    '''
def save():
    '''    public void save()
    '''
def enterReadingOnMaterialIssue():
    '''    public boolean enterReadingOnMaterialIssue()
    '''
def validateALNEnteredDecimalValue():
    '''    public void validateALNEnteredDecimalValue(final String readingAttribute)
    '''
def pmForecastExistsForMeterOnPM():
    '''    public boolean pmForecastExistsForMeterOnPM()
    '''
def validateALNValueForDecimalUse():
    '''    public validateALNValueForDecimalUse()
    '''
def getDecimalRegex():
    '''    public String getDecimalRegex(final Locale locale)
    '''
