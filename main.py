import csv

// setup your file location here
sourceFile = "C:/Users/wwwle/Desktop/book2.csv"  //replace it with the data file path
targetFile = "C:/Users/wwwle/Desktop/book3.csv"  //replace it with the result file path

// init `dict` and `list` files.
dict1 = {}
finalList = [[]]

with open(sourceFile) as f:
    // number each element and store the result in `dict1`
    reader = csv.reader(f)
    names = list(reader)
    for each1 in names:
        for each2 in each1:
            if each2 == "":
                pass
            elif each2 in dict1.keys():
                dict1[each2] += 1
            else:
                dict1[each2] = 1
                
    // export data from `dict1` to `finalList`
    keynum = len(dict1)
    for i in range(keynum):
        (key, value) = dict1.popitem()
        finalList.append([key, value])
        keynum -= 1
    f.close()
    
// write results from `finalList` to targetFile.
with open(targetFile, 'w', newline='') as f:
    writer = csv.writer(f)
    for row in finalList:
        writer.writerow(row)
    f.close()
