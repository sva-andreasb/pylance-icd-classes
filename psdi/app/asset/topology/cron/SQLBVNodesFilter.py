SQL_FOR_ASSETNUMS_TO_BE_EXCLUDED_DIRECTLY = "String  \"select assetnum from extnodesinastlocrel where assetnum in (select assetnum from dclnodesinbv)\""
def findAssetsToBeExcludedInBV():
    '''returns Set<String>\n\n
    findAssetsToBeExcludedInBV()\n
    '''
