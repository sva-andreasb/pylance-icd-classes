def StructuredDataMessage():
'''public StructuredDataMessage(final String id, final String msg, final String type)
public StructuredDataMessage(final String id, final String msg, final String type, final int maxLength)
public StructuredDataMessage(final String id, final String msg, final String type, final Map<String, String> data)
public StructuredDataMessage(final String id, final String msg, final String type, final Map<String, String> data, final int maxLength)
public StructuredDataMessage(final StructuredDataId id, final String msg, final String type)
public StructuredDataMessage(final StructuredDataId id, final String msg, final String type, final int maxLength)
public StructuredDataMessage(final StructuredDataId id, final String msg, final String type, final Map<String, String> data)
public StructuredDataMessage(final StructuredDataId id, final String msg, final String type, final Map<String, String> data, final int maxLength)
'''
pass
def getFormats():
'''public String[] getFormats()
'''
pass
def getId():
'''public StructuredDataId getId()
'''
pass
def getType():
'''public String getType()
'''
pass
def formatTo():
'''public void formatTo(final StringBuilder buffer)
public void formatTo(final String[] formats, final StringBuilder buffer)
'''
pass
def getFormat():
'''public String getFormat()
'''
pass
def asString():
'''public String asString()
public String asString(final String format)
public final String asString(final Format format, final StructuredDataId structuredDataId)
public final void asString(final Format format, final StructuredDataId structuredDataId, final StringBuilder sb)
'''
pass
def getFormattedMessage():
'''public String getFormattedMessage()
public String getFormattedMessage(final String[] formats)
'''
pass
def toString():
'''public String toString()
'''
pass
def newInstance():
'''public StructuredDataMessage newInstance(final Map<String, String> map)
'''
pass
def equals():
'''public boolean equals(final Object o)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
