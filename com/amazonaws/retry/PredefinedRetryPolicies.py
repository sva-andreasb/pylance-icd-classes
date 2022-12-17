DEFAULT_MAX_ERROR_RETRY = "int  3"
DYNAMODB_DEFAULT_MAX_ERROR_RETRY = "int  10"
def shouldRetry():
    '''returns boolean\n\n
    shouldRetry(final AmazonWebServiceRequest originalRequest, final AmazonClientException exception, final int retriesAttempted)\n
    '''
