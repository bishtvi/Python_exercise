dict = {"name":"Plato","country":"India", "born":1983, "teacher": "Socrates", "student": "Aristotle"}

answer_1 = dict.get("born")
answer_2 = dict["born"]
dict["born"]= 1985
answer_3=dict["born"]
print(answer_1)
print(answer_2)
print(answer_3)


dict={"son's name": "Lucas", "son's eye color": "green", "son's height": 32, "son's weight": 25,"son's age":5}

#Type your answer here.
ans_1=dict.get("son's age")

print(ans_1)
