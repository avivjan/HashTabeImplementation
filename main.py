from data_structure import DataStructure
from Text_reader import TextReader


# This func is the main func of the program it adds item and checks existence.
def main():
    ds = create_ds()
    TextReader.add_all_items_from_file("Data/evens.txt", ds)
    TextReader.check_if_items_exist_from_file("Data/all.txt", ds)


# This func gets the value from the user and create the ds.
def create_ds():
    m = int(input("Please enter the size of the hash table: "))
    k = int(input("Please enter the number of hushing functions: "))
    ds = DataStructure(k, m)
    return ds


if __name__ == "__main__":
    main()

