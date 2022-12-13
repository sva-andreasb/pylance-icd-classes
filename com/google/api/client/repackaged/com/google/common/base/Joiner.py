def on():
    '''    public static Joiner on(final String separator)
    public static Joiner on(final char separator)
    '''
def appendTo():
    '''    public <A extends Appendable> A appendTo(final A appendable, final Iterable<?> parts)
    public <A extends Appendable> A appendTo(final A appendable, final Iterator<?> parts)
    public final <A extends Appendable> A appendTo(final A appendable, final Object[] parts)
    public final <A extends Appendable> A appendTo(final A appendable, @Nullable final Object first, @Nullable final Object second, final Object... rest)
    public final StringBuilder appendTo(final StringBuilder builder, final Iterable<?> parts)
    public final StringBuilder appendTo(final StringBuilder builder, final Iterator<?> parts)
    public final StringBuilder appendTo(final StringBuilder builder, final Object[] parts)
    public final StringBuilder appendTo(final StringBuilder builder, @Nullable final Object first, @Nullable final Object second, final Object... rest)
    public <A extends Appendable> A appendTo(final A appendable, final Iterator<?> parts)
    public <A extends Appendable> A appendTo(final A appendable, final Map<?, ?> map)
    public StringBuilder appendTo(final StringBuilder builder, final Map<?, ?> map)
    public <A extends Appendable> A appendTo(final A appendable, final Iterable<? extends Map.Entry<?, ?>> entries)
    public <A extends Appendable> A appendTo(final A appendable, final Iterator<? extends Map.Entry<?, ?>> parts)
    public StringBuilder appendTo(final StringBuilder builder, final Iterable<? extends Map.Entry<?, ?>> entries)
    public StringBuilder appendTo(final StringBuilder builder, final Iterator<? extends Map.Entry<?, ?>> entries)
    '''
def join():
    '''    public final String join(final Iterable<?> parts)
    public final String join(final Iterator<?> parts)
    public final String join(final Object[] parts)
    public final String join(@Nullable final Object first, @Nullable final Object second, final Object... rest)
    public String join(final Map<?, ?> map)
    public String join(final Iterable<? extends Map.Entry<?, ?>> entries)
    public String join(final Iterator<? extends Map.Entry<?, ?>> entries)
    '''
def useForNull():
    '''    public Joiner useForNull(final String nullText)
    public Joiner useForNull(final String nullText)
    public Joiner useForNull(final String nullText)
    public MapJoiner useForNull(final String nullText)
    '''
def skipNulls():
    '''    public Joiner skipNulls()
    public Joiner skipNulls()
    '''
def withKeyValueSeparator():
    '''    public MapJoiner withKeyValueSeparator(final String kvs)
    public MapJoiner withKeyValueSeparator(final char keyValueSeparator)
    public MapJoiner withKeyValueSeparator(final String keyValueSeparator)
    '''
def size():
    '''    public int size()
    '''
def get():
    '''    public Object get(final int index)
    '''
