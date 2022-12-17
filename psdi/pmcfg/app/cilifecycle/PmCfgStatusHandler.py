NOCHANGESTATUSCHECK = "long  2097152L"
def ():
    '''returns PmCfgStatusHandler\n\n
    (final CI ci)\n
    '''
def checkStatusChangeAuthorization():
    '''returns None\n\n
    checkStatusChangeAuthorization(final String desiredStatus)\n
    '''
def canChangeStatus():
    '''returns None\n\n
    canChangeStatus(final String currentStatus, final String desiredStatus, final long accessModifier)\n
    '''
def preStatusChange():
    '''returns None\n\n
    preStatusChange(final String currentStatus, final String desiredStatus, final Date asOfDate, final String memo)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String currentStatus, final String desiredStatus, final Date asOfDate, final String memo)\n
    '''
def validate():
    '''returns None\n\n
    validate(final String status, final boolean checkRFC, final boolean useDefault)\n
    validate()\n
    validate(final boolean checkRFC, final boolean useDefault)\n
    validate(final boolean useDefault)\n
    '''
def setDefaultStatus():
    '''returns None\n\n
    setDefaultStatus(final boolean isDefault)\n
    '''
def isProtected():
    '''returns boolean\n\n
    isProtected(final MboRemote lifecycle, final String status)\n
    '''
def isDefault():
    '''returns boolean\n\n
    isDefault(final MboRemote lifecycle, final String status)\n
    '''
def getDefaultStatus():
    '''returns String\n\n
    getDefaultStatus()\n
    '''
