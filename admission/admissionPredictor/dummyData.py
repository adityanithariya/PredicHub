def create_random_data(filename):
    import random
    branches = {
        "AI" : "Artificial Intelligence - 0.3",
        "DS" : "Data Science - 0.3",
        # "CS" : "Cyber Security - 0.4",
        "CSE" : "Computer Science - 0.4",
        # "ME" : "Mechanical Engineering - 0.2",
        # "CE" : "Civil Engineering - 1",
        # "ECE" : "Electronics and Communication Engineering - 1",
        # "EEE" : "Electrical and Electronics Engineering - 1",
    }

    Categories1 = {
        "Gen" : "General",
        "OBC" : "Other Backward Classes",
        "SC" : "Scheduled Castes",
        "ST" : "Scheduled Tribes",
    }

    Categories2 = {
        "NA" : "None - 0.93",
        "ExSr" : "Ex-Serviceman - 0.05",
        "Pwd" : "Physically Disabled - 0.02",
    }

    States = {
        "HS" : "Home State - 0.6",
        "OS" : "Other State - 0.4",
    }

    data = {
        "branch" : [],
        "cat1" : [],
        "cat2" : [],
        "state" : [],
        "12th" : [],
        "JEE" : []
    }

    def bias(dic):
        zipped = zip(list(dic.keys()), [float(i.split(" - ")[1]) for i in list(dic.values())])
        lst = [[i[0]] * int(i[1]*100) for i in zipped]
        new = [b for i in lst for b in i]
        return new

    for i in range(200):
        branch = random.choice(bias(branches))
        cat1 = random.choice(list(Categories1.keys()))
        cat2 = random.choice(bias(Categories2))
        state = random.choice(bias(States))

        data["branch"].append(branch)
        data["cat1"].append(cat1)
        data["cat2"].append(cat2)
        data["state"].append(state)
        data["12th"].append(random.choice(range(60, 90)))
        data["JEE"].append(random.choice(list(range(40, 80)) + [0]))

    import pandas as pd

    df = pd.DataFrame(data)
    df.to_csv(filename + ".csv", index=False)

create_random_data("db1")
