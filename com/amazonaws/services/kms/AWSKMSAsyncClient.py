def AWSKMSAsyncClient():
    '''public AWSKMSAsyncClient()
    public AWSKMSAsyncClient(final ClientConfiguration clientConfiguration)
    public AWSKMSAsyncClient(final AWSCredentials awsCredentials)
    public AWSKMSAsyncClient(final AWSCredentials awsCredentials, final ExecutorService executorService)
    public AWSKMSAsyncClient(final AWSCredentials awsCredentials, final ClientConfiguration clientConfiguration, final ExecutorService executorService)
    public AWSKMSAsyncClient(final AWSCredentialsProvider awsCredentialsProvider)
    public AWSKMSAsyncClient(final AWSCredentialsProvider awsCredentialsProvider, final ClientConfiguration clientConfiguration)
    public AWSKMSAsyncClient(final AWSCredentialsProvider awsCredentialsProvider, final ExecutorService executorService)
    public AWSKMSAsyncClient(final AWSCredentialsProvider awsCredentialsProvider, final ClientConfiguration clientConfiguration, final ExecutorService executorService)
    '''
def getExecutorService():
    '''public ExecutorService getExecutorService()
    '''
def cancelKeyDeletionAsync():
    '''public Future<CancelKeyDeletionResult> cancelKeyDeletionAsync(final CancelKeyDeletionRequest request)
    public Future<CancelKeyDeletionResult> cancelKeyDeletionAsync(final CancelKeyDeletionRequest request, final AsyncHandler<CancelKeyDeletionRequest, CancelKeyDeletionResult> asyncHandler)
    '''
def call():
    '''public CancelKeyDeletionResult call()
    public CreateAliasResult call()
    public CreateGrantResult call()
    public CreateKeyResult call()
    public DecryptResult call()
    public DeleteAliasResult call()
    public DescribeKeyResult call()
    public DisableKeyResult call()
    public DisableKeyRotationResult call()
    public EnableKeyResult call()
    public EnableKeyRotationResult call()
    public EncryptResult call()
    public GenerateDataKeyResult call()
    public GenerateDataKeyWithoutPlaintextResult call()
    public GenerateRandomResult call()
    public GetKeyPolicyResult call()
    public GetKeyRotationStatusResult call()
    public ListAliasesResult call()
    public ListGrantsResult call()
    public ListKeyPoliciesResult call()
    public ListKeysResult call()
    public ListRetirableGrantsResult call()
    public PutKeyPolicyResult call()
    public ReEncryptResult call()
    public RetireGrantResult call()
    public RevokeGrantResult call()
    public ScheduleKeyDeletionResult call()
    public UpdateAliasResult call()
    public UpdateKeyDescriptionResult call()
    '''
def createAliasAsync():
    '''public Future<CreateAliasResult> createAliasAsync(final CreateAliasRequest request)
    public Future<CreateAliasResult> createAliasAsync(final CreateAliasRequest request, final AsyncHandler<CreateAliasRequest, CreateAliasResult> asyncHandler)
    '''
def createGrantAsync():
    '''public Future<CreateGrantResult> createGrantAsync(final CreateGrantRequest request)
    public Future<CreateGrantResult> createGrantAsync(final CreateGrantRequest request, final AsyncHandler<CreateGrantRequest, CreateGrantResult> asyncHandler)
    '''
def createKeyAsync():
    '''public Future<CreateKeyResult> createKeyAsync(final CreateKeyRequest request)
    public Future<CreateKeyResult> createKeyAsync(final CreateKeyRequest request, final AsyncHandler<CreateKeyRequest, CreateKeyResult> asyncHandler)
    public Future<CreateKeyResult> createKeyAsync()
    public Future<CreateKeyResult> createKeyAsync(final AsyncHandler<CreateKeyRequest, CreateKeyResult> asyncHandler)
    '''
def decryptAsync():
    '''public Future<DecryptResult> decryptAsync(final DecryptRequest request)
    public Future<DecryptResult> decryptAsync(final DecryptRequest request, final AsyncHandler<DecryptRequest, DecryptResult> asyncHandler)
    '''
def deleteAliasAsync():
    '''public Future<DeleteAliasResult> deleteAliasAsync(final DeleteAliasRequest request)
    public Future<DeleteAliasResult> deleteAliasAsync(final DeleteAliasRequest request, final AsyncHandler<DeleteAliasRequest, DeleteAliasResult> asyncHandler)
    '''
