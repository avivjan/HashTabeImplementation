from mmh3 import hash


class DataStructure:
    hash_table = None  # This var is an array - hash table
    hash_seeds = None  # This var contains K seeds for K hash functions

    # This ctor gets k - num of seeds, m - length of hash table
    # It creates two arrays with that lengths and creates k unique seeds.
    def __init__(self, k, m):
        self.hash_table = [0] * m
        self.hash_seeds = [0] * k
        self.create_k_seeds()

    # This function fill the array of seeds with k unique values.
    def create_k_seeds(self):
        for index, seed in enumerate(self.hash_seeds):
            self.hash_seeds[index] = index

    # This function gets a new item to be added and goes through all its hash values and turn them on
    # By this it adds this item to the data structure
    def add(self, item):
        for seed in self.hash_seeds:
            self.hash_table[self.calculate_hash_value(item, seed)] = 1

    # This function gets an item and check if it exists in the data structure
    # The func goes through all the hash values - if all of them are on if returns true otherwise false
    def check_if_exists(self, item):
        for seed in self.hash_seeds:
            if self.hash_table[self.calculate_hash_value(item, seed)] == 0:
                return False
        return True

    # This func gets an item and a seed and return the hash value.
    def calculate_hash_value(self, item, seed):
        return (hash(item, seed, False)) % len(self.hash_table)
