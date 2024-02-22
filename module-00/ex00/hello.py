ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
#you

ft_list[1] = "World!"

mutateTuple = list(ft_tuple)
mutateTuple[1] = "France"
ft_tuple = tuple(mutateTuple)

# ft_tuple = ("Hello", "France!")

ft_set.remove("tutu!")
ft_set.add("Paris!")

ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
# print(sorted(ft_set))
print(ft_dict)
