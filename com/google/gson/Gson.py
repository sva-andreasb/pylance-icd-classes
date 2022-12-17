def ():
    '''returns Gson\n\n
    ()\n
    '''
def serialize():
    '''returns JsonElement\n\n
    serialize(final Object src)\n
    serialize(final Object src, final Type typeOfSrc)\n
    '''
def read():
    '''returns T\n\n
    read(final JsonReader in)\n
    read(final JsonReader in)\n
    read(final JsonReader in)\n
    read(final JsonReader in)\n
    '''
def write():
    '''returns None\n\n
    write(final JsonWriter out, final Number value)\n
    write(final JsonWriter out, final Number value)\n
    write(final JsonWriter out, final Number value)\n
    write(final JsonWriter out, final T value)\n
    '''
def toJsonTree():
    '''returns JsonElement\n\n
    toJsonTree(final Object src)\n
    toJsonTree(final Object src, final Type typeOfSrc)\n
    '''
def toJson():
    '''returns None\n\n
    toJson(final Object src)\n
    toJson(final Object src, final Type typeOfSrc)\n
    toJson(final Object src, final Appendable writer)\n
    toJson(final Object src, final Type typeOfSrc, final Appendable writer)\n
    toJson(final Object src, final Type typeOfSrc, final JsonWriter writer)\n
    toJson(final JsonElement jsonElement)\n
    toJson(final JsonElement jsonElement, final Appendable writer)\n
    toJson(final JsonElement jsonElement, final JsonWriter writer)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def setDelegate():
    '''returns None\n\n
    setDelegate(final TypeAdapter<T> typeAdapter)\n
    '''
