import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("https://www.mohfw.gov.in/")
soup = BeautifulSoup(page.content,'html.parser')
# print()
table_container = soup.find_all(class_ ="table table-striped")

# print(table_container[0]

TBody = table_container[0].find("tbody")

Td = TBody.find_all("td")

##############

data = [i.get_text() for i in Td]

srno = 0
state = 1
confirmed = 2
cured = 3
death = 4

# print(data[2])

ListSrNo = []
ListState= []
ListConfirmed = []
ListCured = []
ListDeath = []

for i in range (len(data)):
    if i >= srno:
        ListSrNo.append(data[srno])
        srno = srno + 5
    if i >= state:
        ListState.append(data[state])
        state = state + 5
    if i >= confirmed:
        ListConfirmed.append(data[confirmed])
        confirmed = confirmed + 5
    if i >= cured:
        ListCured.append(data[cured])
        cured = cured + 5
    if i >= death:
        ListDeath.append(data[death])
        death = death + 5

# print(SrNo)
# print(State)
# print(Confirmed)
# print(Cured)
# print(Death)

TruncSrNo = ListSrNo[0:33]
TruncState = ListState[0:33]
TruncConfirmed = ListConfirmed[0:33]
TruncCured = ListCured[0:33]
TruncDeath = ListDeath[0:33]

print(TruncConfirmed)
print(TruncSrNo)
print(TruncCured)
print(TruncState)
print(TruncDeath)



Data = pd.DataFrame({
    "Sr.No" : TruncSrNo,
    "State" : TruncState,
    "Confirmed Cases" : TruncConfirmed,
    "Cured" : TruncCured,
    "Death" : TruncDeath,
})

print(Data)

Data.to_csv("NewData.csv")

print(Data)
#
