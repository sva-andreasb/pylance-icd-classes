def S3EventNotification():
    '''public S3EventNotification(@JsonProperty("Records") final List<S3EventNotificationRecord> records)
    '''
def parseJson():
    '''public static S3EventNotification parseJson(final String json)
    '''
def getRecords():
    '''public List<S3EventNotificationRecord> getRecords()
    '''
def toJson():
    '''public String toJson()
    '''
def UserIdentityEntity():
    '''public UserIdentityEntity(@JsonProperty("principalId") final String principalId)
    '''
def getPrincipalId():
    '''public String getPrincipalId()
    '''
def S3BucketEntity():
    '''public S3BucketEntity(@JsonProperty("name") final String name, @JsonProperty("ownerIdentity") final UserIdentityEntity ownerIdentity, @JsonProperty("arn") final String arn)
    '''
def getName():
    '''public String getName()
    '''
def getOwnerIdentity():
    '''public UserIdentityEntity getOwnerIdentity()
    '''
def getArn():
    '''public String getArn()
    '''
def S3ObjectEntity():
    '''public S3ObjectEntity(final String key, final Integer size, final String eTag, final String versionId)
    public S3ObjectEntity(@JsonProperty("key") final String key, @JsonProperty("size") final Long size, @JsonProperty("eTag") final String eTag, @JsonProperty("versionId") final String versionId)
    '''
def getKey():
    '''public String getKey()
    '''
def getSize():
    '''public Integer getSize()
    '''
def getSizeAsLong():
    '''public Long getSizeAsLong()
    '''
def geteTag():
    '''public String geteTag()
    '''
def getVersionId():
    '''public String getVersionId()
    '''
def S3Entity():
    '''public S3Entity(@JsonProperty("configurationId") final String configurationId, @JsonProperty("bucket") final S3BucketEntity bucket, @JsonProperty("object") final S3ObjectEntity object, @JsonProperty("s3SchemaVersion") final String s3SchemaVersion)
    '''
def getConfigurationId():
    '''public String getConfigurationId()
    '''
def getBucket():
    '''public S3BucketEntity getBucket()
    '''
def getObject():
    '''public S3ObjectEntity getObject()
    '''
def getS3SchemaVersion():
    '''public String getS3SchemaVersion()
    '''
def RequestParametersEntity():
    '''public RequestParametersEntity(@JsonProperty("sourceIPAddress") final String sourceIPAddress)
    '''
def getSourceIPAddress():
    '''public String getSourceIPAddress()
    '''
def ResponseElementsEntity():
    '''public ResponseElementsEntity(@JsonProperty("x-amz-id-2") final String xAmzId2, @JsonProperty("x-amz-request-id") final String xAmzRequestId)
    '''
def getxAmzId2():
    '''public String getxAmzId2()
    '''
def getxAmzRequestId():
    '''public String getxAmzRequestId()
    '''
def S3EventNotificationRecord():
    '''public S3EventNotificationRecord(@JsonProperty("awsRegion") final String awsRegion, @JsonProperty("eventName") final String eventName, @JsonProperty("eventSource") final String eventSource, @JsonProperty("eventTime") final String eventTime, @JsonProperty("eventVersion") final String eventVersion, @JsonProperty("requestParameters") final RequestParametersEntity requestParameters, @JsonProperty("responseElements") final ResponseElementsEntity responseElements, @JsonProperty("s3") final S3Entity s3, @JsonProperty("userIdentity") final UserIdentityEntity userIdentity)
    '''
def getAwsRegion():
    '''public String getAwsRegion()
    '''
def getEventName():
    '''public String getEventName()
    '''
def getEventSource():
    '''public String getEventSource()
    '''
def getEventTime():
    '''public DateTime getEventTime()
    '''
def getEventVersion():
    '''public String getEventVersion()
    '''
def getRequestParameters():
    '''public RequestParametersEntity getRequestParameters()
    '''
def getResponseElements():
    '''public ResponseElementsEntity getResponseElements()
    '''
def getS3():
    '''public S3Entity getS3()
    '''
def getUserIdentity():
    '''public UserIdentityEntity getUserIdentity()
    '''
