import load_data 
import win32com.client

cpp_fora = []

class contratos():
    def atribui_contrato(self):
        SapGuiAuto = win32com.client.GetObject("SAPGUI")
        application = SapGuiAuto.GetScriptingEngine
        connection = application.Children(0)
        session = connection.Children(0)
        
        listas = load_data.Listas()
        listas.load_data()
        status = 0
        cpp_ordem = session.findById("wnd[0]/usr/subSUB_ALL:SAPLCOIH:3001/ssubSUB_LEVEL:SAPLCOIH:1300/subSUB_KMP:SAPLCOMD:3001/ctxtRESBD-MATNR").text
        for i in range(len(listas.cpp)):
            if str(cpp_ordem) == str(listas.cpp[i]):
                session.findById("wnd[0]/usr/subSUB_ALL:SAPLCOIH:3001/ssubSUB_LEVEL:SAPLCOIH:1300/tabsTS_1300/tabpEINK/ssubSUB_KMP_DETAIL:SAPLCOMD:3170/txtRESBD-GPREIS").text = str(listas.valor[i]).replace(".", ",")
                session.findById("wnd[0]/usr/subSUB_ALL:SAPLCOIH:3001/ssubSUB_LEVEL:SAPLCOIH:1300/tabsTS_1300/tabpEINK/ssubSUB_KMP_DETAIL:SAPLCOMD:3170/ctxtRESBD-SAKNR").text = str(440142)
                session.findById("wnd[0]/usr/subSUB_ALL:SAPLCOIH:3001/ssubSUB_LEVEL:SAPLCOIH:1300/tabsTS_1300/tabpEINK/ssubSUB_KMP_DETAIL:SAPLCOMD:3170/ctxtRESBD-KONNR").text = str(listas.contrato[i])
                session.findById("wnd[0]/usr/subSUB_ALL:SAPLCOIH:3001/ssubSUB_LEVEL:SAPLCOIH:1300/tabsTS_1300/tabpEINK/ssubSUB_KMP_DETAIL:SAPLCOMD:3170/ctxtRESBD-KTPNR").text = str(listas.item[i])
                session.findById("wnd[0]/tbar[0]/btn[0]").press()
                status = 1
            else:
                if (str(cpp_ordem) != str(listas.cpp[i])) and (str(i) == str(int(len(listas.cpp))-1)) and (str(status) == '0'):
                    cpp_fora.append(cpp_ordem)
                    status = 0
        print(cpp_fora)