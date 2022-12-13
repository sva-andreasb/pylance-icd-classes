def transformingMap():
    '''    public static <K, V> TransformedMultiValuedMap<K, V> transformingMap(final MultiValuedMap<K, V> map, final Transformer<? super K, ? extends K> keyTransformer, final Transformer<? super V, ? extends V> valueTransformer)
    '''
def transformedMap():
    '''    public static <K, V> TransformedMultiValuedMap<K, V> transformedMap(final MultiValuedMap<K, V> map, final Transformer<? super K, ? extends K> keyTransformer, final Transformer<? super V, ? extends V> valueTransformer)
    '''
def put():
    '''    public boolean put(final K key, final V value)
    '''
def putAll():
    '''    public boolean putAll(final K key, final Iterable<? extends V> values)
    public boolean putAll(final Map<? extends K, ? extends V> map)
    public boolean putAll(final MultiValuedMap<? extends K, ? extends V> map)
    '''
