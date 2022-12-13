def throwIfInstanceOf():
'''public static <X extends Throwable> void throwIfInstanceOf(final Throwable throwable, final Class<X> declaredType)
'''
pass
def propagateIfInstanceOf():
'''public static <X extends Throwable> void propagateIfInstanceOf(@Nullable final Throwable throwable, final Class<X> declaredType)
'''
pass
def throwIfUnchecked():
'''public static void throwIfUnchecked(final Throwable throwable)
'''
pass
def propagateIfPossible():
'''public static void propagateIfPossible(@Nullable final Throwable throwable)
public static <X extends Throwable> void propagateIfPossible(@Nullable final Throwable throwable, final Class<X> declaredType)
public static <X1 extends Throwable, X2 extends Throwable> void propagateIfPossible(@Nullable final Throwable throwable, final Class<X1> declaredType1, final Class<X2> declaredType2)
'''
pass
def propagate():
'''public static RuntimeException propagate(final Throwable throwable)
'''
pass
def getRootCause():
'''public static Throwable getRootCause(Throwable throwable)
'''
pass
def getCausalChain():
'''public static List<Throwable> getCausalChain(Throwable throwable)
'''
pass
def getStackTraceAsString():
'''public static String getStackTraceAsString(final Throwable throwable)
'''
pass
def lazyStackTrace():
'''public static List<StackTraceElement> lazyStackTrace(final Throwable throwable)
'''
pass
def lazyStackTraceIsLazy():
'''public static boolean lazyStackTraceIsLazy()
'''
pass
def get():
'''public StackTraceElement get(final int n)
'''
pass
def size():
'''public int size()
'''
pass
