import flet as ft
import datetime

from cruds_catalogo import EventoCRUD

class CrudEventos(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__(expand=True)
        self.page = page
        #self.page.title = "CRUD Eventos"
        #self.page.window_min_height = 500
        #self.page.window_min_width = 100
        
        self.data = EventoCRUD()
        self.selected_row = None
        
        self.nombre_evento = ft.TextField(
            label="Nombre del Evento",
            label_style=ft.TextStyle(font_family="Minecraft", size=12),
            border_color="White",
            text_style=ft.TextStyle(color="white", font_family="Minecraft", size=15),
        )
        
        self.fecha_evento = ft.TextField(
            label="Fecha del Evento (DD/MM/YYYY)",
            hint_text="YYYY-MM-DD",
            label_style=ft.TextStyle(font_family="Minecraft", size=12),
            border_color="White",
            text_style=ft.TextStyle(color="white", font_family="Minecraft", size=15),
        )
        
        self.search_field = ft.TextField(
            label="Buscar por nombre de evento",
            suffix_icon=ft.Icons.SEARCH,
            border=ft.InputBorder.UNDERLINE,
            border_color="white",
            label_style=ft.TextStyle(color="white", font_family="Minecraft", size=12),
            text_style=ft.TextStyle(color="white", font_family="Minecraft", size=15),
            on_change=self.search_data,
        )
        
        self.data_table = ft.DataTable(
            expand=True,
            border=ft.border.all(2, "white"),
            data_row_color={ft.ControlState.SELECTED: "Gray", ft.ControlState.PRESSED: "Gray"},
            border_radius=10,
            show_checkbox_column=True,
            columns=[
                ft.DataColumn(ft.Text("ID Evento", color="white", weight="bold", font_family="Minecraft", size=11, text_align="center")),
                ft.DataColumn(ft.Text("Nombre Evento", color="white", weight="bold", font_family="Minecraft", size=11, text_align="center")),
                ft.DataColumn(ft.Text("Fecha Evento", color="white", weight="bold", font_family="Minecraft", size=11, text_align="center")),
            ]
        )
        
        self.show_data()
        
        self.form = ft.Container(
            bgcolor = "#2f3136",
            border_radius = ft.border_radius.all(8),
            col = 4,
            padding = 20,
            margin=ft.Margin(left=0, right=0, top=10, bottom=10),
            width=350,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                horizontal_alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Text("Ingrese los datos del evento: ",
                            size=40,
                            text_align="center",
                            font_family="Minecrafter Alt",),
                    
                    self.nombre_evento,
                    self.fecha_evento,
                    
                    ft.Container(
                        ft.Row(
                            spacing=5,
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.TextButton(
                                    text="Guardar",
                                    icon=ft.Icons.SAVE,
                                    style=ft.ButtonStyle(
                                        color="Black",
                                        bgcolor="White",
                                        icon_color="Black",
                                        text_style=ft.TextStyle(font_family="Minecraft", size=10)
                                    ),
                                    on_click=self.add_data
                                ),
                                ft.TextButton(
                                    text="Actualizar",
                                    icon=ft.Icons.UPDATE,
                                    style=ft.ButtonStyle(
                                        color="Black",
                                        bgcolor="White",
                                        icon_color="Black",
                                        text_style=ft.TextStyle(font_family="Minecraft", size=10)
                                    ),
                                    on_click=self.update_data
                                ),
                                ft.TextButton(
                                    text="Borrar",
                                    icon=ft.Icons.DELETE,
                                    style=ft.ButtonStyle(
                                        color="Black",
                                        bgcolor="White",
                                        icon_color="Black",
                                        text_style=ft.TextStyle(font_family="Minecraft", size=10)
                                    ),
                                    on_click=self.delete_data
                                )
                            ]
                        )
                    )
                ]
            )
        )
        
        self.table = ft.Container(
            bgcolor = "#2f3136",
            border_radius = ft.border_radius.all(8),
            padding=20,
            margin=ft.Margin(left=5, right=10, top=10, bottom=10),
            col = 8,
            content=ft.Column(
                controls=[
                    ft.Container(
                        padding=10,
                        content=ft.Row(
                            controls=[
                                self.search_field,
                                ft.IconButton(tooltip="Editar",
                                              icon=ft.Icons.EDIT,
                                              icon_color="white",
                                              on_click=self.edit_field_text,),
                            ]
                        )
                    ),
                    ft.Column(
                        expand=True,
                        scroll="auto",
                        controls=[
                            ft.ResponsiveRow([
                                self.data_table,
                            ])
                        ]
                    )
                ]
            )
        )
        
        self.content = ft.ResponsiveRow(
            expand=True,
            controls=[
                self.form,
                self.table
            ]
        )
        
        self.controls = [self.content]
        
        """self.page.add(
            ft.ResponsiveRow(
                expand=True,
                controls=[
                    self.form,
                    self.table
                ]  
            )
        )"""
    
    def show_data(self):
        self.data_table.rows.clear()
        for x in self.data.leer_eventos():
            self.data_table.rows.append(
                ft.DataRow(
                    on_select_changed=self.get_index,
                    cells=[
                        ft.DataCell(ft.Text(str(x[0]), color="white", font_family="Minecraft", size=11)),
                        ft.DataCell(ft.Text(x[1], color="white", font_family="Minecraft", size=11)),
                        ft.DataCell(ft.Text(x[2], color="white", font_family="Minecraft", size=11)),
                    ]
                )
            )
        self.page.update()
        
    def add_data(self, e):
        nombre_evento = self.nombre_evento.value
        fecha_evento = self.fecha_evento.value
        self.page.update()
        
        if len(nombre_evento) > 0 and len(fecha_evento) > 0:
            event_exist = False
            for row in self.data.leer_eventos():
                if row[1] == nombre_evento:
                    event_exist = True
                    break
            if not event_exist:
                self.clean_fields()
                self.data.insertar_evento(nombre_evento, fecha_evento)
                self.show_data()
            else:
                print("El evento ya existe.")
    
    def get_index(self, e):
        e.control.selected = not e.control.selected
        
        try:
            name = int(e.control.cells[0].content.value)
            for row in self.data.leer_eventos():
                if row[0] == name:
                    self.selected_row = row
                    break
            print(self.selected_row)
        except Exception as ex:
            print("Error al seleccionar fila:", ex)
        
        self.page.update()

       
    def edit_field_text(self, e):
        try:
            self.nombre_evento.value = self.selected_row[1]
            self.fecha_evento.value = self.selected_row[2]
            self.page.update()
        except TypeError:
            print("Error")  
        
    def update_data(self, e):
        nombre_evento = self.nombre_evento.value
        fecha_evento = self.fecha_evento.value
        self.page.update()
        
        if len(nombre_evento) > 0 and len(str(fecha_evento)) > 0:
            self.clean_fields()
            self.data.actualizar_evento(self.selected_row[0], nombre_evento, fecha_evento)
            self.show_data()
            self.selected_row = None
            self.page.update()
    
    def search_data(self, e):
        search = self.search_field.value.lower()
        eventos = list(filter(lambda x: search in x[1].lower(), self.data.leer_eventos()))
        self.data_table.rows = []
        if not self.search_field.value == "":
            if len(eventos) > 0:
                for x in eventos:
                    self.data_table.rows.append(
                        ft.DataRow(
                            on_select_changed=self.get_index,
                            cells=[
                                ft.DataCell(ft.Text(str(x[0]))),
                                ft.DataCell(ft.Text(x[1])),
                                ft.DataCell(ft.Text(x[2])),
                            ]
                        )
                    )
                    self.page.update()
        else:
            self.show_data()

    def delete_data(self, e):
        if self.selected_row is not None: 
            self.data.eliminar_evento(self.selected_row[0]) 
            self.clean_fields()
            self.show_data() 
            self.selected_row = None  

            self.nombre_evento.value = ""
            self.fecha_evento.value = ""
            
            self.page.update()
            print("Evento eliminado exitosamente.")
        else:
            print("No hay ningún evento seleccionado para eliminar.")

    def clean_fields(self):
        self.nombre_evento.value = ""
        self.fecha_evento.value = ""
        
        self.page.update()

def main(page: ft.Page):
    CrudEventos(page)

if __name__ == "__main__":
    ft.app(target=main)
