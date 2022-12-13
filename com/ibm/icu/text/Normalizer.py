UNICODE_3_2 = "int 32"
DONE = "int -1"
IGNORE_HANGUL = "int 1"
FOLD_CASE_DEFAULT = "int 0"
INPUT_IS_FCD = "int 131072"
COMPARE_IGNORE_CASE = "int 65536"
COMPARE_CODE_POINT_ORDER = "int 32768"
FOLD_CASE_EXCLUDE_SPECIAL_I = "int 1"
COMPARE_NORM_OPTIONS_SHIFT = "int 20"
def Normalizer():
'''public Normalizer(final String str, final Mode mode, final int opt)
public Normalizer(final CharacterIterator iter, final Mode mode, final int opt)
public Normalizer(final UCharacterIterator iter, final Mode mode, final int options)
'''
pass
def clone():
'''public Object clone()
'''
pass
def compose():
'''public static String compose(final String str, final boolean compat)
public static String compose(final String str, final boolean compat, final int options)
public static int compose(final char[] source, final char[] target, final boolean compat, final int options)
public static int compose(final char[] src, final int srcStart, final int srcLimit, final char[] dest, final int destStart, final int destLimit, final boolean compat, final int options)
'''
pass
def decompose():
'''public static String decompose(final String str, final boolean compat)
public static String decompose(final String str, final boolean compat, final int options)
public static int decompose(final char[] source, final char[] target, final boolean compat, final int options)
public static int decompose(final char[] src, final int srcStart, final int srcLimit, final char[] dest, final int destStart, final int destLimit, final boolean compat, final int options)
'''
pass
def normalize():
'''public static String normalize(final String str, final Mode mode, final int options)
public static String normalize(final String src, final Mode mode)
public static int normalize(final char[] source, final char[] target, final Mode mode, final int options)
public static int normalize(final char[] src, final int srcStart, final int srcLimit, final char[] dest, final int destStart, final int destLimit, final Mode mode, final int options)
public static String normalize(final int char32, final Mode mode, final int options)
public static String normalize(final int char32, final Mode mode)
'''
pass
def quickCheck():
'''public static QuickCheckResult quickCheck(final String source, final Mode mode)
public static QuickCheckResult quickCheck(final String source, final Mode mode, final int options)
public static QuickCheckResult quickCheck(final char[] source, final Mode mode, final int options)
public static QuickCheckResult quickCheck(final char[] source, final int start, final int limit, final Mode mode, final int options)
'''
pass
def isNormalized():
'''public static boolean isNormalized(final char[] src, final int start, final int limit, final Mode mode, final int options)
public static boolean isNormalized(final String str, final Mode mode, final int options)
public static boolean isNormalized(final int char32, final Mode mode, final int options)
'''
pass
def compare():
'''public static int compare(final char[] s1, final int s1Start, final int s1Limit, final char[] s2, final int s2Start, final int s2Limit, final int options)
public static int compare(final String s1, final String s2, final int options)
public static int compare(final char[] s1, final char[] s2, final int options)
public static int compare(final int char32a, final int char32b, final int options)
public static int compare(final int char32a, final String str2, final int options)
'''
pass
def concatenate():
'''public static int concatenate(final char[] left, final int leftStart, final int leftLimit, final char[] right, final int rightStart, final int rightLimit, final char[] dest, final int destStart, final int destLimit, final Mode mode, final int options)
public static String concatenate(final char[] left, final char[] right, final Mode mode, final int options)
public static String concatenate(final String left, final String right, final Mode mode, final int options)
'''
pass
def getFC_NFKC_Closure():
'''public static int getFC_NFKC_Closure(final int c, final char[] dest)
public static String getFC_NFKC_Closure(final int c)
'''
pass
def current():
'''public int current()
'''
pass
def next():
'''public int next()
'''
pass
def previous():
'''public int previous()
'''
pass
def reset():
'''public void reset()
'''
pass
def setIndexOnly():
'''public void setIndexOnly(final int index)
'''
pass
def setIndex():
'''public int setIndex(final int index)
'''
pass
def getBeginIndex():
'''public int getBeginIndex()
'''
pass
def getEndIndex():
'''public int getEndIndex()
'''
pass
def first():
'''public int first()
'''
pass
def last():
'''public int last()
'''
pass
def getIndex():
'''public int getIndex()
'''
pass
def startIndex():
'''public int startIndex()
'''
pass
def endIndex():
'''public int endIndex()
'''
pass
def setMode():
'''public void setMode(final Mode newMode)
'''
pass
def getMode():
'''public Mode getMode()
'''
pass
def setOption():
'''public void setOption(final int option, final boolean value)
'''
pass
def getOption():
'''public int getOption(final int option)
'''
pass
def getText():
'''public int getText(final char[] fillIn)
public String getText()
'''
pass
def getLength():
'''public int getLength()
'''
pass
def setText():
'''public void setText(final StringBuffer newText)
public void setText(final char[] newText)
public void setText(final String newText)
public void setText(final CharacterIterator newText)
public void setText(final UCharacterIterator newText)
'''
pass
def CharsAppendable():
'''public CharsAppendable(final char[] dest, final int destStart, final int destLimit)
'''
pass
def length():
'''public int length()
'''
pass
def append():
'''public Appendable append(final char c)
public Appendable append(final CharSequence s)
public Appendable append(final CharSequence s, int sStart, final int sLimit)
'''
pass
