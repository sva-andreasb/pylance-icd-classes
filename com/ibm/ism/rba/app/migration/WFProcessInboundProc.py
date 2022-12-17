DOCINFO = "String  \"DOCINFO\""
URLNAME = "String  \"URLNAME\""
DOCLINKS = "String  \"DOCLINKS\""
OWNERTABLE = "String  \"OWNERTABLE\""
OWNERID = "String  \"OWNERID\""
DOCINFOID = "String  \"DOCINFOID\""
DOCTYPE = "String  \"DOCTYPE\""
DOCUMENT = "String  \"DOCUMENT\""
def ():
    '''returns WFProcessInboundProc\n\n
    ()\n
    '''
def checkBusinessRules():
    '''returns int\n\n
    checkBusinessRules()\n
    checkBusinessRules(final MboSetRemote mboSet, final String tableName)\n
    '''
def deleteAll():
    '''returns None\n\n
    deleteAll(final MboRemote owner, final MboSetRemote mboSet)\n
    '''
def setAdditionalData():
    '''returns None\n\n
    setAdditionalData(final MboSetRemote mboSet, final String objectName)\n
    '''
def checkValidateErrors():
    '''returns None\n\n
    checkValidateErrors()\n
    '''
def isNull():
    '''returns boolean\n\n
    isNull(final String t)\n
    '''
def createMboSet():
    '''returns MboSetRemote\n\n
    createMboSet(final boolean isPrimaryMbo, final MboRemote parentMbo, final MosDetailInfo mdi, final String processTable)\n
    '''
def afterReplace():
    '''returns None\n\n
    afterReplace(final MboRemote child)\n
    '''
def delete():
    '''returns None\n\n
    delete(final MboRemote mbo, final MosDetailInfo mdi)\n
    '''
