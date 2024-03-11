import pandas

def readExcel(path):
    dtTask = pandas.read_excel(path)
    dtTask['Data de conclusão'] = dtTask['Data de conclusão'].dt.strftime('%d/%m/%Y')
    return dtTask.to_numpy()

print(readExcel("./assets/Task.xlsx"))