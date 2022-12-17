def ():
    '''returns AWSKMSClient\n\n
    ()\n
    (final ClientConfiguration clientConfiguration)\n
    (final AWSCredentials awsCredentials)\n
    (final AWSCredentials awsCredentials, final ClientConfiguration clientConfiguration)\n
    (final AWSCredentialsProvider awsCredentialsProvider)\n
    (final AWSCredentialsProvider awsCredentialsProvider, final ClientConfiguration clientConfiguration)\n
    (final AWSCredentialsProvider awsCredentialsProvider, final ClientConfiguration clientConfiguration, final RequestMetricCollector requestMetricCollector)\n
    '''
def cancelKeyDeletion():
    '''returns CancelKeyDeletionResult\n\n
    cancelKeyDeletion(final CancelKeyDeletionRequest cancelKeyDeletionRequest)\n
    '''
def createAlias():
    '''returns CreateAliasResult\n\n
    createAlias(final CreateAliasRequest createAliasRequest)\n
    '''
def createGrant():
    '''returns CreateGrantResult\n\n
    createGrant(final CreateGrantRequest createGrantRequest)\n
    '''
def createKey():
    '''returns CreateKeyResult\n\n
    createKey(final CreateKeyRequest createKeyRequest)\n
    createKey()\n
    '''
def decrypt():
    '''returns DecryptResult\n\n
    decrypt(final DecryptRequest decryptRequest)\n
    '''
def deleteAlias():
    '''returns DeleteAliasResult\n\n
    deleteAlias(final DeleteAliasRequest deleteAliasRequest)\n
    '''
def describeKey():
    '''returns DescribeKeyResult\n\n
    describeKey(final DescribeKeyRequest describeKeyRequest)\n
    '''
def disableKey():
    '''returns DisableKeyResult\n\n
    disableKey(final DisableKeyRequest disableKeyRequest)\n
    '''
def disableKeyRotation():
    '''returns DisableKeyRotationResult\n\n
    disableKeyRotation(final DisableKeyRotationRequest disableKeyRotationRequest)\n
    '''
def enableKey():
    '''returns EnableKeyResult\n\n
    enableKey(final EnableKeyRequest enableKeyRequest)\n
    '''
def enableKeyRotation():
    '''returns EnableKeyRotationResult\n\n
    enableKeyRotation(final EnableKeyRotationRequest enableKeyRotationRequest)\n
    '''
def encrypt():
    '''returns EncryptResult\n\n
    encrypt(final EncryptRequest encryptRequest)\n
    '''
def generateDataKey():
    '''returns GenerateDataKeyResult\n\n
    generateDataKey(final GenerateDataKeyRequest generateDataKeyRequest)\n
    '''
def generateDataKeyWithoutPlaintext():
    '''returns GenerateDataKeyWithoutPlaintextResult\n\n
    generateDataKeyWithoutPlaintext(final GenerateDataKeyWithoutPlaintextRequest generateDataKeyWithoutPlaintextRequest)\n
    '''
def generateRandom():
    '''returns GenerateRandomResult\n\n
    generateRandom(final GenerateRandomRequest generateRandomRequest)\n
    generateRandom()\n
    '''
def getKeyPolicy():
    '''returns GetKeyPolicyResult\n\n
    getKeyPolicy(final GetKeyPolicyRequest getKeyPolicyRequest)\n
    '''
def getKeyRotationStatus():
    '''returns GetKeyRotationStatusResult\n\n
    getKeyRotationStatus(final GetKeyRotationStatusRequest getKeyRotationStatusRequest)\n
    '''
def listAliases():
    '''returns ListAliasesResult\n\n
    listAliases(final ListAliasesRequest listAliasesRequest)\n
    listAliases()\n
    '''
def listGrants():
    '''returns ListGrantsResult\n\n
    listGrants(final ListGrantsRequest listGrantsRequest)\n
    '''
def listKeyPolicies():
    '''returns ListKeyPoliciesResult\n\n
    listKeyPolicies(final ListKeyPoliciesRequest listKeyPoliciesRequest)\n
    '''
def listKeys():
    '''returns ListKeysResult\n\n
    listKeys(final ListKeysRequest listKeysRequest)\n
    listKeys()\n
    '''
def listRetirableGrants():
    '''returns ListRetirableGrantsResult\n\n
    listRetirableGrants(final ListRetirableGrantsRequest listRetirableGrantsRequest)\n
    '''
def putKeyPolicy():
    '''returns PutKeyPolicyResult\n\n
    putKeyPolicy(final PutKeyPolicyRequest putKeyPolicyRequest)\n
    '''
def reEncrypt():
    '''returns ReEncryptResult\n\n
    reEncrypt(final ReEncryptRequest reEncryptRequest)\n
    '''
def retireGrant():
    '''returns RetireGrantResult\n\n
    retireGrant(final RetireGrantRequest retireGrantRequest)\n
    retireGrant()\n
    '''
def revokeGrant():
    '''returns RevokeGrantResult\n\n
    revokeGrant(final RevokeGrantRequest revokeGrantRequest)\n
    '''
def scheduleKeyDeletion():
    '''returns ScheduleKeyDeletionResult\n\n
    scheduleKeyDeletion(final ScheduleKeyDeletionRequest scheduleKeyDeletionRequest)\n
    '''
def updateAlias():
    '''returns UpdateAliasResult\n\n
    updateAlias(final UpdateAliasRequest updateAliasRequest)\n
    '''
def updateKeyDescription():
    '''returns UpdateKeyDescriptionResult\n\n
    updateKeyDescription(final UpdateKeyDescriptionRequest updateKeyDescriptionRequest)\n
    '''
def getCachedResponseMetadata():
    '''returns ResponseMetadata\n\n
    getCachedResponseMetadata(final AmazonWebServiceRequest request)\n
    '''
