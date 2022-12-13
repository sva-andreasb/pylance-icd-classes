def XmlStringBuilder():
    '''public XmlStringBuilder()
    public XmlStringBuilder(final String enclosingNamespace)
    public XmlStringBuilder(final ExtensionElement pe)
    public XmlStringBuilder(final NamedElement e)
    public XmlStringBuilder(final ExtensionElement ee, final String enclosingNamespace)
    '''
def escapedElement():
    '''public XmlStringBuilder escapedElement(final String name, final String escapedContent)
    '''
def element():
    '''public XmlStringBuilder element(final String name, final String content)
    public XmlStringBuilder element(final String name, final Date content)
    public XmlStringBuilder element(final String name, final CharSequence content)
    public XmlStringBuilder element(final String name, final Enum<?> content)
    public XmlStringBuilder element(final Element element)
    '''
def optElement():
    '''public XmlStringBuilder optElement(final String name, final String content)
    public XmlStringBuilder optElement(final String name, final Date content)
    public XmlStringBuilder optElement(final String name, final CharSequence content)
    public XmlStringBuilder optElement(final Element element)
    public XmlStringBuilder optElement(final String name, final Enum<?> content)
    public XmlStringBuilder optElement(final String name, final Object object)
    '''
def optIntElement():
    '''public XmlStringBuilder optIntElement(final String name, final int value)
    '''
def halfOpenElement():
    '''public XmlStringBuilder halfOpenElement(final String name)
    public XmlStringBuilder halfOpenElement(final NamedElement namedElement)
    '''
def openElement():
    '''public XmlStringBuilder openElement(final String name)
    '''
def closeElement():
    '''public XmlStringBuilder closeElement(final String name)
    public XmlStringBuilder closeElement(final NamedElement e)
    '''
def closeEmptyElement():
    '''public XmlStringBuilder closeEmptyElement()
    '''
def rightAngleBracket():
    '''public XmlStringBuilder rightAngleBracket()
    '''
def rightAngelBracket():
    '''public XmlStringBuilder rightAngelBracket()
    '''
def attribute():
    '''public XmlStringBuilder attribute(final String name, final String value)
    public XmlStringBuilder attribute(final String name, final boolean bool)
    public XmlStringBuilder attribute(final String name, final Date value)
    public XmlStringBuilder attribute(final String name, final CharSequence value)
    public XmlStringBuilder attribute(final String name, final Enum<?> value)
    public XmlStringBuilder attribute(final String name, final int value)
    '''
def optAttribute():
    '''public XmlStringBuilder optAttribute(final String name, final String value)
    public XmlStringBuilder optAttribute(final String name, final Date value)
    public XmlStringBuilder optAttribute(final String name, final CharSequence value)
    public XmlStringBuilder optAttribute(final String name, final Enum<?> value)
    '''
def optIntAttribute():
    '''public XmlStringBuilder optIntAttribute(final String name, final int value)
    '''
def optLongAttribute():
    '''public XmlStringBuilder optLongAttribute(final String name, final Long value)
    '''
def optBooleanAttribute():
    '''public XmlStringBuilder optBooleanAttribute(final String name, final boolean bool)
    '''
def optBooleanAttributeDefaultTrue():
    '''public XmlStringBuilder optBooleanAttributeDefaultTrue(final String name, final boolean bool)
    '''
def xmlnsAttribute():
    '''public XmlStringBuilder xmlnsAttribute(final String value)
    '''
def xmllangAttribute():
    '''public XmlStringBuilder xmllangAttribute(final String value)
    '''
def optXmlLangAttribute():
    '''public XmlStringBuilder optXmlLangAttribute(final String lang)
    '''
def escape():
    '''public XmlStringBuilder escape(final String text)
    public XmlStringBuilder escape(final CharSequence text)
    '''
def escapeAttributeValue():
    '''public XmlStringBuilder escapeAttributeValue(final String value)
    '''
def optEscape():
    '''public XmlStringBuilder optEscape(final CharSequence text)
    '''
def prelude():
    '''public XmlStringBuilder prelude(final ExtensionElement pe)
    public XmlStringBuilder prelude(final String elementName, final String namespace)
    '''
def optAppend():
    '''public XmlStringBuilder optAppend(final CharSequence csq)
    public XmlStringBuilder optAppend(final Element element)
    '''
def append():
    '''public XmlStringBuilder append(final XmlStringBuilder xsb)
    public XmlStringBuilder append(final Collection<? extends Element> elements)
    public XmlStringBuilder append(final Collection<? extends Element> elements, final String enclosingNamespace)
    public XmlStringBuilder append(final CharSequence csq)
    public XmlStringBuilder append(final CharSequence csq, final int start, final int end)
    public XmlStringBuilder append(final char c)
    '''
def emptyElement():
    '''public XmlStringBuilder emptyElement(final Enum<?> element)
    public XmlStringBuilder emptyElement(final String element)
    '''
def condEmptyElement():
    '''public XmlStringBuilder condEmptyElement(final boolean condition, final String element)
    '''
def condAttribute():
    '''public XmlStringBuilder condAttribute(final boolean condition, final String name, final String value)
    '''
def length():
    '''public int length()
    public int length()
    '''
def charAt():
    '''public char charAt(final int index)
    public char charAt(final int index)
    '''
def subSequence():
    '''public CharSequence subSequence(final int start, final int end)
    public CharSequence subSequence(final int start, final int end)
    '''
def toString():
    '''public String toString()
    public String toString()
    '''
def equals():
    '''public boolean equals(final Object other)
    '''
def hashCode():
    '''public int hashCode()
    '''
def write():
    '''public void write(final Writer writer, String enclosingNamespace)
    '''
def toXML():
    '''public CharSequence toXML(final String enclosingNamespace)
    '''
