#! /path/to/Rscript
library('igraph')
#LOAD DATA
nodes <- read.csv2("nodes.csv", as.is = TRUE, header = TRUE, sep = ",",
                   #nrows = 100,
                   row.names = NULL				
)
edges <- read.csv2("edges.csv", as.is = TRUE, header = TRUE, sep = ",",
                   #nrows = 100,
                   row.names = NULL				
)

#SETUP NETWORK

net <- graph_from_data_frame(edges, directed=TRUE, vertices=nodes)
cutoff <- 30

#VISUALIZE

#Degree distribution

dd <- degree.distribution(net, cumulative=T, mode="all")
plot(dd, pch=19, cex=0.5, col="orange", xlab="Degree", ylab="Cumulative Frequency")

#Whole network with highly citated nodes outlined in red

l <- layout_with_lgl(net) #very large graph layout
l <- layout.norm(l, ymin=-1, ymax=1, xmin=-1, xmax=1) #Sets up graph area
in_degree <- degree(net, mode="in") #mode can be all, out or in

plot(net, 
     vertex.size = log(in_degree+1), #Size of node determained by connections into it
     vertex.label.color = "black",
     #vertex.label = ifelse(degree(net, mode = "in", loops = FALSE) > cutoff, V(net)$Last_Author, NA),
     vertex.label = NA,
     vertex.color = ifelse(degree(net, mode = "in", loops = FALSE) > cutoff, "red", "white"), #Color nodes differently based on their pubtype
     edge.width = .4,
     edge.curved = 0,
     edge.arrow.size = 0,
     rescale = FALSE,
     main = "Network",
     layout = l*1.4 #For playing around with the size of the graph
)
legend(x=-2, y=-1, # position
       legend = c(paste("Nodes >", cutoff, "degrees"), paste("Nodes <", cutoff, " degrees")), 
       pch = 21, #open point
       pt.bg = c("Red","White"),
       pt.cex=2, 
       cex=.8, bty="n", 
       ncol=1
)
legend(x=1, y=-1, # position
       legend = c(paste("Nodes :", vcount(net)), paste("Edges :", ecount(net))), 
       pt.bg = c("black"),
       pt.cex=2, 
       cex=.8, bty="n", 
       ncol=1
)

#EXTRACT DATA

#Show data for articles with a minimum number of citations
#net.vs <- V(net)[degree(net) < cutoff] #identify those vertices part of less than cutoff value
#net.cutoff <- delete.vertices(net, net.vs) #exclude them from object