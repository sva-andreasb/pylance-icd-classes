def ():
    '''returns WOTKTCommonFld\n\n
    ()\n
    '''
def hasPromptedAndCancelled():
    '''returns boolean\n\n
    hasPromptedAndCancelled(final UserInfo userInfo)\n
    '''
def needsToConfirmLocation():
    '''returns boolean\n\n
    needsToConfirmLocation(final UserInfo userInfo)\n
    '''
def confirmLocation():
    '''returns None\n\n
    confirmLocation(final MboValue mboValue, final MboRemote locWithNoSiteid)\n
    confirmLocation(final MboValue mboValue)\n
    '''
def executeAction():
    '''returns None\n\n
    executeAction(final MboValue mboValue)\n
    '''
def confirmAsset():
    '''returns None\n\n
    confirmAsset(final MboValue mboValue)\n
    confirmAsset(final MboValue mboValue, final MboRemote assetRetrievedWithoutSiteId)\n
    '''
def needsToConfirmAsset():
    '''returns boolean\n\n
    needsToConfirmAsset(final UserInfo userInfo)\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def executeNonInteractiveFlow():
    '''returns None\n\n
    executeNonInteractiveFlow(final MboValue mboValue)\n
    '''
def confirmReplacementByAssetOrDelete():
    '''returns int\n\n
    confirmReplacementByAssetOrDelete(final MboValue assetMboValue)\n
    '''
def confirmReplacementByLocationsOrDelete():
    '''returns int\n\n
    confirmReplacementByLocationsOrDelete(final MboValue locationMboValue)\n
    '''
