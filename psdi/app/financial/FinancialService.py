def FinancialService():
    '''public FinancialService()
    public FinancialService(final MXServer mxServer)
    '''
def validateFullGLAccount():
    '''public boolean validateFullGLAccount(final UserInfo user, final String account, final String orgID)
    '''
def validatePartialGLAccount():
    '''public boolean validatePartialGLAccount(final UserInfo user, final String account, final String orgID)
    '''
def getSpecificFinancialPeriod():
    '''public String getSpecificFinancialPeriod(final UserInfo user, final Date transDate, final String orgID)
    '''
def getActiveFinancialPeriod():
    '''public String getActiveFinancialPeriod(final UserInfo user, final Date transDate, final String orgID)
    public String getActiveFinancialPeriod(final UserInfo user, final Date transDate, final String orgID, final Boolean useNextPeriodIfInactive)
    '''
def getAccountDefaults():
    '''public String getAccountDefaults(final UserInfo user, final String defaultGroup, final String groupValue, final String orgID)
    public String getAccountDefaults(final UserInfo user, final String defaultGroup, final String orgID)
    '''
def validateTax():
    '''public boolean validateTax(final UserInfo user, final String typeCode, final String taxCode, final String orgID)
    '''
def getTaxRate():
    '''public double getTaxRate(final UserInfo user, final String typeCode, final String taxCode, final String orgID)
    '''
def getAddTaxIndcr():
    '''public int getAddTaxIndcr(final UserInfo user, final String typeCode, final String orgID, final MboRemote mbo)
    '''
def getIncludeTax():
    '''public boolean[] getIncludeTax(final UserInfo user, final String typeCode, final String orgID, final MboRemote mbo)
    '''
def getTaxTypeSet():
    '''public MboSetRemote getTaxTypeSet(final UserInfo user, final String typeCode, final String orgID, final MboRemote mbo)
    '''
def getTaxSet():
    '''public MboSetRemote getTaxSet(final UserInfo user, final String typeCode, final String taxCode, final String orgID, final MboRemote mbo)
    '''
def isFullySpecified():
    '''public boolean isFullySpecified(final UserInfo user, final String account, final String orgID)
    '''
def update():
    '''public void update(final UserInfo user, final String updateDBCriteria, final String orgID)
    '''
def glRequiredForTrans():
    '''public boolean glRequiredForTrans(final UserInfo user, final String orgID)
    '''
def setGLDefaultDescription():
    '''public void setGLDefaultDescription(final MboRemote chartOfAccount)
    '''
def getActiveFinancialPeriodInfo():
    '''public Vector getActiveFinancialPeriodInfo(final UserInfo user, final Date transDate, final String orgID)
    '''
def validateFinancialPeriod():
    '''public Boolean validateFinancialPeriod(final UserInfo user, final Date transDate, final String orgID)
    '''
def basicAccountSetup():
    '''public void basicAccountSetup(final String orgid, final String compname, final String compvalue, final String comptext, final UserInfo userInfo)
    '''
def disableGLValidation():
    '''public void disableGLValidation(final String orgid, final UserInfo userInfo)
    '''
def resetGLOrder():
    '''public void resetGLOrder(final String orgid, final UserInfo userInfo)
    '''
def advancedAccountSetup():
    '''public void advancedAccountSetup(final Map<String, Object> components, final String compvalue, final UserInfo userInfo)
    '''
def componenetsSetup():
    '''public void componenetsSetup(final Map<String, Object> components, final String orgid, final String compvalue, final MXTransaction trans, final UserInfo userInfo)
    '''
def setupFinancialPeriods():
    '''public void setupFinancialPeriods(final String orgid, final String period, final String startmonth, final int numyears, final boolean disableperiods, final UserInfo userInfo)
    '''
def setupFinancialPeriodsFull():
    '''public void setupFinancialPeriodsFull(final String orgid, String period, String startmonth, final int numyears, final boolean disableperiods, final UserInfo userInfo, final boolean updateApptracker)
    '''
def skipSetup():
    '''public void skipSetup(final UserInfo userInfo)
    '''
def updateApptracker():
    '''public void updateApptracker(final JSONArray ja, final boolean complete, final UserInfo userInfo, MXTransaction trans)
    '''
def addCOA():
    '''public void addCOA(final String orgid, final String compvalue, final String comptext, final UserInfo userInfo, final MXTransaction trans)
    '''
