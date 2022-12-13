NOCHANGESTATUSCHECK = "long  2097152L"
def PmCfgStatusHandler():
'''public PmCfgStatusHandler(final CI ci)
'''
pass
def checkStatusChangeAuthorization():
'''public void checkStatusChangeAuthorization(final String desiredStatus)
'''
pass
def canChangeStatus():
'''public void canChangeStatus(final String currentStatus, final String desiredStatus, final long accessModifier)
'''
pass
def preStatusChange():
'''public void preStatusChange(final String currentStatus, final String desiredStatus, final Date asOfDate, final String memo)
'''
pass
def changeStatus():
'''public void changeStatus(final String currentStatus, final String desiredStatus, final Date asOfDate, final String memo)
'''
pass
def validate():
'''public void validate(final String status, final boolean checkRFC, final boolean useDefault)
public void validate()
public void validate(final boolean checkRFC, final boolean useDefault)
public void validate(final boolean useDefault)
'''
pass
def setDefaultStatus():
'''public void setDefaultStatus(final boolean isDefault)
'''
pass
def isProtected():
'''public boolean isProtected(final MboRemote lifecycle, final String status)
'''
pass
def isDefault():
'''public boolean isDefault(final MboRemote lifecycle, final String status)
'''
pass
def getDefaultStatus():
'''public String getDefaultStatus()
'''
pass
