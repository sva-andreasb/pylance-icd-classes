NOCHANGESTATUSCHECK = "long  2097152L"
def PmCfgStatusHandler():
    '''    public PmCfgStatusHandler(final CI ci)
    '''
def checkStatusChangeAuthorization():
    '''    public void checkStatusChangeAuthorization(final String desiredStatus)
    '''
def canChangeStatus():
    '''    public void canChangeStatus(final String currentStatus, final String desiredStatus, final long accessModifier)
    '''
def preStatusChange():
    '''    public void preStatusChange(final String currentStatus, final String desiredStatus, final Date asOfDate, final String memo)
    '''
def changeStatus():
    '''    public void changeStatus(final String currentStatus, final String desiredStatus, final Date asOfDate, final String memo)
    '''
def validate():
    '''    public void validate(final String status, final boolean checkRFC, final boolean useDefault)
    public void validate()
    public void validate(final boolean checkRFC, final boolean useDefault)
    public void validate(final boolean useDefault)
    '''
def setDefaultStatus():
    '''    public void setDefaultStatus(final boolean isDefault)
    '''
def isProtected():
    '''    public boolean isProtected(final MboRemote lifecycle, final String status)
    '''
def isDefault():
    '''    public boolean isDefault(final MboRemote lifecycle, final String status)
    '''
def getDefaultStatus():
    '''    public String getDefaultStatus()
    '''
