def SafetyPlan():
    '''    public SafetyPlan(final MboSet ms)
    '''
def init():
    '''    public void init()
    '''
def add():
    '''    public void add()
    '''
def modify():
    '''    public void modify()
    '''
def canDelete():
    '''    public void canDelete()
    '''
def delete():
    '''    public void delete(final long accessModifier)
    '''
def undelete():
    '''    public void undelete()
    '''
def appValidate():
    '''    public void appValidate()
    '''
def associateHazardToSafetyPlan():
    '''    public MboSetRemote associateHazardToSafetyPlan(MboSetRemote spwset, final String hazardid, final String relatedassetnum, final String relatedlocation)
    public void associateHazardToSafetyPlan(final MboRemote spw, final MboRemote spRelatedAsset, final MboSetRemote hazardSet)
    public void associateHazardToSafetyPlan(final MboSetRemote safetyLexiconSet)
    public void associateHazardToSafetyPlan(final MboRemote spw, final MboSetRemote safetyLexiconSet)
    '''
def removeHazardFromSafetyPlan():
    '''    public MboSetRemote removeHazardFromSafetyPlan(MboSetRemote spwset, final String hazardid, final String relatedassetnum, final String relatedlocation)
    '''
def associateTagOutToSafetyPlan():
    '''    public MboSetRemote associateTagOutToSafetyPlan(MboSetRemote spwset, final String hazardid, final String tagoutid, final String relatedassetnum, final String relatedlocation)
    '''
def removeTagOutFromSafetyPlan():
    '''    public MboSetRemote removeTagOutFromSafetyPlan(MboSetRemote spwset, final String hazardid, final String tagoutid, final String relatedassetnum, final String relatedlocation)
    '''
def duplicate():
    '''    public MboRemote duplicate()
    '''
def initRelationship():
    '''    public void initRelationship(final String relationName, final MboSetRemote mboSet)
    '''
