def ():
    '''returns LoaderProduct\n\n
    (final ModelLoaderBase loader)\n
    '''
def canProcessItem():
    '''returns boolean\n\n
    canProcessItem(final ItemTYPE attrib)\n
    '''
def matchItem():
    '''returns MboRemote\n\n
    matchItem(final ItemTYPE type, final MboSetRemote typeSet)\n
    '''
def update():
    '''returns None\n\n
    update(final MboRemote mbo, final ItemTYPE type)\n
    '''
def addAttributeValues():
    '''returns int\n\n
    addAttributeValues(final MboRemote productMbo, final ItemTYPE product)\n
    '''
def addItemMaster():
    '''returns MboRemote\n\n
    addItemMaster(final ItemTYPE product)\n
    '''
def addVendorToItem():
    '''returns boolean\n\n
    addVendorToItem(final MboRemote itemMbo, final ItemTYPE product)\n
    '''
def findMatchingDesignSpecById():
    '''returns boolean\n\n
    findMatchingDesignSpecById(final MboRemote mboProduct, final ItemTYPE type)\n
    '''
