def Gson():
'''public Gson()
'''
pass
def deserialize():
'''public <T> T deserialize(final JsonElement json, final Type typeOfT)
'''
pass
def serialize():
'''public JsonElement serialize(final Object src)
public JsonElement serialize(final Object src, final Type typeOfSrc)
'''
pass
def read():
'''public Double read(final JsonReader in)
public Float read(final JsonReader in)
public Number read(final JsonReader in)
public T read(final JsonReader in)
'''
pass
def write():
'''public void write(final JsonWriter out, final Number value)
public void write(final JsonWriter out, final Number value)
public void write(final JsonWriter out, final Number value)
public void write(final JsonWriter out, final T value)
'''
pass
def getAdapter():
'''public <T> TypeAdapter<T> getAdapter(final TypeToken<T> type)
public <T> TypeAdapter<T> getAdapter(final Class<T> type)
'''
pass
def getDelegateAdapter():
'''public <T> TypeAdapter<T> getDelegateAdapter(final TypeAdapterFactory skipPast, final TypeToken<T> type)
'''
pass
def toJsonTree():
'''public JsonElement toJsonTree(final Object src)
public JsonElement toJsonTree(final Object src, final Type typeOfSrc)
'''
pass
def toJson():
'''public String toJson(final Object src)
public String toJson(final Object src, final Type typeOfSrc)
public void toJson(final Object src, final Appendable writer)
public void toJson(final Object src, final Type typeOfSrc, final Appendable writer)
public void toJson(final Object src, final Type typeOfSrc, final JsonWriter writer)
public String toJson(final JsonElement jsonElement)
public void toJson(final JsonElement jsonElement, final Appendable writer)
public void toJson(final JsonElement jsonElement, final JsonWriter writer)
'''
pass
def fromJson():
'''public <T> T fromJson(final String json, final Class<T> classOfT)
public <T> T fromJson(final String json, final Type typeOfT)
public <T> T fromJson(final Reader json, final Class<T> classOfT)
public <T> T fromJson(final Reader json, final Type typeOfT)
public <T> T fromJson(final JsonReader reader, final Type typeOfT)
public <T> T fromJson(final JsonElement json, final Class<T> classOfT)
public <T> T fromJson(final JsonElement json, final Type typeOfT)
'''
pass
def toString():
'''public String toString()
'''
pass
def setDelegate():
'''public void setDelegate(final TypeAdapter<T> typeAdapter)
'''
pass
