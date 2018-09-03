import csv
#----------------------------------------------------------------------
def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    """
    reader = csv.DictReader(file_obj, delimiter=',')
    i=1
    for line in reader:
        #print(line["Product Code"]),
        #print(line["Image link 2"])
        p=Jewellery(id1=line["Product Code"],name=i,img=file = cStringIO.StringIO(urllib.urlopen(line["Image link 2"]).read()))
        i=i+1
        p.save()
#----------------------------------------------------------------------
if __name__ == "__main__":
    with open("product.csv") as f_obj:
        csv_dict_reader(f_obj)