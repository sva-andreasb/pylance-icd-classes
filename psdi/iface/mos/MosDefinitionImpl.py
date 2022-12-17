def ():
    '''returns MosDefinitionImpl\n\n
    ()\n
    '''
def setDefinitionMetaData():
    '''returns None\n\n
    setDefinitionMetaData(final Map<String, ?> defnMetaData)\n
    '''
def forceDiscardChildMboSet():
    '''returns boolean\n\n
    forceDiscardChildMboSet(final boolean event, final MboSetRemote mboSet, final MosDetailInfo msd)\n
    '''
def createNewMbo():
    '''returns MboRemote\n\n
    createNewMbo(final MboSetRemote mboSet)\n
    '''
def checkBusinessRules():
    '''returns int\n\n
    checkBusinessRules(final MboRemote mbo, final MosDetailInfo mosDetInfo, final Map<String, Object> ovrdColValueMap)\n
    '''
def applyAPICondition():
    '''returns int\n\n
    applyAPICondition(final MboRemote mbo, final MosDetailInfo mosDetInfo)\n
    '''
def postSerializationRules():
    '''returns None\n\n
    postSerializationRules(final MboRemote mbo, final MosDetailInfo mosDetInfo)\n
    '''
def getColumnsToSkip():
    '''returns Set<String>\n\n
    getColumnsToSkip(final MboRemote mbo)\n
    '''
def serializationEnd():
    '''returns byte[]\n\n
    serializationEnd(final byte[] serializedData)\n
    '''
def myCompletedList():
    '''returns None\n\n
    myCompletedList(final MboSetRemote msr, final String queryName, final String app, final String owner)\n
    '''
def myNotCompletedList():
    '''returns None\n\n
    myNotCompletedList(final MboSetRemote msr, final String queryName, final String app, final String owner)\n
    '''
