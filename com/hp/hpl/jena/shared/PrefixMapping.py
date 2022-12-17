Standard = "PrefixMapping  Factory.create().setNsPrefix(\"rdfs\", RDFS.getURI()).setNsPrefix(\"rdf\", RDF.getURI()).setNsPrefix(\"dc\", DC_11.getURI()).setNsPrefix(\"owl\", OWL.getURI()).setNsPrefix(\"xsd\", XSD.getURI()).lock()"
Extended = "PrefixMapping  Factory.create().setNsPrefixes(PrefixMapping.Standard).setNsPrefix(\"daml\", \"http://www.daml.org/2001/03/daml+oil#\").setNsPrefix(\"rss\", RSS.getURI()).setNsPrefix(\"vcard\", VCARD.getURI()).setNsPrefix(\"ja\", JA.getURI()).setNsPrefix(\"eg\", \"http://www.example.org/\").lock()"
def ():
    '''returns JenaLockedException\n\n
    (final String prefixName)\n
    (final PrefixMapping pm)\n
    '''
