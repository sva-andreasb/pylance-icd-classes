def getAmiId():
    '''public static String getAmiId()
    '''
def getAmiLaunchIndex():
    '''public static String getAmiLaunchIndex()
    '''
def getAmiManifestPath():
    '''public static String getAmiManifestPath()
    '''
def getAncestorAmiIds():
    '''public static List<String> getAncestorAmiIds()
    '''
def getInstanceAction():
    '''public static String getInstanceAction()
    '''
def getInstanceId():
    '''public static String getInstanceId()
    public String getInstanceId()
    '''
def getInstanceType():
    '''public static String getInstanceType()
    public String getInstanceType()
    '''
def getLocalHostName():
    '''public static String getLocalHostName()
    '''
def getMacAddress():
    '''public static String getMacAddress()
    public String getMacAddress()
    '''
def getPrivateIpAddress():
    '''public static String getPrivateIpAddress()
    '''
def getAvailabilityZone():
    '''public static String getAvailabilityZone()
    public String getAvailabilityZone()
    '''
def getProductCodes():
    '''public static List<String> getProductCodes()
    '''
def getPublicKey():
    '''public static String getPublicKey()
    '''
def getRamdiskId():
    '''public static String getRamdiskId()
    public String getRamdiskId()
    '''
def getReservationId():
    '''public static String getReservationId()
    '''
def getSecurityGroups():
    '''public static List<String> getSecurityGroups()
    public List<String> getSecurityGroups()
    '''
def getIAMInstanceProfileInfo():
    '''public static IAMInfo getIAMInstanceProfileInfo()
    '''
def getInstanceInfo():
    '''public static InstanceInfo getInstanceInfo()
    '''
def getEC2InstanceRegion():
    '''public static String getEC2InstanceRegion()
    '''
def getIAMSecurityCredentials():
    '''public static Map<String, IAMSecurityCredential> getIAMSecurityCredentials()
    '''
def getBlockDeviceMapping():
    '''public static Map<String, String> getBlockDeviceMapping()
    '''
def getNetworkInterfaces():
    '''public static List<NetworkInterface> getNetworkInterfaces()
    '''
def getUserData():
    '''public static String getUserData()
    '''
def getData():
    '''public static String getData(final String path)
    public static String getData(final String path, final int tries)
    '''
def getItems():
    '''public static List<String> getItems(final String path)
    public static List<String> getItems(final String path, final int tries)
    '''
def InstanceInfo():
    '''public InstanceInfo(@JsonProperty(value = "pendingTime", required = true) final String pendingTime, @JsonProperty(value = "instanceType", required = true) final String instanceType, @JsonProperty(value = "imageId", required = true) final String imageId, @JsonProperty(value = "instanceId", required = true) final String instanceId, @JsonProperty(value = "billingProducts", required = false) final String[] billingProducts, @JsonProperty(value = "architecture", required = true) final String architecture, @JsonProperty(value = "accountId", required = true) final String accountId, @JsonProperty(value = "kernelId", required = true) final String kernelId, @JsonProperty(value = "ramdiskId", required = false) final String ramdiskId, @JsonProperty(value = "region", required = true) final String region, @JsonProperty(value = "version", required = true) final String version, @JsonProperty(value = "availabilityZone", required = true) final String availabilityZone, @JsonProperty(value = "privateIp", required = true) final String privateIp, @JsonProperty(value = "devpayProductCodes", required = false) final String[] devpayProductCodes)
    '''
def getPendingTime():
    '''public String getPendingTime()
    '''
def getImageId():
    '''public String getImageId()
    '''
def getBillingProducts():
    '''public String[] getBillingProducts()
    '''
def getArchitecture():
    '''public String getArchitecture()
    '''
def getAccountId():
    '''public String getAccountId()
    '''
def getKernelId():
    '''public String getKernelId()
    '''
def getRegion():
    '''public String getRegion()
    '''
def getVersion():
    '''public String getVersion()
    '''
def getPrivateIp():
    '''public String getPrivateIp()
    '''
def getDevpayProductCodes():
    '''public String[] getDevpayProductCodes()
    '''
def NetworkInterface():
    '''public NetworkInterface(final String macAddress)
    '''
def getOwnerId():
    '''public String getOwnerId()
    '''
def getProfile():
    '''public String getProfile()
    '''
def getHostname():
    '''public String getHostname()
    '''
def getLocalIPv4s():
    '''public List<String> getLocalIPv4s()
    '''
def getPublicHostname():
    '''public String getPublicHostname()
    '''
def getPublicIPv4s():
    '''public List<String> getPublicIPv4s()
    '''
def getSecurityGroupIds():
    '''public List<String> getSecurityGroupIds()
    '''
def getSubnetIPv4CidrBlock():
    '''public String getSubnetIPv4CidrBlock()
    '''
def getSubnetId():
    '''public String getSubnetId()
    '''
def getVpcIPv4CidrBlock():
    '''public String getVpcIPv4CidrBlock()
    '''
def getVpcId():
    '''public String getVpcId()
    '''
def getIPv4Association():
    '''public List<String> getIPv4Association(final String publicIp)
    '''
