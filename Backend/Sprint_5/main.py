from package_classes import *

dictJSON = JSONtoDict("eventos_black.json")

cliente_1= Client(dictJSON,ACCOUNTS_RESTRICTIONS)

HTMLname = 'INFORME_' + cliente_1.name.upper() + '_' + cliente_1.lastname.upper() + '.html'

stringToHtml(HTMLname,cliente_1.dataToHTML())