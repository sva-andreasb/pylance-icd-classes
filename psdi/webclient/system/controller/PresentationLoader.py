XML_VERSION_TAG = "String  <?xml version=\"1.0\" encoding=\"UTF-8\"?>""
XML_VERSION_TAG_REGEX = "String  <\\?\\s*xml[^>]*>\\s*""
def PresentationLoader():
'''public PresentationLoader()
'''
pass
def importPresentationSet():
'''public void importPresentationSet(final WebClientSession wcs, final String xml)
'''
pass
def importApp():
'''public void importApp(final WebClientSession wcs, final String xml)
public void importApp(final WebClientSession wcs, final String xml, final boolean saveLabels)
'''
pass
def importAdhocReportDialog():
'''public void importAdhocReportDialog(final WebClientSession wcs, final String completeXml, final String dialogXml)
'''
pass
def getAppID():
'''public String getAppID()
'''
pass
def isMaxLabelProperty():
'''public static boolean isMaxLabelProperty(final String property)
'''
pass
def exportSQL():
'''public void exportSQL(final WebClientSession wcs)
public void exportSQL(final WebClientSession wcs, String appID, final PrintWriter out)
'''
pass
def exportXML():
'''public String exportXML(final WebClientSession wcs, String appID)
'''
pass
def getXMLString():
'''public String getXMLString(final WebClientSession wcs, final ControlInstance control)
'''
pass
def getXMLSafePropertyString():
'''public String getXMLSafePropertyString(final ControlInstance control, final HashMap<String, String> cachedLabels)
'''
pass
def makesafevalue():
'''public static String makesafevalue(String value)
'''
pass
def writeFormattedXML():
'''public void writeFormattedXML(final PrintWriter out, final String xml, final LabelCache appLabelCache)
'''
pass
