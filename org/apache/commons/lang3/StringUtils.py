SPACE = "String   ""
EMPTY = "String  "
LF = "String  \n""
CR = "String  \r""
INDEX_NOT_FOUND = "int  -1"
def isEmpty():
'''public static boolean isEmpty(final CharSequence cs)
'''
pass
def isNotEmpty():
'''public static boolean isNotEmpty(final CharSequence cs)
'''
pass
def isAnyEmpty():
'''public static boolean isAnyEmpty(final CharSequence... css)
'''
pass
def isNoneEmpty():
'''public static boolean isNoneEmpty(final CharSequence... css)
'''
pass
def isBlank():
'''public static boolean isBlank(final CharSequence cs)
'''
pass
def isNotBlank():
'''public static boolean isNotBlank(final CharSequence cs)
'''
pass
def isAnyBlank():
'''public static boolean isAnyBlank(final CharSequence... css)
'''
pass
def isNoneBlank():
'''public static boolean isNoneBlank(final CharSequence... css)
'''
pass
def trim():
'''public static String trim(final String str)
'''
pass
def trimToNull():
'''public static String trimToNull(final String str)
'''
pass
def trimToEmpty():
'''public static String trimToEmpty(final String str)
'''
pass
def strip():
'''public static String strip(final String str)
public static String strip(String str, final String stripChars)
'''
pass
def stripToNull():
'''public static String stripToNull(String str)
'''
pass
def stripToEmpty():
'''public static String stripToEmpty(final String str)
'''
pass
def stripStart():
'''public static String stripStart(final String str, final String stripChars)
'''
pass
def stripEnd():
'''public static String stripEnd(final String str, final String stripChars)
'''
pass
def stripAll():
'''public static String[] stripAll(final String... strs)
public static String[] stripAll(final String[] strs, final String stripChars)
'''
pass
def stripAccents():
'''public static String stripAccents(final String input)
'''
pass
def equals():
'''public static boolean equals(final CharSequence cs1, final CharSequence cs2)
'''
pass
def equalsIgnoreCase():
'''public static boolean equalsIgnoreCase(final CharSequence str1, final CharSequence str2)
'''
pass
def indexOf():
'''public static int indexOf(final CharSequence seq, final int searchChar)
public static int indexOf(final CharSequence seq, final int searchChar, final int startPos)
public static int indexOf(final CharSequence seq, final CharSequence searchSeq)
public static int indexOf(final CharSequence seq, final CharSequence searchSeq, final int startPos)
'''
pass
def ordinalIndexOf():
'''public static int ordinalIndexOf(final CharSequence str, final CharSequence searchStr, final int ordinal)
'''
pass
def indexOfIgnoreCase():
'''public static int indexOfIgnoreCase(final CharSequence str, final CharSequence searchStr)
public static int indexOfIgnoreCase(final CharSequence str, final CharSequence searchStr, int startPos)
'''
pass
def lastIndexOf():
'''public static int lastIndexOf(final CharSequence seq, final int searchChar)
public static int lastIndexOf(final CharSequence seq, final int searchChar, final int startPos)
public static int lastIndexOf(final CharSequence seq, final CharSequence searchSeq)
public static int lastIndexOf(final CharSequence seq, final CharSequence searchSeq, final int startPos)
'''
pass
def lastOrdinalIndexOf():
'''public static int lastOrdinalIndexOf(final CharSequence str, final CharSequence searchStr, final int ordinal)
'''
pass
def lastIndexOfIgnoreCase():
'''public static int lastIndexOfIgnoreCase(final CharSequence str, final CharSequence searchStr)
public static int lastIndexOfIgnoreCase(final CharSequence str, final CharSequence searchStr, int startPos)
'''
pass
def contains():
'''public static boolean contains(final CharSequence seq, final int searchChar)
public static boolean contains(final CharSequence seq, final CharSequence searchSeq)
'''
pass
def containsIgnoreCase():
'''public static boolean containsIgnoreCase(final CharSequence str, final CharSequence searchStr)
'''
pass
def containsWhitespace():
'''public static boolean containsWhitespace(final CharSequence seq)
'''
pass
def indexOfAny():
'''public static int indexOfAny(final CharSequence cs, final char... searchChars)
public static int indexOfAny(final CharSequence cs, final String searchChars)
public static int indexOfAny(final CharSequence str, final CharSequence... searchStrs)
'''
pass
def containsAny():
'''public static boolean containsAny(final CharSequence cs, final char... searchChars)
public static boolean containsAny(final CharSequence cs, final CharSequence searchChars)
public static boolean containsAny(final CharSequence cs, final CharSequence... searchCharSequences)
'''
pass
def indexOfAnyBut():
'''public static int indexOfAnyBut(final CharSequence cs, final char... searchChars)
public static int indexOfAnyBut(final CharSequence seq, final CharSequence searchChars)
'''
pass
def containsOnly():
'''public static boolean containsOnly(final CharSequence cs, final char... valid)
public static boolean containsOnly(final CharSequence cs, final String validChars)
'''
pass
def containsNone():
'''public static boolean containsNone(final CharSequence cs, final char... searchChars)
public static boolean containsNone(final CharSequence cs, final String invalidChars)
'''
pass
def lastIndexOfAny():
'''public static int lastIndexOfAny(final CharSequence str, final CharSequence... searchStrs)
'''
pass
def substring():
'''public static String substring(final String str, int start)
public static String substring(final String str, int start, int end)
'''
pass
def left():
'''public static String left(final String str, final int len)
'''
pass
def right():
'''public static String right(final String str, final int len)
'''
pass
def mid():
'''public static String mid(final String str, int pos, final int len)
'''
pass
def substringBefore():
'''public static String substringBefore(final String str, final String separator)
'''
pass
def substringAfter():
'''public static String substringAfter(final String str, final String separator)
'''
pass
def substringBeforeLast():
'''public static String substringBeforeLast(final String str, final String separator)
'''
pass
def substringAfterLast():
'''public static String substringAfterLast(final String str, final String separator)
'''
pass
def substringBetween():
'''public static String substringBetween(final String str, final String tag)
public static String substringBetween(final String str, final String open, final String close)
'''
pass
def substringsBetween():
'''public static String[] substringsBetween(final String str, final String open, final String close)
'''
pass
def split():
'''public static String[] split(final String str)
public static String[] split(final String str, final char separatorChar)
public static String[] split(final String str, final String separatorChars)
public static String[] split(final String str, final String separatorChars, final int max)
'''
pass
def splitByWholeSeparator():
'''public static String[] splitByWholeSeparator(final String str, final String separator)
public static String[] splitByWholeSeparator(final String str, final String separator, final int max)
'''
pass
def splitByWholeSeparatorPreserveAllTokens():
'''public static String[] splitByWholeSeparatorPreserveAllTokens(final String str, final String separator)
public static String[] splitByWholeSeparatorPreserveAllTokens(final String str, final String separator, final int max)
'''
pass
def splitPreserveAllTokens():
'''public static String[] splitPreserveAllTokens(final String str)
public static String[] splitPreserveAllTokens(final String str, final char separatorChar)
public static String[] splitPreserveAllTokens(final String str, final String separatorChars)
public static String[] splitPreserveAllTokens(final String str, final String separatorChars, final int max)
'''
pass
def splitByCharacterType():
'''public static String[] splitByCharacterType(final String str)
'''
pass
def splitByCharacterTypeCamelCase():
'''public static String[] splitByCharacterTypeCamelCase(final String str)
'''
pass
def join():
'''public static <T> String join(final T... elements)
public static String join(final Object[] array, final char separator)
public static String join(final long[] array, final char separator)
public static String join(final int[] array, final char separator)
public static String join(final short[] array, final char separator)
public static String join(final byte[] array, final char separator)
public static String join(final char[] array, final char separator)
public static String join(final float[] array, final char separator)
public static String join(final double[] array, final char separator)
public static String join(final Object[] array, final char separator, final int startIndex, final int endIndex)
public static String join(final long[] array, final char separator, final int startIndex, final int endIndex)
public static String join(final int[] array, final char separator, final int startIndex, final int endIndex)
public static String join(final byte[] array, final char separator, final int startIndex, final int endIndex)
public static String join(final short[] array, final char separator, final int startIndex, final int endIndex)
public static String join(final char[] array, final char separator, final int startIndex, final int endIndex)
public static String join(final double[] array, final char separator, final int startIndex, final int endIndex)
public static String join(final float[] array, final char separator, final int startIndex, final int endIndex)
public static String join(final Object[] array, final String separator)
public static String join(final Object[] array, String separator, final int startIndex, final int endIndex)
public static String join(final Iterator<?> iterator, final char separator)
public static String join(final Iterator<?> iterator, final String separator)
public static String join(final Iterable<?> iterable, final char separator)
public static String join(final Iterable<?> iterable, final String separator)
'''
pass
def deleteWhitespace():
'''public static String deleteWhitespace(final String str)
'''
pass
def removeStart():
'''public static String removeStart(final String str, final String remove)
'''
pass
def removeStartIgnoreCase():
'''public static String removeStartIgnoreCase(final String str, final String remove)
'''
pass
def removeEnd():
'''public static String removeEnd(final String str, final String remove)
'''
pass
def removeEndIgnoreCase():
'''public static String removeEndIgnoreCase(final String str, final String remove)
'''
pass
def remove():
'''public static String remove(final String str, final String remove)
public static String remove(final String str, final char remove)
'''
pass
def replaceOnce():
'''public static String replaceOnce(final String text, final String searchString, final String replacement)
'''
pass
def replacePattern():
'''public static String replacePattern(final String source, final String regex, final String replacement)
'''
pass
def removePattern():
'''public static String removePattern(final String source, final String regex)
'''
pass
def replace():
'''public static String replace(final String text, final String searchString, final String replacement)
public static String replace(final String text, final String searchString, final String replacement, int max)
'''
pass
def replaceEach():
'''public static String replaceEach(final String text, final String[] searchList, final String[] replacementList)
'''
pass
def replaceEachRepeatedly():
'''public static String replaceEachRepeatedly(final String text, final String[] searchList, final String[] replacementList)
'''
pass
def replaceChars():
'''public static String replaceChars(final String str, final char searchChar, final char replaceChar)
public static String replaceChars(final String str, final String searchChars, String replaceChars)
'''
pass
def overlay():
'''public static String overlay(final String str, String overlay, int start, int end)
'''
pass
def chomp():
'''public static String chomp(final String str)
public static String chomp(final String str, final String separator)
'''
pass
def chop():
'''public static String chop(final String str)
'''
pass
def repeat():
'''public static String repeat(final String str, final int repeat)
public static String repeat(final String str, final String separator, final int repeat)
public static String repeat(final char ch, final int repeat)
'''
pass
def rightPad():
'''public static String rightPad(final String str, final int size)
public static String rightPad(final String str, final int size, final char padChar)
public static String rightPad(final String str, final int size, String padStr)
'''
pass
def leftPad():
'''public static String leftPad(final String str, final int size)
public static String leftPad(final String str, final int size, final char padChar)
public static String leftPad(final String str, final int size, String padStr)
'''
pass
def length():
'''public static int length(final CharSequence cs)
'''
pass
def center():
'''public static String center(final String str, final int size)
public static String center(String str, final int size, final char padChar)
public static String center(String str, final int size, String padStr)
'''
pass
def upperCase():
'''public static String upperCase(final String str)
public static String upperCase(final String str, final Locale locale)
'''
pass
def lowerCase():
'''public static String lowerCase(final String str)
public static String lowerCase(final String str, final Locale locale)
'''
pass
def capitalize():
'''public static String capitalize(final String str)
'''
pass
def uncapitalize():
'''public static String uncapitalize(final String str)
'''
pass
def swapCase():
'''public static String swapCase(final String str)
'''
pass
def countMatches():
'''public static int countMatches(final CharSequence str, final CharSequence sub)
public static int countMatches(final CharSequence str, final char ch)
'''
pass
def isAlpha():
'''public static boolean isAlpha(final CharSequence cs)
'''
pass
def isAlphaSpace():
'''public static boolean isAlphaSpace(final CharSequence cs)
'''
pass
def isAlphanumeric():
'''public static boolean isAlphanumeric(final CharSequence cs)
'''
pass
def isAlphanumericSpace():
'''public static boolean isAlphanumericSpace(final CharSequence cs)
'''
pass
def isAsciiPrintable():
'''public static boolean isAsciiPrintable(final CharSequence cs)
'''
pass
def isNumeric():
'''public static boolean isNumeric(final CharSequence cs)
'''
pass
def isNumericSpace():
'''public static boolean isNumericSpace(final CharSequence cs)
'''
pass
def isWhitespace():
'''public static boolean isWhitespace(final CharSequence cs)
'''
pass
def isAllLowerCase():
'''public static boolean isAllLowerCase(final CharSequence cs)
'''
pass
def isAllUpperCase():
'''public static boolean isAllUpperCase(final CharSequence cs)
'''
pass
def defaultString():
'''public static String defaultString(final String str)
public static String defaultString(final String str, final String defaultStr)
'''
pass
def defaultIfBlank():
'''public static <T extends CharSequence> T defaultIfBlank(final T str, final T defaultStr)
'''
pass
def defaultIfEmpty():
'''public static <T extends CharSequence> T defaultIfEmpty(final T str, final T defaultStr)
'''
pass
def reverse():
'''public static String reverse(final String str)
'''
pass
def reverseDelimited():
'''public static String reverseDelimited(final String str, final char separatorChar)
'''
pass
def abbreviate():
'''public static String abbreviate(final String str, final int maxWidth)
public static String abbreviate(final String str, int offset, final int maxWidth)
'''
pass
def abbreviateMiddle():
'''public static String abbreviateMiddle(final String str, final String middle, final int length)
'''
pass
def difference():
'''public static String difference(final String str1, final String str2)
'''
pass
def indexOfDifference():
'''public static int indexOfDifference(final CharSequence cs1, final CharSequence cs2)
public static int indexOfDifference(final CharSequence... css)
'''
pass
def getCommonPrefix():
'''public static String getCommonPrefix(final String... strs)
'''
pass
def getLevenshteinDistance():
'''public static int getLevenshteinDistance(CharSequence s, CharSequence t)
public static int getLevenshteinDistance(CharSequence s, CharSequence t, final int threshold)
'''
pass
def getJaroWinklerDistance():
'''public static double getJaroWinklerDistance(final CharSequence first, final CharSequence second)
'''
pass
def getFuzzyDistance():
'''public static int getFuzzyDistance(final CharSequence term, final CharSequence query, final Locale locale)
'''
pass
def startsWith():
'''public static boolean startsWith(final CharSequence str, final CharSequence prefix)
'''
pass
def startsWithIgnoreCase():
'''public static boolean startsWithIgnoreCase(final CharSequence str, final CharSequence prefix)
'''
pass
def startsWithAny():
'''public static boolean startsWithAny(final CharSequence string, final CharSequence... searchStrings)
'''
pass
def endsWith():
'''public static boolean endsWith(final CharSequence str, final CharSequence suffix)
'''
pass
def endsWithIgnoreCase():
'''public static boolean endsWithIgnoreCase(final CharSequence str, final CharSequence suffix)
'''
pass
def normalizeSpace():
'''public static String normalizeSpace(final String str)
'''
pass
def endsWithAny():
'''public static boolean endsWithAny(final CharSequence string, final CharSequence... searchStrings)
'''
pass
def appendIfMissing():
'''public static String appendIfMissing(final String str, final CharSequence suffix, final CharSequence... suffixes)
'''
pass
def appendIfMissingIgnoreCase():
'''public static String appendIfMissingIgnoreCase(final String str, final CharSequence suffix, final CharSequence... suffixes)
'''
pass
def prependIfMissing():
'''public static String prependIfMissing(final String str, final CharSequence prefix, final CharSequence... prefixes)
'''
pass
def prependIfMissingIgnoreCase():
'''public static String prependIfMissingIgnoreCase(final String str, final CharSequence prefix, final CharSequence... prefixes)
'''
pass
def toString():
'''public static String toString(final byte[] bytes, final String charsetName)
'''
pass
def toEncodedString():
'''public static String toEncodedString(final byte[] bytes, final Charset charset)
'''
pass
def wrap():
'''public static String wrap(final String str, final char wrapWith)
public static String wrap(final String str, final String wrapWith)
'''
pass
