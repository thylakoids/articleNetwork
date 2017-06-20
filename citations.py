from Bio import Entrez
Entrez.email = '812033546@qq.com'
pmid = '14630660'
results = Entrez.read(Entrez.elink(dbfrom="pubmed", db="pmc",LinkName="pubmed_pmc_refs", id=pmid))
pmc_ids = [link["Id"] for link in results[0]["LinkSetDb"][0]["Link"]]
#transfer id from pmc to pubmed
results2 = Entrez.read(Entrez.elink(dbfrom="pmc", db="pubmed", LinkName="pmc_pubmed", id=",".join(pmc_ids)))
pubmed_ids = [link["Id"] for link in results2[0]["LinkSetDb"][0]["Link"]]
pubmed_ids