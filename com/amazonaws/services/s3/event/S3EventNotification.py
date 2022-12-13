def S3EventNotification():
'''public S3EventNotification(@JsonProperty("Records") final List<S3EventNotificationRecord> records)
'''
pass
def parseJson():
'''public static S3EventNotification parseJson(final String json)
'''
pass
def getRecords():
'''public List<S3EventNotificationRecord> getRecords()
'''
pass
def toJson():
'''public String toJson()
'''
pass
def UserIdentityEntity():
'''public UserIdentityEntity(@JsonProperty("principalId") final String principalId)
'''
pass
def getPrincipalId():
'''public String getPrincipalId()
'''
pass
def S3BucketEntity():
'''public S3BucketEntity(@JsonProperty("name") final String name, @JsonProperty("ownerIdentity") final UserIdentityEntity ownerIdentity, @JsonProperty("arn") final String arn)
'''
pass
def getName():
'''public String getName()
'''
pass
def getOwnerIdentity():
'''public UserIdentityEntity getOwnerIdentity()
'''
pass
def getArn():
'''public String getArn()
'''
pass
def S3ObjectEntity():
'''public S3ObjectEntity(final String key, final Integer size, final String eTag, final String versionId)
public S3ObjectEntity(@JsonProperty("key") final String key, @JsonProperty("size") final Long size, @JsonProperty("eTag") final String eTag, @JsonProperty("versionId") final String versionId)
'''
pass
def getKey():
'''public String getKey()
'''
pass
def getSize():
'''public Integer getSize()
'''
pass
def getSizeAsLong():
'''public Long getSizeAsLong()
'''
pass
def geteTag():
'''public String geteTag()
'''
pass
def getVersionId():
'''public String getVersionId()
'''
pass
def S3Entity():
'''public S3Entity(@JsonProperty("configurationId") final String configurationId, @JsonProperty("bucket") final S3BucketEntity bucket, @JsonProperty("object") final S3ObjectEntity object, @JsonProperty("s3SchemaVersion") final String s3SchemaVersion)
'''
pass
def getConfigurationId():
'''public String getConfigurationId()
'''
pass
def getBucket():
'''public S3BucketEntity getBucket()
'''
pass
def getObject():
'''public S3ObjectEntity getObject()
'''
pass
def getS3SchemaVersion():
'''public String getS3SchemaVersion()
'''
pass
def RequestParametersEntity():
'''public RequestParametersEntity(@JsonProperty("sourceIPAddress") final String sourceIPAddress)
'''
pass
def getSourceIPAddress():
'''public String getSourceIPAddress()
'''
pass
def ResponseElementsEntity():
'''public ResponseElementsEntity(@JsonProperty("x-amz-id-2") final String xAmzId2, @JsonProperty("x-amz-request-id") final String xAmzRequestId)
'''
pass
def getxAmzId2():
'''public String getxAmzId2()
'''
pass
def getxAmzRequestId():
'''public String getxAmzRequestId()
'''
pass
def S3EventNotificationRecord():
'''public S3EventNotificationRecord(@JsonProperty("awsRegion") final String awsRegion, @JsonProperty("eventName") final String eventName, @JsonProperty("eventSource") final String eventSource, @JsonProperty("eventTime") final String eventTime, @JsonProperty("eventVersion") final String eventVersion, @JsonProperty("requestParameters") final RequestParametersEntity requestParameters, @JsonProperty("responseElements") final ResponseElementsEntity responseElements, @JsonProperty("s3") final S3Entity s3, @JsonProperty("userIdentity") final UserIdentityEntity userIdentity)
'''
pass
def getAwsRegion():
'''public String getAwsRegion()
'''
pass
def getEventName():
'''public String getEventName()
'''
pass
def getEventSource():
'''public String getEventSource()
'''
pass
def getEventTime():
'''public DateTime getEventTime()
'''
pass
def getEventVersion():
'''public String getEventVersion()
'''
pass
def getRequestParameters():
'''public RequestParametersEntity getRequestParameters()
'''
pass
def getResponseElements():
'''public ResponseElementsEntity getResponseElements()
'''
pass
def getS3():
'''public S3Entity getS3()
'''
pass
def getUserIdentity():
'''public UserIdentityEntity getUserIdentity()
'''
pass
