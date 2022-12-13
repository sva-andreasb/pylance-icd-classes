SPACE = "String  \" \""
EMPTY = "String  \"\""
LF = "String  \"\n\""
CR = "String  \"\r\""
INDEX_NOT_FOUND = "int  -1"
def isEmpty():
    '''public static boolean isEmpty(final CharSequence cs)
    '''
def isNotEmpty():
    '''public static boolean isNotEmpty(final CharSequence cs)
    '''
def isAnyEmpty():
    '''public static boolean isAnyEmpty(final CharSequence... css)
    '''
def isNoneEmpty():
    '''public static boolean isNoneEmpty(final CharSequence... css)
    '''
def isBlank():
    '''public static boolean isBlank(final CharSequence cs)
    '''
def isNotBlank():
    '''public static boolean isNotBlank(final CharSequence cs)
    '''
def isAnyBlank():
    '''public static boolean isAnyBlank(final CharSequence... css)
    '''
def isNoneBlank():
    '''public static boolean isNoneBlank(final CharSequence... css)
    '''
def trim():
    '''public static String trim(final String str)
    '''
def trimToNull():
    '''public static String trimToNull(final String str)
    '''
def trimToEmpty():
    '''public static String trimToEmpty(final String str)
    '''
def strip():
    '''public static String strip(final String str)
    public static String strip(String str, final String stripChars)
    '''
def stripToNull():
    '''public static String stripToNull(String str)
    '''
def stripToEmpty():
    '''public static String stripToEmpty(final String str)
    '''
def stripStart():
    '''public static String stripStart(final String str, final String stripChars)
    '''
def stripEnd():
    '''public static String stripEnd(final String str, final String stripChars)
    '''
def stripAll():
    '''public static String[] stripAll(final String... strs)
    public static String[] stripAll(final String[] strs, final String stripChars)
    '''
def stripAccents():
    '''public static String stripAccents(final String input)
    '''
def equals():
    '''public static boolean equals(final CharSequence cs1, final CharSequence cs2)
    '''
def equalsIgnoreCase():
    '''public static boolean equalsIgnoreCase(final CharSequence str1, final CharSequence str2)
    '''
def indexOf():
    '''public static int indexOf(final CharSequence seq, final int searchChar)
    public static int indexOf(final CharSequence seq, final int searchChar, final int startPos)
    public static int indexOf(final CharSequence seq, final CharSequence searchSeq)
    public static int indexOf(final CharSequence seq, final CharSequence searchSeq, final int startPos)
    '''
def ordinalIndexOf():
    '''public static int ordinalIndexOf(final CharSequence str, final CharSequence searchStr, final int ordinal)
    '''
def indexOfIgnoreCase():
    '''public static int indexOfIgnoreCase(final CharSequence str, final CharSequence searchStr)
    public static int indexOfIgnoreCase(final CharSequence str, final CharSequence searchStr, int startPos)
    '''
def lastIndexOf():
    '''public static int lastIndexOf(final CharSequence seq, final int searchChar)
    public static int lastIndexOf(final CharSequence seq, final int searchChar, final int startPos)
    public static int lastIndexOf(final CharSequence seq, final CharSequence searchSeq)
    public static int lastIndexOf(final CharSequence seq, final CharSequence searchSeq, final int startPos)
    '''
def lastOrdinalIndexOf():
    '''public static int lastOrdinalIndexOf(final CharSequence str, final CharSequence searchStr, final int ordinal)
    '''
def lastIndexOfIgnoreCase():
    '''public static int lastIndexOfIgnoreCase(final CharSequence str, final CharSequence searchStr)
    public static int lastIndexOfIgnoreCase(final CharSequence str, final CharSequence searchStr, int startPos)
    '''
def contains():
    '''public static boolean contains(final CharSequence seq, final int searchChar)
    public static boolean contains(final CharSequence seq, final CharSequence searchSeq)
    '''
def containsIgnoreCase():
    '''public static boolean containsIgnoreCase(final CharSequence str, final CharSequence searchStr)
    '''
def containsWhitespace():
    '''public static boolean containsWhitespace(final CharSequence seq)
    '''
def indexOfAny():
    '''public static int indexOfAny(final CharSequence cs, final char... searchChars)
    public static int indexOfAny(final CharSequence cs, final String searchChars)
    public static int indexOfAny(final CharSequence str, final CharSequence... searchStrs)
    '''
def containsAny():
    '''public static boolean containsAny(final CharSequence cs, final char... searchChars)
    public static boolean containsAny(final CharSequence cs, final CharSequence searchChars)
    public static boolean containsAny(final CharSequence cs, final CharSequence... searchCharSequences)
    '''
def indexOfAnyBut():
    '''public static int indexOfAnyBut(final CharSequence cs, final char... searchChars)
    public static int indexOfAnyBut(final CharSequence seq, final CharSequence searchChars)
    '''
def containsOnly():
    '''public static boolean containsOnly(final CharSequence cs, final char... valid)
    public static boolean containsOnly(final CharSequence cs, final String validChars)
    '''
