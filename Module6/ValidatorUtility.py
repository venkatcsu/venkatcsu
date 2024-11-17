class ValidatorUtility:
    @staticmethod
    def validate_int(prompt, error_message):
        while True:
            try:
                value = int(input(prompt))
                if value < 0:
                    print(error_message)
                else:
                    return value
            except ValueError:
                print(error_message)

    @staticmethod
    def validate_float(prompt, error_message):
        while True:
            try:
                value = float(input(prompt))
                if value < 0:
                    print(error_message)
                else:
                    return value
            except ValueError:
                print(error_message)