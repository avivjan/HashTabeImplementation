class Logger:
    @staticmethod
    def inform_about_existing_item(item):
        print(f"Item: {item} - was found in the hash table")

    @staticmethod
    def inform_about_unexisting_item(item):
        print(f"Item: {item} - is not exist in the hash table")
