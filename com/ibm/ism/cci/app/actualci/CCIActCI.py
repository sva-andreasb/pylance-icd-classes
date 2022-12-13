IBM_COPYRIGHT = "String \n\nLicensed Materials - Property of IBM\n5725-E24\n(C)Copyright IBM Corporation 2007, 2013.\nAll Rights Reserved.\nUS Government Users Restricted Rights - Use, duplication \nor disclosure restricted by GSA ADP Schedule Contract with IBM Corp.\n\n""
def CCIActCI():
'''public CCIActCI(final MboSet ms)
'''
pass
def init():
'''public void init()
'''
pass
def isLinkedToCI():
'''public boolean isLinkedToCI()
'''
pass
def delete():
'''public void delete(final long accessModifier)
'''
pass
def customDelete():
'''public void customDelete(final long accessModifier, final CCIActCISetRemote actCISet)
'''
pass
def undelete():
'''public void undelete(final long accessModifier)
'''
pass
def isDualClassPromotionEnabled():
'''public boolean isDualClassPromotionEnabled()
'''
pass
def createAuthorizedCI():
'''public ArrayList<CCIPromotionResults> createAuthorizedCI(final String authCIClassID, final String authTopCIClassId, final boolean copyAttributes, final boolean updateExistingCI)
public ArrayList<CCIPromotionResults> createAuthorizedCI(final String authCIClassID, final String authTopCIClassId, final boolean copyAttributes, final boolean checkForExistingCI, final boolean updateExistingCI)
public ArrayList<CCIPromotionResults> createAuthorizedCI(final String authCIClassID, final String authTopCIClassId, final boolean copyAttributes, final boolean checkForExistingCI, final boolean updateExistingCI, final boolean allowDupDISGuids)
'''
pass
def updateAuthorizedCI():
'''public ArrayList<CCIPromotionResults> updateAuthorizedCI(final long synchronizationOptions)
public ArrayList<CCIPromotionResults> updateAuthorizedCI(final CCICIRemote toBeUpdated, final long synchronizationOptions, final CCITraversalCache tc)
'''
pass
def syncAuthorizedCI():
'''public ArrayList<CCIPromotionResults> syncAuthorizedCI(final String authCIClassID, final String authTopCIClassId, final long synchronizationOptions, final Hashtable<String, Boolean> synchronizedAuthorizedCIs)
public ArrayList<CCIPromotionResults> syncAuthorizedCI(final String authCIClassID, final String authTopCIClassId, final long synchronizationOptions, final Hashtable<String, Boolean> synchronizedAuthorizedCIs, final CCIActCIRemote topLevelActCI)
'''
pass
def getSpecificationAttribute():
'''public SpecificationMboRemote getSpecificationAttribute(final String assetAttrID)
'''
pass
def getSourceRelations():
'''public MboSetRemote getSourceRelations()
'''
pass
def getTargetRelations():
'''public MboSetRemote getTargetRelations()
'''
pass
def copyAttributes():
'''public boolean copyAttributes(final MboRemote actualCI, final MboRemote authorizedCI, final boolean overwriteAttributes)
'''
pass
def findCIForActCI():
'''public CCICISetRemote findCIForActCI(final MboRemote actCI)
'''
pass
def isClassificationAllowed():
'''public boolean isClassificationAllowed(final String customer, final MboRemote classstructure)
'''
pass
def getLinkedCI():
'''public MboSetRemote getLinkedCI()
'''
pass
def getLinkedCINum():
'''public String getLinkedCINum()
'''
pass
def setCINum():
'''public void setCINum()
'''
pass
