productName = "String  \"Tivoli's process automation engine\""
majorVersion = "String  \"7\""
minorVersion = "String  \"5\""
modLevel = "String  \"0\""
patch = "String  \"0\""
DBBuild = "String  \"V7500-243\""
build = "String  \"20100513-0804\""
hotfix = "String  \"0\""
hfDBBuild = "String  \"0\""
def getString():
    '''public static String getString()
    '''
def getConnection():
    '''public static Connection getConnection()
    '''
def getXMLInputStream():
    '''public HashMap<String, InputStream> getXMLInputStream()
    '''
def getStreamFromBundle():
    '''public HashMap<String, InputStream> getStreamFromBundle(final String productDir)
    '''
def getStreamFromJar():
    '''public HashMap<String, InputStream> getStreamFromJar(final String productDir)
    '''
def getStreamfromDirectory():
    '''public HashMap<String, InputStream> getStreamfromDirectory(final String productDir)
    '''
def main():
    '''public static void main(final String[] argv)
    '''
def getProductInfoFromXMLStream():
    '''public static Map<String, String> getProductInfoFromXMLStream(final HashMap<String, InputStream> xmlMap, final Connection con)
    '''
def checkAndSetMaxVarInDB():
    '''public static boolean checkAndSetMaxVarInDB(final String dbmaxvarname, final String dbBuild, final Connection con)
    '''
def getBaseProductName():
    '''public static String getBaseProductName()
    '''
def getRelDBBuildStrings():
    '''public static String[] getRelDBBuildStrings(final String previousDBBuilds)
    '''
