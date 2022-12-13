DISABLE_GET_OBJECT_MD5_VALIDATION_PROPERTY = "String  com.amazonaws.services.s3.disableGetObjectMD5Validation""
DISABLE_PUT_OBJECT_MD5_VALIDATION_PROPERTY = "String  com.amazonaws.services.s3.disablePutObjectMD5Validation""
def skipClientSideValidationPerGetResponse():
'''public boolean skipClientSideValidationPerGetResponse(final ObjectMetadata metadata)
'''
pass
def skipClientSideValidationPerPutResponse():
'''public boolean skipClientSideValidationPerPutResponse(final ObjectMetadata metadata)
'''
pass
def skipClientSideValidationPerUploadPartResponse():
'''public boolean skipClientSideValidationPerUploadPartResponse(final ObjectMetadata metadata)
'''
pass
def skipClientSideValidation():
'''public boolean skipClientSideValidation(final GetObjectRequest request, final ObjectMetadata returnedMetadata)
'''
pass
def skipClientSideValidationPerRequest():
'''public boolean skipClientSideValidationPerRequest(final PutObjectRequest request)
public boolean skipClientSideValidationPerRequest(final UploadPartRequest request)
public boolean skipClientSideValidationPerRequest(final GetObjectRequest request)
'''
pass
def skipServerSideValidation():
'''public boolean skipServerSideValidation(final PutObjectRequest request)
public boolean skipServerSideValidation(final UploadPartRequest request)
'''
pass
