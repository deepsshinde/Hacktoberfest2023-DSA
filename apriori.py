def load_dataset():
    # Example transaction dataset
    dataset = [
        ['milk', 'bread', 'nuts'],
        ['milk', 'bread'],
        ['milk', 'diapers'],
        ['milk', 'nuts'],
        ['bread', 'diapers'],
    ]
    return dataset

def create_candidate_itemsets(dataset, k):
    candidate_itemsets = []
    for transaction in dataset:
        for item in transaction:
            if [item] not in candidate_itemsets:
                candidate_itemsets.append([item])
    candidate_itemsets.sort()
    return list(map(frozenset, candidate_itemsets))

def scan_dataset(dataset, candidate_itemsets, min_support):
    itemset_counts = {}
    for transaction in dataset:
        for itemset in candidate_itemsets:
            if itemset.issubset(transaction):
                itemset_counts[itemset] = itemset_counts.get(itemset, 0) + 1
    
    num_transactions = len(dataset)
    frequent_itemsets = []
    support_counts = {}
    
    for itemset, count in itemset_counts.items():
        support = count / num_transactions
        if support >= min_support:
            frequent_itemsets.append(itemset)
        support_counts[itemset] = support
    
    return frequent_itemsets, support_counts

def apriori(dataset, min_support):
    frequent_itemsets = []
    support_counts = {}
    
    candidate_itemsets = create_candidate_itemsets(dataset, 1)
    k = 2
    
    while candidate_itemsets:
        frequent_itemsets_k, support_counts_k = scan_dataset(dataset, candidate_itemsets, min_support)
        frequent_itemsets.extend(frequent_itemsets_k)
        support_counts.update(support_counts_k)
        candidate_itemsets = create_candidate_itemsets(frequent_itemsets_k, k)
        k += 1
    
    return frequent_itemsets, support_counts

if __name__ == "__main__":
    dataset = load_dataset()
    min_support = 0.4
    frequent_itemsets, support_counts = apriori(dataset, min_support)
    
    print("Frequent Itemsets:")
    for itemset in frequent_itemsets:
        print(itemset)
    
    print("\nSupport Counts:")
    for itemset, support in support_counts.items():
        print(f"{itemset}: {support}")
