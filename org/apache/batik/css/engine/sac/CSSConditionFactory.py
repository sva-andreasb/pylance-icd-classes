def ():
    '''returns CSSConditionFactory\n\n
    (final String cns, final String cln, final String idns, final String idln)\n
    '''
def createAndCondition():
    '''returns CombinatorCondition\n\n
    createAndCondition(final Condition first, final Condition second)\n
    '''
def createOrCondition():
    '''returns CombinatorCondition\n\n
    createOrCondition(final Condition first, final Condition second)\n
    '''
def createNegativeCondition():
    '''returns NegativeCondition\n\n
    createNegativeCondition(final Condition condition)\n
    '''
def createPositionalCondition():
    '''returns PositionalCondition\n\n
    createPositionalCondition(final int position, final boolean typeNode, final boolean type)\n
    '''
def createAttributeCondition():
    '''returns AttributeCondition\n\n
    createAttributeCondition(final String localName, final String namespaceURI, final boolean specified, final String value)\n
    '''
def createIdCondition():
    '''returns AttributeCondition\n\n
    createIdCondition(final String value)\n
    '''
def createLangCondition():
    '''returns LangCondition\n\n
    createLangCondition(final String lang)\n
    '''
def createOneOfAttributeCondition():
    '''returns AttributeCondition\n\n
    createOneOfAttributeCondition(final String localName, final String nsURI, final boolean specified, final String value)\n
    '''
def createBeginHyphenAttributeCondition():
    '''returns AttributeCondition\n\n
    createBeginHyphenAttributeCondition(final String localName, final String namespaceURI, final boolean specified, final String value)\n
    '''
def createClassCondition():
    '''returns AttributeCondition\n\n
    createClassCondition(final String namespaceURI, final String value)\n
    '''
def createPseudoClassCondition():
    '''returns AttributeCondition\n\n
    createPseudoClassCondition(final String namespaceURI, final String value)\n
    '''
def createOnlyChildCondition():
    '''returns Condition\n\n
    createOnlyChildCondition()\n
    '''
def createOnlyTypeCondition():
    '''returns Condition\n\n
    createOnlyTypeCondition()\n
    '''
def createContentCondition():
    '''returns ContentCondition\n\n
    createContentCondition(final String data)\n
    '''
