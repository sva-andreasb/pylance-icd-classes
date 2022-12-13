SINGLE_CHAR_BOUNDARY = "int 1"
LEAD_SURROGATE_BOUNDARY = "int 2"
TRAIL_SURROGATE_BOUNDARY = "int 5"
CODEPOINT_MIN_VALUE = "int 0"
CODEPOINT_MAX_VALUE = "int 1114111"
SUPPLEMENTARY_MIN_VALUE = "int 65536"
LEAD_SURROGATE_MIN_VALUE = "int 55296"
TRAIL_SURROGATE_MIN_VALUE = "int 56320"
LEAD_SURROGATE_MAX_VALUE = "int 56319"
TRAIL_SURROGATE_MAX_VALUE = "int 57343"
SURROGATE_MIN_VALUE = "int 55296"
SURROGATE_MAX_VALUE = "int 57343"
FOLD_CASE_DEFAULT = "int 0"
FOLD_CASE_EXCLUDE_SPECIAL_I = "int 1"
def charAt():
'''public static int charAt(final String source, final int offset16)
public static int charAt(final CharSequence source, final int offset16)
public static int charAt(final StringBuffer source, int offset16)
public static int charAt(final char[] source, final int start, final int limit, int offset16)
public static int charAt(final Replaceable source, int offset16)
'''
pass
def getCharCount():
'''public static int getCharCount(final int char32)
'''
pass
def bounds():
'''public static int bounds(final String source, int offset16)
public static int bounds(final StringBuffer source, int offset16)
public static int bounds(final char[] source, final int start, final int limit, int offset16)
'''
pass
def isSurrogate():
'''public static boolean isSurrogate(final char char16)
'''
pass
def isTrailSurrogate():
'''public static boolean isTrailSurrogate(final char char16)
'''
pass
def isLeadSurrogate():
'''public static boolean isLeadSurrogate(final char char16)
'''
pass
def getLeadSurrogate():
'''public static char getLeadSurrogate(final int char32)
'''
pass
def getTrailSurrogate():
'''public static char getTrailSurrogate(final int char32)
'''
pass
def valueOf():
'''public static String valueOf(final int char32)
public static String valueOf(final String source, final int offset16)
public static String valueOf(final StringBuffer source, final int offset16)
public static String valueOf(final char[] source, final int start, final int limit, final int offset16)
'''
pass
def findOffsetFromCodePoint():
'''public static int findOffsetFromCodePoint(final String source, final int offset32)
public static int findOffsetFromCodePoint(final StringBuffer source, final int offset32)
public static int findOffsetFromCodePoint(final char[] source, final int start, final int limit, final int offset32)
'''
pass
def findCodePointOffset():
'''public static int findCodePointOffset(final String source, final int offset16)
public static int findCodePointOffset(final StringBuffer source, final int offset16)
public static int findCodePointOffset(final char[] source, final int start, final int limit, int offset16)
'''
pass
def append():
'''public static StringBuffer append(final StringBuffer target, final int char32)
public static int append(final char[] target, int limit, final int char32)
'''
pass
def appendCodePoint():
'''public static StringBuffer appendCodePoint(final StringBuffer target, final int cp)
'''
pass
def countCodePoint():
'''public static int countCodePoint(final String source)
public static int countCodePoint(final StringBuffer source)
public static int countCodePoint(final char[] source, final int start, final int limit)
'''
pass
def setCharAt():
'''public static void setCharAt(final StringBuffer target, int offset16, final int char32)
public static int setCharAt(final char[] target, final int limit, int offset16, final int char32)
'''
pass
def moveCodePointOffset():
'''public static int moveCodePointOffset(final String source, final int offset16, final int shift32)
public static int moveCodePointOffset(final StringBuffer source, final int offset16, final int shift32)
public static int moveCodePointOffset(final char[] source, final int start, final int limit, final int offset16, final int shift32)
'''
pass
def insert():
'''public static StringBuffer insert(final StringBuffer target, int offset16, final int char32)
public static int insert(final char[] target, final int limit, int offset16, final int char32)
'''
pass
def delete():
'''public static StringBuffer delete(final StringBuffer target, int offset16)
public static int delete(final char[] target, final int limit, int offset16)
'''
pass
def indexOf():
'''public static int indexOf(final String source, final int char32)
public static int indexOf(final String source, final String str)
public static int indexOf(final String source, final int char32, final int fromIndex)
public static int indexOf(final String source, final String str, final int fromIndex)
'''
pass
def lastIndexOf():
'''public static int lastIndexOf(final String source, final int char32)
public static int lastIndexOf(final String source, final String str)
public static int lastIndexOf(final String source, final int char32, final int fromIndex)
public static int lastIndexOf(final String source, final String str, final int fromIndex)
'''
pass
def replace():
'''public static String replace(final String source, final int oldChar32, final int newChar32)
public static String replace(final String source, final String oldStr, final String newStr)
'''
pass
def reverse():
'''public static StringBuffer reverse(final StringBuffer source)
'''
pass
def hasMoreCodePointsThan():
'''public static boolean hasMoreCodePointsThan(final String source, int number)
public static boolean hasMoreCodePointsThan(final char[] source, int start, final int limit, int number)
public static boolean hasMoreCodePointsThan(final StringBuffer source, int number)
'''
pass
def newString():
'''public static String newString(final int[] codePoints, final int offset, final int count)
'''
pass
def getSingleCodePoint():
'''public static int getSingleCodePoint(final CharSequence s)
'''
pass
def compareCodePoint():
'''public static int compareCodePoint(final int codePoint, final CharSequence s)
'''
pass
def StringComparator():
'''public StringComparator()
public StringComparator(final boolean codepointcompare, final boolean ignorecase, final int foldcaseoption)
'''
pass
def setCodePointCompare():
'''public void setCodePointCompare(final boolean flag)
'''
pass
def setIgnoreCase():
'''public void setIgnoreCase(final boolean ignorecase, final int foldcaseoption)
'''
pass
def getCodePointCompare():
'''public boolean getCodePointCompare()
'''
pass
def getIgnoreCase():
'''public boolean getIgnoreCase()
'''
pass
def getIgnoreCaseOption():
'''public int getIgnoreCaseOption()
'''
pass
def compare():
'''public int compare(final String a, final String b)
'''
pass
