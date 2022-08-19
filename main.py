def polindrom(string):
    string = string.lower()
    return  string == string [::-1]
string = input()
print(polindrom(string))
