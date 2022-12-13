def AWSKMSClient():
    '''public AWSKMSClient()
    public AWSKMSClient(final ClientConfiguration clientConfiguration)
    public AWSKMSClient(final AWSCredentials awsCredentials)
    public AWSKMSClient(final AWSCredentials awsCredentials, final ClientConfiguration clientConfiguration)
    public AWSKMSClient(final AWSCredentialsProvider awsCredentialsProvider)
    public AWSKMSClient(final AWSCredentialsProvider awsCredentialsProvider, final ClientConfiguration clientConfiguration)
    public AWSKMSClient(final AWSCredentialsProvider awsCredentialsProvider, final ClientConfiguration clientConfiguration, final RequestMetricCollector requestMetricCollector)
    '''
def cancelKeyDeletion():
    '''public CancelKeyDeletionResult cancelKeyDeletion(final CancelKeyDeletionRequest cancelKeyDeletionRequest)
    '''
def createAlias():
    '''public CreateAliasResult createAlias(final CreateAliasRequest createAliasRequest)
    '''
def createGrant():
    '''public CreateGrantResult createGrant(final CreateGrantRequest createGrantRequest)
    '''
def createKey():
    '''public CreateKeyResult createKey(final CreateKeyRequest createKeyRequest)
    public CreateKeyResult createKey()
    '''
def decrypt():
    '''public DecryptResult decrypt(final DecryptRequest decryptRequest)
    '''
def deleteAlias():
    '''public DeleteAliasResult deleteAlias(final DeleteAliasRequest deleteAliasRequest)
    '''
def describeKey():
    '''public DescribeKeyResult describeKey(final DescribeKeyRequest describeKeyRequest)
    '''
def disableKey():
    '''public DisableKeyResult disableKey(final DisableKeyRequest disableKeyRequest)
    '''
def disableKeyRotation():
    '''public DisableKeyRotationResult disableKeyRotation(final DisableKeyRotationRequest disableKeyRotationRequest)
    '''
def enableKey():
    '''public EnableKeyResult enableKey(final EnableKeyRequest enableKeyRequest)
    '''
def enableKeyRotation():
    '''public EnableKeyRotationResult enableKeyRotation(final EnableKeyRotationRequest enableKeyRotationRequest)
    '''
def encrypt():
    '''public EncryptResult encrypt(final EncryptRequest encryptRequest)
    '''
def generateDataKey():
    '''public GenerateDataKeyResult generateDataKey(final GenerateDataKeyRequest generateDataKeyRequest)
    '''
def generateDataKeyWithoutPlaintext():
    '''public GenerateDataKeyWithoutPlaintextResult generateDataKeyWithoutPlaintext(final GenerateDataKeyWithoutPlaintextRequest generateDataKeyWithoutPlaintextRequest)
    '''
def generateRandom():
    '''public GenerateRandomResult generateRandom(final GenerateRandomRequest generateRandomRequest)
    public GenerateRandomResult generateRandom()
    '''
def getKeyPolicy():
    '''public GetKeyPolicyResult getKeyPolicy(final GetKeyPolicyRequest getKeyPolicyRequest)
    '''
def getKeyRotationStatus():
    '''public GetKeyRotationStatusResult getKeyRotationStatus(final GetKeyRotationStatusRequest getKeyRotationStatusRequest)
    '''
def listAliases():
    '''public ListAliasesResult listAliases(final ListAliasesRequest listAliasesRequest)
    public ListAliasesResult listAliases()
    '''
def listGrants():
    '''public ListGrantsResult listGrants(final ListGrantsRequest listGrantsRequest)
    '''
def listKeyPolicies():
    '''public ListKeyPoliciesResult listKeyPolicies(final ListKeyPoliciesRequest listKeyPoliciesRequest)
    '''
def listKeys():
    '''public ListKeysResult listKeys(final ListKeysRequest listKeysRequest)
    public ListKeysResult listKeys()
    '''
def listRetirableGrants():
    '''public ListRetirableGrantsResult listRetirableGrants(final ListRetirableGrantsRequest listRetirableGrantsRequest)
    '''
def putKeyPolicy():
    '''public PutKeyPolicyResult putKeyPolicy(final PutKeyPolicyRequest putKeyPolicyRequest)
    '''
def reEncrypt():
    '''public ReEncryptResult reEncrypt(final ReEncryptRequest reEncryptRequest)
    '''
def retireGrant():
    '''public RetireGrantResult retireGrant(final RetireGrantRequest retireGrantRequest)
    public RetireGrantResult retireGrant()
    '''
def revokeGrant():
    '''public RevokeGrantResult revokeGrant(final RevokeGrantRequest revokeGrantRequest)
    '''
def scheduleKeyDeletion():
    '''public ScheduleKeyDeletionResult scheduleKeyDeletion(final ScheduleKeyDeletionRequest scheduleKeyDeletionRequest)
    '''
def updateAlias():
    '''public UpdateAliasResult updateAlias(final UpdateAliasRequest updateAliasRequest)
    '''
def updateKeyDescription():
    '''public UpdateKeyDescriptionResult updateKeyDescription(final UpdateKeyDescriptionRequest updateKeyDescriptionRequest)
    '''
def getCachedResponseMetadata():
    '''public ResponseMetadata getCachedResponseMetadata(final AmazonWebServiceRequest request)
    '''
