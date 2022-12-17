def ():
    '''returns MosProcessImpl\n\n
    ()\n
    '''
def processObjectStructureService():
    '''returns byte[]\n\n
    processObjectStructureService(final StructureData data, final String mosName, final String msgType, final UserInfo info, final MXTransaction trans)\n
    '''
def processExternalData():
    '''returns byte[]\n\n
    processExternalData(final StructureData data, final String mosName, final UserInfo info, final MXTransaction trans)\n
    '''
def processMboSet():
    '''returns MboSetRemote\n\n
    processMboSet(final boolean isPrimaryMbo, final MboRemote parentMbo, final MosDetailInfo mdi, final String processTable)\n
    '''
def createMboSet():
    '''returns MboSetRemote\n\n
    createMboSet(final boolean isPrimaryMbo, final MboRemote parentMbo, final MicSetInfo micInfo, final String processTable)\n
    createMboSet(final boolean isPrimaryMbo, final MboRemote parentMbo, final MosDetailInfo mdi, final String processTable)\n
    '''
def copyParentKey():
    '''returns None\n\n
    copyParentKey(final String attributeName, final String value)\n
    '''
def delete():
    '''returns None\n\n
    delete(final MboRemote mbo, final MosDetailInfo mdi)\n
    '''
def checkValidateErrors():
    '''returns None\n\n
    checkValidateErrors()\n
    '''
def isEsigVerified():
    '''returns boolean\n\n
    isEsigVerified()\n
    '''
def setEsigVerified():
    '''returns None\n\n
    setEsigVerified()\n
    '''
def verifyEsig():
    '''returns None\n\n
    verifyEsig()\n
    '''
def compareMboKeyValues():
    '''returns boolean\n\n
    compareMboKeyValues(final MboSetRemote mboSet, final MicSetInfo micInfo, final String[] keys)\n
    compareMboKeyValues(final MboSetRemote mboSet, final MosDetailInfo mdi, final String[] keys)\n
    '''
def deleteAll():
    '''returns None\n\n
    deleteAll(final MboRemote owner, final MboSetRemote mboSet)\n
    '''
def addMbo():
    '''returns MboRemote\n\n
    addMbo(final MboSetRemote mboSet)\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
def checkAdditionalRules():
    '''returns None\n\n
    checkAdditionalRules()\n
    '''
def cleanup():
    '''returns None\n\n
    cleanup()\n
    '''
def checkForUpdate():
    '''returns boolean\n\n
    checkForUpdate()\n
    '''
def resetMboSet():
    '''returns MboSetRemote\n\n
    resetMboSet(final MboSetRemote childMboSet)\n
    '''
def getLanguage():
    '''returns String\n\n
    getLanguage()\n
    '''
def checkBusinessRules():
    '''returns int\n\n
    checkBusinessRules()\n
    checkBusinessRules(final MboSetRemote mboSet, final String tableName)\n
    '''
def presetMboRules():
    '''returns int\n\n
    presetMboRules()\n
    '''
def setAdditionalData():
    '''returns None\n\n
    setAdditionalData(final MboSetRemote MboSet, final String tableName)\n
    '''
def setAttachments():
    '''returns None\n\n
    setAttachments()\n
    '''
def checkDocumnetMaxSize():
    '''returns None\n\n
    checkDocumnetMaxSize(final byte[] document)\n
    '''
def getAttachmentFileName():
    '''returns String\n\n
    getAttachmentFileName(final String directory, String fileName)\n
    '''
def setAutokeyFlag():
    '''returns None\n\n
    setAutokeyFlag(final MboSetRemote set, final MosDetailInfo info)\n
    '''
def getOrg():
    '''returns String\n\n
    getOrg()\n
    '''
def getSite():
    '''returns String\n\n
    getSite()\n
    '''
def getItemSet():
    '''returns String\n\n
    getItemSet()\n
    '''
def getCompanySet():
    '''returns String\n\n
    getCompanySet()\n
    '''
def getAccessModifier():
    '''returns long\n\n
    getAccessModifier()\n
    '''
def setAccessModifier():
    '''returns None\n\n
    setAccessModifier(final long amd)\n
    '''
def setSkipSetFields():
    '''returns None\n\n
    setSkipSetFields(final String field)\n
    '''
def setValidOrgSite():
    '''returns None\n\n
    setValidOrgSite(final boolean v)\n
    '''
def findTargetMbo():
    '''returns MboRemote\n\n
    findTargetMbo(final MosDetailInfo mdi)\n
    '''
def afterProcess():
    '''returns None\n\n
    afterProcess()\n
    '''
def writeAttachments():
    '''returns None\n\n
    writeAttachments()\n
    '''
def afterReplace():
    '''returns None\n\n
    afterReplace(final MboRemote child)\n
    '''
def isBranchFilterOn():
    '''returns boolean\n\n
    isBranchFilterOn()\n
    '''
