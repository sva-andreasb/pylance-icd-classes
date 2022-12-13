COPYCI2ASSET = "String  COPYCI2ASSET""
COPYASSET2CI = "String  COPYASSET2CI""
MAXVARNAMESYNCSERIALNUM = "String  CCISYNCSERIALNUM""
def syncCIAsset():
'''public static void syncCIAsset(final CIRemote ci, final AssetRemote asset)
public static void syncCIAsset(final CIRemote ci, final AssetRemote asset, String syncOption)
'''
pass
def syncCIAssetSpec():
'''public static void syncCIAssetSpec(final MboRemote source, final MboRemote target, final boolean overrideNull)
public static void syncCIAssetSpec(final MboRemote source, final MboRemote target, final boolean overrideNull, final boolean syncStaticAttr)
public static boolean syncCIAssetSpec(final SpecificationMbo saveSpecMbo)
public static boolean syncCIAssetSpec(final SpecificationMbo saveSpecMbo, final MboRemote saveMbo, final MboRemote targetMbo, final boolean overrideNull, final boolean syncAssetStaticAttr)
'''
pass
def copyCIAssetSpec():
'''public static boolean copyCIAssetSpec(final SpecificationMbo srcSpec, final SpecificationMbo targetSpec, final boolean overrideNull)
'''
pass
def copySpecValue():
'''public static boolean copySpecValue(final String specAttrColName, final SpecificationMbo srcSpec, final SpecificationMbo targetSpec, final boolean overrideNull)
'''
pass
def copyAssetAttributesToCISpec():
'''public static void copyAssetAttributesToCISpec(final AssetRemote asset, final int assetStaticAttrID)
public static void copyAssetAttributesToCISpec(final AssetRemote asset, final CIRemote ci, final int assetStaticAttrID, final boolean overrideNull)
public static void copyAssetAttributesToCISpec(final AssetRemote asset, final CIRemote ci, final boolean overrideNull)
public static boolean copyAssetAttributesToCISpec(final CISpecRemote ciSpec, final AssetRemote asset, final int assetStaticAttrID, final boolean overrideNull)
'''
pass
def copyCISpecToAssetAttributes():
'''public static boolean copyCISpecToAssetAttributes(final CISpecRemote ciSpec, final AssetRemote asset, final int assetStaticAttrID, final boolean overrideNull)
public static void copyCISpecToAssetAttributes(final CIRemote ci, final AssetRemote asset, final boolean overrideNull)
'''
pass
def getSyncOption():
'''public static String getSyncOption(final MboRemote ci, final MboRemote asset, final boolean fromSyncDialog)
public static String getSyncOption(final MboRemote ci, final MboRemote asset)
'''
pass
def getMaxVarLinkOption():
'''public static String getMaxVarLinkOption()
'''
pass
def getMaxVarSyncSerialNumOption():
'''public static boolean getMaxVarSyncSerialNumOption()
'''
pass
def getMaxVarSyncOption():
'''public static boolean getMaxVarSyncOption()
'''
pass
def copyAttributes():
'''public static void copyAttributes(final MboRemote src, final MboRemote target, final String srcAttrName, final String targetAttrName)
'''
pass
def syncCIAssetForNewSpec():
'''public static boolean syncCIAssetForNewSpec(final SpecificationMbo newSpecMbo)
'''
pass
def initializeSpecValuesFromLinkMbo():
'''public static void initializeSpecValuesFromLinkMbo(final MboRemote linkMbo, final MboRemote changeSpecMbo)
'''
pass
def getParentMbo():
'''public static MboRemote getParentMbo(final SpecificationMboRemote specificationMbo)
'''
pass
def hasSpecValue():
'''public static boolean hasSpecValue(final SpecificationMbo specificationMbo)
'''
pass
def isAuthorizedCI():
'''public static boolean isAuthorizedCI(final String cinum, final UserInfo userInfo)
'''
pass
def isAuthorizedAsset():
'''public static boolean isAuthorizedAsset(final String assetNum, final String siteID, final UserInfo userInfo)
'''
pass
def getLinkedAsset():
'''public static AssetRemote getLinkedAsset(final CIRemote ci)
'''
pass
def getCISpecAssetAttributePairs():
'''public static final String[][] getCISpecAssetAttributePairs()
'''
pass
def synchronizeAssetCI():
'''public static int synchronizeAssetCI(final MboRemote syncDialogMbo)
'''
pass