def describeKeyAsync():
    '''public Future<DescribeKeyResult> describeKeyAsync(final DescribeKeyRequest request)
    public Future<DescribeKeyResult> describeKeyAsync(final DescribeKeyRequest request, final AsyncHandler<DescribeKeyRequest, DescribeKeyResult> asyncHandler)
    '''
def disableKeyAsync():
    '''public Future<DisableKeyResult> disableKeyAsync(final DisableKeyRequest request)
    public Future<DisableKeyResult> disableKeyAsync(final DisableKeyRequest request, final AsyncHandler<DisableKeyRequest, DisableKeyResult> asyncHandler)
    '''
def disableKeyRotationAsync():
    '''public Future<DisableKeyRotationResult> disableKeyRotationAsync(final DisableKeyRotationRequest request)
    public Future<DisableKeyRotationResult> disableKeyRotationAsync(final DisableKeyRotationRequest request, final AsyncHandler<DisableKeyRotationRequest, DisableKeyRotationResult> asyncHandler)
    '''
def enableKeyAsync():
    '''public Future<EnableKeyResult> enableKeyAsync(final EnableKeyRequest request)
    public Future<EnableKeyResult> enableKeyAsync(final EnableKeyRequest request, final AsyncHandler<EnableKeyRequest, EnableKeyResult> asyncHandler)
    '''
def enableKeyRotationAsync():
    '''public Future<EnableKeyRotationResult> enableKeyRotationAsync(final EnableKeyRotationRequest request)
    public Future<EnableKeyRotationResult> enableKeyRotationAsync(final EnableKeyRotationRequest request, final AsyncHandler<EnableKeyRotationRequest, EnableKeyRotationResult> asyncHandler)
    '''
def encryptAsync():
    '''public Future<EncryptResult> encryptAsync(final EncryptRequest request)
    public Future<EncryptResult> encryptAsync(final EncryptRequest request, final AsyncHandler<EncryptRequest, EncryptResult> asyncHandler)
    '''
def generateDataKeyAsync():
    '''public Future<GenerateDataKeyResult> generateDataKeyAsync(final GenerateDataKeyRequest request)
    public Future<GenerateDataKeyResult> generateDataKeyAsync(final GenerateDataKeyRequest request, final AsyncHandler<GenerateDataKeyRequest, GenerateDataKeyResult> asyncHandler)
    '''
def generateDataKeyWithoutPlaintextAsync():
    '''public Future<GenerateDataKeyWithoutPlaintextResult> generateDataKeyWithoutPlaintextAsync(final GenerateDataKeyWithoutPlaintextRequest request)
    public Future<GenerateDataKeyWithoutPlaintextResult> generateDataKeyWithoutPlaintextAsync(final GenerateDataKeyWithoutPlaintextRequest request, final AsyncHandler<GenerateDataKeyWithoutPlaintextRequest, GenerateDataKeyWithoutPlaintextResult> asyncHandler)
    '''
def generateRandomAsync():
    '''public Future<GenerateRandomResult> generateRandomAsync(final GenerateRandomRequest request)
    public Future<GenerateRandomResult> generateRandomAsync(final GenerateRandomRequest request, final AsyncHandler<GenerateRandomRequest, GenerateRandomResult> asyncHandler)
    public Future<GenerateRandomResult> generateRandomAsync()
    public Future<GenerateRandomResult> generateRandomAsync(final AsyncHandler<GenerateRandomRequest, GenerateRandomResult> asyncHandler)
    '''
def getKeyPolicyAsync():
    '''public Future<GetKeyPolicyResult> getKeyPolicyAsync(final GetKeyPolicyRequest request)
    public Future<GetKeyPolicyResult> getKeyPolicyAsync(final GetKeyPolicyRequest request, final AsyncHandler<GetKeyPolicyRequest, GetKeyPolicyResult> asyncHandler)
    '''
def getKeyRotationStatusAsync():
    '''public Future<GetKeyRotationStatusResult> getKeyRotationStatusAsync(final GetKeyRotationStatusRequest request)
    public Future<GetKeyRotationStatusResult> getKeyRotationStatusAsync(final GetKeyRotationStatusRequest request, final AsyncHandler<GetKeyRotationStatusRequest, GetKeyRotationStatusResult> asyncHandler)
    '''
def listAliasesAsync():
    '''public Future<ListAliasesResult> listAliasesAsync(final ListAliasesRequest request)
    public Future<ListAliasesResult> listAliasesAsync(final ListAliasesRequest request, final AsyncHandler<ListAliasesRequest, ListAliasesResult> asyncHandler)
    public Future<ListAliasesResult> listAliasesAsync()
    public Future<ListAliasesResult> listAliasesAsync(final AsyncHandler<ListAliasesRequest, ListAliasesResult> asyncHandler)
    '''
