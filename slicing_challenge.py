#!/usr/bin/env python3

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]


#use challenge list for forming first statement by slicing
challenge1 = challenge[2][1]  #should select "eyes" from challenge list
challenge2 = challenge[2][0]  #should select "goggles" from challenge list
challenge3 = challenge[3]  #should select "nothing" from challenge list

print(f"My {challenge1}! The {challenge2} do {challenge3}!")

#use trial list to pull strings eyes, goggles, and nothing to create same output.
trial1 = trial[2] #trial1 becomes {"eyes": "goggles", "goggles": "eyes"}
t1 = trial1["goggles"]
t2 = trial1["eyes"]
t3 = trial[3]

print(f"My {t1}! The {t2} do {t3}!")


#use nightmare list to create the same output
n2 = nightmare[0]
n2 = n2["kumquat"] #gives back goggles as output
#print(n2)


n1 = nightmare[0] #contents basically the same as nightmare, but goes inside brackets

#focuses on {"awesome": "c", "name": {"first": "eyes", "last": "toes"}}
n1 = n1["user"] 

#should focus on {"first": "eyes", "last": "toes"}
n1 = n1["name"]

n1 = n1["first"] #should give back eyes as output
#print(n1)


n3 = nightmare[0]
n3 = n3["d"]
#print(n3)

print(f"My {n1}! The {n2} do {n3}!")
