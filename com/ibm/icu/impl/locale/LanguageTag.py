SEP = "String  \"-\""
PRIVATEUSE = "String  \"x\""
def getLanguage():
    '''public String getLanguage()
    '''
def getExtlangs():
    '''public List<String> getExtlangs()
    '''
def getScript():
    '''public String getScript()
    '''
def getRegion():
    '''public String getRegion()
    '''
def getVariants():
    '''public List<String> getVariants()
    '''
def getExtensions():
    '''public SortedMap<Character, Extension> getExtensions()
    '''
def getPrivateuse():
    '''public String getPrivateuse()
    '''
def getGrandfathered():
    '''public String getGrandfathered()
    '''
def getBaseLocale():
    '''public BaseLocale getBaseLocale()
    '''
def getLocaleExtensions():
    '''public LocaleExtensions getLocaleExtensions()
    '''
def getID():
    '''public String getID()
    '''
def toString():
    '''public String toString()
    '''
def isLanguage():
    '''public static boolean isLanguage(final String s)
    '''
def isExtlang():
    '''public static boolean isExtlang(final String s)
    '''
def isScript():
    '''public static boolean isScript(final String s)
    '''
def isRegion():
    '''public static boolean isRegion(final String s)
    '''
def isVariant():
    '''public static boolean isVariant(final String s)
    '''
def isExtensionSingleton():
    '''public static boolean isExtensionSingleton(final String s)
    '''
def isExtensionSubtag():
    '''public static boolean isExtensionSubtag(final String s)
    '''
def isPrivateuseSingleton():
    '''public static boolean isPrivateuseSingleton(final String s)
    '''
def isPrivateuseSubtag():
    '''public static boolean isPrivateuseSubtag(final String s)
    '''
def canonicalizeLanguage():
    '''public static String canonicalizeLanguage(final String s)
    '''
def canonicalizeExtlang():
    '''public static String canonicalizeExtlang(final String s)
    '''
def canonicalizeScript():
    '''public static String canonicalizeScript(final String s)
    '''
def canonicalizeRegion():
    '''public static String canonicalizeRegion(final String s)
    '''
def canonicalizeVariant():
    '''public static String canonicalizeVariant(final String s)
    '''
def canonicalizeExtensionSingleton():
    '''public static String canonicalizeExtensionSingleton(final String s)
    '''
def canonicalizeExtensionSubtag():
    '''public static String canonicalizeExtensionSubtag(final String s)
    '''
def canonicalizePrivateuseSubtag():
    '''public static String canonicalizePrivateuseSubtag(final String s)
    '''
def parse():
    '''public static LanguageTag parse(final String str, final boolean javaCompatVar)
    '''
def parseStrict():
    '''public static LanguageTag parseStrict(final String str, final boolean javaCompatVar)
    '''
def parseLocale():
    '''public static LanguageTag parseLocale(final BaseLocale base, final LocaleExtensions locExts)
    '''
def ParseStatus():
    '''public ParseStatus()
    '''
def reset():
    '''public void reset()
    '''
def parseLanguage():
    '''public String parseLanguage(final StringTokenIterator itr, final ParseStatus sts)
    '''
def parseExtlangs():
    '''public List<String> parseExtlangs(final StringTokenIterator itr, final ParseStatus sts)
    '''
def parseScript():
    '''public String parseScript(final StringTokenIterator itr, final ParseStatus sts)
    '''
def parseRegion():
    '''public String parseRegion(final StringTokenIterator itr, final ParseStatus sts)
    '''
def parseVariants():
    '''public List<String> parseVariants(final StringTokenIterator itr, final ParseStatus sts)
    '''
def parseExtensions():
    '''public SortedMap<Character, Extension> parseExtensions(final StringTokenIterator itr, final ParseStatus sts)
    '''
def parsePrivateuse():
    '''public String parsePrivateuse(final StringTokenIterator itr, final ParseStatus sts)
    '''
