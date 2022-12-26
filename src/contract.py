import win32com.client
import load_contract
import interface

class ordem():
    def acesso_ordem(self, ordem_teste):
        

        x = interface.telas()

        buscar_contrato = load_contract.contratos()
        
        
        SapGuiAuto = win32com.client.GetObject("SAPGUI")
        application = SapGuiAuto.GetScriptingEngine
        connection = application.Children(0)
        session = connection.Children(0)


        session.findById("wnd[0]/tbar[0]/okcd").text = "/niw32"
        session.findById("wnd[0]/tbar[0]/btn[0]").press()

        # .replace(" ", "")   # "500061834777"
        session.findById("wnd[0]/usr/ctxtCAUFVD-AUFNR").text = str(ordem_teste)
        session.findById("wnd[0]/tbar[1]/btn[18]").press()

        session.findById("wnd[0]/usr/subSUB_ALL:SAPLCOIH:3001/ssubSUB_LEVEL:SAPLCOIH:1101/tabsTS_1100/tabpMUEB/ssubSUB_AUFTRAG:SAPLCOMK:3020/btnBTN_MKAG").press()


        while True:
            x = session.findById("wnd[0]/usr/subSUB_ALL:SAPLCOIH:3001/ssubSUB_LEVEL:SAPLCOIH:1300/subSUB_KMP:SAPLCOMD:3001/ctxtRESBD-POSTP").text
            if x == "N":
                session.findById("wnd[0]/usr/subSUB_ALL:SAPLCOIH:3001/ssubSUB_LEVEL:SAPLCOIH:1300/tabsTS_1300/tabpEINK").select()
                
                buscar_contrato.atribui_contrato()
                
                
                t = session.findById("wnd[0]/usr/subSUB_ALL:SAPLCOIH:3001/ssubSUB_LEVEL:SAPLCOIH:1300/subSUB_KMP:SAPLCOMD:3001/txtRESBD-POSNR").text
                print(t) 
                session.findById("wnd[0]/tbar[1]/btn[39]").press()
                if t == session.findById("wnd[0]/usr/subSUB_ALL:SAPLCOIH:3001/ssubSUB_LEVEL:SAPLCOIH:1300/subSUB_KMP:SAPLCOMD:3001/txtRESBD-POSNR").text:
                    session.findById("wnd[1]/tbar[0]/btn[0]").press()
                    break
            else:
                session.findById("wnd[0]/tbar[1]/btn[39]").press()

        session.findById("wnd[0]/tbar[0]/btn[3]").press()
        session.findById("wnd[0]/usr/subSUB_ALL:SAPLCOIH:3001/ssubSUB_LEVEL:SAPLCOIH:1101/tabsTS_1100/tabpKOAU").select()
        session.findById("wnd[0]/tbar[1]/btn[29]").press()
        session.findById("wnd[0]/usr/subSUB_ALL:SAPLCOIH:3001/ssubSUB_LEVEL:SAPLCOIH:1101/tabsTS_1100/tabpKOAU/ssubSUB_AUFTRAG:SAPLICO1:1100/tabsTABSTRIP/tabpTS10").select()
        valor = session.findById("wnd[0]/usr/subSUB_ALL:SAPLCOIH:3001/ssubSUB_LEVEL:SAPLCOIH:1101/tabsTS_1100/tabpKOAU/ssubSUB_AUFTRAG:SAPLICO1:1100/tabsTABSTRIP/tabpTS10/ssubVALUES:SAPLICO1:1110/tblSAPLICO1TCTRL_1110/txtPMCOEA-PKOSTENKGR[2,3]").text
        session.findById("wnd[0]/usr/subSUB_ALL:SAPLCOIH:3001/ssubSUB_LEVEL:SAPLCOIH:1101/tabsTS_1100/tabpIHKZ").select()
        session.findById("wnd[0]/usr/subSUB_ALL:SAPLCOIH:3001/ssubSUB_LEVEL:SAPLCOIH:1100/tabsTS_1100/tabpIHKZ/ssubSUB_AUFTRAG:SAPLCOIH:1120/subHEADER:SAPLCOIH:0154/txtCAUFVD-USER4").text = str(valor)
        session.findById("wnd[0]/tbar[0]/btn[0]").press()
        session.findById("wnd[0]/tbar[0]/btn[11]").press()
