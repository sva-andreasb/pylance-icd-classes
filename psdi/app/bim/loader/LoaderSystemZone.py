def ():
    '''returns LoaderSystemZone\n\n
    (final ModelLoaderBase loader, final boolean isSystem)\n
    '''
def getMboSet():
    '''returns MboSetRemote\n\n
    getMboSet()\n
    '''
def canProcessItem():
    '''returns boolean\n\n
    canProcessItem(final ItemSystemBase<SystemType> item)\n
    '''
def matchItem():
    '''returns MboRemote\n\n
    matchItem(final ItemSystemBase<SystemType> item, final MboSetRemote locSystemSet)\n
    '''
def addItem():
    '''returns MboRemote\n\n
    addItem(final ItemSystemBase<SystemType> item, final MboSetRemote locSystemSet)\n
    '''
def update():
    '''returns None\n\n
    update(final MboRemote mbo, final ItemSystemBase<SystemType> system)\n
    '''
def addAttributeValues():
    '''returns int\n\n
    addAttributeValues(final MboRemote mbo, final ItemSystemBase<SystemType> item)\n
    '''
def validateItem():
    '''returns None\n\n
    validateItem(final ItemSystemBase<SystemType> item, final MboSetRemote mboSet)\n
    '''
def cleanup():
    '''returns None\n\n
    cleanup()\n
    '''
def addHeaderLocation():
    '''returns MboRemote\n\n
    addHeaderLocation(final ItemSystemBase<SystemType> system, final String parentId)\n
    '''
