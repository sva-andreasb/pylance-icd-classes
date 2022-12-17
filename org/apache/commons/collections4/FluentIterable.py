def append():
    '''returns FluentIterable<E>\n\n
    append(final E... elements)\n
    append(final Iterable<? extends E> other)\n
    '''
def collate():
    '''returns FluentIterable<E>\n\n
    collate(final Iterable<? extends E> other)\n
    collate(final Iterable<? extends E> other, final Comparator<? super E> comparator)\n
    '''
def eval():
    '''returns FluentIterable<E>\n\n
    eval()\n
    '''
def filter():
    '''returns FluentIterable<E>\n\n
    filter(final Predicate<? super E> predicate)\n
    '''
def limit():
    '''returns FluentIterable<E>\n\n
    limit(final long maxSize)\n
    '''
def loop():
    '''returns FluentIterable<E>\n\n
    loop()\n
    '''
def reverse():
    '''returns FluentIterable<E>\n\n
    reverse()\n
    '''
def skip():
    '''returns FluentIterable<E>\n\n
    skip(final long elementsToSkip)\n
    '''
def unique():
    '''returns FluentIterable<E>\n\n
    unique()\n
    '''
def unmodifiable():
    '''returns FluentIterable<E>\n\n
    unmodifiable()\n
    '''
def zip():
    '''returns FluentIterable<E>\n\n
    zip(final Iterable<? extends E> other)\n
    zip(final Iterable<? extends E>... others)\n
    '''
def iterator():
    '''returns Iterator<E>\n\n
    iterator()\n
    '''
def asEnumeration():
    '''returns Enumeration<E>\n\n
    asEnumeration()\n
    '''
def allMatch():
    '''returns boolean\n\n
    allMatch(final Predicate<? super E> predicate)\n
    '''
def anyMatch():
    '''returns boolean\n\n
    anyMatch(final Predicate<? super E> predicate)\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final Object object)\n
    '''
def forEach():
    '''returns None\n\n
    forEach(final Closure<? super E> closure)\n
    '''
def get():
    '''returns E\n\n
    get(final int position)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def copyInto():
    '''returns None\n\n
    copyInto(final Collection<? super E> collection)\n
    '''
def toArray():
    '''returns E[]\n\n
    toArray(final Class<E> arrayClass)\n
    '''
def toList():
    '''returns List<E>\n\n
    toList()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
