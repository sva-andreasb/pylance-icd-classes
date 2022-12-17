def process():
    '''returns None\n\n
    process(final boolean useCOS, final String tenantCode, String adminUser, final UserInfo userInfo)\n
    '''
def loadData():
    '''returns None\n\n
    loadData(final int tenantID, final String userId, final UserInfo userInfo)\n
    loadData(final int tenantId, final String userId, final UserInfo userInfo, final boolean toCOS, final boolean loadDemoData)\n
    '''
def processDemoData():
    '''returns None\n\n
    processDemoData(final String userId, final UserInfo userInfo, final int tenantID, final COSApi cosAPI, final String bucketName, final boolean toCOS)\n
    '''
def processImages():
    '''returns None\n\n
    processImages(final String userId, final UserInfo userInfo, final int tenantID, final COSApi cosAPI, final String bucketName, final boolean toCOS)\n
    '''
def loadTestData():
    '''returns None\n\n
    loadTestData(final Map<Integer, JSONObject> dataMap, final Map<Integer, byte[]> imageMap, final String adminUser, final UserInfo userInfo, final int tenantID, final COSApi cosAPI, final String bucketName, final boolean toCOS)\n
    '''
def loadImagesForSeedData():
    '''returns None\n\n
    loadImagesForSeedData(final Map<String, byte[]> imageMap, final UserInfo userInfo, final int tenantID, final COSApi cosAPI, final String bucketName, final boolean toCOS)\n
    '''
def loadImages():
    '''returns None\n\n
    loadImages(final MboRemote mbo, final byte[] imageData, final COSApi cosAPI, final String bucketName, final boolean toCOS)\n
    '''
