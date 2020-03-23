import csv
from datetime import datetime

path = "GOOG.csv"
file = open(path, newline='')
reader = csv.reader(file)

header = next(reader)
data = []
for row in reader:
    date = datetime.strptime(row[0], '%m/%d/%Y')
    open_price = float(row[1])
    high=float(row[2])
    low=float(row[3])
    close=float(row[4])
    volume = float(row[6])
    adj_close=float(row[5])

    data.append([date, open_price, high, low, close, volume, adj_close])

sma_path ="sma.csv"
file = open(sma_path, 'w')
writer = csv.writer(file)
writer.writerow(["Date", "50 SMA","20 SMA"])


for i in range(len(data)):
    todays_row  = data[i]
    todays_date = todays_row[0]
    todays_price = todays_row[4]
    br1d = data [i-1]
    bp1d = br1d[3]
    br2d = data [i-2]
    bp2d = br2d[3]
    br3d = data [i-3]
    bp3d = br3d[3]
    br4d = data[i-4]
    bp4d = br4d[3]
    br5d = data[i-5]
    bp5d = br5d[3]
    br6d = data[i-6]
    bp6d = br6d[3]

    sma5 = (bp1d + bp2d + bp3d + bp4d + bp5d)/5
    writer.writerow([todays_date, sma5])



print (bp1d)
print (bp2d)
print (bp3d)
print (bp4d)
print (bp5d)

