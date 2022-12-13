SOURCE_WORKORDER = "String  \"WO\""
SOURCE_WORKPLAN = "String  \"WP\""
SOURCE_SAFETYPLAN = "String  \"SP\""
def WoSafetyLinkSet():
    '''public WoSafetyLinkSet(final MboServerInterface ms)
    '''
def setThisRelationName():
    '''public void setThisRelationName(final String relName)
    '''
def getThisRelationName():
    '''public String getThisRelationName()
    '''
def copyHazardFromSafetyLexicon():
    '''public void copyHazardFromSafetyLexicon(final MboRemote safetylex, final String dataSource, final MboSetRemote woHazardSet, final MboSetRemote woHazardPrecSet, final MboSetRemote woPrecautionSet)
    '''
def copyHazard():
    '''public MboRemote copyHazard(final String hazardid, final String assetnum, final String location, final String dataSource, final MboSetRemote woHazardSet, final MboSetRemote woHazardPrecSet, final MboSetRemote woPrecautionSet)
    '''
def addHazardSafetyLink():
    '''public MboRemote addHazardSafetyLink(final String hazardID, final String assetnum, final String location, final String dataSource, final MboSetRemote woHazardSet)
    '''
def copyTagOutFromSafetyLexicon():
    '''public void copyTagOutFromSafetyLexicon(final MboRemote safetylex, final String dataSource, final MboSetRemote woTagOutSet, final MboSetRemote woTagLockSet, final MboSetRemote woLockOutSet)
    '''
def addTagOutSafetyLink():
    '''public MboRemote[] addTagOutSafetyLink(final String hazardID, final String tagoutID, final String assetnum, final String location, final String applyseq, final String removeseq, final String dataSource, final MboSetRemote woTagOutSet)
    '''
def clearSafetyPlanLinks():
    '''public void clearSafetyPlanLinks()
    '''
def removeHazardousMaterialLink():
    '''public void removeHazardousMaterialLink(final String hazardID, final String dataSource)
    '''
def canAdd():
    '''public void canAdd()
    '''
def setHazardTagOutBeingDeleted():
    '''public void setHazardTagOutBeingDeleted(final boolean beingDeleted)
    '''
