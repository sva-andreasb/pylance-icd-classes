def ():
    '''returns XmlStringBuilder\n\n
    ()\n
    (final String enclosingNamespace)\n
    (final ExtensionElement pe)\n
    (final NamedElement e)\n
    (final ExtensionElement ee, final String enclosingNamespace)\n
    '''
def escapedElement():
    '''returns XmlStringBuilder\n\n
    escapedElement(final String name, final String escapedContent)\n
    '''
def element():
    '''returns XmlStringBuilder\n\n
    element(final String name, final String content)\n
    element(final String name, final Date content)\n
    element(final String name, final CharSequence content)\n
    element(final String name, final Enum<?> content)\n
    element(final Element element)\n
    '''
def optElement():
    '''returns XmlStringBuilder\n\n
    optElement(final String name, final String content)\n
    optElement(final String name, final Date content)\n
    optElement(final String name, final CharSequence content)\n
    optElement(final Element element)\n
    optElement(final String name, final Enum<?> content)\n
    optElement(final String name, final Object object)\n
    '''
def optIntElement():
    '''returns XmlStringBuilder\n\n
    optIntElement(final String name, final int value)\n
    '''
def halfOpenElement():
    '''returns XmlStringBuilder\n\n
    halfOpenElement(final String name)\n
    halfOpenElement(final NamedElement namedElement)\n
    '''
def openElement():
    '''returns XmlStringBuilder\n\n
    openElement(final String name)\n
    '''
def closeElement():
    '''returns XmlStringBuilder\n\n
    closeElement(final String name)\n
    closeElement(final NamedElement e)\n
    '''
def closeEmptyElement():
    '''returns XmlStringBuilder\n\n
    closeEmptyElement()\n
    '''
def rightAngleBracket():
    '''returns XmlStringBuilder\n\n
    rightAngleBracket()\n
    '''
def rightAngelBracket():
    '''returns XmlStringBuilder\n\n
    rightAngelBracket()\n
    '''
def attribute():
    '''returns XmlStringBuilder\n\n
    attribute(final String name, final String value)\n
    attribute(final String name, final boolean bool)\n
    attribute(final String name, final Date value)\n
    attribute(final String name, final CharSequence value)\n
    attribute(final String name, final Enum<?> value)\n
    attribute(final String name, final int value)\n
    '''
def optAttribute():
    '''returns XmlStringBuilder\n\n
    optAttribute(final String name, final String value)\n
    optAttribute(final String name, final Date value)\n
    optAttribute(final String name, final CharSequence value)\n
    optAttribute(final String name, final Enum<?> value)\n
    '''
def optIntAttribute():
    '''returns XmlStringBuilder\n\n
    optIntAttribute(final String name, final int value)\n
    '''
def optLongAttribute():
    '''returns XmlStringBuilder\n\n
    optLongAttribute(final String name, final Long value)\n
    '''
def optBooleanAttribute():
    '''returns XmlStringBuilder\n\n
    optBooleanAttribute(final String name, final boolean bool)\n
    '''
def optBooleanAttributeDefaultTrue():
    '''returns XmlStringBuilder\n\n
    optBooleanAttributeDefaultTrue(final String name, final boolean bool)\n
    '''
def xmlnsAttribute():
    '''returns XmlStringBuilder\n\n
    xmlnsAttribute(final String value)\n
    '''
def xmllangAttribute():
    '''returns XmlStringBuilder\n\n
    xmllangAttribute(final String value)\n
    '''
def optXmlLangAttribute():
    '''returns XmlStringBuilder\n\n
    optXmlLangAttribute(final String lang)\n
    '''
def escape():
    '''returns XmlStringBuilder\n\n
    escape(final String text)\n
    escape(final CharSequence text)\n
    '''
def escapeAttributeValue():
    '''returns XmlStringBuilder\n\n
    escapeAttributeValue(final String value)\n
    '''
def optEscape():
    '''returns XmlStringBuilder\n\n
    optEscape(final CharSequence text)\n
    '''
def prelude():
    '''returns XmlStringBuilder\n\n
    prelude(final ExtensionElement pe)\n
    prelude(final String elementName, final String namespace)\n
    '''
def optAppend():
    '''returns XmlStringBuilder\n\n
    optAppend(final CharSequence csq)\n
    optAppend(final Element element)\n
    '''
def append():
    '''returns XmlStringBuilder\n\n
    append(final XmlStringBuilder xsb)\n
    append(final Collection<? extends Element> elements)\n
    append(final Collection<? extends Element> elements, final String enclosingNamespace)\n
    append(final CharSequence csq)\n
    append(final CharSequence csq, final int start, final int end)\n
    append(final char c)\n
    '''
def emptyElement():
    '''returns XmlStringBuilder\n\n
    emptyElement(final Enum<?> element)\n
    emptyElement(final String element)\n
    '''
def condEmptyElement():
    '''returns XmlStringBuilder\n\n
    condEmptyElement(final boolean condition, final String element)\n
    '''
def condAttribute():
    '''returns XmlStringBuilder\n\n
    condAttribute(final boolean condition, final String name, final String value)\n
    '''
def length():
    '''returns int\n\n
    length()\n
    length()\n
    '''
def charAt():
    '''returns char\n\n
    charAt(final int index)\n
    charAt(final int index)\n
    '''
def subSequence():
    '''returns CharSequence\n\n
    subSequence(final int start, final int end)\n
    subSequence(final int start, final int end)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def write():
    '''returns None\n\n
    write(final Writer writer, String enclosingNamespace)\n
    '''
def toXML():
    '''returns CharSequence\n\n
    toXML(final String enclosingNamespace)\n
    '''
