class CalcModel:
    ERROR_MESSAGE = 'Error occured'

    def evaluate_expression(self, expr):
        try:
            return str(eval(expr))
        except Exception:
            return self.__class__.ERROR_MESSAGE
