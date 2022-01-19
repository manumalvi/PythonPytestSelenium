key_value = {}
key_value[2] = '64'
key_value[1] = '69'
key_value[4] = '23'
key_value[5] = '65'
key_value[6] = '34'
key_value[3] = '76'

print(key_value)

for key in sorted(key_value.keys()):
    print(key)

##############################################
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
new_dict={}
# a = zip(keys,values)
# print(dict(a))

for i in range(0,len(keys)):
    new_dict.update({keys[i]:values[i]})
print(new_dict)

###########################
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)

#################
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict["class"]["student"]["marks"]["history"])