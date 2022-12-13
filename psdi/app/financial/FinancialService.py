def FinancialService():
'''public FinancialService()
public FinancialService(final MXServer mxServer)
'''
pass
def validateFullGLAccount():
'''public boolean validateFullGLAccount(final UserInfo user, final String account, final String orgID)
'''
pass
def validatePartialGLAccount():
'''public boolean validatePartialGLAccount(final UserInfo user, final String account, final String orgID)
'''
pass
def getSpecificFinancialPeriod():
'''public String getSpecificFinancialPeriod(final UserInfo user, final Date transDate, final String orgID)
'''
pass
def getActiveFinancialPeriod():
'''public String getActiveFinancialPeriod(final UserInfo user, final Date transDate, final String orgID)
public String getActiveFinancialPeriod(final UserInfo user, final Date transDate, final String orgID, final Boolean useNextPeriodIfInactive)
'''
pass
def getAccountDefaults():
'''public String getAccountDefaults(final UserInfo user, final String defaultGroup, final String groupValue, final String orgID)
public String getAccountDefaults(final UserInfo user, final String defaultGroup, final String orgID)
'''
pass
def validateTax():
'''public boolean validateTax(final UserInfo user, final String typeCode, final String taxCode, final String orgID)
'''
pass
def getTaxRate():
'''public double getTaxRate(final UserInfo user, final String typeCode, final String taxCode, final String orgID)
'''
pass
def getAddTaxIndcr():
'''public int getAddTaxIndcr(final UserInfo user, final String typeCode, final String orgID, final MboRemote mbo)
'''
pass
def getIncludeTax():
'''public boolean[] getIncludeTax(final UserInfo user, final String typeCode, final String orgID, final MboRemote mbo)
'''
pass
def getTaxTypeSet():
'''public MboSetRemote getTaxTypeSet(final UserInfo user, final String typeCode, final String orgID, final MboRemote mbo)
'''
pass
def getTaxSet():
'''public MboSetRemote getTaxSet(final UserInfo user, final String typeCode, final String taxCode, final String orgID, final MboRemote mbo)
'''
pass
def isFullySpecified():
'''public boolean isFullySpecified(final UserInfo user, final String account, final String orgID)
'''
pass
def update():
'''public void update(final UserInfo user, final String updateDBCriteria, final String orgID)
'''
pass
def glRequiredForTrans():
'''public boolean glRequiredForTrans(final UserInfo user, final String orgID)
'''
pass
def setGLDefaultDescription():
'''public void setGLDefaultDescription(final MboRemote chartOfAccount)
'''
pass
def getActiveFinancialPeriodInfo():
'''public Vector getActiveFinancialPeriodInfo(final UserInfo user, final Date transDate, final String orgID)
'''
pass
def validateFinancialPeriod():
'''public Boolean validateFinancialPeriod(final UserInfo user, final Date transDate, final String orgID)
'''
pass
def basicAccountSetup():
'''public void basicAccountSetup(final String orgid, final String compname, final String compvalue, final String comptext, final UserInfo userInfo)
'''
pass
def disableGLValidation():
'''public void disableGLValidation(final String orgid, final UserInfo userInfo)
'''
pass
def resetGLOrder():
'''public void resetGLOrder(final String orgid, final UserInfo userInfo)
'''
pass
def advancedAccountSetup():
'''public void advancedAccountSetup(final Map<String, Object> components, final String compvalue, final UserInfo userInfo)
'''
pass
def componenetsSetup():
'''public void componenetsSetup(final Map<String, Object> components, final String orgid, final String compvalue, final MXTransaction trans, final UserInfo userInfo)
'''
pass
def setupFinancialPeriods():
'''public void setupFinancialPeriods(final String orgid, final String period, final String startmonth, final int numyears, final boolean disableperiods, final UserInfo userInfo)
'''
pass
def setupFinancialPeriodsFull():
'''public void setupFinancialPeriodsFull(final String orgid, String period, String startmonth, final int numyears, final boolean disableperiods, final UserInfo userInfo, final boolean updateApptracker)
'''
pass
def skipSetup():
'''public void skipSetup(final UserInfo userInfo)
'''
pass
def updateApptracker():
'''public void updateApptracker(final JSONArray ja, final boolean complete, final UserInfo userInfo, MXTransaction trans)
'''
pass
def addCOA():
'''public void addCOA(final String orgid, final String compvalue, final String comptext, final UserInfo userInfo, final MXTransaction trans)
'''
pass
