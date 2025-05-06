import flet as ft

from cruds_catalogo import ArticuloCRUD, CategoriaCRUD

class CrudArticulos(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__(expand=True)
        self.page = page
        #self.page.title = "CRUD Articulos"
        #self.page.window_min_height = 500
        #self.page.window_min_width = 100
        
        self.data = ArticuloCRUD()
        self.cat_crud = CategoriaCRUD()
        self.categorias = self.cat_crud.leer_categorias()
        self.selected_row = None
        
        self.nombre = ft.TextField(
            label="Nombre",
            label_style=ft.TextStyle(font_family="Minecraft", size = 12),
            border_color="White",
            text_style = ft.TextStyle(color = "white", font_family="Minecraft", size= 15),
        )
        
        self.descripcion = ft.TextField(
            label="Descripcion",
            label_style=ft.TextStyle(font_family="Minecraft", size = 12),
            border_color="White",
            text_style = ft.TextStyle(color = "white", font_family="Minecraft", size= 15),
        )
        
        self.precio = ft.TextField(
            label="Precio",
            label_style=ft.TextStyle(font_family="Minecraft", size = 12),
            border_color="White",
            text_style = ft.TextStyle(color = "white", font_family="Minecraft", size= 15),
        )
        
        self.costo = ft.TextField(
            label="Costo",
            label_style=ft.TextStyle(font_family="Minecraft", size = 12),
            border_color="White",
            text_style = ft.TextStyle(color = "white", font_family="Minecraft", size= 15),
        )
        
        self.stock = ft.TextField(
            label="Stock",
            label_style=ft.TextStyle(font_family="Minecraft", size = 12),
            border_color="White",
            text_style = ft.TextStyle(color = "white", font_family="Minecraft", size= 15),
        )
        
        self.categoria = ft.Dropdown(
            label="Categoria",
            label_style=ft.TextStyle(font_family="Minecraft", size = 12),
            border_color="White",
            text_style = ft.TextStyle(color = "white", font_family="Minecraft", size= 15),
            options=[
                ft.dropdown.Option(str(c[0]), text=c[1]) for c in self.categorias
            ],
            width=150
        )
        
        self.codigo = ft.TextField(
            label="Codigo",
            label_style=ft.TextStyle(font_family="Minecraft", size = 12),
            border_color="White",
            text_style = ft.TextStyle(color = "white", font_family="Minecraft", size= 15),
        )
        
        self.search_filed = ft.TextField(
            label = "Buscar por Codigo",
            suffix_icon=ft.Icons.SEARCH,
            border = ft.InputBorder.UNDERLINE,
            border_color = "white",
            label_style = ft.TextStyle(color = "white", font_family="Minecraft", size = 12),
            text_style = ft.TextStyle(color = "white", font_family="Minecraft", size= 15),
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
                ft.DataColumn(ft.Text("Codigo", color="white", weight="bold", font_family="Minecraft", size = 11, text_align="center")),
                ft.DataColumn(ft.Text("Nombre", color="white", weight="bold", font_family="Minecraft", size = 11, text_align="center")),
                ft.DataColumn(ft.Text("Descripcion", color="white", weight="bold", font_family="Minecraft", size = 11, text_align="center")),
                ft.DataColumn(ft.Text("Precio", color="white", weight="bold", font_family="Minecraft", size = 11, text_align="center")),
                ft.DataColumn(ft.Text("Costo", color="white", weight="bold", font_family="Minecraft", size = 11, text_align="center")),
                ft.DataColumn(ft.Text("Stock", color="white", weight="bold", font_family="Minecraft", size = 11, text_align="center")),
                ft.DataColumn(ft.Text("Categoria", color="white", weight="bold", font_family="Minecraft", size = 11, text_align="center")),
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
                    self.descripcion,
                    self.precio,
                    self.costo,
                    self.stock,
                    self.categoria,
                    self.codigo,
                    
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
        for x in self.data.leer_articulos():
            self.data_table.rows.append(
                ft.DataRow(
                    on_select_changed=self.get_index,
                    cells=[
                        ft.DataCell(ft.Text(x[0], color="white", font_family="Minecraft", size = 11)),
                        ft.DataCell(ft.Text(x[1], color="white", font_family="Minecraft", size = 11)),
                        ft.DataCell(ft.Text(x[2], color="white", font_family="Minecraft", size = 11)),
                        ft.DataCell(ft.Text(x[3], color="white", font_family="Minecraft", size = 11)),
                        ft.DataCell(ft.Text(x[4], color="white", font_family="Minecraft", size = 11)),
                        ft.DataCell(ft.Text(x[5], color="white", font_family="Minecraft", size = 11)),
                        ft.DataCell(ft.Text(x[6], color="white", font_family="Minecraft", size = 11)),
                    ]
                )
            )
        self.page.update()
        
    def add_data(self, e):
        nombre = self.nombre.value
        descripcion = self.descripcion.value
        precio = self.precio.value
        costo = self.costo.value
        stock = self.stock.value
        categoria_id = self.categoria.value
        codigo = self.codigo.value
        self.page.update()

        if len(codigo) > 0 and len(nombre) > 0 and len(descripcion) > 0 and len(precio) > 0 and len(costo) > 0 and len(stock) > 0:
            contact_exist = False
            for row in self.data.leer_articulos():
                if row[0] == codigo:
                    contact_exist = True
                    break
            if not contact_exist:
                self.clean_fields()
                self.data.insertar_articulo(codigo, nombre, descripcion, precio, costo, stock, categoria_id)
                self.show_data()
            else:
                print("El contacto ya existe.")
    
    def cargar_categorias_dropdown(self):
        categorias = self.data.leer_categorias()
        self.categoria.options = [
            ft.dropdown.Option(str(c[0]), text=c[1]) for c in categorias
        ]
        self.categoria.value = str(categorias[0][0]) if categorias else None
        self.page.update()
    
    def get_index(self, e):
        e.control.selected = not e.control.selected
        
        name = e.control.cells[0].content.value
        for row in self.data.leer_articulos():
            if row[0] == name:
                self.selected_row = row
                break
        print(self.selected_row)
        self.page.update()
       
    def edit_field_text(self, e):
        try:
            self.codigo.value = self.selected_row[0]    
            self.nombre.value = self.selected_row[1]      
            self.descripcion.value = self.selected_row[2] 
            self.precio.value = self.selected_row[3]     
            self.costo.value = self.selected_row[4]        
            self.stock.value = self.selected_row[5]        
            self.categoria.value = str(self.selected_row[6])  
            self.page.update()
        except TypeError:
            print("Error")  
        
    def update_data(self, e):
        nombre = self.nombre.value
        descripcion = self.descripcion.value
        precio = self.precio.value
        costo = self.costo.value
        stock = self.stock.value
        codigo = self.codigo.value
        categoria_id = self.categoria.value
        self.page.update()

        if len(codigo) and len(nombre) and len(descripcion) > 0:
            self.clean_fields()
            self.data.actualizar_articulo(self.selected_row[0], nombre, descripcion, precio, costo, stock, categoria_id)
            self.show_data()
            self.selected_row = None
            self.page.update()
    
    def search_data(self, e):
        search = self.search_filed.value.lower()
        codigo = list(filter(lambda x: search in x[0].lower(), self.data.leer_articulos()))
        self.data_table.rows = []
        if not self.search_filed.value == "":
            if len(codigo) > 0:
                for x in codigo:
                    self.data_table.rows.append(
                        ft.DataRow(
                            on_select_changed=self.get_index,
                            cells=[
                                ft.DataCell(ft.Text(x[0])),
                                ft.DataCell(ft.Text(x[1])),
                                ft.DataCell(ft.Text(x[2])),
                                ft.DataCell(ft.Text(x[3])),
                                ft.DataCell(ft.Text(x[4])),
                                ft.DataCell(ft.Text(x[5])),
                                ft.DataCell(ft.Text(x[6])),
                                ft.DataCell(ft.Text(x[7])),
                            ]
                        )
                    )
                    self.page.update()
        else:
            self.show_data()

    def delete_data(self, e):
        if self.selected_row is not None:
            self.data.eliminar_articulo(self.selected_row[0]) 
            self.clean_fields()
            self.show_data()
            self.selected_row = None 
            
            self.nombre.value = ""
            self.descripcion.value = ""
            self.precio.value = ""
            self.costo.value = ""
            self.stock.value = ""
            self.codigo.value = ""
            self.categoria.value = None
            
            self.page.update()
            print("Registro eliminado exitosamente.")
        else:
            print("No hay ninguna fila seleccionada para eliminar.")
    
    def clean_fields(self):
        self.nombre.value = ""
        self.descripcion.value = ""
        self.precio.value = ""
        self.costo.value = ""
        self.stock.value = ""
        self.codigo.value = ""
        
        self.page.update()

def main(page: ft.Page):
    CrudArticulos(page)

if __name__ == "__main__":
    ft.app(target=main)