data = []


def load(data):
    with open("database.csv", "r") as f:
        rows = f.read().split("\n")
        for i in rows:
            object = []
            if not rows.index(i) == 0:
                object.append(i.split(",")[1]) #FIXME: INDEXError
                object.append(i.split(",")[2])

            
            data.append(object)
                
            # data += [i.split(",")[1], i.split(",")[2], i.split(",")[3], i.split(",")[4]]
        print(data)



load(data)