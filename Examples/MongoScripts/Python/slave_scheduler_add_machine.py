import pymongo

if __name__ == '__main__':
    myclient = pymongo.MongoClient("mongodb://localhost:27100")
    mydb = myclient["deadline10db"]
    mycol = mydb["DeadlineSettings"]

    myquery = {"_id": "deadline_network_settings"}

    mydoc = mycol.find(myquery)
    rpl1 = mydoc[0]["SlaveSchedulingGroups"]
    sgroup = []
    for sgp in rpl1:
        sgp["SlaveNames"].append("rm4-015")
        sgroup.append(sgp)

    newvalues = {"$set" : {"SlaveSchedulingGroups": sgroup}}
    x = mycol.update_one(myquery, newvalues)
    print(x.modified_count, "documents updated.")