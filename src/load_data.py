from openpyxl import load_workbook


class Listas:
    def __init__(self):
        self.cpp = []
        self.descricao = []
        self.item = []
        self.contrato = []
        self.valor = []

    def load_data(self):
        wb = load_workbook("C:\\Users\\547058\\Desktop\\projeto\\Lancamento_custo\\.venv\\docs\\info.xlsx")
        ws = wb["Planilha1"]
        for row in ws.iter_rows(min_row=1):
            self.cpp.append(row[0].value)
            self.descricao.append(row[1].value)
            self.item.append(row[2].value)
            self.contrato.append(row[3].value)
            self.valor.append(row[4].value)
        print("upload concluido com sucesso!")

