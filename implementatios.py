# A care taker supervisor needs to create a schedule for all the carers over a 7 day period,
# subject to the following conditions:
# Each day is divided into three 8-hour shifts every day, each shift is assigned
# to a single carer, and no carer works more than one shift. Each carer is assigned to at least three shifts during the
# 7 day period

# importing library
from ortools.sat.python import cp_model

# creating data for the example

carers = {"CareWorker1": "Jhon", "CareWorker2": "Kate", "CareWorker3": "Will", "CareWorker4": "Jack"}
customers = {"Customer1": "Vicky", "Customer2": "Raul", "Customer3": "Bill", "Customer4": "Denise"}
days = {"Day1": "Monday", "Day2": "Tuesday", "Day3": "Wednesday", "Day4": "Thursday", "Day5": "Friday",
        "Day6": "Saturday", "Day7": "Sunday"}

num_carers = range(len(carers))
print(num_carers)
num_customers = range(len(customers))
print(num_customers)
num_days = range(len(days))
print(num_days)