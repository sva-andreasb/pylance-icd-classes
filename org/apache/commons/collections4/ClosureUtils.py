def exceptionClosure():
'''public static <E> Closure<E> exceptionClosure()
'''
pass
def nopClosure():
'''public static <E> Closure<E> nopClosure()
'''
pass
def asClosure():
'''public static <E> Closure<E> asClosure(final Transformer<? super E, ?> transformer)
'''
pass
def forClosure():
'''public static <E> Closure<E> forClosure(final int count, final Closure<? super E> closure)
'''
pass
def whileClosure():
'''public static <E> Closure<E> whileClosure(final Predicate<? super E> predicate, final Closure<? super E> closure)
'''
pass
def doWhileClosure():
'''public static <E> Closure<E> doWhileClosure(final Closure<? super E> closure, final Predicate<? super E> predicate)
'''
pass
def invokerClosure():
'''public static <E> Closure<E> invokerClosure(final String methodName)
public static <E> Closure<E> invokerClosure(final String methodName, final Class<?>[] paramTypes, final Object[] args)
'''
pass
def chainedClosure():
'''public static <E> Closure<E> chainedClosure(final Closure<? super E>... closures)
public static <E> Closure<E> chainedClosure(final Collection<? extends Closure<? super E>> closures)
'''
pass
def ifClosure():
'''public static <E> Closure<E> ifClosure(final Predicate<? super E> predicate, final Closure<? super E> trueClosure)
public static <E> Closure<E> ifClosure(final Predicate<? super E> predicate, final Closure<? super E> trueClosure, final Closure<? super E> falseClosure)
'''
pass
def switchClosure():
'''public static <E> Closure<E> switchClosure(final Predicate<? super E>[] predicates, final Closure<? super E>[] closures)
public static <E> Closure<E> switchClosure(final Predicate<? super E>[] predicates, final Closure<? super E>[] closures, final Closure<? super E> defaultClosure)
public static <E> Closure<E> switchClosure(final Map<Predicate<E>, Closure<E>> predicatesAndClosures)
'''
pass
def switchMapClosure():
'''public static <E> Closure<E> switchMapClosure(final Map<? extends E, Closure<E>> objectsAndClosures)
'''
pass
