SOURCE_WORKORDER = "String  \"WO\""
SOURCE_WORKPLAN = "String  \"WP\""
SOURCE_SAFETYPLAN = "String  \"SP\""
def ():
    '''returns WoSafetyLinkSet\n\n
    (final MboServerInterface ms)\n
    '''
def setThisRelationName():
    '''returns None\n\n
    setThisRelationName(final String relName)\n
    '''
def getThisRelationName():
    '''returns String\n\n
    getThisRelationName()\n
    '''
def copyHazardFromSafetyLexicon():
    '''returns None\n\n
    copyHazardFromSafetyLexicon(final MboRemote safetylex, final String dataSource, final MboSetRemote woHazardSet, final MboSetRemote woHazardPrecSet, final MboSetRemote woPrecautionSet)\n
    '''
def copyHazard():
    '''returns MboRemote\n\n
    copyHazard(final String hazardid, final String assetnum, final String location, final String dataSource, final MboSetRemote woHazardSet, final MboSetRemote woHazardPrecSet, final MboSetRemote woPrecautionSet)\n
    '''
def addHazardSafetyLink():
    '''returns MboRemote\n\n
    addHazardSafetyLink(final String hazardID, final String assetnum, final String location, final String dataSource, final MboSetRemote woHazardSet)\n
    '''
def copyTagOutFromSafetyLexicon():
    '''returns None\n\n
    copyTagOutFromSafetyLexicon(final MboRemote safetylex, final String dataSource, final MboSetRemote woTagOutSet, final MboSetRemote woTagLockSet, final MboSetRemote woLockOutSet)\n
    '''
def addTagOutSafetyLink():
    '''returns MboRemote[]\n\n
    addTagOutSafetyLink(final String hazardID, final String tagoutID, final String assetnum, final String location, final String applyseq, final String removeseq, final String dataSource, final MboSetRemote woTagOutSet)\n
    '''
def clearSafetyPlanLinks():
    '''returns None\n\n
    clearSafetyPlanLinks()\n
    '''
def removeHazardousMaterialLink():
    '''returns None\n\n
    removeHazardousMaterialLink(final String hazardID, final String dataSource)\n
    '''
def canAdd():
    '''returns None\n\n
    canAdd()\n
    '''
def setHazardTagOutBeingDeleted():
    '''returns None\n\n
    setHazardTagOutBeingDeleted(final boolean beingDeleted)\n
    '''
