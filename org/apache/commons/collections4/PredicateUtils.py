def exceptionPredicate():
    '''    public static <T> Predicate<T> exceptionPredicate()
    '''
def truePredicate():
    '''    public static <T> Predicate<T> truePredicate()
    '''
def falsePredicate():
    '''    public static <T> Predicate<T> falsePredicate()
    '''
def nullPredicate():
    '''    public static <T> Predicate<T> nullPredicate()
    '''
def notNullPredicate():
    '''    public static <T> Predicate<T> notNullPredicate()
    '''
def equalPredicate():
    '''    public static <T> Predicate<T> equalPredicate(final T value)
    '''
def identityPredicate():
    '''    public static <T> Predicate<T> identityPredicate(final T value)
    '''
def instanceofPredicate():
    '''    public static Predicate<Object> instanceofPredicate(final Class<?> type)
    '''
def uniquePredicate():
    '''    public static <T> Predicate<T> uniquePredicate()
    '''
def invokerPredicate():
    '''    public static <T> Predicate<T> invokerPredicate(final String methodName)
    public static <T> Predicate<T> invokerPredicate(final String methodName, final Class<?>[] paramTypes, final Object[] args)
    '''
def andPredicate():
    '''    public static <T> Predicate<T> andPredicate(final Predicate<? super T> predicate1, final Predicate<? super T> predicate2)
    '''
def allPredicate():
    '''    public static <T> Predicate<T> allPredicate(final Predicate<? super T>... predicates)
    public static <T> Predicate<T> allPredicate(final Collection<? extends Predicate<? super T>> predicates)
    '''
def orPredicate():
    '''    public static <T> Predicate<T> orPredicate(final Predicate<? super T> predicate1, final Predicate<? super T> predicate2)
    '''
def anyPredicate():
    '''    public static <T> Predicate<T> anyPredicate(final Predicate<? super T>... predicates)
    public static <T> Predicate<T> anyPredicate(final Collection<? extends Predicate<? super T>> predicates)
    '''
def eitherPredicate():
    '''    public static <T> Predicate<T> eitherPredicate(final Predicate<? super T> predicate1, final Predicate<? super T> predicate2)
    '''
def onePredicate():
    '''    public static <T> Predicate<T> onePredicate(final Predicate<? super T>... predicates)
    public static <T> Predicate<T> onePredicate(final Collection<? extends Predicate<? super T>> predicates)
    '''
def neitherPredicate():
    '''    public static <T> Predicate<T> neitherPredicate(final Predicate<? super T> predicate1, final Predicate<? super T> predicate2)
    '''
def nonePredicate():
    '''    public static <T> Predicate<T> nonePredicate(final Predicate<? super T>... predicates)
    public static <T> Predicate<T> nonePredicate(final Collection<? extends Predicate<? super T>> predicates)
    '''
def notPredicate():
    '''    public static <T> Predicate<T> notPredicate(final Predicate<? super T> predicate)
    '''
def asPredicate():
    '''    public static <T> Predicate<T> asPredicate(final Transformer<? super T, Boolean> transformer)
    '''
def nullIsExceptionPredicate():
    '''    public static <T> Predicate<T> nullIsExceptionPredicate(final Predicate<? super T> predicate)
    '''
def nullIsFalsePredicate():
    '''    public static <T> Predicate<T> nullIsFalsePredicate(final Predicate<? super T> predicate)
    '''
def nullIsTruePredicate():
    '''    public static <T> Predicate<T> nullIsTruePredicate(final Predicate<? super T> predicate)
    '''
def transformedPredicate():
    '''    public static <T> Predicate<T> transformedPredicate(final Transformer<? super T, ? extends T> transformer, final Predicate<? super T> predicate)
    '''
