def ():
    '''returns ServerMboAdapter\n\n
    (final Mbo mbo)\n
    '''
def getMbo():
    '''returns Mbo\n\n
    getMbo()\n
    '''
def getMboSet():
    '''returns MboSetAdapter\n\n
    getMboSet(final String relationshipName)\n
    '''
def getThisMboSet():
    '''returns MboSetAdapter\n\n
    getThisMboSet()\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final String attributeName, final String value)\n
    setValue(final String attributeName, final String value, final long flags)\n
    setValue(final String attributeName, final boolean value)\n
    setValue(final String attributeName, final boolean value, final long flags)\n
    setValue(final String attributeName, final int value)\n
    setValue(final String attributeName, final int value, final long flags)\n
    setValue(final String attributeName, final Date value)\n
    setValue(final String attributeName, final Date value, final long flags)\n
    '''
def setValueIfDifferent():
    '''returns None\n\n
    setValueIfDifferent(final String attributeName, final boolean value)\n
    setValueIfDifferent(final String attributeName, final boolean value, final long flags)\n
    '''
def getString():
    '''returns String\n\n
    getString(final String attributeName)\n
    '''
def getBoolean():
    '''returns boolean\n\n
    getBoolean(final String attributeName)\n
    '''
def getInt():
    '''returns int\n\n
    getInt(final String attributeName)\n
    '''
def getDate():
    '''returns Date\n\n
    getDate(final String attributeName)\n
    '''
def isNull():
    '''returns boolean\n\n
    isNull(final String attributeName)\n
    '''
def isReadOnly():
    '''returns boolean\n\n
    isReadOnly(final String attributeName)\n
    '''
def setReadOnly():
    '''returns None\n\n
    setReadOnly(final String attributeName, final boolean readOnly)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getOwner():
    '''returns MboAdapter\n\n
    getOwner()\n
    '''
def newApplicationException():
    '''returns Exception\n\n
    newApplicationException(final String group, final String key, final Object[] params)\n
    newApplicationException(final String group, final String key)\n
    '''
def getMaxVarString():
    '''returns String\n\n
    getMaxVarString(final String maxvarName)\n
    '''
def getMaxVarInt():
    '''returns int\n\n
    getMaxVarInt(final String maxvarName)\n
    '''
def getMaxVarBoolean():
    '''returns boolean\n\n
    getMaxVarBoolean(final String maxvarName)\n
    '''
def toBeDeleted():
    '''returns boolean\n\n
    toBeDeleted()\n
    '''
