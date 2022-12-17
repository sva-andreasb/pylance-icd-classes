IBM_COPYRIGHT = "String  \"\n\nLicensed Materials - Property of IBM\n5725-E24\n(C)Copyright IBM Corporation 2007, 2013.\nAll Rights Reserved.\nUS Government Users Restricted Rights - Use, duplication \nor disclosure restricted by GSA ADP Schedule Contract with IBM Corp.\n\n\""
def ():
    '''returns CCIActCI\n\n
    (final MboSet ms)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def isLinkedToCI():
    '''returns boolean\n\n
    isLinkedToCI()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    '''
def customDelete():
    '''returns None\n\n
    customDelete(final long accessModifier, final CCIActCISetRemote actCISet)\n
    '''
def undelete():
    '''returns None\n\n
    undelete(final long accessModifier)\n
    '''
def isDualClassPromotionEnabled():
    '''returns boolean\n\n
    isDualClassPromotionEnabled()\n
    '''
def createAuthorizedCI():
    '''returns ArrayList<CCIPromotionResults>\n\n
    createAuthorizedCI(final String authCIClassID, final String authTopCIClassId, final boolean copyAttributes, final boolean updateExistingCI)\n
    createAuthorizedCI(final String authCIClassID, final String authTopCIClassId, final boolean copyAttributes, final boolean checkForExistingCI, final boolean updateExistingCI)\n
    createAuthorizedCI(final String authCIClassID, final String authTopCIClassId, final boolean copyAttributes, final boolean checkForExistingCI, final boolean updateExistingCI, final boolean allowDupDISGuids)\n
    '''
def updateAuthorizedCI():
    '''returns ArrayList<CCIPromotionResults>\n\n
    updateAuthorizedCI(final long synchronizationOptions)\n
    updateAuthorizedCI(final CCICIRemote toBeUpdated, final long synchronizationOptions, final CCITraversalCache tc)\n
    '''
def syncAuthorizedCI():
    '''returns ArrayList<CCIPromotionResults>\n\n
    syncAuthorizedCI(final String authCIClassID, final String authTopCIClassId, final long synchronizationOptions, final Hashtable<String, Boolean> synchronizedAuthorizedCIs)\n
    syncAuthorizedCI(final String authCIClassID, final String authTopCIClassId, final long synchronizationOptions, final Hashtable<String, Boolean> synchronizedAuthorizedCIs, final CCIActCIRemote topLevelActCI)\n
    '''
def getSpecificationAttribute():
    '''returns SpecificationMboRemote\n\n
    getSpecificationAttribute(final String assetAttrID)\n
    '''
def getSourceRelations():
    '''returns MboSetRemote\n\n
    getSourceRelations()\n
    '''
def getTargetRelations():
    '''returns MboSetRemote\n\n
    getTargetRelations()\n
    '''
def copyAttributes():
    '''returns boolean\n\n
    copyAttributes(final MboRemote actualCI, final MboRemote authorizedCI, final boolean overwriteAttributes)\n
    '''
def findCIForActCI():
    '''returns CCICISetRemote\n\n
    findCIForActCI(final MboRemote actCI)\n
    '''
def isClassificationAllowed():
    '''returns boolean\n\n
    isClassificationAllowed(final String customer, final MboRemote classstructure)\n
    '''
def getLinkedCI():
    '''returns MboSetRemote\n\n
    getLinkedCI()\n
    '''
def getLinkedCINum():
    '''returns String\n\n
    getLinkedCINum()\n
    '''
def setCINum():
    '''returns None\n\n
    setCINum()\n
    '''
