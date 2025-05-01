# def doh():
#     return ["Homer: D'Oh!", "Marge: A deer!", "lisa: A Female deer!"]
#
#
# for line in doh():
#     print(line)
#
def doh2():
    yield "Homer: D'Oh!"
    yield "Marge: A deer!"
    yield "Lisa: A female deer!"


for line in doh2():
    print(line)
