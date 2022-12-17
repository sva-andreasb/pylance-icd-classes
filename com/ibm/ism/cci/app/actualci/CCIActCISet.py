IBM_COPYRIGHT = "String  \"\n\nLicensed Materials - Property of IBM\n5725-E24\n(C)Copyright IBM Corporation 2007, 2013.\nAll Rights Reserved.\nUS Government Users Restricted Rights - Use, duplication \nor disclosure restricted by GSA ADP Schedule Contract with IBM Corp.\n\n\""
def ():
    '''returns CCIActCISet\n\n
    (final MboServerInterface ms)\n
    '''
def getHierarchyPath():
    '''returns String\n\n
    getHierarchyPath(final CCIActCIRemote actCI, final String ClassStructureID)\n
    '''
def createAuthorizedCIs():
    '''returns None\n\n
    createAuthorizedCIs(final Vector selected, final boolean copyAttributes, final String authClassID)\n
    createAuthorizedCIs(final Vector selected, final boolean copyAttributes, final boolean isAsync, final String toEmailAddr, final String authClassID)\n
    createAuthorizedCIs(final Vector selected, final boolean copyAttributes, final boolean updateExistingCIs, final boolean isAsync, final String toEmailAddr, final String authClassID)\n
    createAuthorizedCIs(final Vector selected, final boolean copyAttributes, final boolean checkForExistingCIs, final boolean updateExistingCIs, final boolean allowDupDISGuids, final boolean isAsync, final String toEmailAddr, final String authClassID)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
def deleteAll():
    '''returns None\n\n
    deleteAll(final long accessModifier)\n
    '''
def getNextItems():
    '''returns None\n\n
    getNextItems(final TraversalState traversalState, final UserInfo userInfo)\n
    '''
def isCancelled():
    '''returns boolean\n\n
    isCancelled()\n
    '''
def postTraverseAction():
    '''returns None\n\n
    postTraverseAction(final UserInfo userInfo)\n
    '''
def processState():
    '''returns None\n\n
    processState(final TraversalState state, final UserInfo userInfo)\n
    '''
def writeEmail():
    '''returns None\n\n
    writeEmail(final String toEmailAddr, final String subject, String Message, final StringBuffer attachmentStuff)\n
    '''
