def ():
    '''returns DMPackageDef\n\n
    (final MboSet ms)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def extractPkgData():
    '''returns None\n\n
    extractPkgData(MboRemote newPkg)\n
    '''
def loadCFGDATAGrpsForPkg():
    '''returns boolean\n\n
    loadCFGDATAGrpsForPkg(final MboRemote pkgMbo, final List<String> grpV, final UserInfo msgUI)\n
    '''
def getDMCfgDataObjGroupInOrder():
    '''returns MboSetRemote\n\n
    getDMCfgDataObjGroupInOrder(final List<String> cfgGroups)\n
    '''
def loadDDMETADATAGrpForPkg():
    '''returns boolean\n\n
    loadDDMETADATAGrpForPkg(final MboRemote pkgMbo, final UserInfo msgUI)\n
    '''
def loadPKGMETADATAGrpForPkg():
    '''returns None\n\n
    loadPKGMETADATAGrpForPkg(final MboRemote pkgMbo, final boolean reCreatePkgMeta, final UserInfo msgUI)\n
    '''
def loadManifestForPkg():
    '''returns None\n\n
    loadManifestForPkg(final MboRemote newPkg)\n
    '''
def extractRecordsForCfgGroup():
    '''returns boolean\n\n
    extractRecordsForCfgGroup(final String type, final MboRemote cfgGrp, final MboRemote newPkg, final boolean reCreatePkgMeta, final UserInfo msgUI)\n
    '''
def loadAllGroupsForPkg():
    '''returns List<String>\n\n
    loadAllGroupsForPkg()\n
    '''
def duplicate():
    '''returns MboRemote\n\n
    duplicate()\n
    '''
def loadStagingForPkg():
    '''returns MboRemote\n\n
    loadStagingForPkg(final MboRemote pkgMbo, final String type, final UserInfo msgUI)\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def setReloadOnSave():
    '''returns None\n\n
    setReloadOnSave(final boolean flag)\n
    '''
def getReloadOnSave():
    '''returns boolean\n\n
    getReloadOnSave()\n
    '''
def canDeletePkgDef():
    '''returns None\n\n
    canDeletePkgDef()\n
    '''
def warnDeletePkgDef():
    '''returns None\n\n
    warnDeletePkgDef()\n
    '''
def canEdit():
    '''returns None\n\n
    canEdit()\n
    '''
def canEditSetWhere():
    '''returns None\n\n
    canEditSetWhere()\n
    '''
def setReadOnly():
    '''returns None\n\n
    setReadOnly()\n
    '''
def canCreatePackage():
    '''returns None\n\n
    canCreatePackage()\n
    '''
def canSetWhere():
    '''returns None\n\n
    canSetWhere()\n
    '''
def setSnapshotFlag():
    '''returns None\n\n
    setSnapshotFlag(final boolean snapshot)\n
    '''
def getSnapshotFlag():
    '''returns boolean\n\n
    getSnapshotFlag()\n
    '''
def getPkgTypeAsInt():
    '''returns int\n\n
    getPkgTypeAsInt()\n
    '''
def setPkgTypeAsInt():
    '''returns None\n\n
    setPkgTypeAsInt(final int type)\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    '''
def getStatusListName():
    '''returns String\n\n
    getStatusListName()\n
    '''
def moveEventTrackingToHistory():
    '''returns None\n\n
    moveEventTrackingToHistory()\n
    '''
def cantPerformOnLocked():
    '''returns None\n\n
    cantPerformOnLocked()\n
    '''
def pkgContainsUserDefinedMOS():
    '''returns boolean\n\n
    pkgContainsUserDefinedMOS()\n
    '''
def validateChangePkgDef():
    '''returns None\n\n
    validateChangePkgDef()\n
    '''
