def extractData():
    '''public static String extractData(final String extractFileID, final String extSysName, final String esName, final String fileFormat, final String sourceFile, final String delimiter, final String textQualifier, final String fileAttributes, final Date importDate)
    '''
def writeExtractData():
    '''public static String writeExtractData(final Document doc, final String extSysName, final String esName, final String fileFormat, final String sourceFile, final String delimiter, final String textQualifier, final String fileAttributes, final Date importDate)
    public static String writeExtractData(final Document doc, final String extSysName, final String esName, final String fileFormat, final String sourceFile, final String delimiter, final String textQualifier, final String fileAttributes, final Date importDate, final boolean tempFile)
    '''
def deleteErrorFiles():
    '''public static void deleteErrorFiles(final String extractFileID, final String extSysName, final String esName, final Connection connection)
    '''
def addToMasterDoc():
    '''public static void addToMasterDoc(final Document masterDoc, final Element element, final String mosName, final String operation)
    '''
def mergeFiles():
    '''public static String mergeFiles(final List<String> tempFiles, final String extSysName, final String fileFormat, final String sourceFile, final Date importDate, final String mosName, final String operation)
    '''
