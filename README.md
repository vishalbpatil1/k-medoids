# K Medoids Clustring 

A Python package to get k medoids clustring .
# Cluster
Clustring  is organizing a set of disirganized objects with respect to a porperty. So , a clustring is collection on of objects which are similar between them and diffrent/dissimilar with objects of other cluster.
# k medoids 
k medoids attemps to minimize the sum of dissimilarities between objects labeled to be in a cluster and one of the objects designated as the reprsentative of that cluster.This representative are called medoids. k medoids chooses medoids from the data point in the set (array) 

A cluster with a data set whose average dissimilarity to all the objects in the cluster is minimal.

# Cost
The dissimilarity of each non-medoids point with the medoids is calculated.

# Swap Cost
Each point is assigned to the cluster of that medoid whose dissimilarity is less.
Now again randomly selected one non-medoid point and re-calculate the cost.
swap cost = present cost - previous cost  .


## parameters
 x= Satandard data matrices array of shape  [n_samples,n_features].
 k= Number of clusters.
 iteration=Number of iterations run.

 