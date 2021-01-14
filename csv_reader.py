from logger import Logger


class TextReader:
    @staticmethod
    def add_all_items_from_file(path, ds):
        reader = open(path, "r")
        text_to_add = reader.read()
        arr_items_to_add = text_to_add.split(",")
        for item in arr_items_to_add:
            ds.add(item)

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

