def ():
    '''returns AMCrewLabor\n\n
    (final MboSet ms)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
def checkForCrewAlreadyAssigned():
    '''returns boolean\n\n
    checkForCrewAlreadyAssigned(final String laborCode, final Date EffectiveDate)\n
    '''
def checkForCalShifNum():
    '''returns boolean\n\n
    checkForCalShifNum()\n
    '''
def checkForValidQualification():
    '''returns boolean\n\n
    checkForValidQualification(final String sPosition)\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def getStandardRate():
    '''returns double\n\n
    getStandardRate()\n
    '''
def getEffectiveDate():
    '''returns Date\n\n
    getEffectiveDate(Date effectivedate)\n
    '''
def checkForLaborAlreadyAssigned():
    '''returns None\n\n
    checkForLaborAlreadyAssigned(final String laborCode, final Date SpecifiedEffectiveDate)\n
    '''
def checkForDatesOverlapping():
    '''returns None\n\n
    checkForDatesOverlapping(final MboRemote mbo)\n
    '''
def checkForRules():
    '''returns None\n\n
    checkForRules(final MboRemote mbo)\n
    '''
def isDatesOverlapping():
    '''returns boolean\n\n
    isDatesOverlapping()\n
    '''
def setisDatesOverlapping():
    '''returns None\n\n
    setisDatesOverlapping(final boolean datesOverlapping)\n
    '''
def setValidateLaborField():
    '''returns None\n\n
    setValidateLaborField(final boolean validateLaborField)\n
    '''
def getValidateLaborField():
    '''returns boolean\n\n
    getValidateLaborField()\n
    '''
def setValidateCraftField():
    '''returns None\n\n
    setValidateCraftField(final boolean validateCraftField)\n
    '''
def getValidateCraftField():
    '''returns boolean\n\n
    getValidateCraftField()\n
    '''
def setValidateSkillLevelField():
    '''returns None\n\n
    setValidateSkillLevelField(final boolean validateSkillLevelField)\n
    '''
def getValidateSkillLevelField():
    '''returns boolean\n\n
    getValidateSkillLevelField()\n
    '''
def setValidateVendorField():
    '''returns None\n\n
    setValidateVendorField(final boolean validateVendorField)\n
    '''
def getValidateVendorField():
    '''returns boolean\n\n
    getValidateVendorField()\n
    '''
def setValidateContractField():
    '''returns None\n\n
    setValidateContractField(final boolean validateContractField)\n
    '''
def getValidateContractField():
    '''returns boolean\n\n
    getValidateContractField()\n
    '''
def setEffectiveDateIsLater():
    '''returns None\n\n
    setEffectiveDateIsLater(final boolean laterEffectivedate)\n
    '''
def isLaterEffectiveDate():
    '''returns boolean\n\n
    isLaterEffectiveDate()\n
    '''
def setEarlierEndDate():
    '''returns None\n\n
    setEarlierEndDate(final boolean earlierEndDate)\n
    '''
def isEndDateEarlier():
    '''returns boolean\n\n
    isEndDateEarlier()\n
    '''
def findAvailableTime():
    '''returns double\n\n
    findAvailableTime(final Date shiftStart, final Date shiftEnd, final Date crewDate)\n
    '''
def setCreatedBySplit():
    '''returns None\n\n
    setCreatedBySplit(final boolean cbs)\n
    '''
def getCreatedBySplit():
    '''returns boolean\n\n
    getCreatedBySplit()\n
    '''
def getHasCrewPrompt():
    '''returns boolean\n\n
    getHasCrewPrompt()\n
    '''
def setHasCrewPrompt():
    '''returns None\n\n
    setHasCrewPrompt(final boolean prompt)\n
    '''
