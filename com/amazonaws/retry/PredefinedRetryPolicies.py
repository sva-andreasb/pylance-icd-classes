DEFAULT_MAX_ERROR_RETRY = "int  3"
DYNAMODB_DEFAULT_MAX_ERROR_RETRY = "int  10"
def getDefaultRetryPolicy():
'''public static RetryPolicy getDefaultRetryPolicy()
'''
pass
def getDynamoDBDefaultRetryPolicy():
'''public static RetryPolicy getDynamoDBDefaultRetryPolicy()
'''
pass
def getDefaultRetryPolicyWithCustomMaxRetries():
'''public static RetryPolicy getDefaultRetryPolicyWithCustomMaxRetries(final int maxErrorRetry)
'''
pass
def getDynamoDBDefaultRetryPolicyWithCustomMaxRetries():
'''public static RetryPolicy getDynamoDBDefaultRetryPolicyWithCustomMaxRetries(final int maxErrorRetry)
'''
pass
def shouldRetry():
'''public boolean shouldRetry(final AmazonWebServiceRequest originalRequest, final AmazonClientException exception, final int retriesAttempted)
'''
pass
def delayBeforeNextRetry():
'''public final long delayBeforeNextRetry(final AmazonWebServiceRequest originalRequest, final AmazonClientException exception, final int retriesAttempted)
public final long delayBeforeNextRetry(final AmazonWebServiceRequest originalRequest, final AmazonClientException exception, final int retriesAttempted)
'''
pass
