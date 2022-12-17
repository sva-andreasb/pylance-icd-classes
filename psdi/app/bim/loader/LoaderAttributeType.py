def ():
    '''returns LoaderAttributeType\n\n
    (final ModelProcessIntf loader)\n
    '''
def canProcessItem():
    '''returns boolean\n\n
    canProcessItem(final ItemAttributeType attrib)\n
    '''
def getMboSet():
    '''returns MboSetRemote\n\n
    getMboSet()\n
    '''
def matchItem():
    '''returns MboRemote\n\n
    matchItem(final ItemAttributeType attrib, final MboSetRemote attribSet)\n
    '''
def addItem():
    '''returns MboRemote\n\n
    addItem(final ItemAttributeType attrib, final MboSetRemote attribSet)\n
    '''
def update():
    '''returns None\n\n
    update(final MboRemote mbo, final ItemAttributeType item)\n
    '''
def validateItem():
    '''returns None\n\n
    validateItem(final ItemAttributeType item, final MboSetRemote mboSet)\n
    '''
def addAttributeValues():
    '''returns int\n\n
    addAttributeValues(final MboRemote mbo, final ItemAttributeType item)\n
    '''
def testMatchForDatatype():
    '''returns MboRemote\n\n
    testMatchForDatatype(final ItemAttributeType attrib, final MboSetRemote attribSet, final boolean isNumeric)\n
    '''
