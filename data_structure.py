from mmh3 import hash


class DataStructure:
    hash_table = None;
    hash_seeds = list()

    def __init__(self, k, m):
        self.hash_table = [0] * m
        self.hash_seeds = [0] * k
        self.create_k_seeds()

    def create_k_seeds(self):
        for index, seed in enumerate(self.hash_seeds):
            self.hash_seeds[index] = index

    def add(self, item):
        for seed in self.hash_seeds:
            self.hash_table[self.calculate_hash_value(item, seed)] = 1

    def check_if_exists(self, item):
        for seed in self.hash_seeds:
            if self.hash_table[self.calculate_hash_value(item, seed)] == 0:
                return False
        return True

    def calculate_hash_value(self, item, seed):
        return (hash(item, seed, False)) % len(self.hash_table)
