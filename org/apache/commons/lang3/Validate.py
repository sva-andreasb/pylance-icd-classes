def isTrue():
    '''    public static void isTrue(final boolean expression, final String message, final long value)
    public static void isTrue(final boolean expression, final String message, final double value)
    public static void isTrue(final boolean expression, final String message, final Object... values)
    public static void isTrue(final boolean expression)
    '''
def notNull():
    '''    public static <T> T notNull(final T object)
    public static <T> T notNull(final T object, final String message, final Object... values)
    '''
def notEmpty():
    '''    public static <T> T[] notEmpty(final T[] array, final String message, final Object... values)
    public static <T> T[] notEmpty(final T[] array)
    public static <T extends CharSequence> T notEmpty(final T chars, final String message, final Object... values)
    public static <T extends CharSequence> T notEmpty(final T chars)
    '''
def notBlank():
    '''    public static <T extends CharSequence> T notBlank(final T chars, final String message, final Object... values)
    public static <T extends CharSequence> T notBlank(final T chars)
    '''
def noNullElements():
    '''    public static <T> T[] noNullElements(final T[] array, final String message, final Object... values)
    public static <T> T[] noNullElements(final T[] array)
    '''
def validIndex():
    '''    public static <T> T[] validIndex(final T[] array, final int index, final String message, final Object... values)
    public static <T> T[] validIndex(final T[] array, final int index)
    public static <T extends CharSequence> T validIndex(final T chars, final int index, final String message, final Object... values)
    public static <T extends CharSequence> T validIndex(final T chars, final int index)
    '''
def validState():
    '''    public static void validState(final boolean expression)
    public static void validState(final boolean expression, final String message, final Object... values)
    '''
def matchesPattern():
    '''    public static void matchesPattern(final CharSequence input, final String pattern)
    public static void matchesPattern(final CharSequence input, final String pattern, final String message, final Object... values)
    '''
def inclusiveBetween():
    '''    public static <T> void inclusiveBetween(final T start, final T end, final Comparable<T> value)
    public static <T> void inclusiveBetween(final T start, final T end, final Comparable<T> value, final String message, final Object... values)
    public static void inclusiveBetween(final long start, final long end, final long value)
    public static void inclusiveBetween(final long start, final long end, final long value, final String message)
    public static void inclusiveBetween(final double start, final double end, final double value)
    public static void inclusiveBetween(final double start, final double end, final double value, final String message)
    '''
def exclusiveBetween():
    '''    public static <T> void exclusiveBetween(final T start, final T end, final Comparable<T> value)
    public static <T> void exclusiveBetween(final T start, final T end, final Comparable<T> value, final String message, final Object... values)
    public static void exclusiveBetween(final long start, final long end, final long value)
    public static void exclusiveBetween(final long start, final long end, final long value, final String message)
    public static void exclusiveBetween(final double start, final double end, final double value)
    public static void exclusiveBetween(final double start, final double end, final double value, final String message)
    '''
def isInstanceOf():
    '''    public static void isInstanceOf(final Class<?> type, final Object obj)
    public static void isInstanceOf(final Class<?> type, final Object obj, final String message, final Object... values)
    '''
def isAssignableFrom():
    '''    public static void isAssignableFrom(final Class<?> superType, final Class<?> type)
    public static void isAssignableFrom(final Class<?> superType, final Class<?> type, final String message, final Object... values)
    '''
