import pandas
import hashlib

df = pandas.read_csv('annual-enterprise-survey-2020-financial-year-provisional-csv.csv', usecols=[2])
line_count=1
concat=""
for i in range(len(df)):
  if line_count % 2 == 1:
      concat+=str(df.iloc[i, 0])
  line_count+=1
print(concat)
hash_object = hashlib.md5(concat.encode())
md5_hash = hash_object.hexdigest().upper()
print(md5_hash)


