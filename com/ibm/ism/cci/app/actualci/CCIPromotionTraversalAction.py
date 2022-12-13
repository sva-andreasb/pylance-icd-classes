IBM_COPYRIGHT = "String \n\nLicensed Materials - Property of IBM\n5725-E24\n(C)Copyright IBM Corporation 2007, 2013.\nAll Rights Reserved.\nUS Government Users Restricted Rights - Use, duplication \nor disclosure restricted by GSA ADP Schedule Contract with IBM Corp.\n\n""
COPY_ATTRIBUTES = "long 1L"
OVERWRITE_ATTRIBUTES = "long 2L"
SYNC_RELATED_CIS = "long 4L"
CREATE_RELATIONSHIPS = "long 8L"
CREATE_RELATED_CIS = "long 16L"
COPY_ATTRIBUTES_FOR_NEW = "long 32L"
ALLOW_DUP_DISGUID = "long 268435456L"
def CCIPromotionTraversalAction():
'''public CCIPromotionTraversalAction(final String authTopCIClassId, final long synchronizationOptions, final CCITraversalCache tc, final Set<String> inProcessSet)
'''
pass
def getFailedRelations():
'''public Map<String, CIRelationHelper> getFailedRelations()
'''
pass
def processState():
'''public void processState(final TraversalState state, final UserInfo userInfo)
'''
pass
def isNull():
'''public boolean isNull(final String input)
'''
pass
def postTraverseAction():
'''public void postTraverseAction(final UserInfo userInfo)
'''
pass
def processRelation():
'''public static boolean processRelation(final CIRelationHelper relation, final CCICIRelationSetRemote newCiRelations, final CCICIRelationSetRemote ciExistingRelations, final Map<String, LinkedCIInfo> actCIToCIMap, final boolean createRelationships, final UserInfo userInfo)
'''
pass
def getExistingCIsMap():
'''public Map<String, LinkedCIInfo> getExistingCIsMap()
'''
pass
def copyAttributes():
'''public boolean copyAttributes(final MboRemote actualCI, final MboRemote authorizedCI, final boolean overwriteAttributes, final boolean removeBlanksOnly, final boolean createdCI)
'''
pass
def getResults():
'''public List<CCIPromotionResults> getResults()
'''
pass
