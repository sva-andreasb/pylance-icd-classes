def ():
    '''returns DMPackage\n\n
    (final MboSet ms)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    '''
def deleteForPreview():
    '''returns None\n\n
    deleteForPreview(final long accessModifier)\n
    '''
def writeMosToXML():
    '''returns boolean\n\n
    writeMosToXML(final String type, final String defClassName, final String mosName, final MboSetRemote mosMboSet, final boolean isChange, final int batchSize, final boolean useDefaultXMLAction)\n
    '''
def getStatusListName():
    '''returns String\n\n
    getStatusListName()\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String status, final String progressStatus, final Date date, final String memo, final long accessModifier)\n
    '''
def canDistribute():
    '''returns None\n\n
    canDistribute()\n
    '''
def distributeZipPackage():
    '''returns boolean\n\n
    distributeZipPackage()\n
    '''
def distributePackage():
    '''returns String\n\n
    distributePackage()\n
    '''
def deployPackage():
    '''returns None\n\n
    deployPackage(final MboSetRemote pkgDefSet)\n
    '''
def getLongopPreviewOKMsg():
    '''returns None\n\n
    getLongopPreviewOKMsg(final String pkgName, final UserInfo ui, final MboSetRemote defSet)\n
    '''
def changeMaxStatus():
    '''returns None\n\n
    changeMaxStatus(final String status, final String progressStatus, final Date asOfDate, final String memo, final long accessModifier)\n
    '''
def previewLogger():
    '''returns None\n\n
    previewLogger(final String pkgName, final boolean load)\n
    '''
def processPreviewXML():
    '''returns None\n\n
    processPreviewXML(final MXTransaction mxTrans, final UserInfo ui, final String mos, final byte[] content, final boolean recordRollback)\n
    '''
def confirmCompSrcDeployed():
    '''returns MboRemote\n\n
    confirmCompSrcDeployed()\n
    '''
def closePkg():
    '''returns None\n\n
    closePkg()\n
    '''
def uploadCompiledSrcFile():
    '''returns None\n\n
    uploadCompiledSrcFile(final String fileName, final byte[] content)\n
    '''
def canDownloadPkg():
    '''returns String\n\n
    canDownloadPkg()\n
    '''
def canDownloadFile():
    '''returns String\n\n
    canDownloadFile(final MboRemote cmpSrc)\n
    '''
def getRedistribute():
    '''returns boolean\n\n
    getRedistribute()\n
    '''
def setRedistribute():
    '''returns None\n\n
    setRedistribute(final boolean isRedistribute)\n
    '''
def getPackageDef():
    '''returns MboRemote\n\n
    getPackageDef()\n
    '''
def canDownloadPreviewLog():
    '''returns String\n\n
    canDownloadPreviewLog()\n
    '''
def canDownloadScriptLog():
    '''returns String\n\n
    canDownloadScriptLog()\n
    '''
def applyFix():
    '''returns None\n\n
    applyFix()\n
    '''
def setMosName():
    '''returns None\n\n
    setMosName(final String mos)\n
    '''
def getMosName():
    '''returns String\n\n
    getMosName()\n
    '''
def setGroupName():
    '''returns None\n\n
    setGroupName(final String grp)\n
    '''
def getGroupName():
    '''returns String\n\n
    getGroupName()\n
    '''
def setMosStarted():
    '''returns None\n\n
    setMosStarted(final boolean flag)\n
    '''
def isMosStarted():
    '''returns boolean\n\n
    isMosStarted()\n
    '''
def setMosEnded():
    '''returns None\n\n
    setMosEnded(final boolean flag)\n
    '''
def isMosEnded():
    '''returns boolean\n\n
    isMosEnded()\n
    '''
def setGroupStarted():
    '''returns None\n\n
    setGroupStarted(final boolean flag)\n
    '''
def isGroupStarted():
    '''returns boolean\n\n
    isGroupStarted()\n
    '''
def setGroupEnded():
    '''returns None\n\n
    setGroupEnded(final boolean flag)\n
    '''
def isGroupEnded():
    '''returns boolean\n\n
    isGroupEnded()\n
    '''
