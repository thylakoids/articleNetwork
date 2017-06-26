#! /path/to/Rscript
rm(list=ls())
library('igraph')
library(visNetwork)
#LOAD DATA
nodes <- read.csv("nodes.csv")
edges <- read.csv("edges.csv")
net = graph_from_data_frame(edges, directed=TRUE, vertices=nodes)
#
in_degree =degree(net, mode="out")
nodes$size= log2(in_degree+1)
nodes$color='yellow'
nodes$label=NA
edges$color='gray'
edges$arrows='to'
edges$arrows.scaleFactor=0.3
#SETUP NETWORK
g=visNetwork(nodes,edges)
visIgraphLayout(g,layout='layout_with_lgl',physics = FALSE)%>%
  visOptions(highlightNearest = TRUE)