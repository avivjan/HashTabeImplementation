from data_structure import DataStructure
from csv_reader import TextReader


def main():
    m = int(input("Please enter the size of the hash table: "))
    k = int(input("Please enter the number of hushing functions: "))
    ds = DataStructure(k, m)
    TextReader.add_all_items_from_file("Data/all.txt", ds)
    TextReader.check_if_items_exist_from_file("Data/all.txt", ds)


if __name__ == "__main__":
    main()

