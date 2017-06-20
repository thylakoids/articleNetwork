from Bio import Entrez
Entrez.email = '812033546@qq.com'
pmid = '14630660'
results = Entrez.read(Entrez.elink(dbfrom="pubmed", db="pubmed",LinkName="pubmed_pubmed_citedin", id=pmid))


for linksetdb in results[0]["LinkSetDb"]:                             
	print(linksetdb["DbTo"], linksetdb["LinkName"], len(linksetdb["Link"]))

results[0]['LinkSetDb']