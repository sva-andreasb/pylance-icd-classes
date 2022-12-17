XML_VERSION_TAG = "String  \"<?xml version=\\"1.0\\" encoding=\\"UTF-8\\"?>\""
XML_VERSION_TAG_REGEX = "String  \"<\\?\\s*xml[^>]*>\\s*\""
def ():
    '''returns PresentationLoader\n\n
    ()\n
    '''
def importPresentationSet():
    '''returns None\n\n
    importPresentationSet(final WebClientSession wcs, final String xml)\n
    '''
def importApp():
    '''returns None\n\n
    importApp(final WebClientSession wcs, final String xml)\n
    importApp(final WebClientSession wcs, final String xml, final boolean saveLabels)\n
    '''
def importAdhocReportDialog():
    '''returns None\n\n
    importAdhocReportDialog(final WebClientSession wcs, final String completeXml, final String dialogXml)\n
    '''
def getAppID():
    '''returns String\n\n
    getAppID()\n
    '''
def exportSQL():
    '''returns None\n\n
    exportSQL(final WebClientSession wcs)\n
    exportSQL(final WebClientSession wcs, String appID, final PrintWriter out)\n
    '''
def exportXML():
    '''returns String\n\n
    exportXML(final WebClientSession wcs, String appID)\n
    '''
def getXMLString():
    '''returns String\n\n
    getXMLString(final WebClientSession wcs, final ControlInstance control)\n
    '''
def getXMLSafePropertyString():
    '''returns String\n\n
    getXMLSafePropertyString(final ControlInstance control, final HashMap<String, String> cachedLabels)\n
    '''
def writeFormattedXML():
    '''returns None\n\n
    writeFormattedXML(final PrintWriter out, final String xml, final LabelCache appLabelCache)\n
    '''