def containsNone():
    '''public static boolean containsNone(final CharSequence cs, final char... searchChars)
    public static boolean containsNone(final CharSequence cs, final String invalidChars)
    '''
def lastIndexOfAny():
    '''public static int lastIndexOfAny(final CharSequence str, final CharSequence... searchStrs)
    '''
def substring():
    '''public static String substring(final String str, int start)
    public static String substring(final String str, int start, int end)
    '''
def left():
    '''public static String left(final String str, final int len)
    '''
def right():
    '''public static String right(final String str, final int len)
    '''
def mid():
    '''public static String mid(final String str, int pos, final int len)
    '''
def substringBefore():
    '''public static String substringBefore(final String str, final String separator)
    '''
def substringAfter():
    '''public static String substringAfter(final String str, final String separator)
    '''
def substringBeforeLast():
    '''public static String substringBeforeLast(final String str, final String separator)
    '''
def substringAfterLast():
    '''public static String substringAfterLast(final String str, final String separator)
    '''
def substringBetween():
    '''public static String substringBetween(final String str, final String tag)
    public static String substringBetween(final String str, final String open, final String close)
    '''
def substringsBetween():
    '''public static String[] substringsBetween(final String str, final String open, final String close)
    '''
def split():
    '''public static String[] split(final String str)
    public static String[] split(final String str, final char separatorChar)
    public static String[] split(final String str, final String separatorChars)
    public static String[] split(final String str, final String separatorChars, final int max)
    '''
def splitByWholeSeparator():
    '''public static String[] splitByWholeSeparator(final String str, final String separator)
    public static String[] splitByWholeSeparator(final String str, final String separator, final int max)
    '''
def splitByWholeSeparatorPreserveAllTokens():
    '''public static String[] splitByWholeSeparatorPreserveAllTokens(final String str, final String separator)
    public static String[] splitByWholeSeparatorPreserveAllTokens(final String str, final String separator, final int max)
    '''
def splitPreserveAllTokens():
    '''public static String[] splitPreserveAllTokens(final String str)
    public static String[] splitPreserveAllTokens(final String str, final char separatorChar)
    public static String[] splitPreserveAllTokens(final String str, final String separatorChars)
    public static String[] splitPreserveAllTokens(final String str, final String separatorChars, final int max)
    '''
def splitByCharacterType():
    '''public static String[] splitByCharacterType(final String str)
    '''
def splitByCharacterTypeCamelCase():
    '''public static String[] splitByCharacterTypeCamelCase(final String str)
    '''
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
def deleteWhitespace():
    '''public static String deleteWhitespace(final String str)
    '''
def removeStart():
    '''public static String removeStart(final String str, final String remove)
    '''
def removeStartIgnoreCase():
    '''public static String removeStartIgnoreCase(final String str, final String remove)
    '''
def removeEnd():
    '''public static String removeEnd(final String str, final String remove)
    '''
def removeEndIgnoreCase():
    '''public static String removeEndIgnoreCase(final String str, final String remove)
    '''
def remove():
    '''public static String remove(final String str, final String remove)
    public static String remove(final String str, final char remove)
    '''
def replaceOnce():
    '''public static String replaceOnce(final String text, final String searchString, final String replacement)
    '''
def replacePattern():
    '''public static String replacePattern(final String source, final String regex, final String replacement)
    '''
def removePattern():
    '''public static String removePattern(final String source, final String regex)
    '''
def replace():
    '''public static String replace(final String text, final String searchString, final String replacement)
    public static String replace(final String text, final String searchString, final String replacement, int max)
    '''
def replaceEach():
    '''public static String replaceEach(final String text, final String[] searchList, final String[] replacementList)
    '''
def replaceEachRepeatedly():
    '''public static String replaceEachRepeatedly(final String text, final String[] searchList, final String[] replacementList)
    '''
def replaceChars():
    '''public static String replaceChars(final String str, final char searchChar, final char replaceChar)
    public static String replaceChars(final String str, final String searchChars, String replaceChars)
    '''
def overlay():
    '''public static String overlay(final String str, String overlay, int start, int end)
    '''
def chomp():
    '''public static String chomp(final String str)
    public static String chomp(final String str, final String separator)
    '''
def chop():
    '''public static String chop(final String str)
    '''
def repeat():
    '''public static String repeat(final String str, final int repeat)
    public static String repeat(final String str, final String separator, final int repeat)
    public static String repeat(final char ch, final int repeat)
    '''
def rightPad():
    '''public static String rightPad(final String str, final int size)
    public static String rightPad(final String str, final int size, final char padChar)
    public static String rightPad(final String str, final int size, String padStr)
    '''
def leftPad():
    '''public static String leftPad(final String str, final int size)
    public static String leftPad(final String str, final int size, final char padChar)
    public static String leftPad(final String str, final int size, String padStr)
    '''
def length():
    '''public static int length(final CharSequence cs)
    '''
def center():
    '''public static String center(final String str, final int size)
    public static String center(String str, final int size, final char padChar)
    public static String center(String str, final int size, String padStr)
    '''
