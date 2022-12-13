def makeKey():
    '''public static String makeKey(final String locale, final String app, final String type)
    '''
def getAppLabelCache():
    '''public static synchronized LabelCache getAppLabelCache(final String app, final WebClientSession wcs)
    '''
def getSystemLabelCache():
    '''public static synchronized LabelCache getSystemLabelCache(final WebClientSession wcs)
    '''
def getRepLibraryLabelCache():
    '''public static synchronized LabelCache getRepLibraryLabelCache(final WebClientSession wcs)
    '''
def setLabelCache():
    '''public static synchronized void setLabelCache(final String cacheId, final WebClientSession wcs, final LabelCache cache)
    '''
def clearCache():
    '''public static LabelCache clearCache(final String app, final WebClientSession wcs)
    '''
def clearSystemCache():
    '''public static LabelCache clearSystemCache(final WebClientSession sc)
    '''
def clearAll():
    '''public static void clearAll()
    '''
def removeRepLibraryLabels():
    '''public static void removeRepLibraryLabels()
    '''
def loadRepLibraryLabels():
    '''public static LabelCache loadRepLibraryLabels(final WebClientSession wcs)
    '''
def loadRepLibraryLabelsInbBatch():
    '''public static LabelCache loadRepLibraryLabelsInbBatch(final WebClientSession wcs, final int batchSize)
    '''
