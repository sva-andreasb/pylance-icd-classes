HYPHEN = "char  '-'"
PERIOD = "char  '.'"
COLON = "char  ':'"
USCORE = "char  '_'"
DOT = "char  '·'"
TELEIA = "char  '\u0387'"
AYAH = "char  '\u06dd'"
ELHIZB = "char  '\u06de'"
def isValidJavaIdentifier():
    '''public static boolean isValidJavaIdentifier(final String id)
    '''
def getClassNameFromQName():
    '''public static String getClassNameFromQName(final QName qname)
    public static String getClassNameFromQName(final QName qname, final boolean useJaxRpcRules)
    '''
def getNamespaceFromPackage():
    '''public static String getNamespaceFromPackage(final Class clazz)
    '''
def getPackageFromNamespace():
    '''public static String getPackageFromNamespace(final String uri)
    public static String getPackageFromNamespace(final String uri, final boolean useJaxRpcRules)
    '''
def main():
    '''public static void main(final String[] args)
    '''
def upperCaseUnderbar():
    '''public static String upperCaseUnderbar(final String xml_name)
    '''
def upperCamelCase():
    '''public static String upperCamelCase(final String xml_name)
    public static String upperCamelCase(final String xml_name, final boolean useJaxRpcRules)
    '''
def lowerCamelCase():
    '''public static String lowerCamelCase(final String xml_name)
    public static String lowerCamelCase(final String xml_name, final boolean useJaxRpcRules, final boolean fixGeneratedName)
    '''
def upperCaseFirstLetter():
    '''public static String upperCaseFirstLetter(final String s)
    '''
def splitWords():
    '''public static List splitWords(final String name, final boolean useJaxRpcRules)
    '''
def getCharClass():
    '''public static int getCharClass(final char c, final boolean useJaxRpcRules)
    '''
def isPunctuation():
    '''public static boolean isPunctuation(final char c, final boolean useJaxRpcRules)
    '''
def nonJavaKeyword():
    '''public static String nonJavaKeyword(final String word)
    '''
def nonExtraKeyword():
    '''public static String nonExtraKeyword(final String word)
    '''
def nonJavaCommonClassName():
    '''public static String nonJavaCommonClassName(final String name)
    '''
def isJavaCommonClassName():
    '''public static boolean isJavaCommonClassName(final String word)
    '''
