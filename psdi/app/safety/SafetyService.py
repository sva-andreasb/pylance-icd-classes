def ():
    '''returns SafetyService\n\n
    ()\n
    (final MXServer mxServer)\n
    '''
def associateHazardToAsset():
    '''returns MboSetRemote\n\n
    associateHazardToAsset(final MboRemote assetMbo, MboSetRemote lexSet, final String hazardid)\n
    '''
def removeHazardFromAsset():
    '''returns MboSetRemote\n\n
    removeHazardFromAsset(final MboRemote assetMbo, MboSetRemote lexSet, final String hazardid)\n
    '''
def associateTagOutToAsset():
    '''returns MboSetRemote\n\n
    associateTagOutToAsset(final MboRemote assetMbo, MboSetRemote lexSet, final String hazardid, final String tagoutid)\n
    '''
def removeTagOutFromAsset():
    '''returns MboSetRemote\n\n
    removeTagOutFromAsset(final MboRemote assetMbo, MboSetRemote lexSet, final String hazardid, final String tagoutid)\n
    '''
def tagoutsMustBelongToHazards():
    '''returns boolean\n\n
    tagoutsMustBelongToHazards()\n
    '''
