def arrayEquals():
    '''    public static final boolean arrayEquals(final Object[] source, final Object target)
    public static final boolean arrayEquals(final int[] source, final Object target)
    public static final boolean arrayEquals(final double[] source, final Object target)
    public static final boolean arrayEquals(final byte[] source, final Object target)
    public static final boolean arrayEquals(final Object source, final Object target)
    '''
def arrayRegionMatches():
    '''    public static final boolean arrayRegionMatches(final Object[] source, final int sourceStart, final Object[] target, final int targetStart, final int len)
    public static final boolean arrayRegionMatches(final char[] source, final int sourceStart, final char[] target, final int targetStart, final int len)
    public static final boolean arrayRegionMatches(final int[] source, final int sourceStart, final int[] target, final int targetStart, final int len)
    public static final boolean arrayRegionMatches(final double[] source, final int sourceStart, final double[] target, final int targetStart, final int len)
    public static final boolean arrayRegionMatches(final byte[] source, final int sourceStart, final byte[] target, final int targetStart, final int len)
    '''
def objectEquals():
    '''    public static final boolean objectEquals(final Object a, final Object b)
    '''
def checkCompare():
    '''    public static <T extends Comparable<T>> int checkCompare(final T a, final T b)
    '''
def checkHash():
    '''    public static int checkHash(final Object a)
    '''
def arrayToRLEString():
    '''    public static final String arrayToRLEString(final int[] a)
    public static final String arrayToRLEString(final short[] a)
    public static final String arrayToRLEString(final char[] a)
    public static final String arrayToRLEString(final byte[] a)
    '''
def RLEStringToIntArray():
    '''    public static final int[] RLEStringToIntArray(final String s)
    '''
def RLEStringToShortArray():
    '''    public static final short[] RLEStringToShortArray(final String s)
    '''
def RLEStringToCharArray():
    '''    public static final char[] RLEStringToCharArray(final String s)
    '''
def RLEStringToByteArray():
    '''    public static final byte[] RLEStringToByteArray(final String s)
    '''
def formatForSource():
    '''    public static final String formatForSource(final String s)
    '''
def format1ForSource():
    '''    public static final String format1ForSource(final String s)
    '''
def escape():
    '''    public static final String escape(final String s)
    '''
def unescapeAt():
    '''    public static int unescapeAt(final String s, final int[] offset16)
    '''
def unescape():
    '''    public static String unescape(final String s)
    '''
def unescapeLeniently():
    '''    public static String unescapeLeniently(final String s)
    '''
def hex():
    '''    public static String hex(final long ch)
    public static String hex(long i, final int places)
    public static String hex(final CharSequence s)
    public static <S extends CharSequence, U extends CharSequence, T extends Appendable> T hex(final S s, final int width, final U separator, final boolean useCodePoints, final T result)
    public static <S extends CharSequence> String hex(final S s, final int width, final S separator)
    '''
def split():
    '''    public static void split(final String s, final char divider, final String[] output)
    public static String[] split(final String s, final char divider)
    '''
def lookup():
    '''    public static int lookup(final String source, final String[] target)
    '''
def skipWhitespace():
    '''    public static int skipWhitespace(final String str, int pos)
    public static void skipWhitespace(final String str, final int[] pos)
    '''
def deleteRuleWhiteSpace():
    '''    public static String deleteRuleWhiteSpace(final String str)
    '''
def parseChar():
    '''    public static boolean parseChar(final String id, final int[] pos, final char ch)
    '''
def parsePattern():
    '''    public static int parsePattern(final String rule, int pos, final int limit, final String pattern, final int[] parsedInts)
    public static int parsePattern(final String pat, final Replaceable text, int index, final int limit)
    '''
def parseInteger():
    '''    public static int parseInteger(final String rule, final int[] pos, final int limit)
    '''
def parseUnicodeIdentifier():
    '''    public static String parseUnicodeIdentifier(final String str, final int[] pos)
    '''
def appendNumber():
    '''    public static <T extends Appendable> T appendNumber(final T result, final int n, final int radix, final int minDigits)
    '''
def parseNumber():
    '''    public static int parseNumber(final String text, final int[] pos, final int radix)
    '''
def isUnprintable():
    '''    public static boolean isUnprintable(final int c)
    '''
def escapeUnprintable():
    '''    public static <T extends Appendable> boolean escapeUnprintable(final T result, final int c)
    '''
def quotedIndexOf():
    '''    public static int quotedIndexOf(final String text, final int start, final int limit, final String setOfChars)
    '''
def appendToRule():
    '''    public static void appendToRule(final StringBuffer rule, final int c, final boolean isLiteral, final boolean escapeUnprintable, final StringBuffer quoteBuf)
    public static void appendToRule(final StringBuffer rule, final String text, final boolean isLiteral, final boolean escapeUnprintable, final StringBuffer quoteBuf)
    public static void appendToRule(final StringBuffer rule, final UnicodeMatcher matcher, final boolean escapeUnprintable, final StringBuffer quoteBuf)
    '''
def compareUnsigned():
    '''    public static final int compareUnsigned(int source, int target)
    '''
def highBit():
    '''    public static final byte highBit(int n)
    '''
def valueOf():
    '''    public static String valueOf(final int[] source)
    '''
def repeat():
    '''    public static String repeat(final String s, final int count)
    '''
def splitString():
    '''    public static String[] splitString(final String src, final String target)
    '''
def splitWhitespace():
    '''    public static String[] splitWhitespace(final String src)
    '''
def fromHex():
    '''    public static String fromHex(final String string, final int minLength, final String separator)
    public static String fromHex(final String string, final int minLength, final Pattern separator)
    '''
def getFallbackClassLoader():
    '''    public static ClassLoader getFallbackClassLoader()
    '''
