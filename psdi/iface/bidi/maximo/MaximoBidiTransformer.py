MAXIMO_INBOUND_ILYNN = "String  \"ILYNN\""
MAXIMO_OUTBOUND_ICYNN = "String  \"ICYNN\""
ERR_KEY_INVALID_ATTRIBUTES = "String  \"invalid.bidi.attributes\""
ERR_KEY_INVALID_IN_OUT_ATTRIBUTES = "String  \"invalid.bidi.attributes.pair\""
ERR_KEY_NULL_ATTRIBUTES = "String  \"null.attributes\""
ERR_KEY_NULL_XML_DOCUMENT = "String  \"null.xml\""
ERR_KEY_BAD_XML_DOCUMENT = "String  \"bad.xml\""
def transformToMaximoFormat():
    '''    public static String transformToMaximoFormat(final String text, final String inFormat)
    public static List<String> transformToMaximoFormat(final List<String> inStrs, final String inFormat)
    public static List<String> transformToMaximoFormat(final List<String> inStrs, final String inFormat, final Map<Integer, MXApplicationException> errors)
    public static Document transformToMaximoFormat(final Document inDoc, final String inFormat)
    public static Document transformToMaximoFormat(final Document inDoc, final String inFormat, final Set<String> exclusionsSet)
    public static Document transformToMaximoFormat(final Document inDoc, final String inFormat, final Set<String> exclusionsSet, final boolean transformAttributes)
    '''
def transformFromMaximoFormat():
    '''    public static String transformFromMaximoFormat(final String text, final String outFormat)
    public static List<String> transformFromMaximoFormat(final List<String> inStrs, final String outFormat)
    public static List<String> transformFromMaximoFormat(final List<String> inStrs, final String outFormat, final Map<Integer, MXApplicationException> errors)
    public static Document transformFromMaximoFormat(final Document inDoc, final String outFormat)
    public static Document transformFromMaximoFormat(final Document inDoc, final String outFormat, final Set<String> exclusionsSet)
    public static Document transformFromMaximoFormat(final Document inDoc, final String outFormat, final Set<String> exclusionsSet, final boolean transformAttributes)
    '''
