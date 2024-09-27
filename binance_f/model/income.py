class Income:

    def __init__(self):
        self.symbol = ""
        self.incomeType = ""
        self.income = 0.0
        self.asset = ""
        self.time = 0
        self.tranId = ""
    
    @staticmethod
    def json_parse(json_data):
        result = Income()
        result.symbol = json_data.get_string("symbol")
        result.incomeType = json_data.get_string("incomeType")
        result.income = json_data.get_float("income")
        result.asset = json_data.get_string("asset")
        result.time = json_data.get_int("time")
        result.tranId = json_data.get_string("tranId")
        return result
