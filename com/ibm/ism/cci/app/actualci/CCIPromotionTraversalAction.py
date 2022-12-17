IBM_COPYRIGHT = "String  \"\n\nLicensed Materials - Property of IBM\n5725-E24\n(C)Copyright IBM Corporation 2007, 2013.\nAll Rights Reserved.\nUS Government Users Restricted Rights - Use, duplication \nor disclosure restricted by GSA ADP Schedule Contract with IBM Corp.\n\n\""
COPY_ATTRIBUTES = "long  1L"
OVERWRITE_ATTRIBUTES = "long  2L"
SYNC_RELATED_CIS = "long  4L"
CREATE_RELATIONSHIPS = "long  8L"
CREATE_RELATED_CIS = "long  16L"
COPY_ATTRIBUTES_FOR_NEW = "long  32L"
ALLOW_DUP_DISGUID = "long  268435456L"
def ():
    '''returns CCIPromotionTraversalAction\n\n
    (final String authTopCIClassId, final long synchronizationOptions, final CCITraversalCache tc, final Set<String> inProcessSet)\n
    '''
def processState():
    '''returns None\n\n
    processState(final TraversalState state, final UserInfo userInfo)\n
    '''
def isNull():
    '''returns boolean\n\n
    isNull(final String input)\n
    '''
def postTraverseAction():
    '''returns None\n\n
    postTraverseAction(final UserInfo userInfo)\n
    '''
def copyAttributes():
    '''returns boolean\n\n
    copyAttributes(final MboRemote actualCI, final MboRemote authorizedCI, final boolean overwriteAttributes, final boolean removeBlanksOnly, final boolean createdCI)\n
    '''
def getResults():
    '''returns List<CCIPromotionResults>\n\n
    getResults()\n
    '''
