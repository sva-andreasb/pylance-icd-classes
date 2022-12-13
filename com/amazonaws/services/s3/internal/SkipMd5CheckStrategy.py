DISABLE_GET_OBJECT_MD5_VALIDATION_PROPERTY = "String  \"com.amazonaws.services.s3.disableGetObjectMD5Validation\""
DISABLE_PUT_OBJECT_MD5_VALIDATION_PROPERTY = "String  \"com.amazonaws.services.s3.disablePutObjectMD5Validation\""
def skipClientSideValidationPerGetResponse():
    '''public boolean skipClientSideValidationPerGetResponse(final ObjectMetadata metadata)
    '''
def skipClientSideValidationPerPutResponse():
    '''public boolean skipClientSideValidationPerPutResponse(final ObjectMetadata metadata)
    '''
def skipClientSideValidationPerUploadPartResponse():
    '''public boolean skipClientSideValidationPerUploadPartResponse(final ObjectMetadata metadata)
    '''
def skipClientSideValidation():
    '''public boolean skipClientSideValidation(final GetObjectRequest request, final ObjectMetadata returnedMetadata)
    '''
def skipClientSideValidationPerRequest():
    '''public boolean skipClientSideValidationPerRequest(final PutObjectRequest request)
    public boolean skipClientSideValidationPerRequest(final UploadPartRequest request)
    public boolean skipClientSideValidationPerRequest(final GetObjectRequest request)
    '''
def skipServerSideValidation():
    '''public boolean skipServerSideValidation(final PutObjectRequest request)
    public boolean skipServerSideValidation(final UploadPartRequest request)
    '''
