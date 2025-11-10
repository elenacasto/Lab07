import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    # funzione che riempie il dropdown con i dati presi dal model
    def popola_dropdown(self):
        musei = self._model.get_musei()
        if musei:
            self._view.mostra_musei.options = [ft.dropdown.Option(m) for m in musei]
        else:
            self._view.show_alert("Museo non trovato!")

        epoche = self._model.get_epoche()
        if epoche:
            self._view.mostra_epoche.options = [ft.dropdown.Option(e) for e in epoche]
        else:
            self._view.show_alert("Epoca non trovata!")

        self._view.page.update()

    # CALLBACKS DROPDOWN
    def on_museo_change(self, e):
        self.museo_selezionato = e.control.value
        print(f"Museo selezionato: {self.museo_selezionato}")

        self.handler_btn_mostra_artefatti()

    def on_epoca_change(self, e):
        self.epoca_selezionata = e.control.value
        print(f"Epoca selezionata: {self.epoca_selezionata}")

        self.handler_btn_mostra_artefatti()

    # AZIONE: MOSTRA ARTEFATTI
    def handler_btn_mostra_artefatti(self):
        print("Mostra artefatti")
        museo = self._view.mostra_musei.value
        if not museo:
            self._view.show_alert("Selezaiona prima un museo!")
            return

        epoca = self._view.mostra_epoche.value
        if not epoca:
            self._view.show_alert("Selezaiona prima un epoca!")
            return

        artefatti = self._model.get_artefatti_filtrati(museo, epoca)
        if not artefatti:
            self._view.show_alert(f"Nessun artefatto trovato per {museo}!")
            return