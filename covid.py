import pygsheets

from selenium import webdriver

chromedriver = '/usr/local/chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get("https://docs.google.com/spreadsheets/d/e/2PACX-1vQjf_HNeEZKM-XJX-q5v4cfNrB3kcv4gOT8kFbV9rurfoX_H5Qv9112Pv0PgYNFSzbReyNlQkLrJib3/pubhtml?utm_source=google&utm_medium=cpc&utm_campaign=%E6%B8%85%E5%86%A0%E4%B8%80%E8%99%9F%E5%8B%95%E6%85%8B%E8%A1%A8")
print(driver.title)


# # 金鑰位置
# auth_file = "./excel/useful-flame-378613-3b01638aaf40.json"
# gc = pygsheets.authorize(service_file=auth_file)

# # google共用表單位置 google sheet
# sheet_url = "https://docs.google.com/spreadsheets/d/1hFq3RTsbdT7wC6__ZwO8OjYJeS4foL0cPlaXFCNBwjE/edit?usp=sharing"
# sheet = gc.open_by_url(sheet_url)

# # 選取對應工作表 by名稱
# sheet_01 = sheet.worksheet_by_title("工作表1")

# # 讀取工作表  read
# A1 = sheet_01.cell('A1')
# print(A1)
# print(A1.value)
