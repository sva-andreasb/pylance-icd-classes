def ():
    '''returns SafetyPlan\n\n
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
def modify():
    '''returns None\n\n
    modify()\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    '''
def undelete():
    '''returns None\n\n
    undelete()\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def associateHazardToSafetyPlan():
    '''returns None\n\n
    associateHazardToSafetyPlan(MboSetRemote spwset, final String hazardid, final String relatedassetnum, final String relatedlocation)\n
    associateHazardToSafetyPlan(final MboRemote spw, final MboRemote spRelatedAsset, final MboSetRemote hazardSet)\n
    associateHazardToSafetyPlan(final MboSetRemote safetyLexiconSet)\n
    associateHazardToSafetyPlan(final MboRemote spw, final MboSetRemote safetyLexiconSet)\n
    '''
def removeHazardFromSafetyPlan():
    '''returns MboSetRemote\n\n
    removeHazardFromSafetyPlan(MboSetRemote spwset, final String hazardid, final String relatedassetnum, final String relatedlocation)\n
    '''
def associateTagOutToSafetyPlan():
    '''returns MboSetRemote\n\n
    associateTagOutToSafetyPlan(MboSetRemote spwset, final String hazardid, final String tagoutid, final String relatedassetnum, final String relatedlocation)\n
    '''
def removeTagOutFromSafetyPlan():
    '''returns MboSetRemote\n\n
    removeTagOutFromSafetyPlan(MboSetRemote spwset, final String hazardid, final String tagoutid, final String relatedassetnum, final String relatedlocation)\n
    '''
def duplicate():
    '''returns MboRemote\n\n
    duplicate()\n
    '''
def initRelationship():
    '''returns None\n\n
    initRelationship(final String relationName, final MboSetRemote mboSet)\n
    '''
