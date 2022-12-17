def ():
    '''returns SetObjectAclRequest\n\n
    (final String bucketName, final String key, final AccessControlList acl)\n
    (final String bucketName, final String key, final CannedAccessControlList acl)\n
    (final String bucketName, final String key, final String versionId, final AccessControlList acl)\n
    (final String bucketName, final String key, final String versionId, final CannedAccessControlList acl)\n
    '''
def getBucketName():
    '''returns String\n\n
    getBucketName()\n
    '''
def getKey():
    '''returns String\n\n
    getKey()\n
    '''
def getVersionId():
    '''returns String\n\n
    getVersionId()\n
    '''
def getAcl():
    '''returns AccessControlList\n\n
    getAcl()\n
    '''
def getCannedAcl():
    '''returns CannedAccessControlList\n\n
    getCannedAcl()\n
    '''
def isRequesterPays():
    '''returns boolean\n\n
    isRequesterPays()\n
    '''
def setRequesterPays():
    '''returns None\n\n
    setRequesterPays(final boolean isRequesterPays)\n
    '''
def withRequesterPays():
    '''returns SetObjectAclRequest\n\n
    withRequesterPays(final boolean isRequesterPays)\n
    '''
