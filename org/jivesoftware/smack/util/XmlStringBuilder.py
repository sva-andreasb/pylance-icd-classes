def XmlStringBuilder():
'''public XmlStringBuilder()
public XmlStringBuilder(final String enclosingNamespace)
public XmlStringBuilder(final ExtensionElement pe)
public XmlStringBuilder(final NamedElement e)
public XmlStringBuilder(final ExtensionElement ee, final String enclosingNamespace)
'''
pass
def escapedElement():
'''public XmlStringBuilder escapedElement(final String name, final String escapedContent)
'''
pass
def element():
'''public XmlStringBuilder element(final String name, final String content)
public XmlStringBuilder element(final String name, final Date content)
public XmlStringBuilder element(final String name, final CharSequence content)
public XmlStringBuilder element(final String name, final Enum<?> content)
public XmlStringBuilder element(final Element element)
'''
pass
def optElement():
'''public XmlStringBuilder optElement(final String name, final String content)
public XmlStringBuilder optElement(final String name, final Date content)
public XmlStringBuilder optElement(final String name, final CharSequence content)
public XmlStringBuilder optElement(final Element element)
public XmlStringBuilder optElement(final String name, final Enum<?> content)
public XmlStringBuilder optElement(final String name, final Object object)
'''
pass
def optIntElement():
'''public XmlStringBuilder optIntElement(final String name, final int value)
'''
pass
def halfOpenElement():
'''public XmlStringBuilder halfOpenElement(final String name)
public XmlStringBuilder halfOpenElement(final NamedElement namedElement)
'''
pass
def openElement():
'''public XmlStringBuilder openElement(final String name)
'''
pass
def closeElement():
'''public XmlStringBuilder closeElement(final String name)
public XmlStringBuilder closeElement(final NamedElement e)
'''
pass
def closeEmptyElement():
'''public XmlStringBuilder closeEmptyElement()
'''
pass
def rightAngleBracket():
'''public XmlStringBuilder rightAngleBracket()
'''
pass
def rightAngelBracket():
'''public XmlStringBuilder rightAngelBracket()
'''
pass
def attribute():
'''public XmlStringBuilder attribute(final String name, final String value)
public XmlStringBuilder attribute(final String name, final boolean bool)
public XmlStringBuilder attribute(final String name, final Date value)
public XmlStringBuilder attribute(final String name, final CharSequence value)
public XmlStringBuilder attribute(final String name, final Enum<?> value)
public XmlStringBuilder attribute(final String name, final int value)
'''
pass
def optAttribute():
'''public XmlStringBuilder optAttribute(final String name, final String value)
public XmlStringBuilder optAttribute(final String name, final Date value)
public XmlStringBuilder optAttribute(final String name, final CharSequence value)
public XmlStringBuilder optAttribute(final String name, final Enum<?> value)
'''
pass
def optIntAttribute():
'''public XmlStringBuilder optIntAttribute(final String name, final int value)
'''
pass
def optLongAttribute():
'''public XmlStringBuilder optLongAttribute(final String name, final Long value)
'''
pass
def optBooleanAttribute():
'''public XmlStringBuilder optBooleanAttribute(final String name, final boolean bool)
'''
pass
def optBooleanAttributeDefaultTrue():
'''public XmlStringBuilder optBooleanAttributeDefaultTrue(final String name, final boolean bool)
'''
pass
def xmlnsAttribute():
'''public XmlStringBuilder xmlnsAttribute(final String value)
'''
pass
def xmllangAttribute():
'''public XmlStringBuilder xmllangAttribute(final String value)
'''
pass
def optXmlLangAttribute():
'''public XmlStringBuilder optXmlLangAttribute(final String lang)
'''
pass
def escape():
'''public XmlStringBuilder escape(final String text)
public XmlStringBuilder escape(final CharSequence text)
'''
pass
def escapeAttributeValue():
'''public XmlStringBuilder escapeAttributeValue(final String value)
'''
pass
def optEscape():
'''public XmlStringBuilder optEscape(final CharSequence text)
'''
pass
def prelude():
'''public XmlStringBuilder prelude(final ExtensionElement pe)
public XmlStringBuilder prelude(final String elementName, final String namespace)
'''
pass
def optAppend():
'''public XmlStringBuilder optAppend(final CharSequence csq)
public XmlStringBuilder optAppend(final Element element)
'''
pass
def append():
'''public XmlStringBuilder append(final XmlStringBuilder xsb)
public XmlStringBuilder append(final Collection<? extends Element> elements)
public XmlStringBuilder append(final Collection<? extends Element> elements, final String enclosingNamespace)
public XmlStringBuilder append(final CharSequence csq)
public XmlStringBuilder append(final CharSequence csq, final int start, final int end)
public XmlStringBuilder append(final char c)
'''
pass
def emptyElement():
'''public XmlStringBuilder emptyElement(final Enum<?> element)
public XmlStringBuilder emptyElement(final String element)
'''
pass
def condEmptyElement():
'''public XmlStringBuilder condEmptyElement(final boolean condition, final String element)
'''
pass
def condAttribute():
'''public XmlStringBuilder condAttribute(final boolean condition, final String name, final String value)
'''
pass
def length():
'''public int length()
public int length()
'''
pass
def charAt():
'''public char charAt(final int index)
public char charAt(final int index)
'''
pass
def subSequence():
'''public CharSequence subSequence(final int start, final int end)
public CharSequence subSequence(final int start, final int end)
'''
pass
def toString():
'''public String toString()
public String toString()
'''
pass
def equals():
'''public boolean equals(final Object other)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def write():
'''public void write(final Writer writer, String enclosingNamespace)
'''
pass
def toXML():
'''public CharSequence toXML(final String enclosingNamespace)
'''
pass
