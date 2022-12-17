DISABLE_GET_OBJECT_MD5_VALIDATION_PROPERTY = "String  \"com.amazonaws.services.s3.disableGetObjectMD5Validation\""
DISABLE_PUT_OBJECT_MD5_VALIDATION_PROPERTY = "String  \"com.amazonaws.services.s3.disablePutObjectMD5Validation\""
def skipClientSideValidationPerGetResponse():
    '''returns boolean\n\n
    skipClientSideValidationPerGetResponse(final ObjectMetadata metadata)\n
    '''
def skipClientSideValidationPerPutResponse():
    '''returns boolean\n\n
    skipClientSideValidationPerPutResponse(final ObjectMetadata metadata)\n
    '''
def skipClientSideValidationPerUploadPartResponse():
    '''returns boolean\n\n
    skipClientSideValidationPerUploadPartResponse(final ObjectMetadata metadata)\n
    '''
def skipClientSideValidation():
    '''returns boolean\n\n
    skipClientSideValidation(final GetObjectRequest request, final ObjectMetadata returnedMetadata)\n
    '''
def skipClientSideValidationPerRequest():
    '''returns boolean\n\n
    skipClientSideValidationPerRequest(final PutObjectRequest request)\n
    skipClientSideValidationPerRequest(final UploadPartRequest request)\n
    skipClientSideValidationPerRequest(final GetObjectRequest request)\n
    '''
def skipServerSideValidation():
    '''returns boolean\n\n
    skipServerSideValidation(final PutObjectRequest request)\n
    skipServerSideValidation(final UploadPartRequest request)\n
    '''
