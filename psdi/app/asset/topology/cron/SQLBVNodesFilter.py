SQL_FOR_ASSETNUMS_TO_BE_EXCLUDED_DIRECTLY = "String  \"select assetnum from extnodesinastlocrel where assetnum in (select assetnum from dclnodesinbv)\""
def findAssetsToBeExcludedInBV():
    '''    public Set<String> findAssetsToBeExcludedInBV()
    public static Set<String> findAssetsToBeExcludedInBV(final Connection connection)
    '''