def upperCase():
    '''public static String upperCase(final String str)
    public static String upperCase(final String str, final Locale locale)
    '''
def lowerCase():
    '''public static String lowerCase(final String str)
    public static String lowerCase(final String str, final Locale locale)
    '''
def capitalize():
    '''public static String capitalize(final String str)
    '''
def uncapitalize():
    '''public static String uncapitalize(final String str)
    '''
def swapCase():
    '''public static String swapCase(final String str)
    '''
def countMatches():
    '''public static int countMatches(final CharSequence str, final CharSequence sub)
    public static int countMatches(final CharSequence str, final char ch)
    '''
def isAlpha():
    '''public static boolean isAlpha(final CharSequence cs)
    '''
def isAlphaSpace():
    '''public static boolean isAlphaSpace(final CharSequence cs)
    '''
def isAlphanumeric():
    '''public static boolean isAlphanumeric(final CharSequence cs)
    '''
def isAlphanumericSpace():
    '''public static boolean isAlphanumericSpace(final CharSequence cs)
    '''
def isAsciiPrintable():
    '''public static boolean isAsciiPrintable(final CharSequence cs)
    '''
def isNumeric():
    '''public static boolean isNumeric(final CharSequence cs)
    '''
def isNumericSpace():
    '''public static boolean isNumericSpace(final CharSequence cs)
    '''
def isWhitespace():
    '''public static boolean isWhitespace(final CharSequence cs)
    '''
def isAllLowerCase():
    '''public static boolean isAllLowerCase(final CharSequence cs)
    '''
def isAllUpperCase():
    '''public static boolean isAllUpperCase(final CharSequence cs)
    '''
def defaultString():
    '''public static String defaultString(final String str)
    public static String defaultString(final String str, final String defaultStr)
    '''
def defaultIfBlank():
    '''public static <T extends CharSequence> T defaultIfBlank(final T str, final T defaultStr)
    '''
def defaultIfEmpty():
    '''public static <T extends CharSequence> T defaultIfEmpty(final T str, final T defaultStr)
    '''
def reverse():
    '''public static String reverse(final String str)
    '''
def reverseDelimited():
    '''public static String reverseDelimited(final String str, final char separatorChar)
    '''
def abbreviate():
    '''public static String abbreviate(final String str, final int maxWidth)
    public static String abbreviate(final String str, int offset, final int maxWidth)
    '''
def abbreviateMiddle():
    '''public static String abbreviateMiddle(final String str, final String middle, final int length)
    '''
def difference():
    '''public static String difference(final String str1, final String str2)
    '''
def indexOfDifference():
    '''public static int indexOfDifference(final CharSequence cs1, final CharSequence cs2)
    public static int indexOfDifference(final CharSequence... css)
    '''
def getCommonPrefix():
    '''public static String getCommonPrefix(final String... strs)
    '''
def getLevenshteinDistance():
    '''public static int getLevenshteinDistance(CharSequence s, CharSequence t)
    public static int getLevenshteinDistance(CharSequence s, CharSequence t, final int threshold)
    '''
def getJaroWinklerDistance():
    '''public static double getJaroWinklerDistance(final CharSequence first, final CharSequence second)
    '''
def getFuzzyDistance():
    '''public static int getFuzzyDistance(final CharSequence term, final CharSequence query, final Locale locale)
    '''
def startsWith():
    '''public static boolean startsWith(final CharSequence str, final CharSequence prefix)
    '''
def startsWithIgnoreCase():
    '''public static boolean startsWithIgnoreCase(final CharSequence str, final CharSequence prefix)
    '''
def startsWithAny():
    '''public static boolean startsWithAny(final CharSequence string, final CharSequence... searchStrings)
    '''
def endsWith():
    '''public static boolean endsWith(final CharSequence str, final CharSequence suffix)
    '''
def endsWithIgnoreCase():
    '''public static boolean endsWithIgnoreCase(final CharSequence str, final CharSequence suffix)
    '''
def normalizeSpace():
    '''public static String normalizeSpace(final String str)
    '''
def endsWithAny():
    '''public static boolean endsWithAny(final CharSequence string, final CharSequence... searchStrings)
    '''
def appendIfMissing():
    '''public static String appendIfMissing(final String str, final CharSequence suffix, final CharSequence... suffixes)
    '''
def appendIfMissingIgnoreCase():
    '''public static String appendIfMissingIgnoreCase(final String str, final CharSequence suffix, final CharSequence... suffixes)
    '''
def prependIfMissing():
    '''public static String prependIfMissing(final String str, final CharSequence prefix, final CharSequence... prefixes)
    '''
def prependIfMissingIgnoreCase():
    '''public static String prependIfMissingIgnoreCase(final String str, final CharSequence prefix, final CharSequence... prefixes)
    '''
def toString():
    '''public static String toString(final byte[] bytes, final String charsetName)
    '''
def toEncodedString():
    '''public static String toEncodedString(final byte[] bytes, final Charset charset)
    '''
def wrap():
    '''public static String wrap(final String str, final char wrapWith)
    public static String wrap(final String str, final String wrapWith)
    '''
