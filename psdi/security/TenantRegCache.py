def ():
    '''returns TenantRegCache\n\n
    ()\n
    '''
def reload():
    '''returns None\n\n
    reload()\n
    reload(final String key)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def tenantStartupRoutine():
    '''returns None\n\n
    tenantStartupRoutine()\n
    '''
def hasTenant():
    '''returns boolean\n\n
    hasTenant(final int tenantID)\n
    '''
def hasTenantSession():
    '''returns boolean\n\n
    hasTenantSession(final int tenantID)\n
    '''
def setTenantSession():
    '''returns None\n\n
    setTenantSession(final int tenantID)\n
    '''
def removeTenantSession():
    '''returns None\n\n
    removeTenantSession(final int tenantID)\n
    '''
def getTenantIDFromTenantCode():
    '''returns int\n\n
    getTenantIDFromTenantCode(final String tenantCode)\n
    '''
def getTenantCode():
    '''returns String\n\n
    getTenantCode(final UserInfo info)\n
    getTenantCode(final int id)\n
    '''
def getTenantLoginId():
    '''returns String\n\n
    getTenantLoginId(final UserInfo info)\n
    '''
def getPartNumber():
    '''returns String\n\n
    getPartNumber(final int id)\n
    '''
def getDescription():
    '''returns String\n\n
    getDescription(final int id)\n
    '''
def getSubscriptionID():
    '''returns long\n\n
    getSubscriptionID(final UserInfo info)\n
    '''
def getCustomerID():
    '''returns long\n\n
    getCustomerID(final UserInfo info)\n
    '''
def getStartTime():
    '''returns long\n\n
    getStartTime(final int id)\n
    '''
def getNumberOfSeats():
    '''returns long\n\n
    getNumberOfSeats(final UserInfo info)\n
    '''
