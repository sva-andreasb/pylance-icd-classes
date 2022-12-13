XML_VERSION_TAG = "String  \"<?xml version=\\"1.0\\" encoding=\\"UTF-8\\"?>\""
XML_VERSION_TAG_REGEX = "String  \"<\\?\\s*xml[^>]*>\\s*\""
def PresentationLoader():
    '''    public PresentationLoader()
    '''
def importPresentationSet():
    '''    public void importPresentationSet(final WebClientSession wcs, final String xml)
    '''
def importApp():
    '''    public void importApp(final WebClientSession wcs, final String xml)
    public void importApp(final WebClientSession wcs, final String xml, final boolean saveLabels)
    '''
def importAdhocReportDialog():
    '''    public void importAdhocReportDialog(final WebClientSession wcs, final String completeXml, final String dialogXml)
    '''
def getAppID():
    '''    public String getAppID()
    '''
def isMaxLabelProperty():
    '''    public static boolean isMaxLabelProperty(final String property)
    '''
def exportSQL():
    '''    public void exportSQL(final WebClientSession wcs)
    public void exportSQL(final WebClientSession wcs, String appID, final PrintWriter out)
    '''
def exportXML():
    '''    public String exportXML(final WebClientSession wcs, String appID)
    '''
def getXMLString():
    '''    public String getXMLString(final WebClientSession wcs, final ControlInstance control)
    '''
def getXMLSafePropertyString():
    '''    public String getXMLSafePropertyString(final ControlInstance control, final HashMap<String, String> cachedLabels)
    '''
def makesafevalue():
    '''    public static String makesafevalue(String value)
    '''
def writeFormattedXML():
    '''    public void writeFormattedXML(final PrintWriter out, final String xml, final LabelCache appLabelCache)
    '''
