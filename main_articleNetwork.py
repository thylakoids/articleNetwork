import references
import Queue
import time
import pandas as pd
start = time.time()
q_all=Queue.Queue()
L_put=list()
L_get=list()
fromlist=list()
tolist=list()
seednode='19112483'

q_all.put(seednode)
L_put.append(seednode)
dict_all=dict()
count = 1
while not q_all.empty() and len(L_get)<100000:############<1000
	mynode=q_all.get()
	print '>>>>>>>>>>>>>>>>>>>>>mynode:',count,mynode
	count += 1
	L_get.append(mynode)

	###################################################### try except###############
	flag = 1
	count_try =1
	while(flag):
		try:
			flag=0
			citationList = references.get_citation_id(mynode)
		except Exception, e:
			flag =1
			count_try+=1
			print '+++++++++++++++++++++>>Warning:network error!'
			print e
			print 'Try time:',count_try,'(',count-1,mynode,')'
	#################################################################################
	fromlist.extend([mynode]*len(citationList))
	tolist.extend(citationList)
	dict_all[mynode]=citationList
	for tmp in citationList:
		if tmp not in L_put:
			L_put.append(tmp)
			q_all.put(tmp)
	now=time.time()
	print '*********************time:',now-start




output_edges=pd.DataFrame({'from':fromlist,'to':tolist})
output_edges.to_csv('edges1.csv',index=False)
fromlist.extend(tolist)
fromlist=list(set(fromlist))
output_nodes=pd.DataFrame(fromlist,columns=['id'])
output_nodes.to_csv('nodes1.csv',index=False)

