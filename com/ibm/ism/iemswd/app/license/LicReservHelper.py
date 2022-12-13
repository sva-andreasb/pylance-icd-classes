ACTIVE_STATUS = "String ACTIVE""
FAILED_STATUS = "String FAILED""
OVERALLOCATED_STATUS = "String OVERALLOCATED""
SUCCESS_STATUS = "String SUCCESS""
DEFAULT_LICENSE_VALUE = "String 1""
INACTIVE_LICENSE_VALUE = "String -1""
OTHER_LICENSE_VALUE = "String 0""
def getDefaultLicenseForSoftware():
'''public static MboRemote getDefaultLicenseForSoftware(final long tloamsoftwareid, final UserInfo userInfo)
public static ArrayList<MboRemote> getDefaultLicenseForSoftware(final ArrayList<Long> tloamsoftwareids, final UserInfo userInfo)
'''
pass
def isLicenseAvailable():
'''public static boolean isLicenseAvailable(final MboSetRemote assetSet, final String licensenum, final String orgid, final UserInfo userInfo)
public static boolean isLicenseAvailable(final String assetNum, final String assetSiteID, final ArrayList<String> licensenums, final ArrayList<String> orgids, final UserInfo userInfo)
'''
pass
def reserveLicense():
'''public static boolean reserveLicense(final MboSetRemote assetSet, final String licensenum, final String orgid, final long tloamsoftwareid, final MboRemote workOrder, final boolean overAllocate)
'''
pass
def reserveLicensesForAsset():
'''public static boolean reserveLicensesForAsset(final String assetnum, final String assetSiteID, final ArrayList<String> licensenums, final ArrayList<String> orgids, final ArrayList<Long> tloamsoftwareids, final MboRemote workOrder, final boolean overAllocate)
'''
pass
def allocateLicenseToAssets():
'''public static boolean allocateLicenseToAssets(final IEMSWDCustomMboSetRemote assetSet, final MboRemote workOrder)
'''
pass
def allocateLicense():
'''public static boolean allocateLicense(final ArrayList<IEMSWDCustomMboRemote> assetList, final String licensenum, final String orgid, final MboRemote workOrder)
'''
pass
def allocateLicensesForAsset():
'''public static boolean allocateLicensesForAsset(final IEMSWDCustomMboSetRemote licenseSet, final MboRemote workOrder)
'''
pass
def removeLicenseReservation():
'''public static double removeLicenseReservation(final MboSetRemote assetSet, final String licensenum, final String orgid, final MboRemote workOrder)
'''
pass
def removeLicenseReservationsForAsset():
'''public static double removeLicenseReservationsForAsset(final String assetNum, final String assetSiteID, final ArrayList<String> licensenums, final ArrayList<String> orgids, final MboRemote workOrder)
'''
pass
def deleteLicenseAllocationsForAsset():
'''public static void deleteLicenseAllocationsForAsset(final String assetNum, final String siteID, final UserInfo userInfo)
'''
pass
def getSoftwareFromAssetAllocations():
'''public static HashMap<String, String[]> getSoftwareFromAssetAllocations(final String assetNum, final String siteID, final UserInfo userInfo)
'''
pass
