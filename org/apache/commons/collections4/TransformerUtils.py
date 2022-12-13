def exceptionTransformer():
    '''public static <I, O> Transformer<I, O> exceptionTransformer()
    '''
def nullTransformer():
    '''public static <I, O> Transformer<I, O> nullTransformer()
    '''
def nopTransformer():
    '''public static <T> Transformer<T, T> nopTransformer()
    '''
def cloneTransformer():
    '''public static <T> Transformer<T, T> cloneTransformer()
    '''
def constantTransformer():
    '''public static <I, O> Transformer<I, O> constantTransformer(final O constantToReturn)
    '''
def asTransformer():
    '''public static <T> Transformer<T, T> asTransformer(final Closure<? super T> closure)
    public static <T> Transformer<T, Boolean> asTransformer(final Predicate<? super T> predicate)
    public static <I, O> Transformer<I, O> asTransformer(final Factory<? extends O> factory)
    '''
def chainedTransformer():
    '''public static <T> Transformer<T, T> chainedTransformer(final Transformer<? super T, ? extends T>... transformers)
    public static <T> Transformer<T, T> chainedTransformer(final Collection<? extends Transformer<? super T, ? extends T>> transformers)
    '''
def ifTransformer():
    '''public static <T> Transformer<T, T> ifTransformer(final Predicate<? super T> predicate, final Transformer<? super T, ? extends T> trueTransformer)
    public static <I, O> Transformer<I, O> ifTransformer(final Predicate<? super I> predicate, final Transformer<? super I, ? extends O> trueTransformer, final Transformer<? super I, ? extends O> falseTransformer)
    '''
def switchTransformer():
    '''public static <I, O> Transformer<I, O> switchTransformer(final Predicate<? super I> predicate, final Transformer<? super I, ? extends O> trueTransformer, final Transformer<? super I, ? extends O> falseTransformer)
    public static <I, O> Transformer<I, O> switchTransformer(final Predicate<? super I>[] predicates, final Transformer<? super I, ? extends O>[] transformers)
    public static <I, O> Transformer<I, O> switchTransformer(final Predicate<? super I>[] predicates, final Transformer<? super I, ? extends O>[] transformers, final Transformer<? super I, ? extends O> defaultTransformer)
    public static <I, O> Transformer<I, O> switchTransformer(final Map<Predicate<I>, Transformer<I, O>> predicatesAndTransformers)
    '''
def switchMapTransformer():
    '''public static <I, O> Transformer<I, O> switchMapTransformer(final Map<I, Transformer<I, O>> objectsAndTransformers)
    '''
def mapTransformer():
    '''public static <I, O> Transformer<I, O> mapTransformer(final Map<? super I, ? extends O> map)
    '''
def invokerTransformer():
    '''public static <I, O> Transformer<I, O> invokerTransformer(final String methodName)
    public static <I, O> Transformer<I, O> invokerTransformer(final String methodName, final Class<?>[] paramTypes, final Object[] args)
    '''
def stringValueTransformer():
    '''public static <T> Transformer<T, String> stringValueTransformer()
    '''
