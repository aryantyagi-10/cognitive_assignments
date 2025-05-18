sample_dict = {"name" : "Kelly", "age" : 25, "salary" : 8000, "city" : "New York"};
print("Original dictionary is",sample_dict);
sample_dict["location"] = sample_dict["city"];
del sample_dict["city"];
print("Modified dictionary is",sample_dict);