class CustomException(Exception):
    def __init__(self, msg):
        with open("logs.txt", "a") as file:
            file.write(msg)
            file.write("\n")


#raise CustomException("Something went wrong")
raise CustomException("My leg hurts")
