def CodelandUsernameValidation(strParam):
    if "_" in strParam and strParam[-1] not in "_":
        strParam = strParam.replace("_", "a")
    if strParam.isalnum() and strParam[0].isalpha() and strParam[-1] not in "_" and 3 < len(strParam) < 26:
        strParam = "true"
    else:
        strParam = "false"
    return strParam


# Main
print(CodelandUsernameValidation(input()))
