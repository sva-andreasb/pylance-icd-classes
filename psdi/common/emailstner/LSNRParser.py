def ():
    '''returns LSNRParser\n\n
    ()\n
    '''
def emailFormatMode():
    '''returns int\n\n
    emailFormatMode(final MboRemote inboundComm)\n
    '''
def getObjectName():
    '''returns String\n\n
    getObjectName(final MboRemote inboundComm, final int formatMode)\n
    '''
def getActionName():
    '''returns String\n\n
    getActionName(final MboRemote inboundComm, final int formatMode)\n
    '''
def isPrimaryKeyProvided():
    '''returns boolean\n\n
    isPrimaryKeyProvided(final MboRemote inboundComm, final String objectName, final Hashtable has)\n
    '''
def getPrimaryKeyCols():
    '''returns String[]\n\n
    getPrimaryKeyCols(final MboRemote inboundComm)\n
    '''
def getAttributeValues():
    '''returns Hashtable\n\n
    getAttributeValues(final MboRemote inboundComm, final int formatMode)\n
    '''
def readFormattedMessageToHashtable():
    '''returns Hashtable\n\n
    readFormattedMessageToHashtable(final MboRemote inboundComm, final int formatMode)\n
    '''
def getWhereClauseForQuery():
    '''returns String\n\n
    getWhereClauseForQuery(final MboRemote inboundComm, final int formatMode)\n
    '''
def getResultColumnsForQuery():
    '''returns String\n\n
    getResultColumnsForQuery(final MboRemote inboundComm, final int formatMode)\n
    '''
