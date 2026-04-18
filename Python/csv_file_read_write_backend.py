import csv
# with open("annual-enterprise-survey-2024-financial-year-provisional.csv","r")as f:
#     reader=csv.reader(f)
#     # print(reader)
#     for row in reader:
#         print(row)


# # skip first row header
# with open ("annual-enterprise-survey-2024-financial-year-provisional.csv","r")as f:
#     reader=csv.reader(f)
#     next(reader)
#     for row in reader:
#         print(row)

# with open ("annual-enterprise-survey-2024-financial-year-provisional.csv","r")as f:
#     reader=csv.reader(f)
#     for row in reader:
#         name=row[0]
#         age=row[1]
#         print(name,age)

with open("annual-enterprise-survey-2024-financial-year-provisional.csv","r")as f:
    reader=csv.DictReader(f)
    for row in reader:
        print(row["Year"],row["Industry_aggregation_NZSIOC"])