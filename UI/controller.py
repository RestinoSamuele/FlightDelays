import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._airportA=None
        self._airportP = None

    def handle_hello(self, e):
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def handleAnalizza(self,e):

        nMinStr=int(self._view._txtInNumC.value)
        try:
            nMin=int(nMinStr)
        except ValueError:
            self._view.txt_result.controls.append(ft.Text("Il valore inserito non è intero"))
            self._view.update_page()
            return
        self._model.buildGraph(nMin)
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato"))
        self._view.txt_result.controls.append(ft.Text(f"NumNodi {self._model.getNodi()}, Num archi {self._model.getArchi()}"))
        self._view._ddAeroportP.disabled=False
        self._view._ddAeroportA.disabled = False
        self._view._txtInNumTratto.disabled=False
        self._view._btnCercaItenerario.disabled=False
        self._view._btnConnessi.disabled=False
        self._view._btnCercaConnessione.disabled=False
        self._view.update_page()

    def handleConnessi(self,e):
        if self._airportP is None:
            self._view.txt_result.controls.append(ft.Text("Inserire l'aeroporto di partenza"))
            self._view.update_page()
            return
        v0=self._airportP
        vicini=self._model.getVicini(v0)
        self._view.txt_result.controls.append(ft.Text(f"I vicini di {v0} sono:"))
        for v in vicini:
            self._view.txt_result.controls.append(ft.Text(f"{v[1]} - {v[0]}"))
        self._view.update_page()


    def handleCercaItinerario(self,e):
        v0=self._airportP
        v1=self._airportA
        t=int(self._view._txtInNumTratto.value)

        path=self._model.getCamminoOttimo(v0,v1,t)
        self._view.txt_result.controls.clear()
        for p in path:
            self._view.txt_result.controls.append(ft.Text(p))
        self._view.update_page()

    def fillDD(self):
        aeroporti=self._model.getAllNodes()
        for n in aeroporti:
            self._view._ddAeroportA.options.append(ft.dropdown.Option(data=n,on_click=self.readDDAirportA,text=n.AIRPORT))
            self._view._ddAeroportP.options.append(ft.dropdown.Option(data=n, on_click=self.readDDAirportP, text=n.AIRPORT))

    def readDDAirportA(self,e):
        if e.control.data is None:
            self._airportA=None
        else:
            self._airportA=e.control.data

    def readDDAirportP(self,e):
        if e.control.data is None:
            self._airportP=None
        else:
            self._airportP=e.control.data

    def handleTestConnessione(self,e):
        self._view.txt_result.controls.clear()
        v0=self._airportP
        v1=self._airportA
        if not self._model.esistePercorso(v0, v1):
            self._view.txt_result.controls.append(ft.Text("Non esiste percorso"))
        else:
            self._view.txt_result.controls.append(ft.Text("Esiste percorso"))
        self._view.update_page()

        path=self._model.trovaCamminoBFS(v0,v1)
        self._view.txt_result.controls.append(ft.Text(f"Il cammino con minor numero di archi è: "))
        for p in path:
            self._view.txt_result.controls.append(ft.Text(f"{p}"))
        self._view.update_page()







