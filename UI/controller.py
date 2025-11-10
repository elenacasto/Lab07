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
    def popola_musei(self):
        musei = self._model.get_musei()
        self._view.mostra_musei.options.clear()
        self._view.mostra_musei.options.append(ft.dropdown.Option(key="", text=musei))
        for museo in musei:
            self._view.mostra_musei.options.append(ft.dropdown.Option(key=museo.id, text=museo.nome))

        self._view.update()

    def popola_epoche(self):
        epoche = self._model.get_epoche()
        self._view.mostra_epoche.options.clear()
        self._view.mostra_epoche.options.append(ft.dropdown.Option(key="", text=epoche))
        for epoca in epoche:
            self._view.mostra_epoche.options.append(ft.dropdown.Option(key=epoca, text=epoca))

        self._view.update()

    # CALLBACKS DROPDOWN
    def on_museo_change(self, e):
        self.museo_selezionato = e.control.value

    def on_epoca_change(self, e):
        self.epoca_selezionata = e.control.value

    # AZIONE: MOSTRA ARTEFATTI
    def handler_btn_mostra_artefatti(self):
        print("Mostra artefatti")
        museo = self.museo_selezionato
        if not museo:
            self._view.show_alert("Selezaiona prima un museo!")
            return

        epoca = self.epoca_selezionata
        if not epoca:
            self._view.show_alert("Selezaiona prima un epoca!")
            return

        artefatti = self._model.get_artefatti_filtrati(museo, epoca)
        if not artefatti:
            self._view.show_alert(f"Nessun artefatto trovato per {museo}!")
            return
        else:
            for artefatto in artefatti:
                self._view.mostra_artefatti.controls.append(
                    ft.Text(f"{artefatto.id}: {artefatto.nome}, {artefatto.tipologia}, {artefatto.epoca}")
                )

        self._view.update()