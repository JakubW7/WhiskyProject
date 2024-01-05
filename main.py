import pandas as pd
import numpy as np
from scipy.stats import spearmanr

data = pd.read_csv("./data/whisky.csv", delimiter= ",")

data = data.drop(columns = ["RowID"])


def calculate_similarities(products):
    """Calculate the similarity measures between all pairs of products.
    
    Parameters
    ----------
    products : list
        A list of dictionaries containing the attributes of the products.
    
    Returns
    -------
    spearman_similarietes : numpy array
        An array containing the Pearson correlation coefficient between each pair of products.
    """
    # Initialize arrays to store the similarity measures
    spearman_similarietes = np.zeros((len(products), len(products)))

    # Calculate all the similarity measures in a single loop
    for i in range(len(products)):
        for j in range(i+1, len(products)):
            p1 = products[i]['attributes']
            p2 = products[j]['attributes']

            # Calculate Pearson correlation coefficient
            spearman_similarietes[i][j] = spearmanr(p1, p2).correlation
            spearman_similarietes[j][i] = spearman_similarietes[i][j]
            
    return spearman_similarietes

def find_similar(coefs, name):
    """Print 3 most similar products to the one that is given with their Spearman correlation.
    
    Parameters
    ----------
    coefs : numpy array
        An array containing the Spearman correlation coefficient between each pair of products.
    name : string
        String representing name of the product 
    
    Returns
    -------
    out : list
        A list of dictionaries containing 3 most similar products and their Spearman correlation.
        
    """
    if name == 'list':
        print(data["Distillery"].to_string())
        return 0
    if name not in data['Distillery'].values:
        print('Incorrect name or Distillery is not in the database, for list of all disilerys type "list"')
        return 0
    id = data[data['Distillery'] == name].index.values[0]
    topid = np.argsort(coefs[id])[-3:]
    out = []
    for i in topid:
        out.append({'name': data[data.index == i]['Distillery'].values[0], 'coef': round(coefs[id][i],2)})
    return out

# Define the products and their attributes
products = []
for i in data.index:
    products.append({'name': data['Distillery'][i], 'attributes': data.iloc[i,1:12].values.tolist()}) 

# Calculate similarieties
spearman_similarietes = calculate_similarities(products)

# Get imput from user and find similiar products
while True:
    name = input("Enter name of destillery: ")
    if find_similar(spearman_similarietes, name) != 0:
        out = find_similar(spearman_similarietes, name)
        break

# Print results
for i in out:
    print(f"Name of Destillery: {i['name']} \nCoefficient with choosen Destillery: {i['coef']} \n")
