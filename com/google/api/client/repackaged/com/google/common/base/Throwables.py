def throwIfInstanceOf():
    '''    public static <X extends Throwable> void throwIfInstanceOf(final Throwable throwable, final Class<X> declaredType)
    '''
def propagateIfInstanceOf():
    '''    public static <X extends Throwable> void propagateIfInstanceOf(@Nullable final Throwable throwable, final Class<X> declaredType)
    '''
def throwIfUnchecked():
    '''    public static void throwIfUnchecked(final Throwable throwable)
    '''
def propagateIfPossible():
    '''    public static void propagateIfPossible(@Nullable final Throwable throwable)
    public static <X extends Throwable> void propagateIfPossible(@Nullable final Throwable throwable, final Class<X> declaredType)
    public static <X1 extends Throwable, X2 extends Throwable> void propagateIfPossible(@Nullable final Throwable throwable, final Class<X1> declaredType1, final Class<X2> declaredType2)
    '''
def propagate():
    '''    public static RuntimeException propagate(final Throwable throwable)
    '''
def getRootCause():
    '''    public static Throwable getRootCause(Throwable throwable)
    '''
def getCausalChain():
    '''    public static List<Throwable> getCausalChain(Throwable throwable)
    '''
def getStackTraceAsString():
    '''    public static String getStackTraceAsString(final Throwable throwable)
    '''
def lazyStackTrace():
    '''    public static List<StackTraceElement> lazyStackTrace(final Throwable throwable)
    '''
def lazyStackTraceIsLazy():
    '''    public static boolean lazyStackTraceIsLazy()
    '''
def get():
    '''    public StackTraceElement get(final int n)
    '''
def size():
    '''    public int size()
    '''
