SQL_FOR_ASSETNUMS_SHOULD_NOT_SHOWN_INBV = "String  \"select assetnum from dclnodesinbv\""
SQL_FOR_ASSETNUMS_EXIST_IN_ASSETLOCRELATION_UNIQ = "String  \"select assetnum from extnodesinastlocrel\""
def findAssetsToBeExcludedInBV():
    '''returns Set<String>\n\n
    findAssetsToBeExcludedInBV()\n
    '''
