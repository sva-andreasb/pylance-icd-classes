def MosProcessImpl():
'''public MosProcessImpl()
'''
pass
def processObjectStructureService():
'''public byte[] processObjectStructureService(final StructureData data, final String mosName, final String msgType, final UserInfo info, final MXTransaction trans)
'''
pass
def processExternalData():
'''public byte[] processExternalData(final StructureData data, final String mosName, final UserInfo info, final MXTransaction trans)
'''
pass
def processMboSet():
'''public MboSetRemote processMboSet(final boolean isPrimaryMbo, final MboRemote parentMbo, final MosDetailInfo mdi, final String processTable)
'''
pass
def createMboSet():
'''public MboSetRemote createMboSet(final boolean isPrimaryMbo, final MboRemote parentMbo, final MicSetInfo micInfo, final String processTable)
public MboSetRemote createMboSet(final boolean isPrimaryMbo, final MboRemote parentMbo, final MosDetailInfo mdi, final String processTable)
'''
pass
def copyParentKey():
'''public void copyParentKey(final String attributeName, final String value)
'''
pass
def delete():
'''public void delete(final MboRemote mbo, final MosDetailInfo mdi)
'''
pass
def checkValidateErrors():
'''public void checkValidateErrors()
'''
pass
def isEsigVerified():
'''public boolean isEsigVerified()
'''
pass
def setEsigVerified():
'''public void setEsigVerified()
'''
pass
def verifyEsig():
'''public void verifyEsig()
'''
pass
def compareMboKeyValues():
'''public boolean compareMboKeyValues(final MboSetRemote mboSet, final MicSetInfo micInfo, final String[] keys)
public boolean compareMboKeyValues(final MboSetRemote mboSet, final MosDetailInfo mdi, final String[] keys)
'''
pass
def deleteAll():
'''public void deleteAll(final MboRemote owner, final MboSetRemote mboSet)
'''
pass
def addMbo():
'''public MboRemote addMbo(final MboSetRemote mboSet)
'''
pass
def save():
'''public void save()
'''
pass
def checkAdditionalRules():
'''public void checkAdditionalRules()
'''
pass
def cleanup():
'''public void cleanup()
'''
pass
def checkForUpdate():
'''public boolean checkForUpdate()
'''
pass
def resetMboSet():
'''public MboSetRemote resetMboSet(final MboSetRemote childMboSet)
'''
pass
def getLanguage():
'''public String getLanguage()
'''
pass
def checkBusinessRules():
'''public int checkBusinessRules()
public int checkBusinessRules(final MboSetRemote mboSet, final String tableName)
'''
pass
def presetMboRules():
'''public int presetMboRules()
'''
pass
def setAdditionalData():
'''public void setAdditionalData(final MboSetRemote MboSet, final String tableName)
'''
pass
def setAttachments():
'''public void setAttachments()
'''
pass
def checkDocumnetMaxSize():
'''public void checkDocumnetMaxSize(final byte[] document)
'''
pass
def getAttachmentFileName():
'''public String getAttachmentFileName(final String directory, String fileName)
'''
pass
def setAutokeyFlag():
'''public void setAutokeyFlag(final MboSetRemote set, final MosDetailInfo info)
'''
pass
def getOrg():
'''public String getOrg()
'''
pass
def getSite():
'''public String getSite()
'''
pass
def getItemSet():
'''public String getItemSet()
'''
pass
def getCompanySet():
'''public String getCompanySet()
'''
pass
def getAccessModifier():
'''public long getAccessModifier()
'''
pass
def setAccessModifier():
'''public void setAccessModifier(final long amd)
'''
pass
def setSkipSetFields():
'''public void setSkipSetFields(final String field)
'''
pass
def setValidOrgSite():
'''public void setValidOrgSite(final boolean v)
'''
pass
def findTargetMbo():
'''public MboRemote findTargetMbo(final MosDetailInfo mdi)
'''
pass
def afterProcess():
'''public void afterProcess()
'''
pass
def writeAttachments():
'''public void writeAttachments()
'''
pass
def afterReplace():
'''public void afterReplace(final MboRemote child)
'''
pass
def isBranchFilterOn():
'''public boolean isBranchFilterOn()
'''
pass
