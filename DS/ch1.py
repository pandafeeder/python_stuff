from collections import defaultdict, Counter

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]


def data_scientists_who_like(target_interest):
    return [ atom[0] for atom in interests if atom[1] == target_interest]

print(data_scientists_who_like('Haskell'))

def build_index_ds_interest(interests):
    ds_interests = defaultdict(list)
    for atom in interests:
        ds_interests[atom[0]].append(atom[1])
    return ds_interests

ds_interests = build_index_ds_interest(interests)

print(ds_interests)

def build_index_interest_ds(interests):
    interests_ds = defaultdict(list)
    for ds, interest in interests:
        interests_ds[interest].append(ds)
    return interests_ds

interests_ds = build_index_interest_ds(interests)

print(interests_ds)

def most_common_interests_with(user):
    return Counter(ds for inte in ds_interests[user]
        for ds in interests_ds[inte] if ds != user)

print('the one who has the most common interest with uesr0 is:')
print(most_common_interests_with(0).most_common(1))
