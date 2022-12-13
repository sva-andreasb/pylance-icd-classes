def MosDefinitionImpl():
    '''public MosDefinitionImpl()
    '''
def setDefinitionMetaData():
    '''public void setDefinitionMetaData(final Map<String, ?> defnMetaData)
    '''
def forceDiscardChildMboSet():
    '''public boolean forceDiscardChildMboSet(final boolean event, final MboSetRemote mboSet, final MosDetailInfo msd)
    '''
def createNewMbo():
    '''public MboRemote createNewMbo(final MboSetRemote mboSet)
    '''
def scriptSkipMboRules():
    '''public final int scriptSkipMboRules(final MboRemote mbo, final MosDetailInfo mosDetInfo)
    '''
def scriptOverrideRules():
    '''public final void scriptOverrideRules(final MboRemote mbo, final MosDetailInfo mosDetInfo, final Map<String, Object> ovrdColValueMap)
    '''
def scriptSkipColRules():
    '''public final Set<String> scriptSkipColRules(final MboRemote mbo, final MosDetailInfo mosDetInfo, final Set<String> skipCols)
    '''
def checkBusinessRules():
    '''public int checkBusinessRules(final MboRemote mbo, final MosDetailInfo mosDetInfo, final Map<String, Object> ovrdColValueMap)
    '''
def applyAPICondition():
    '''public int applyAPICondition(final MboRemote mbo, final MosDetailInfo mosDetInfo)
    '''
def postSerializationRules():
    '''public void postSerializationRules(final MboRemote mbo, final MosDetailInfo mosDetInfo)
    '''
def getColumnsToSkip():
    '''public Set<String> getColumnsToSkip(final MboRemote mbo)
    '''
def serializationEnd():
    '''public byte[] serializationEnd(final byte[] serializedData)
    '''
def myCompletedList():
    '''public void myCompletedList(final MboSetRemote msr, final String queryName, final String app, final String owner)
    '''
def myNotCompletedList():
    '''public void myNotCompletedList(final MboSetRemote msr, final String queryName, final String app, final String owner)
    '''
