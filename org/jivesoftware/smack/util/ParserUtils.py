JID = "String  \"jid\""
def assertAtStartTag():
    '''public static void assertAtStartTag(final XmlPullParser parser)
    public static void assertAtStartTag(final XmlPullParser parser, final String name)
    '''
def assertAtEndTag():
    '''public static void assertAtEndTag(final XmlPullParser parser)
    '''
def forwardToEndTagOfDepth():
    '''public static void forwardToEndTagOfDepth(final XmlPullParser parser, final int depth)
    '''
def getJidAttribute():
    '''public static Jid getJidAttribute(final XmlPullParser parser)
    public static Jid getJidAttribute(final XmlPullParser parser, final String name)
    '''
def getBareJidAttribute():
    '''public static EntityBareJid getBareJidAttribute(final XmlPullParser parser)
    public static EntityBareJid getBareJidAttribute(final XmlPullParser parser, final String name)
    '''
def getFullJidAttribute():
    '''public static EntityFullJid getFullJidAttribute(final XmlPullParser parser)
    public static EntityFullJid getFullJidAttribute(final XmlPullParser parser, final String name)
    '''
def getEntityJidAttribute():
    '''public static EntityJid getEntityJidAttribute(final XmlPullParser parser, final String name)
    '''
def getResourcepartAttribute():
    '''public static Resourcepart getResourcepartAttribute(final XmlPullParser parser, final String name)
    '''
def parseXmlBoolean():
    '''public static boolean parseXmlBoolean(final String booleanString)
    '''
def getBooleanAttribute():
    '''public static Boolean getBooleanAttribute(final XmlPullParser parser, final String name)
    public static boolean getBooleanAttribute(final XmlPullParser parser, final String name, final boolean defaultValue)
    '''
def getIntegerAttributeOrThrow():
    '''public static int getIntegerAttributeOrThrow(final XmlPullParser parser, final String name, final String throwMessage)
    '''
def getIntegerAttribute():
    '''public static Integer getIntegerAttribute(final XmlPullParser parser, final String name)
    public static int getIntegerAttribute(final XmlPullParser parser, final String name, final int defaultValue)
    '''
def getIntegerFromNextText():
    '''public static int getIntegerFromNextText(final XmlPullParser parser)
    '''
def getLongAttribute():
    '''public static Long getLongAttribute(final XmlPullParser parser, final String name)
    public static long getLongAttribute(final XmlPullParser parser, final String name, final long defaultValue)
    '''
def getDoubleFromNextText():
    '''public static double getDoubleFromNextText(final XmlPullParser parser)
    '''
def getDoubleAttribute():
    '''public static Double getDoubleAttribute(final XmlPullParser parser, final String name)
    public static double getDoubleAttribute(final XmlPullParser parser, final String name, final long defaultValue)
    '''
def getDateFromNextText():
    '''public static Date getDateFromNextText(final XmlPullParser parser)
    '''
def getUriFromNextText():
    '''public static URI getUriFromNextText(final XmlPullParser parser)
    '''
def getRequiredAttribute():
    '''public static String getRequiredAttribute(final XmlPullParser parser, final String name)
    '''
def getRequiredNextText():
    '''public static String getRequiredNextText(final XmlPullParser parser)
    '''
def getXmlLang():
    '''public static String getXmlLang(final XmlPullParser parser)
    '''
def getQName():
    '''public static QName getQName(final XmlPullParser parser)
    '''
