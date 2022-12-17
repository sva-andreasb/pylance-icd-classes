def ():
    '''returns LoaderComponent\n\n
    (final ModelLoaderBase loader)\n
    '''
def getMboSet():
    '''returns MboSetRemote\n\n
    getMboSet()\n
    '''
def cleanup():
    '''returns None\n\n
    cleanup()\n
    '''
def canProcessItem():
    '''returns boolean\n\n
    canProcessItem(final ItemCOMPONENT component)\n
    '''
def matchItem():
    '''returns MboRemote\n\n
    matchItem(final ItemCOMPONENT component, MboSetRemote assetSet)\n
    '''
def addItem():
    '''returns MboRemote\n\n
    addItem(final ItemCOMPONENT component, final MboSetRemote assetSet)\n
    '''
def update():
    '''returns None\n\n
    update(final MboRemote mbo, final ItemCOMPONENT component)\n
    '''
def validateItem():
    '''returns None\n\n
    validateItem(final ItemCOMPONENT component, final MboSetRemote mboSet)\n
    '''
def addAttributeValues():
    '''returns int\n\n
    addAttributeValues(final MboRemote assetMbo, final ItemCOMPONENT component)\n
    '''
def addOperatinLocation():
    '''returns MboRemote\n\n
    addOperatinLocation(final ItemCOMPONENT component, final String parentId)\n
    '''
def setupPMFromMaster():
    '''returns None\n\n
    setupPMFromMaster(final MboRemote masterpmMbo, final MboRemote pmMbo, final ItemBase item)\n
    '''
