ASSET_WHERE_LIST = "String  \"status in (select value from synonymdomain where domainid = 'LOCASSETSTATUS' and maxvalue in ('NOT READY','OPERATING') and (synonymdomain.ORGID is null or synonymdomain.ORGID=ASSET.orgid)) and ORGID= :0 and classstructureid in (select classstructureid from classancestor where ancestor in (select varvalue from maxvars where varname='ITASSET')) and moved=0 \""
FOR_COMPUTERS = "String  \" and (tloampartition is null or tloampartition=0) and parent is null \""
FOR_PARTITIONS = "String  \" and tloampartition=1 \""
def ():
    '''returns FldLicAssetNum\n\n
    (final MboValue mbv)\n
    '''
def getList():
    '''returns MboSetRemote\n\n
    getList()\n
    '''
def validate():
    '''returns None\n\n
    validate()\n
    '''
