def convert():
'''public final B convert(@Nullable final A a)
'''
pass
def convertAll():
'''public Iterable<B> convertAll(final Iterable<? extends A> fromIterable)
'''
pass
def iterator():
'''public Iterator<B> iterator()
'''
pass
def hasNext():
'''public boolean hasNext()
'''
pass
def next():
'''public B next()
'''
pass
def remove():
'''public void remove()
'''
pass
def reverse():
'''public Converter<B, A> reverse()
public Converter<A, B> reverse()
public IdentityConverter<T> reverse()
'''
pass
def andThen():
'''public final <C> Converter<A, C> andThen(final Converter<B, C> secondConverter)
'''
pass
def apply():
'''public final B apply(@Nullable final A a)
'''
pass
def equals():
'''public boolean equals(@Nullable final Object object)
public boolean equals(@Nullable final Object object)
public boolean equals(@Nullable final Object object)
public boolean equals(@Nullable final Object object)
'''
pass
def from():
'''public static <A, B> Converter<A, B> from(final Function<? super A, ? extends B> forwardFunction, final Function<? super B, ? extends A> backwardFunction)
'''
pass
def identity():
'''public static <T> Converter<T, T> identity()
'''
pass
def hashCode():
'''public int hashCode()
public int hashCode()
public int hashCode()
'''
pass
def toString():
'''public String toString()
public String toString()
public String toString()
public String toString()
'''
pass
