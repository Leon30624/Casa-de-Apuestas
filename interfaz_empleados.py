import flet as ft

from cruds_catalogo import EmpleadoCRUD, CargoCRUD  

class CrudEmpleados(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__(expand=True)
        self.page = page
        self.page.title = "CRUD Empleados"
        self.page.window_min_height = 500
        self.page.window_min_width = 100
        self.bgcolor = "Black"
        
        self.data = EmpleadoCRUD()
        self.cargo_crud = CargoCRUD()
        self.cargos = self.cargo_crud.leer_cargos() 
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
        
        self.contraseña = ft.TextField(
            label="Contraseña",
            label_style=ft.TextStyle(font_family="Minecraft", size = 12),
            border_color="White",
            text_style = ft.TextStyle(color = "white", font_family="Minecraft", size= 15),
            password=True
        )
        
        self.cargo = ft.Dropdown(
            label="Cargo",
            label_style=ft.TextStyle(font_family="Minecraft", size = 12),
            border_color="White",
            text_style = ft.TextStyle(color = "white", font_family="Minecraft", size= 15),
            options=[
                ft.dropdown.Option(str(c[0]), text=c[1]) for c in self.cargos
            ],
            width=150
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
                ft.DataColumn(ft.Text("Contraseña", color="white", weight="bold", font_family="Minecraft", size = 11, text_align="center")),
                ft.DataColumn(ft.Text("Cargo", color="white", weight="bold", font_family="Minecraft", size = 11, text_align="center")),
            ]
        )
        
        self.show_data()
        
        self.form = ft.Container(
            bgcolor = "#222222",
            border_radius = 10,
            col = 4,
            padding= 10,
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
                    self.cargo,
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
            bgcolor = "#222222",
            border_radius = 10,
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
        
        self.page.add(
            ft.ResponsiveRow(
                expand=True,
                controls=[
                    self.form,
                    self.table
                ]  
            )
        )
    
    def show_data(self):
        self.data_table.rows.clear()
        for x in self.data.leer_empleados():
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
        contraseña = self.contraseña.value
        cargo_id = self.cargo.value  # Aquí estamos tomando el ID del cargo seleccionado
        self.page.update()

        if len(telefono) > 0 and len(nombre) > 0 and len(correo) > 0 and len(cargo_id) > 0 and len(contraseña) > 0:
            contact_exist = False
            for row in self.data.leer_empleados():
                if row[0] == telefono:
                    contact_exist = True
                    break
            if not contact_exist:
                self.clean_fields()
                self.data.insertar_empleado(telefono, nombre, correo, contraseña, cargo_id)  # Pasar id_cargo aquí
                self.show_data()
            else:
                print("El contacto ya existe.")
    
    def cargar_cargos_dropdown(self):
        cargos = self.data.leer_cargos()
        self.cargo.options = [
            ft.dropdown.Option(str(c[0]), text=c[1]) for c in cargos
        ]
        self.cargo.value = str(cargos[0][0]) if cargos else None
        self.page.update()
    
    def get_index(self, e):
        e.control.selected = not e.control.selected
        
        name = e.control.cells[0].content.value
        for row in self.data.leer_empleados():
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
            self.contraseña.value = self.selected_row[3]
            self.cargo.value = self.selected_row[4]
            self.page.update()
        except TypeError:
            print("Error")  
        
    def update_data(self, e):
        telefono = self.telefono.value
        nombre = self.nombre.value
        correo = self.correo.value
        contraseña = self.contraseña.value
        cargo_id = self.cargo.value  # Aquí estamos tomando el ID del cargo seleccionado
        self.page.update()

        if len(telefono) and len(nombre) and len(correo) > 0:
            self.clean_fields()
            self.data.actualizar_empleado(self.selected_row[0], nombre, correo, contraseña, cargo_id)  # Pasar id_cargo aquí
            self.show_data()
            self.selected_row = None
            self.page.update()
    
    def search_data(self, e):
        search = self.search_filed.value.lower()
        telefono = list(filter(lambda x: search in x[0].lower(), self.data.leer_empleados()))
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
            self.data.eliminar_empleado(self.selected_row[0])  # Elimina el registro por teléfono
            self.clean_fields()
            self.show_data()  # Refresca la tabla para mostrar los cambios
            self.selected_row = None  # Limpia la selección actual
            
            # Limpia los campos manualmente
            self.telefono.value = ""
            self.nombre.value = ""
            self.correo.value = ""
            self.contraseña.value = ""
            self.cargo.value = ""
            
            self.page.update()
            print("Registro eliminado exitosamente.")
        else:
            print("No hay ninguna fila seleccionada para eliminar.")
    
    def clean_fields(self):
        self.telefono.value = ""
        self.nombre.value = ""
        self.correo.value = ""
        self.contraseña.value = ""
        self.cargo.value = ""
        
        self.page.update()

def main(page: ft.Page):
    CrudEmpleados(page)

ft.app(target=main)