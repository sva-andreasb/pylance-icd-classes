def ():
    '''returns CopyObjectRequest\n\n
    (final String sourceBucketName, final String sourceKey, final String destinationBucketName, final String destinationKey)\n
    (final String sourceBucketName, final String sourceKey, final String sourceVersionId, final String destinationBucketName, final String destinationKey)\n
    '''
def getSourceBucketName():
    '''returns String\n\n
    getSourceBucketName()\n
    '''
def setSourceBucketName():
    '''returns None\n\n
    setSourceBucketName(final String sourceBucketName)\n
    '''
def withSourceBucketName():
    '''returns CopyObjectRequest\n\n
    withSourceBucketName(final String sourceBucketName)\n
    '''
def getSourceKey():
    '''returns String\n\n
    getSourceKey()\n
    '''
def setSourceKey():
    '''returns None\n\n
    setSourceKey(final String sourceKey)\n
    '''
def withSourceKey():
    '''returns CopyObjectRequest\n\n
    withSourceKey(final String sourceKey)\n
    '''
def getSourceVersionId():
    '''returns String\n\n
    getSourceVersionId()\n
    '''
def setSourceVersionId():
    '''returns None\n\n
    setSourceVersionId(final String sourceVersionId)\n
    '''
def withSourceVersionId():
    '''returns CopyObjectRequest\n\n
    withSourceVersionId(final String sourceVersionId)\n
    '''
def getDestinationBucketName():
    '''returns String\n\n
    getDestinationBucketName()\n
    '''
def setDestinationBucketName():
    '''returns None\n\n
    setDestinationBucketName(final String destinationBucketName)\n
    '''
def withDestinationBucketName():
    '''returns CopyObjectRequest\n\n
    withDestinationBucketName(final String destinationBucketName)\n
    '''
def getDestinationKey():
    '''returns String\n\n
    getDestinationKey()\n
    '''
def setDestinationKey():
    '''returns None\n\n
    setDestinationKey(final String destinationKey)\n
    '''
def withDestinationKey():
    '''returns CopyObjectRequest\n\n
    withDestinationKey(final String destinationKey)\n
    '''
def getStorageClass():
    '''returns String\n\n
    getStorageClass()\n
    '''
def setStorageClass():
    '''returns None\n\n
    setStorageClass(final String storageClass)\n
    setStorageClass(final StorageClass storageClass)\n
    '''
def withStorageClass():
    '''returns CopyObjectRequest\n\n
    withStorageClass(final String storageClass)\n
    withStorageClass(final StorageClass storageClass)\n
    '''
def getCannedAccessControlList():
    '''returns CannedAccessControlList\n\n
    getCannedAccessControlList()\n
    '''
def setCannedAccessControlList():
    '''returns None\n\n
    setCannedAccessControlList(final CannedAccessControlList cannedACL)\n
    '''
def withCannedAccessControlList():
    '''returns CopyObjectRequest\n\n
    withCannedAccessControlList(final CannedAccessControlList cannedACL)\n
    '''
def getAccessControlList():
    '''returns AccessControlList\n\n
    getAccessControlList()\n
    '''
def setAccessControlList():
    '''returns None\n\n
    setAccessControlList(final AccessControlList accessControlList)\n
    '''
def withAccessControlList():
    '''returns CopyObjectRequest\n\n
    withAccessControlList(final AccessControlList accessControlList)\n
    '''
def getNewObjectMetadata():
    '''returns ObjectMetadata\n\n
    getNewObjectMetadata()\n
    '''
def setNewObjectMetadata():
    '''returns None\n\n
    setNewObjectMetadata(final ObjectMetadata newObjectMetadata)\n
    '''
def withNewObjectMetadata():
    '''returns CopyObjectRequest\n\n
    withNewObjectMetadata(final ObjectMetadata newObjectMetadata)\n
    '''
def getMatchingETagConstraints():
    '''returns List<String>\n\n
    getMatchingETagConstraints()\n
    '''
def setMatchingETagConstraints():
    '''returns None\n\n
    setMatchingETagConstraints(final List<String> eTagList)\n
    '''
def withMatchingETagConstraint():
    '''returns CopyObjectRequest\n\n
    withMatchingETagConstraint(final String eTag)\n
    '''
def getNonmatchingETagConstraints():
    '''returns List<String>\n\n
    getNonmatchingETagConstraints()\n
    '''
def setNonmatchingETagConstraints():
    '''returns None\n\n
    setNonmatchingETagConstraints(final List<String> eTagList)\n
    '''
def withNonmatchingETagConstraint():
    '''returns CopyObjectRequest\n\n
    withNonmatchingETagConstraint(final String eTag)\n
    '''
def getUnmodifiedSinceConstraint():
    '''returns Date\n\n
    getUnmodifiedSinceConstraint()\n
    '''
def setUnmodifiedSinceConstraint():
    '''returns None\n\n
    setUnmodifiedSinceConstraint(final Date date)\n
    '''
def withUnmodifiedSinceConstraint():
    '''returns CopyObjectRequest\n\n
    withUnmodifiedSinceConstraint(final Date date)\n
    '''
def getModifiedSinceConstraint():
    '''returns Date\n\n
    getModifiedSinceConstraint()\n
    '''
def setModifiedSinceConstraint():
    '''returns None\n\n
    setModifiedSinceConstraint(final Date date)\n
    '''
def withModifiedSinceConstraint():
    '''returns CopyObjectRequest\n\n
    withModifiedSinceConstraint(final Date date)\n
    '''
def setRedirectLocation():
    '''returns None\n\n
    setRedirectLocation(final String redirectLocation)\n
    '''
def getRedirectLocation():
    '''returns String\n\n
    getRedirectLocation()\n
    '''
def withRedirectLocation():
    '''returns CopyObjectRequest\n\n
    withRedirectLocation(final String redirectLocation)\n
    '''
def getSourceSSECustomerKey():
    '''returns SSECustomerKey\n\n
    getSourceSSECustomerKey()\n
    '''
def setSourceSSECustomerKey():
    '''returns None\n\n
    setSourceSSECustomerKey(final SSECustomerKey sseKey)\n
    '''
def withSourceSSECustomerKey():
    '''returns CopyObjectRequest\n\n
    withSourceSSECustomerKey(final SSECustomerKey sseKey)\n
    '''
def getDestinationSSECustomerKey():
    '''returns SSECustomerKey\n\n
    getDestinationSSECustomerKey()\n
    '''
def setDestinationSSECustomerKey():
    '''returns None\n\n
    setDestinationSSECustomerKey(final SSECustomerKey sseKey)\n
    '''
def withDestinationSSECustomerKey():
    '''returns CopyObjectRequest\n\n
    withDestinationSSECustomerKey(final SSECustomerKey sseKey)\n
    '''
def getSSEAwsKeyManagementParams():
    '''returns SSEAwsKeyManagementParams\n\n
    getSSEAwsKeyManagementParams()\n
    '''
def setSSEAwsKeyManagementParams():
    '''returns None\n\n
    setSSEAwsKeyManagementParams(final SSEAwsKeyManagementParams params)\n
    '''
def withSSEAwsKeyManagementParams():
    '''returns CopyObjectRequest\n\n
    withSSEAwsKeyManagementParams(final SSEAwsKeyManagementParams sseAwsKeyManagementParams)\n
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
    '''returns CopyObjectRequest\n\n
    withRequesterPays(final boolean isRequesterPays)\n
    '''
