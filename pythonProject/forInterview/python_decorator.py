# decoraor is a function which takes functon as argument and retrun a function

def decore_result(result_function):
    def distinction(marks):
        for m in marks:
            if m>=75:
                print("Disctinction")
        result_function(marks)
    return distinction

@decore_result
def result(marks):
    for m in marks:
        if m >= 33:
            pass
        else:
            print("Failed")
            break
    else:
        print("pass")

result([50,60,75,33])
