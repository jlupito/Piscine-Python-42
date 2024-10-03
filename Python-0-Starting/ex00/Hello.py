#Liste: Liste classique, s’ecrit avec [ ].
ft_list = ["Hello", "tata!"]
ft_list[1] = 'World!'

#Tuple: Collection ordonnée et immuable. Les éléments d'un tuple sont définis 
#dans un certain ordre et ne peuvent pas être modifiés après la création. 
#S’écrit avec ( ). Pour modifier: convertir en liste, modifier puis conevrtir en tuple.
ft_tuple = ("Hello", "toto!")
ft_tuple_list = list(ft_tuple)
ft_tuple_list[1] = 'France!'
ft_tuple = tuple(ft_tuple_list)

#Set: Collection non ordonnée de valeurs uniques. Les éléments d'un set 
# ne peuvent pas être dupliqués, et ne sont pas indexés.  
# utiles pour stocker des éléments uniques et effectuer des opérations 
# mathématiques comme les unions, intersections, différences, etc.  
# Les sets sont écrits avec des accolades {}
ft_set = {"Hello", "tutu!"}
ft_set.remove("tutu!")
ft_set.add("Paris!")

#Dict: clef/valeur.
ft_dict = {"Hello" : "titi!"}
ft_dict['Hello'] = '42Paris!'

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)