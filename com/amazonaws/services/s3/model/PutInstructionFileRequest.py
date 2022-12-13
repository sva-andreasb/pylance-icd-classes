def PutInstructionFileRequest():
    '''    public PutInstructionFileRequest(final S3ObjectId s3ObjectId, final Map<String, String> matDesc, final String suffix)
    public PutInstructionFileRequest(final S3ObjectId s3ObjectId, final EncryptionMaterials encryptionMaterials, final String suffix)
    '''
def getS3ObjectId():
    '''    public S3ObjectId getS3ObjectId()
    '''
def getMaterialsDescription():
    '''    public Map<String, String> getMaterialsDescription()
    '''
def getEncryptionMaterials():
    '''    public EncryptionMaterials getEncryptionMaterials()
    '''
def getSuffix():
    '''    public String getSuffix()
    '''
def getCannedAcl():
    '''    public CannedAccessControlList getCannedAcl()
    '''
def setCannedAcl():
    '''    public void setCannedAcl(final CannedAccessControlList cannedAcl)
    '''
def withCannedAcl():
    '''    public PutInstructionFileRequest withCannedAcl(final CannedAccessControlList cannedAcl)
    '''
def getAccessControlList():
    '''    public AccessControlList getAccessControlList()
    '''
def setAccessControlList():
    '''    public void setAccessControlList(final AccessControlList accessControlList)
    '''
def withAccessControlList():
    '''    public PutInstructionFileRequest withAccessControlList(final AccessControlList accessControlList)
    '''
def getRedirectLocation():
    '''    public String getRedirectLocation()
    '''
def setRedirectLocation():
    '''    public void setRedirectLocation(final String redirectLocation)
    '''
def withRedirectLocation():
    '''    public PutInstructionFileRequest withRedirectLocation(final String redirectLocation)
    '''
def getStorageClass():
    '''    public String getStorageClass()
    '''
def setStorageClass():
    '''    public void setStorageClass(final String storageClass)
    public void setStorageClass(final StorageClass storageClass)
    '''
def withStorageClass():
    '''    public PutInstructionFileRequest withStorageClass(final String storageClass)
    public PutInstructionFileRequest withStorageClass(final StorageClass storageClass)
    '''
def createPutObjectRequest():
    '''    public PutObjectRequest createPutObjectRequest(final S3Object s3Object)
    '''
