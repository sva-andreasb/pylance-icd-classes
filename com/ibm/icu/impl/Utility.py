def arrayEquals():
'''public static final boolean arrayEquals(final Object[] source, final Object target)
public static final boolean arrayEquals(final int[] source, final Object target)
public static final boolean arrayEquals(final double[] source, final Object target)
public static final boolean arrayEquals(final byte[] source, final Object target)
public static final boolean arrayEquals(final Object source, final Object target)
'''
pass
def arrayRegionMatches():
'''public static final boolean arrayRegionMatches(final Object[] source, final int sourceStart, final Object[] target, final int targetStart, final int len)
public static final boolean arrayRegionMatches(final char[] source, final int sourceStart, final char[] target, final int targetStart, final int len)
public static final boolean arrayRegionMatches(final int[] source, final int sourceStart, final int[] target, final int targetStart, final int len)
public static final boolean arrayRegionMatches(final double[] source, final int sourceStart, final double[] target, final int targetStart, final int len)
public static final boolean arrayRegionMatches(final byte[] source, final int sourceStart, final byte[] target, final int targetStart, final int len)
'''
pass
def objectEquals():
'''public static final boolean objectEquals(final Object a, final Object b)
'''
pass
def checkCompare():
'''public static <T extends Comparable<T>> int checkCompare(final T a, final T b)
'''
pass
def checkHash():
'''public static int checkHash(final Object a)
'''
pass
def arrayToRLEString():
'''public static final String arrayToRLEString(final int[] a)
public static final String arrayToRLEString(final short[] a)
public static final String arrayToRLEString(final char[] a)
public static final String arrayToRLEString(final byte[] a)
'''
pass
def RLEStringToIntArray():
'''public static final int[] RLEStringToIntArray(final String s)
'''
pass
def RLEStringToShortArray():
'''public static final short[] RLEStringToShortArray(final String s)
'''
pass
def RLEStringToCharArray():
'''public static final char[] RLEStringToCharArray(final String s)
'''
pass
def RLEStringToByteArray():
'''public static final byte[] RLEStringToByteArray(final String s)
'''
pass
def formatForSource():
'''public static final String formatForSource(final String s)
'''
pass
def format1ForSource():
'''public static final String format1ForSource(final String s)
'''
pass
def escape():
'''public static final String escape(final String s)
'''
pass
def unescapeAt():
'''public static int unescapeAt(final String s, final int[] offset16)
'''
pass
def unescape():
'''public static String unescape(final String s)
'''
pass
def unescapeLeniently():
'''public static String unescapeLeniently(final String s)
'''
pass
def hex():
'''public static String hex(final long ch)
public static String hex(long i, final int places)
public static String hex(final CharSequence s)
public static <S extends CharSequence, U extends CharSequence, T extends Appendable> T hex(final S s, final int width, final U separator, final boolean useCodePoints, final T result)
public static <S extends CharSequence> String hex(final S s, final int width, final S separator)
'''
pass
def split():
'''public static void split(final String s, final char divider, final String[] output)
public static String[] split(final String s, final char divider)
'''
pass
def lookup():
'''public static int lookup(final String source, final String[] target)
'''
pass
def skipWhitespace():
'''public static int skipWhitespace(final String str, int pos)
public static void skipWhitespace(final String str, final int[] pos)
'''
pass
def deleteRuleWhiteSpace():
'''public static String deleteRuleWhiteSpace(final String str)
'''
pass
def parseChar():
'''public static boolean parseChar(final String id, final int[] pos, final char ch)
'''
pass
def parsePattern():
'''public static int parsePattern(final String rule, int pos, final int limit, final String pattern, final int[] parsedInts)
public static int parsePattern(final String pat, final Replaceable text, int index, final int limit)
'''
pass
def parseInteger():
'''public static int parseInteger(final String rule, final int[] pos, final int limit)
'''
pass
def parseUnicodeIdentifier():
'''public static String parseUnicodeIdentifier(final String str, final int[] pos)
'''
pass
def appendNumber():
'''public static <T extends Appendable> T appendNumber(final T result, final int n, final int radix, final int minDigits)
'''
pass
def parseNumber():
'''public static int parseNumber(final String text, final int[] pos, final int radix)
'''
pass
def isUnprintable():
'''public static boolean isUnprintable(final int c)
'''
pass
def escapeUnprintable():
'''public static <T extends Appendable> boolean escapeUnprintable(final T result, final int c)
'''
pass
def quotedIndexOf():
'''public static int quotedIndexOf(final String text, final int start, final int limit, final String setOfChars)
'''
pass
def appendToRule():
'''public static void appendToRule(final StringBuffer rule, final int c, final boolean isLiteral, final boolean escapeUnprintable, final StringBuffer quoteBuf)
public static void appendToRule(final StringBuffer rule, final String text, final boolean isLiteral, final boolean escapeUnprintable, final StringBuffer quoteBuf)
public static void appendToRule(final StringBuffer rule, final UnicodeMatcher matcher, final boolean escapeUnprintable, final StringBuffer quoteBuf)
'''
pass
def compareUnsigned():
'''public static final int compareUnsigned(int source, int target)
'''
pass
def highBit():
'''public static final byte highBit(int n)
'''
pass
def valueOf():
'''public static String valueOf(final int[] source)
'''
pass
def repeat():
'''public static String repeat(final String s, final int count)
'''
pass
def splitString():
'''public static String[] splitString(final String src, final String target)
'''
pass
def splitWhitespace():
'''public static String[] splitWhitespace(final String src)
'''
pass
def fromHex():
'''public static String fromHex(final String string, final int minLength, final String separator)
public static String fromHex(final String string, final int minLength, final Pattern separator)
'''
pass
def getFallbackClassLoader():
'''public static ClassLoader getFallbackClassLoader()
'''
pass
