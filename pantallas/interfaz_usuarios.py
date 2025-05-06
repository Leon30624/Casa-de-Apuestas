import flet as ft
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cruds_catalogo import Usuario

class CrudUsuarios(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__(expand=True)
        self.page = page
        #self.page.title = "CRUD Usuarios"
        #self.page.window_min_height = 500
        #self.page.window_min_width = 100
        
        self.data = Usuario()
        self.selected_row = None
        
        self.nombre = ft.TextField(
            label="Nombre",
            label_style=ft.TextStyle(font_family="Minecraft", size = 12),
            border_color="White",
            text_style = ft.TextStyle(color = "white", font_family="Minecraft", size= 15),
        )
        
        self.telefono = ft.TextField(
            label="Telefono",
            label_style=ft.TextStyle(font_family="Minecraft", size = 12),
            border_color="White",
            text_style = ft.TextStyle(color = "white", font_family="Minecraft", size= 15),
            input_filter=ft.NumbersOnlyInputFilter(),
            max_length=10,
        )
        
        self.correo = ft.TextField(
            label="Correo",
            label_style=ft.TextStyle(font_family="Minecraft", size = 12),
            border_color="White",
            text_style = ft.TextStyle(color = "white", font_family="Minecraft", size= 15),
        )
        
        self.saldo = ft.TextField(
            label="Saldo",
            label_style=ft.TextStyle(font_family="Minecraft", size = 12),
            border_color="White",
            text_style = ft.TextStyle(color = "white", font_family="Minecraft", size= 15),
        )
        
        self.contraseña = ft.TextField(
            label="Contraseña",
            label_style=ft.TextStyle(font_family="Minecraft", size = 12),
            border_color="White",
            text_style = ft.TextStyle(color = "white", font_family="Minecraft", size= 15),
            password=True
        )
        
        self.search_filed = ft.TextField(
            label = "Buscar por telefono",
            suffix_icon=ft.Icons.SEARCH,
            border = ft.InputBorder.UNDERLINE,
            border_color = "white",
            label_style = ft.TextStyle(color = "white", font_family="Minecraft", size = 12),
            text_style = ft.TextStyle(color = "white", font_family="Minecraft", size= 15),
            input_filter=ft.NumbersOnlyInputFilter(),
            on_change=self.search_data,
        )
        
        self.data_table = ft.DataTable(
            expand = True,
            border = ft.border.all(2, "white"),
            data_row_color = {ft.ControlState.SELECTED: "Gray", 
                              ft.ControlState.PRESSED: "Gray"},
            border_radius=10,
            show_checkbox_column=True,
            columns = [
                ft.DataColumn(ft.Text("Telefono", color="white", weight="bold", font_family="Minecraft", size = 11, text_align="center"), numeric = True),
                ft.DataColumn(ft.Text("Nombre", color="white", weight="bold", font_family="Minecraft", size = 11, text_align="center")),
                ft.DataColumn(ft.Text("Correo", color="white", weight="bold", font_family="Minecraft", size = 11, text_align="center")),
                ft.DataColumn(ft.Text("Saldo", color="white", weight="bold", font_family="Minecraft", size = 11, text_align="center"), numeric = True),
                ft.DataColumn(ft.Text("Contraseña", color="white", weight="bold", font_family="Minecraft", size = 11, text_align="center")),
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
            content = ft.Column(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                horizontal_alignment=ft.MainAxisAlignment.CENTER,
                controls = [
                    ft.Text("Ingrese sus datos: ",
                            size = 40,
                            text_align = "center",
                            font_family = "Minecrafter Alt",),
                    
                    self.nombre,
                    self.telefono,
                    self.correo,
                    self.saldo,
                    self.contraseña,
                    
                    ft.Container(
                        ft.Row(
                            spacing = 5,
                            alignment = ft.MainAxisAlignment.CENTER,
                            controls = [
                                ft.TextButton(
                                    text = "Guardar",
                                    icon = ft.Icons.SAVE,
                                    style = ft.ButtonStyle(
                                        color = "Black",
                                        bgcolor = "White",
                                        icon_color="Black",
                                        text_style=ft.TextStyle(font_family="Minecraft", size = 10)
                                    ),
                                    on_click = self.add_data
                                ),
                                ft.TextButton(
                                    text = "Actualizar",
                                    icon = ft.Icons.UPDATE,
                                    style = ft.ButtonStyle(
                                        color = "Black",
                                        bgcolor = "White",
                                        icon_color="Black",
                                        text_style=ft.TextStyle(font_family="Minecraft", size = 10)
                                    ),
                                    on_click = self.update_data
                                ),
                                ft.TextButton(
                                    text = "Borrar",
                                    icon = ft.Icons.DELETE,
                                    style = ft.ButtonStyle(
                                        color = "Black",
                                        bgcolor = "White",
                                        icon_color="Black",
                                        text_style=ft.TextStyle(font_family="Minecraft", size = 10)
                                    ),
                                    on_click = self.delete_data
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
            content = ft.Column(
                controls = [
                    ft.Container(
                        padding = 10,
                        content = ft.Row(
                            controls = [
                                self.search_filed,
                                ft.IconButton(tooltip = "Editar",
                                            icon = ft.Icons.EDIT,
                                            icon_color = "white",
                                            on_click=self.edit_field_text,),
                            ]
                        )
                    ),
                    ft.Column(
                        expand = True,
                        scroll = "auto",
                        controls = [
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
        for x in self.data.leer_usuarios():
            self.data_table.rows.append(
                ft.DataRow(
                    on_select_changed=self.get_index,
                    cells=[
                        ft.DataCell(ft.Text(x[0], color="white", font_family="Minecraft", size = 11)),
                        ft.DataCell(ft.Text(x[1], color="white", font_family="Minecraft", size = 11)),
                        ft.DataCell(ft.Text(x[2], color="white", font_family="Minecraft", size = 11)),
                        ft.DataCell(ft.Text(x[3], color="white", font_family="Minecraft", size = 11)),
                        ft.DataCell(ft.Text(x[4], color="white", font_family="Minecraft", size = 11)),
                    ]
                )
            )
        self.page.update()
        
    def add_data(self, e):
        telefono = self.telefono.value
        nombre = self.nombre.value
        correo = self.correo.value
        saldo = self.saldo.value
        contraseña = self.contraseña.value
        self.page.update()
        
        if len(telefono) > 0 and len(nombre) > 0 and len(correo) > 0 and len(saldo) > 0 and len(contraseña) > 0:
            contact_exist = False
            for row in self.data.leer_usuarios():
                if row[0] == telefono:
                    contact_exist = True
                    break
            if not contact_exist:
                self.clean_fields()
                self.data.insertar_usuarios(telefono, nombre, correo, saldo, contraseña)
                self.show_data()
            else:
                print("El contacto ya existe.")
    
    def get_index(self, e):
        e.control.selected = not e.control.selected
        
        name = e.control.cells[0].content.value
        for row in self.data.leer_usuarios():
            if row[0] == name:
                self.selected_row = row
                break
        print(self.selected_row)
        self.page.update()
       
    def edit_field_text(self, e):
        try:
            self.telefono.value = self.selected_row[0]
            self.nombre.value = self.selected_row[1]
            self.correo.value = self.selected_row[2]
            self.saldo.value = self.selected_row[3]
            self.contraseña.value = self.selected_row[4]
            self.page.update()
        except TypeError:
            print("Error")  
        
    def update_data(self, e):
        telefono = self.telefono.value
        nombre = self.nombre.value
        correo = self.correo.value
        saldo = self.saldo.value
        contraseña = self.contraseña.value
        self.page.update()
        
        if len(telefono) and len(nombre) and len(correo) > 0:
            self.clean_fields()
            self.data.actualizar_usuarios(self.selected_row[0], nombre, correo, saldo, contraseña)
            self.show_data()
            self.selected_row = None
            self.page.update()
    
    def search_data(self, e):
        search = self.search_filed.value.lower()
        telefono = list(filter(lambda x: search in x[0].lower(), self.data.leer_usuarios()))
        self.data_table.rows = []
        if not self.search_filed.value == "":
            if len(telefono) > 0:
                for x in telefono:
                    self.data_table.rows.append(
                        ft.DataRow(
                            on_select_changed=self.get_index,
                            cells=[
                                ft.DataCell(ft.Text(str(x[0]))),
                                ft.DataCell(ft.Text(x[1])),
                                ft.DataCell(ft.Text(x[2])),
                                ft.DataCell(ft.Text(str(x[3]))),
                                ft.DataCell(ft.Text(x[4])),
                            ]
                        )
                    )
                    self.page.update()
        else:
            self.show_data()

    def delete_data(self, e):
        if self.selected_row is not None:  # Verifica si hay una fila seleccionada
            self.data.eliminar_usuarios(self.selected_row[0])  # Elimina el registro por teléfono
            self.clean_fields()
            self.show_data()  # Refresca la tabla para mostrar los cambios
            self.selected_row = None  # Limpia la selección actual
            
            # Limpia los campos manualmente
            self.telefono.value = ""
            self.nombre.value = ""
            self.correo.value = ""
            self.saldo.value = ""
            self.contraseña.value = ""
            
            self.page.update()
            print("Registro eliminado exitosamente.")
        else:
            print("No hay ninguna fila seleccionada para eliminar.")


    
    def clean_fields(self):
        self.telefono.value = ""
        self.nombre.value = ""
        self.correo.value = ""
        self.saldo.value = ""
        self.contraseña.value = ""
        
        self.page.update()

def main(page: ft.Page):
    CrudUsuarios(page)

if __name__ == "__main__":
    ft.app(target=main)