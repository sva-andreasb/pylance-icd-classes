def process():
'''public void process(final boolean useCOS, final String tenantCode, String adminUser, final UserInfo userInfo)
'''
pass
def loadData():
'''public void loadData(final int tenantID, final String userId, final UserInfo userInfo)
public void loadData(final int tenantId, final String userId, final UserInfo userInfo, final boolean toCOS, final boolean loadDemoData)
'''
pass
def processDemoData():
'''public void processDemoData(final String userId, final UserInfo userInfo, final int tenantID, final COSApi cosAPI, final String bucketName, final boolean toCOS)
'''
pass
def processImages():
'''public void processImages(final String userId, final UserInfo userInfo, final int tenantID, final COSApi cosAPI, final String bucketName, final boolean toCOS)
'''
pass
def loadTestData():
'''public void loadTestData(final Map<Integer, JSONObject> dataMap, final Map<Integer, byte[]> imageMap, final String adminUser, final UserInfo userInfo, final int tenantID, final COSApi cosAPI, final String bucketName, final boolean toCOS)
'''
pass
def loadImagesForSeedData():
'''public void loadImagesForSeedData(final Map<String, byte[]> imageMap, final UserInfo userInfo, final int tenantID, final COSApi cosAPI, final String bucketName, final boolean toCOS)
'''
pass
def loadImages():
'''public void loadImages(final MboRemote mbo, final byte[] imageData, final COSApi cosAPI, final String bucketName, final boolean toCOS)
'''
pass
def getDataToLoad():
'''public Map<Integer, JSONObject> getDataToLoad(final boolean useCOS)
'''
pass
def getImageDataToLoad():
'''public Map<Integer, byte[]> getImageDataToLoad(final boolean useCOS)
'''
pass
def getImageSeedDataToLoad():
'''public Map<String, byte[]> getImageSeedDataToLoad(final boolean useCOS)
'''
pass
def readBinaryData():
'''public static byte[] readBinaryData(final InputStream input)
'''
pass