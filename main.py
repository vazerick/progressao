import sys

from src.gui import gui

def atualizar():
    if gui.ui.aRadio.isChecked():
        pronome = "da Prof.ª"
    else:
        pronome = "do Prof.º"
    nome = gui.ui.nomeEdit.text()
    sei = gui.ui.seiEdit.text()
    comissao_1 = gui.ui.comissaoEdit1.text()
    comissao_2 = gui.ui.comissaoEdit2.text()
    comissao_3 = gui.ui.comissaoEdit3.text()
    de = gui.ui.deEdit.text()
    para = gui.ui.paraEdit.text()
    intesticio_inicio = gui.ui.dateEdit.text()
    intesticio_fim = gui.ui.dateEdit_2.text()
    ensino = gui.ui.ensinoSpin.text()
    pesquisa = gui.ui.pesquisaSpin.text()
    adm = gui.ui.admSpin.text()
    didatico = gui.ui.didaticoSpin.text()
    soma = gui.ui.somaSpin.text()
    if gui.ui.somaSpin_2.value() > 0:
        if gui.ui.ensinoSpin_2.value() > 0:
            ensino_exc = ", " + gui.ui.ensinoSpin_2.text()+", referentes à Atividade de Ensino"
        else:
            ensino_exc = ""
        if gui.ui.pesquisaSpin_2.value() > 0:
            pesquisa_exc = ", " + gui.ui.pesquisaSpin_2.text()+", referentes à Atividade de Pesquisa e/ou Extensão"
        else:
            pesquisa_exc = ""
        if gui.ui.admSpin_2.value() > 0:
            adm_exc = ", " + gui.ui.admSpin_2.text()+", referentes à Atividade de Administração, Representação e Outras"
        else:
            adm_exc = ""
        if gui.ui.didaticoSpin_2.value() > 0:
            didatico_exc = ", " + gui.ui.didaticoSpin_2.text()+", referentes ao Desempenho Didático"
        else:
            didatico_exc = ""
        soma_exc = ", totalizando a soma de "+gui.ui.somaSpin_2.text()
        abertura = "Pontos excedentes para próxima avaliação, " \
                   "que não tenham sido utilizados para completar a pontuação mínima total: "
        excedentes = abertura+ensino_exc+pesquisa_exc+adm_exc+didatico_exc+soma_exc
        excedentes = excedentes.replace(": , ", ": ")
    else:
        excedentes = "Não há pontos excedentes para uma próxima avaliação"
    print(excedentes)
    html = open("texto.html")
    texto = html.read()
    html.close()

    for a, b in [
        ("{pronome}", pronome),
        ("{nome}", nome),
        ("{sei}", sei),
        ("{comissao_1}", comissao_1),
        ("{comissao_2}", comissao_2),
        ("{comissao_3}", comissao_3),
        ("{de}", de),
        ("{para}", para),
        ("{intesticio_inicio}", intesticio_inicio),
        ("{intesticio_fim}", intesticio_fim),
        ("{ensino}", ensino),
        ("{pesquisa}", pesquisa),
        ("{adm}", adm),
        ("{didatico}", didatico),
        ("{soma}", soma),
        ("{excedentes}", excedentes),
    ]:
        print(a, b)
        texto = texto.replace(a, b)

    gui.ui.textBrowser.setHtml(texto)

gui = gui()

sinais = [
    gui.ui.aRadio.toggled,
    gui.ui.oRadio.toggled,
    gui.ui.nomeEdit.textChanged,
    gui.ui.seiEdit.textChanged,
    gui.ui.comissaoEdit1.textChanged,
    gui.ui.comissaoEdit2.textChanged,
    gui.ui.comissaoEdit3.textChanged,
    gui.ui.deEdit.textChanged,
    gui.ui.paraEdit.textChanged,
    gui.ui.dateEdit.dateChanged,
    gui.ui.dateEdit_2.dateChanged,
    gui.ui.ensinoSpin.valueChanged,
    gui.ui.pesquisaSpin.valueChanged,
    gui.ui.didaticoSpin.valueChanged,
    gui.ui.admSpin.valueChanged,
    gui.ui.somaSpin.valueChanged,
    gui.ui.ensinoSpin_2.valueChanged,
    gui.ui.pesquisaSpin_2.valueChanged,
    gui.ui.didaticoSpin_2.valueChanged,
    gui.ui.admSpin_2.valueChanged,
    gui.ui.somaSpin_2.valueChanged,
]
for i in sinais:
    i.connect(atualizar)

atualizar()

sys.exit(gui.app.exec_())