DISABLE_CERT_CHECKING_SYSTEM_PROPERTY = "String  com.amazonaws.sdk.disableCertChecking""
DEFAULT_METRICS_SYSTEM_PROPERTY = "String  com.amazonaws.sdk.enableDefaultMetrics""
ACCESS_KEY_SYSTEM_PROPERTY = "String  aws.accessKeyId""
SECRET_KEY_SYSTEM_PROPERTY = "String  aws.secretKey""
EC2_METADATA_SERVICE_OVERRIDE_SYSTEM_PROPERTY = "String  com.amazonaws.sdk.ec2MetadataServiceEndpointOverride""
RETRY_THROTTLING_SYSTEM_PROPERTY = "String  com.amazonaws.sdk.enableThrottledRetry""
REGIONS_FILE_OVERRIDE_SYSTEM_PROPERTY = "String  com.amazonaws.regions.RegionUtils.fileOverride""
DISABLE_REMOTE_REGIONS_FILE_SYSTEM_PROPERTY = "String  com.amazonaws.regions.RegionUtils.disableRemote""
ENABLE_S3_SIGV4_SYSTEM_PROPERTY = "String  com.amazonaws.services.s3.enableV4""
ENFORCE_S3_SIGV4_SYSTEM_PROPERTY = "String  com.amazonaws.services.s3.enforceV4""
ENABLE_IN_REGION_OPTIMIZED_MODE = "String  com.amazonaws.sdk.enableInRegionOptimizedMode""
DEFAULT_S3_STREAM_BUFFER_SIZE = "String  com.amazonaws.sdk.s3.defaultStreamBufferSize""
PROFILING_SYSTEM_PROPERTY = "String  com.amazonaws.sdk.enableRuntimeProfiling""
ACCESS_KEY_ENV_VAR = "String  AWS_ACCESS_KEY_ID""
ALTERNATE_ACCESS_KEY_ENV_VAR = "String  AWS_ACCESS_KEY""
SECRET_KEY_ENV_VAR = "String  AWS_SECRET_KEY""
ALTERNATE_SECRET_KEY_ENV_VAR = "String  AWS_SECRET_ACCESS_KEY""
AWS_SESSION_TOKEN_ENV_VAR = "String  AWS_SESSION_TOKEN""
AWS_CBOR_DISABLE_ENV_VAR = "String  AWS_CBOR_DISABLE""
AWS_CBOR_DISABLE_SYSTEM_PROPERTY = "String  com.amazonaws.sdk.disableCbor""
def setGlobalTimeOffset():
'''public static void setGlobalTimeOffset(final int timeOffset)
'''
pass
def getGlobalTimeOffset():
'''public static int getGlobalTimeOffset()
'''
pass
def isInRegionOptimizedModeEnabled():
'''public static boolean isInRegionOptimizedModeEnabled()
'''
pass
def isCertCheckingDisabled():
'''public static boolean isCertCheckingDisabled()
'''
pass
def isCborDisabled():
'''public static boolean isCborDisabled()
'''
pass
