from numpy import *

def knn(x,k,e=1e-6): 
	"""Find k-nearest neighbors of x[i,:] for all i
	Set e=0 for optimal solution or higher number
	for faster execution"""
	# Fill nn matrix with references to random neighbors
	nn=random.randint(len(x),size=(len(x),k)).tolist()
	total_mse=ones(len(nn)) # Initialize mse
	old_mse=mean(total_mse)+1
	while mean(total_mse)+e<old_mse: # As long as we can improve
		old_mse=mean(total_mse) 
		for i in range(len(x)): # improve nn[i,:] for all x[i,:]
			candidates=[]
			# Extend candidate list with the neighbors of your neighbors
			for j in range(len(nn[i])): candidates.extend(nn[nn[i][j]])
			random.shuffle(candidates) # randomize list
			candidates=candidates[0:k] # and keep only k
			# Add k random items for good luck
			candidates.extend(random.randint(len(nn),size=k))
			# Exclude yourself!
			candidates=list(set(filter(lambda a:a!=i,candidates)))
			candidates.extend(list(nn[i])) # Remember current neighbors
			# Calculate mse for the candidates
			list_mse=[mean((x[i]-x[a])**2) for a in candidates]
			nn[i]=[] # Flush and add new neighbors
			nn[i].extend(array(candidates)[argsort(list_mse)])
			total_mse[i]=mean(sort(list_mse)[0:k])
		print mean(total_mse),old_mse-mean(total_mse)
	return nn
