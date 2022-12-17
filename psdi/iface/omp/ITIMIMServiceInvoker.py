COPYRIGHT = "String  \"IBM Confidential OCO Source Material\n5725-E24 (C) COPYRIGHT International Business Machines Corp. 2007, 2017\nThe source code for this program is not published or otherwise divested\nof its trade secrets, irrespective of what has been deposited with the\nU.S. Copyright Office.\""
def ():
    '''returns ITIMIMServiceInvoker\n\n
    ()\n
    '''
def printMetaData():
    '''returns None\n\n
    printMetaData(final Map<String, Object> metaData)\n
    '''
def writeToXMLFile():
    '''returns byte[]\n\n
    writeToXMLFile(final Map<String, Object> metaData, final XMLFileHandler handler)\n
    '''
def writeToWebService():
    '''returns byte[]\n\n
    writeToWebService(final Map<String, Object> metaData, final WebServiceHandler handler)\n
    '''
def writeToFlatFile():
    '''returns byte[]\n\n
    writeToFlatFile(final Map<String, Object> metaData, final FlatFileHandler handler)\n
    '''
def invoke():
    '''returns byte[]\n\n
    invoke(final Map<String, Object> metaData, final MboRemote sourceMbo, final MboRemote targetMbo, final String endPointName)\n
    invoke(final Map<String, Object> metaData, final MboRemote sourceMbo, final MboSetRemote targetMboSet, final int action, final String endPointName)\n
    invoke(final Map<String, Object> metaData, final MboSetRemote sourceMboSet, final MboRemote targetMbo, final String endPointName)\n
    invoke(final Map<String, Object> metaData, final MboSetRemote sourceMboSet, final MboSetRemote targetMboSet, final int action, final String endPointName)\n
    '''
def invokeWrapper():
    '''returns None\n\n
    invokeWrapper(final Map<String, Object> metaData, final MboRemote sourceMbo, final MboRemote targetMbo, final String endPointName, final Hashtable tb)\n
    '''
