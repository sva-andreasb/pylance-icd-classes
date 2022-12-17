def createConditionalSelector():
    '''returns ConditionalSelector\n\n
    createConditionalSelector(final SimpleSelector selector, final Condition condition)\n
    '''
def createAnyNodeSelector():
    '''returns SimpleSelector\n\n
    createAnyNodeSelector()\n
    '''
def createRootNodeSelector():
    '''returns SimpleSelector\n\n
    createRootNodeSelector()\n
    '''
def createNegativeSelector():
    '''returns NegativeSelector\n\n
    createNegativeSelector(final SimpleSelector selector)\n
    '''
def createElementSelector():
    '''returns ElementSelector\n\n
    createElementSelector(final String namespaceURI, final String tagName)\n
    '''
def createTextNodeSelector():
    '''returns CharacterDataSelector\n\n
    createTextNodeSelector(final String data)\n
    '''
def createCDataSectionSelector():
    '''returns CharacterDataSelector\n\n
    createCDataSectionSelector(final String data)\n
    '''
def createProcessingInstructionSelector():
    '''returns ProcessingInstructionSelector\n\n
    createProcessingInstructionSelector(final String target, final String data)\n
    '''
def createCommentSelector():
    '''returns CharacterDataSelector\n\n
    createCommentSelector(final String data)\n
    '''
def createPseudoElementSelector():
    '''returns ElementSelector\n\n
    createPseudoElementSelector(final String namespaceURI, final String pseudoName)\n
    '''
def createDescendantSelector():
    '''returns DescendantSelector\n\n
    createDescendantSelector(final Selector parent, final SimpleSelector descendant)\n
    '''
def createChildSelector():
    '''returns DescendantSelector\n\n
    createChildSelector(final Selector parent, final SimpleSelector child)\n
    '''
def createDirectAdjacentSelector():
    '''returns SiblingSelector\n\n
    createDirectAdjacentSelector(final short nodeType, final Selector child, final SimpleSelector directAdjacent)\n
    '''
