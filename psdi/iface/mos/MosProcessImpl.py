def MosProcessImpl():
    '''public MosProcessImpl()
    '''
def processObjectStructureService():
    '''public byte[] processObjectStructureService(final StructureData data, final String mosName, final String msgType, final UserInfo info, final MXTransaction trans)
    '''
def processExternalData():
    '''public byte[] processExternalData(final StructureData data, final String mosName, final UserInfo info, final MXTransaction trans)
    '''
def processMboSet():
    '''public MboSetRemote processMboSet(final boolean isPrimaryMbo, final MboRemote parentMbo, final MosDetailInfo mdi, final String processTable)
    '''
def createMboSet():
    '''public MboSetRemote createMboSet(final boolean isPrimaryMbo, final MboRemote parentMbo, final MicSetInfo micInfo, final String processTable)
    public MboSetRemote createMboSet(final boolean isPrimaryMbo, final MboRemote parentMbo, final MosDetailInfo mdi, final String processTable)
    '''
def copyParentKey():
    '''public void copyParentKey(final String attributeName, final String value)
    '''
def delete():
    '''public void delete(final MboRemote mbo, final MosDetailInfo mdi)
    '''
def checkValidateErrors():
    '''public void checkValidateErrors()
    '''
def isEsigVerified():
    '''public boolean isEsigVerified()
    '''
def setEsigVerified():
    '''public void setEsigVerified()
    '''
def verifyEsig():
    '''public void verifyEsig()
    '''
def compareMboKeyValues():
    '''public boolean compareMboKeyValues(final MboSetRemote mboSet, final MicSetInfo micInfo, final String[] keys)
    public boolean compareMboKeyValues(final MboSetRemote mboSet, final MosDetailInfo mdi, final String[] keys)
    '''
def deleteAll():
    '''public void deleteAll(final MboRemote owner, final MboSetRemote mboSet)
    '''
def addMbo():
    '''public MboRemote addMbo(final MboSetRemote mboSet)
    '''
def save():
    '''public void save()
    '''
def checkAdditionalRules():
    '''public void checkAdditionalRules()
    '''
def cleanup():
    '''public void cleanup()
    '''
def checkForUpdate():
    '''public boolean checkForUpdate()
    '''
def resetMboSet():
    '''public MboSetRemote resetMboSet(final MboSetRemote childMboSet)
    '''
def getLanguage():
    '''public String getLanguage()
    '''
def checkBusinessRules():
    '''public int checkBusinessRules()
    public int checkBusinessRules(final MboSetRemote mboSet, final String tableName)
    '''
def presetMboRules():
    '''public int presetMboRules()
    '''
def setAdditionalData():
    '''public void setAdditionalData(final MboSetRemote MboSet, final String tableName)
    '''
def setAttachments():
    '''public void setAttachments()
    '''
def checkDocumnetMaxSize():
    '''public void checkDocumnetMaxSize(final byte[] document)
    '''
def getAttachmentFileName():
    '''public String getAttachmentFileName(final String directory, String fileName)
    '''
def setAutokeyFlag():
    '''public void setAutokeyFlag(final MboSetRemote set, final MosDetailInfo info)
    '''
def getOrg():
    '''public String getOrg()
    '''
def getSite():
    '''public String getSite()
    '''
def getItemSet():
    '''public String getItemSet()
    '''
def getCompanySet():
    '''public String getCompanySet()
    '''
def getAccessModifier():
    '''public long getAccessModifier()
    '''
def setAccessModifier():
    '''public void setAccessModifier(final long amd)
    '''
def setSkipSetFields():
    '''public void setSkipSetFields(final String field)
    '''
def setValidOrgSite():
    '''public void setValidOrgSite(final boolean v)
    '''
def findTargetMbo():
    '''public MboRemote findTargetMbo(final MosDetailInfo mdi)
    '''
def afterProcess():
    '''public void afterProcess()
    '''
def writeAttachments():
    '''public void writeAttachments()
    '''
def afterReplace():
    '''public void afterReplace(final MboRemote child)
    '''
def isBranchFilterOn():
    '''public boolean isBranchFilterOn()
    '''