def listGrantsAsync():
    '''public Future<ListGrantsResult> listGrantsAsync(final ListGrantsRequest request)
    public Future<ListGrantsResult> listGrantsAsync(final ListGrantsRequest request, final AsyncHandler<ListGrantsRequest, ListGrantsResult> asyncHandler)
    '''
def listKeyPoliciesAsync():
    '''public Future<ListKeyPoliciesResult> listKeyPoliciesAsync(final ListKeyPoliciesRequest request)
    public Future<ListKeyPoliciesResult> listKeyPoliciesAsync(final ListKeyPoliciesRequest request, final AsyncHandler<ListKeyPoliciesRequest, ListKeyPoliciesResult> asyncHandler)
    '''
def listKeysAsync():
    '''public Future<ListKeysResult> listKeysAsync(final ListKeysRequest request)
    public Future<ListKeysResult> listKeysAsync(final ListKeysRequest request, final AsyncHandler<ListKeysRequest, ListKeysResult> asyncHandler)
    public Future<ListKeysResult> listKeysAsync()
    public Future<ListKeysResult> listKeysAsync(final AsyncHandler<ListKeysRequest, ListKeysResult> asyncHandler)
    '''
def listRetirableGrantsAsync():
    '''public Future<ListRetirableGrantsResult> listRetirableGrantsAsync(final ListRetirableGrantsRequest request)
    public Future<ListRetirableGrantsResult> listRetirableGrantsAsync(final ListRetirableGrantsRequest request, final AsyncHandler<ListRetirableGrantsRequest, ListRetirableGrantsResult> asyncHandler)
    '''
def putKeyPolicyAsync():
    '''public Future<PutKeyPolicyResult> putKeyPolicyAsync(final PutKeyPolicyRequest request)
    public Future<PutKeyPolicyResult> putKeyPolicyAsync(final PutKeyPolicyRequest request, final AsyncHandler<PutKeyPolicyRequest, PutKeyPolicyResult> asyncHandler)
    '''
def reEncryptAsync():
    '''public Future<ReEncryptResult> reEncryptAsync(final ReEncryptRequest request)
    public Future<ReEncryptResult> reEncryptAsync(final ReEncryptRequest request, final AsyncHandler<ReEncryptRequest, ReEncryptResult> asyncHandler)
    '''
def retireGrantAsync():
    '''public Future<RetireGrantResult> retireGrantAsync(final RetireGrantRequest request)
    public Future<RetireGrantResult> retireGrantAsync(final RetireGrantRequest request, final AsyncHandler<RetireGrantRequest, RetireGrantResult> asyncHandler)
    public Future<RetireGrantResult> retireGrantAsync()
    public Future<RetireGrantResult> retireGrantAsync(final AsyncHandler<RetireGrantRequest, RetireGrantResult> asyncHandler)
    '''
def revokeGrantAsync():
    '''public Future<RevokeGrantResult> revokeGrantAsync(final RevokeGrantRequest request)
    public Future<RevokeGrantResult> revokeGrantAsync(final RevokeGrantRequest request, final AsyncHandler<RevokeGrantRequest, RevokeGrantResult> asyncHandler)
    '''
def scheduleKeyDeletionAsync():
    '''public Future<ScheduleKeyDeletionResult> scheduleKeyDeletionAsync(final ScheduleKeyDeletionRequest request)
    public Future<ScheduleKeyDeletionResult> scheduleKeyDeletionAsync(final ScheduleKeyDeletionRequest request, final AsyncHandler<ScheduleKeyDeletionRequest, ScheduleKeyDeletionResult> asyncHandler)
    '''
def updateAliasAsync():
    '''public Future<UpdateAliasResult> updateAliasAsync(final UpdateAliasRequest request)
    public Future<UpdateAliasResult> updateAliasAsync(final UpdateAliasRequest request, final AsyncHandler<UpdateAliasRequest, UpdateAliasResult> asyncHandler)
    '''
def updateKeyDescriptionAsync():
    '''public Future<UpdateKeyDescriptionResult> updateKeyDescriptionAsync(final UpdateKeyDescriptionRequest request)
    public Future<UpdateKeyDescriptionResult> updateKeyDescriptionAsync(final UpdateKeyDescriptionRequest request, final AsyncHandler<UpdateKeyDescriptionRequest, UpdateKeyDescriptionResult> asyncHandler)
    '''
def shutdown():
    '''public void shutdown()
    '''
