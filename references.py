from Bio import Entrez
Entrez.email = '812033546@qq.com'
def get_abstract(pmid):
	handle = Entrez.efetch(db='pubmed', id=pmid, retmode='text', rettype='abstract')
	return handle.read()

def get_term_result(term):
#get pubmed  id list for any search term
	links = Entrez.esearch(db="pubmed", retmax = 1000, term=term)	
	record = Entrez.read(links)
	link_list = record[u'IdList']
	return link_list

def get_citation_id(pmid):
#get pubmed id list which cite this article
	links = Entrez.elink(dbfrom="pubmed", id=pmid, linkname="pubmed_pubmed_citedin")	
	record = Entrez.read(links)
	try:
		pubmed_ids = [link["Id"] for link in record[0]["LinkSetDb"][0]["Link"]]
	except Exception,e:
		print '+++++++++++++++++++++>>empty list!'
		print e
		pubmed_ids=[]
	return pubmed_ids

def get_summary(pmid):
#get some useful information for this article
	handle = Entrez.esummary(db="pubmed", id=pmid, retmode="xml")
	records = Entrez.read(handle)
	#records = Entrez.parse(handle)
	return records

### MAIN -----------------------
if __name__=="__main__":
	print(get_term_result("Saffran JR[Author] "))
	print "----------------------------"
	print(get_abstract("26113833"))
	print "----------------------------"
	print(get_citation_id("8943209"))