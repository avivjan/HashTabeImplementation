class Logger:
    # This func print to the console a message about an existing item
    @staticmethod
    def inform_about_existing_item(item):
        print(f"Item: {item} - was found in the hash table")

    # This func print to the console a message about an unexisting item
    @staticmethod
    def inform_about_unexisting_item(item):
        print(f"Item: {item} - is not exist in the hash table")
