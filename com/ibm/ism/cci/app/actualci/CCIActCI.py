IBM_COPYRIGHT = "String  \"\n\nLicensed Materials - Property of IBM\n5725-E24\n(C)Copyright IBM Corporation 2007, 2013.\nAll Rights Reserved.\nUS Government Users Restricted Rights - Use, duplication \nor disclosure restricted by GSA ADP Schedule Contract with IBM Corp.\n\n\""
def CCIActCI():
    '''    public CCIActCI(final MboSet ms)
    '''
def init():
    '''    public void init()
    '''
def isLinkedToCI():
    '''    public boolean isLinkedToCI()
    '''
def delete():
    '''    public void delete(final long accessModifier)
    '''
def customDelete():
    '''    public void customDelete(final long accessModifier, final CCIActCISetRemote actCISet)
    '''
def undelete():
    '''    public void undelete(final long accessModifier)
    '''
def isDualClassPromotionEnabled():
    '''    public boolean isDualClassPromotionEnabled()
    '''
def createAuthorizedCI():
    '''    public ArrayList<CCIPromotionResults> createAuthorizedCI(final String authCIClassID, final String authTopCIClassId, final boolean copyAttributes, final boolean updateExistingCI)
    public ArrayList<CCIPromotionResults> createAuthorizedCI(final String authCIClassID, final String authTopCIClassId, final boolean copyAttributes, final boolean checkForExistingCI, final boolean updateExistingCI)
    public ArrayList<CCIPromotionResults> createAuthorizedCI(final String authCIClassID, final String authTopCIClassId, final boolean copyAttributes, final boolean checkForExistingCI, final boolean updateExistingCI, final boolean allowDupDISGuids)
    '''
def updateAuthorizedCI():
    '''    public ArrayList<CCIPromotionResults> updateAuthorizedCI(final long synchronizationOptions)
    public ArrayList<CCIPromotionResults> updateAuthorizedCI(final CCICIRemote toBeUpdated, final long synchronizationOptions, final CCITraversalCache tc)
    '''
def syncAuthorizedCI():
    '''    public ArrayList<CCIPromotionResults> syncAuthorizedCI(final String authCIClassID, final String authTopCIClassId, final long synchronizationOptions, final Hashtable<String, Boolean> synchronizedAuthorizedCIs)
    public ArrayList<CCIPromotionResults> syncAuthorizedCI(final String authCIClassID, final String authTopCIClassId, final long synchronizationOptions, final Hashtable<String, Boolean> synchronizedAuthorizedCIs, final CCIActCIRemote topLevelActCI)
    '''
def getSpecificationAttribute():
    '''    public SpecificationMboRemote getSpecificationAttribute(final String assetAttrID)
    '''
def getSourceRelations():
    '''    public MboSetRemote getSourceRelations()
    '''
def getTargetRelations():
    '''    public MboSetRemote getTargetRelations()
    '''
def copyAttributes():
    '''    public boolean copyAttributes(final MboRemote actualCI, final MboRemote authorizedCI, final boolean overwriteAttributes)
    '''
def findCIForActCI():
    '''    public CCICISetRemote findCIForActCI(final MboRemote actCI)
    '''
def isClassificationAllowed():
    '''    public boolean isClassificationAllowed(final String customer, final MboRemote classstructure)
    '''
def getLinkedCI():
    '''    public MboSetRemote getLinkedCI()
    '''
def getLinkedCINum():
    '''    public String getLinkedCINum()
    '''
def setCINum():
    '''    public void setCINum()
    '''
