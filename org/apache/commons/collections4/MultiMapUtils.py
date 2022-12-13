def emptyMultiValuedMap():
    '''public static <K, V> MultiValuedMap<K, V> emptyMultiValuedMap()
    '''
def emptyIfNull():
    '''public static <K, V> MultiValuedMap<K, V> emptyIfNull(final MultiValuedMap<K, V> map)
    '''
def isEmpty():
    '''public static boolean isEmpty(final MultiValuedMap<?, ?> map)
    '''
def getCollection():
    '''public static <K, V> Collection<V> getCollection(final MultiValuedMap<K, V> map, final K key)
    '''
def getValuesAsList():
    '''public static <K, V> List<V> getValuesAsList(final MultiValuedMap<K, V> map, final K key)
    '''
def getValuesAsSet():
    '''public static <K, V> Set<V> getValuesAsSet(final MultiValuedMap<K, V> map, final K key)
    '''
def getValuesAsBag():
    '''public static <K, V> Bag<V> getValuesAsBag(final MultiValuedMap<K, V> map, final K key)
    '''
def newListValuedHashMap():
    '''public static <K, V> ListValuedMap<K, V> newListValuedHashMap()
    '''
def newSetValuedHashMap():
    '''public static <K, V> SetValuedMap<K, V> newSetValuedHashMap()
    '''
def unmodifiableMultiValuedMap():
    '''public static <K, V> MultiValuedMap<K, V> unmodifiableMultiValuedMap(final MultiValuedMap<? extends K, ? extends V> map)
    '''
def transformedMultiValuedMap():
    '''public static <K, V> MultiValuedMap<K, V> transformedMultiValuedMap(final MultiValuedMap<K, V> map, final Transformer<? super K, ? extends K> keyTransformer, final Transformer<? super V, ? extends V> valueTransformer)
    '''
