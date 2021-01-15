from logger import Logger


class TextReader:
    # This func read all the data from the file and insert them to an array
    # Then for each item in the array it adds it to the ds using the ds add func
    # path - path of the file
    @staticmethod
    def add_all_items_from_file(path, ds):
        reader = open(path, "r")
        text_to_add = reader.read()
        arr_items_to_add = text_to_add.split(",")
        for item in arr_items_to_add:
            ds.add(item)

    # This func read all the data from the file and insert them to an array
    # Then for each item in the array it checks if it exists in the ds and inform the user accordingly
    # path - path of the file
    @staticmethod
    def check_if_items_exist_from_file(path, ds):
        reader = open(path, "r")
        text_to_check = reader.read()
        arr_items_to_check = text_to_check.split(",")
        for item in arr_items_to_check:
            if ds.check_if_exists(item):
                Logger.inform_about_existing_item(item)
            else:
                Logger.inform_about_unexisting_item(item)

