def convert():
    '''    public final B convert(@Nullable final A a)
    '''
def convertAll():
    '''    public Iterable<B> convertAll(final Iterable<? extends A> fromIterable)
    '''
def iterator():
    '''    public Iterator<B> iterator()
    '''
def hasNext():
    '''    public boolean hasNext()
    '''
def next():
    '''    public B next()
    '''
def remove():
    '''    public void remove()
    '''
def reverse():
    '''    public Converter<B, A> reverse()
    public Converter<A, B> reverse()
    public IdentityConverter<T> reverse()
    '''
def andThen():
    '''    public final <C> Converter<A, C> andThen(final Converter<B, C> secondConverter)
    '''
def apply():
    '''    public final B apply(@Nullable final A a)
    '''
def equals():
    '''    public boolean equals(@Nullable final Object object)
    public boolean equals(@Nullable final Object object)
    public boolean equals(@Nullable final Object object)
    public boolean equals(@Nullable final Object object)
    '''
def from():
    '''    public static <A, B> Converter<A, B> from(final Function<? super A, ? extends B> forwardFunction, final Function<? super B, ? extends A> backwardFunction)
    '''
def identity():
    '''    public static <T> Converter<T, T> identity()
    '''
def hashCode():
    '''    public int hashCode()
    public int hashCode()
    public int hashCode()
    '''
def toString():
    '''    public String toString()
    public String toString()
    public String toString()
    public String toString()
    '''
