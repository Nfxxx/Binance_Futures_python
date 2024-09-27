class MultiAssetsMode:

    def __init__(self):
        self.multiAssetsMargin = None

    @staticmethod
    def json_parse(json_data):
        result = MultiAssetsMode()
        result.multiAssetsMargin = json_data.get_boolean("multiAssetsMargin")

        return result
