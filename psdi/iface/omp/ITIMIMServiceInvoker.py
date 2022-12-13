COPYRIGHT = "String  \"IBM Confidential OCO Source Material\n5725-E24 (C) COPYRIGHT International Business Machines Corp. 2007, 2017\nThe source code for this program is not published or otherwise divested\nof its trade secrets, irrespective of what has been deposited with the\nU.S. Copyright Office.\""
def ITIMIMServiceInvoker():
    '''    public ITIMIMServiceInvoker()
    '''
def printMetaData():
    '''    public void printMetaData(final Map<String, Object> metaData)
    '''
def writeToXMLFile():
    '''    public byte[] writeToXMLFile(final Map<String, Object> metaData, final XMLFileHandler handler)
    '''
def writeToWebService():
    '''    public byte[] writeToWebService(final Map<String, Object> metaData, final WebServiceHandler handler)
    '''
def writeToFlatFile():
    '''    public byte[] writeToFlatFile(final Map<String, Object> metaData, final FlatFileHandler handler)
    '''
def invoke():
    '''    public byte[] invoke(final Map<String, Object> metaData, final MboRemote sourceMbo, final MboRemote targetMbo, final String endPointName)
    public byte[] invoke(final Map<String, Object> metaData, final MboRemote sourceMbo, final MboSetRemote targetMboSet, final int action, final String endPointName)
    public byte[] invoke(final Map<String, Object> metaData, final MboSetRemote sourceMboSet, final MboRemote targetMbo, final String endPointName)
    public byte[] invoke(final Map<String, Object> metaData, final MboSetRemote sourceMboSet, final MboSetRemote targetMboSet, final int action, final String endPointName)
    '''
def invokeWrapper():
    '''    public void invokeWrapper(final Map<String, Object> metaData, final MboRemote sourceMbo, final MboRemote targetMbo, final String endPointName, final Hashtable tb)
    '''
