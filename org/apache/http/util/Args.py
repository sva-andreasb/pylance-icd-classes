def check():
'''public static void check(final boolean expression, final String message)
public static void check(final boolean expression, final String message, final Object... args)
public static void check(final boolean expression, final String message, final Object arg)
'''
pass
def notNull():
'''public static <T> T notNull(final T argument, final String name)
'''
pass
def notEmpty():
'''public static <T extends CharSequence> T notEmpty(final T argument, final String name)
public static <E, T extends Collection<E>> T notEmpty(final T argument, final String name)
'''
pass
def notBlank():
'''public static <T extends CharSequence> T notBlank(final T argument, final String name)
'''
pass
def containsNoBlanks():
'''public static <T extends CharSequence> T containsNoBlanks(final T argument, final String name)
'''
pass
def positive():
'''public static int positive(final int n, final String name)
public static long positive(final long n, final String name)
'''
pass
def notNegative():
'''public static int notNegative(final int n, final String name)
public static long notNegative(final long n, final String name)
'''
pass