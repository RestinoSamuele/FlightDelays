import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Tdp flights manager 2024", color="blue", size=24)
        self._page.controls.append(self._title)

        self._txtInNumC=ft.TextField(label="Num compagnie", width=250)
        self._btnAnalizza=ft.ElevatedButton(text="Analizza Aeroporti",on_click=self._controller.handleAnalizza)
        self._btnConnessi=ft.ElevatedButton(text="Aeropèorti Connessi", on_click=self._controller.handleConnessi,disabled=True)
        row1=ft.Row([self._txtInNumC,self._btnAnalizza,self._btnConnessi],alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self._ddAeroportP=ft.Dropdown(label="Partenza",disabled=True)
        self._ddAeroportA = ft.Dropdown(label="Arrivo",disabled=True)
        self._btnCercaConnessione=ft.ElevatedButton(text="Test Connessione",on_click=self._controller.handleTestConnessione,disabled=True)
        self._controller.fillDD()
        row2 = ft.Row([self._ddAeroportP, self._ddAeroportA,self._btnCercaConnessione], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        self._txtInNumTratto=ft.TextField(label="Num Tratto Max",width=250,disabled=True)
        self._btnCercaItenerario=ft.ElevatedButton(text="Cerca Itinerarario",on_click=self._controller.handleCercaItinerario,disabled=True)
        row3 = ft.Row([self._txtInNumTratto, self._btnCercaItenerario], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)
        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
