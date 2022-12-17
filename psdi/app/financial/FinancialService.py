def ():
    '''returns FinancialService\n\n
    ()\n
    (final MXServer mxServer)\n
    '''
def validateFullGLAccount():
    '''returns boolean\n\n
    validateFullGLAccount(final UserInfo user, final String account, final String orgID)\n
    '''
def validatePartialGLAccount():
    '''returns boolean\n\n
    validatePartialGLAccount(final UserInfo user, final String account, final String orgID)\n
    '''
def getSpecificFinancialPeriod():
    '''returns String\n\n
    getSpecificFinancialPeriod(final UserInfo user, final Date transDate, final String orgID)\n
    '''
def getActiveFinancialPeriod():
    '''returns String\n\n
    getActiveFinancialPeriod(final UserInfo user, final Date transDate, final String orgID)\n
    getActiveFinancialPeriod(final UserInfo user, final Date transDate, final String orgID, final Boolean useNextPeriodIfInactive)\n
    '''
def getAccountDefaults():
    '''returns String\n\n
    getAccountDefaults(final UserInfo user, final String defaultGroup, final String groupValue, final String orgID)\n
    getAccountDefaults(final UserInfo user, final String defaultGroup, final String orgID)\n
    '''
def validateTax():
    '''returns boolean\n\n
    validateTax(final UserInfo user, final String typeCode, final String taxCode, final String orgID)\n
    '''
def getTaxRate():
    '''returns double\n\n
    getTaxRate(final UserInfo user, final String typeCode, final String taxCode, final String orgID)\n
    '''
def getAddTaxIndcr():
    '''returns int\n\n
    getAddTaxIndcr(final UserInfo user, final String typeCode, final String orgID, final MboRemote mbo)\n
    '''
def getIncludeTax():
    '''returns boolean[]\n\n
    getIncludeTax(final UserInfo user, final String typeCode, final String orgID, final MboRemote mbo)\n
    '''
def getTaxTypeSet():
    '''returns MboSetRemote\n\n
    getTaxTypeSet(final UserInfo user, final String typeCode, final String orgID, final MboRemote mbo)\n
    '''
def getTaxSet():
    '''returns MboSetRemote\n\n
    getTaxSet(final UserInfo user, final String typeCode, final String taxCode, final String orgID, final MboRemote mbo)\n
    '''
def isFullySpecified():
    '''returns boolean\n\n
    isFullySpecified(final UserInfo user, final String account, final String orgID)\n
    '''
def update():
    '''returns None\n\n
    update(final UserInfo user, final String updateDBCriteria, final String orgID)\n
    '''
def glRequiredForTrans():
    '''returns boolean\n\n
    glRequiredForTrans(final UserInfo user, final String orgID)\n
    '''
def setGLDefaultDescription():
    '''returns None\n\n
    setGLDefaultDescription(final MboRemote chartOfAccount)\n
    '''
def getActiveFinancialPeriodInfo():
    '''returns Vector\n\n
    getActiveFinancialPeriodInfo(final UserInfo user, final Date transDate, final String orgID)\n
    '''
def validateFinancialPeriod():
    '''returns Boolean\n\n
    validateFinancialPeriod(final UserInfo user, final Date transDate, final String orgID)\n
    '''
def basicAccountSetup():
    '''returns None\n\n
    basicAccountSetup(final String orgid, final String compname, final String compvalue, final String comptext, final UserInfo userInfo)\n
    '''
def disableGLValidation():
    '''returns None\n\n
    disableGLValidation(final String orgid, final UserInfo userInfo)\n
    '''
def resetGLOrder():
    '''returns None\n\n
    resetGLOrder(final String orgid, final UserInfo userInfo)\n
    '''
def advancedAccountSetup():
    '''returns None\n\n
    advancedAccountSetup(final Map<String, Object> components, final String compvalue, final UserInfo userInfo)\n
    '''
def componenetsSetup():
    '''returns None\n\n
    componenetsSetup(final Map<String, Object> components, final String orgid, final String compvalue, final MXTransaction trans, final UserInfo userInfo)\n
    '''
def setupFinancialPeriods():
    '''returns None\n\n
    setupFinancialPeriods(final String orgid, final String period, final String startmonth, final int numyears, final boolean disableperiods, final UserInfo userInfo)\n
    '''
def setupFinancialPeriodsFull():
    '''returns None\n\n
    setupFinancialPeriodsFull(final String orgid, String period, String startmonth, final int numyears, final boolean disableperiods, final UserInfo userInfo, final boolean updateApptracker)\n
    '''
def skipSetup():
    '''returns None\n\n
    skipSetup(final UserInfo userInfo)\n
    '''
def updateApptracker():
    '''returns None\n\n
    updateApptracker(final JSONArray ja, final boolean complete, final UserInfo userInfo, MXTransaction trans)\n
    '''
def addCOA():
    '''returns None\n\n
    addCOA(final String orgid, final String compvalue, final String comptext, final UserInfo userInfo, final MXTransaction trans)\n
    '''
