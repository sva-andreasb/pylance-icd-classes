DELETEONLY = "int  5"
def xmlToMboSet():
    '''public static MboSetRemote xmlToMboSet(final UserInfo info, final ObjectList data, final Map<String, String> params, final MXTransaction trans)
    public static MboSetRemote xmlToMboSet(final UserInfo info, final ObjectList data, final Map<String, String> params, final MXTransaction trans, final String appName)
    public static MboSetRemote xmlToMboSet(final MboSetRemote mboSet, final ObjectList data, final int mboAction)
    public static MboSetRemote xmlToMboSet(final MboSetRemote mboSet, final ObjectList data)
    '''
def xmlToMbo():
    '''public static void xmlToMbo(final MboRemote mbo, final StructureObject data)
    public static void xmlToMbo(final MboRemote mbo, final StructureObject strucObject, final Iterator columns, final long accessModifier)
    '''
def mosXmlToMbo():
    '''public static void mosXmlToMbo(final MboRemote mbo, final StructureObject strucObject, final Map<String, IfaceColumnInfo> data, final long accessModifier, final boolean skipKeys)
    '''
def getMosName():
    '''public static String getMosName(final Document doc)
    '''
def getKeyValues():
    '''public static String[] getKeyValues(final MboSetInfo mboSetInfo, final String[] keys, final StructureObject strucObject)
    '''
def getFullKeyValue():
    '''public static String getFullKeyValue(final MboSetInfo mboSetInfo, final String[] keys, final Object data)
    '''
def getDisplayKeyValue():
    '''public static String getDisplayKeyValue(final MboSetInfo mboSetInfo, final String[] keys, final Object data)
    '''
def checkDefaultValues():
    '''public static boolean checkDefaultValues(final MboValueInfo mvi, final String name, final StructureObject strucObject)
    '''
def convertAction():
    '''public static int convertAction(final String action)
    '''
def checkRowstamp():
    '''public static void checkRowstamp(final MboRemote mbo, final StructureObject strucObject)
    '''
