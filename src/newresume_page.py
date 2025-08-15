import flet as ft  
from database_mgr import delete_row, get_all_rows
from file_mgr import ResumeFile

def main():  
    pass       

def create_newresume_page(page):  
    def handle_expansion_tile_change(e):  
        page.open(  
            ft.SnackBar(  
                ft.Text(  
                    f"ExpansionTile was {'expanded' if e.data=='true' else 'collapsed'}"  
                ),  
                duration=1000,  
            )  
        )  
        if e.control.trailing:  
            e.control.trailing.name = (  
                ft.Icons.ARROW_DROP_DOWN  
                if e.control.trailing.name == ft.Icons.ARROW_DROP_DOWN_CIRCLE  
                else ft.Icons.ARROW_DROP_DOWN_CIRCLE  
            )  
            page.update()  

    def on_button_click(e):  
        print("Button clicked inside expanded tile!")  

    return ft.Column([  
        ft.Text("Generate Page Content"),  
        ft.Row([  
            ft.FilledTonalButton("New", icon=ft.Icons.ADD_OUTLINED),  
            ft.FilledTonalButton("Save", icon=ft.Icons.SAVE_AS_OUTLINED),  
            ft.FilledTonalButton("Export", icon=ft.Icons.IMPORT_EXPORT_OUTLINED),             
        ]),  
        ft.Divider(),  
        ft.ExpansionTile(  
            title=ft.Text("Contact Info"),  
            leading=ft.IconButton(  
                icon=ft.Icons.ADD,   
                on_click=on_button_click,  
            ),  
            controls=[  
                ft.ListTile(  
                    title=ft.Text("Name"),  
                    subtitle=ft.Text("Bob"),  
                ),  
                ft.ListTile(  
                    title=ft.Text("Phone"),  
                    subtitle=ft.Text("555-1212"),  
                ),  
                ft.ListTile(  
                    title=ft.Text("email"),  
                    subtitle=ft.Text("Bob@yahoo.com"),  
                ),  
                ft.ListTile(  
                    title=ft.Text("URL"),  
                    subtitle=ft.Text("url.com"),  
                ),  
            ],  
        ),  
        ft.ExpansionTile(  
            title=ft.Text("Summary"),  
            controls=[  
                ft.ListTile(  
                    title=ft.Text("Summary text block"),  
                )  
            ],  
        ),  
        ft.ExpansionTile(  
            title=ft.Text("History"),  
            controls=[  
                ft.ExpansionTile(  
                    title=ft.Text("History 1"),  
                    controls=[  
                        ft.ListTile(  
                            title=ft.Text("Description 1"),  
                        ),  
                        ft.ListTile(  
                            title=ft.Text("Description 2"),  
                        ),  
                        ft.ListTile(  
                            title=ft.Text("Description 3"),  
                        ),  
                    ]  
                ),  
                ft.ExpansionTile(  
                    title=ft.Text("History 2"),  
                    controls=[  
                        ft.ListTile(  
                            title=ft.Text("Description 1"),  
                        ),  
                        ft.ListTile(  
                            title=ft.Text("Description 2"),  
                        ),  
                        ft.ListTile(  
                            title=ft.Text("Description 3"),  
                        ),  
                    ]  
                ),  
                ft.ExpansionTile(  
                    title=ft.Text("History 3"),  
                    controls=[  
                        ft.ListTile(  
                            title=ft.Text("Description 1"),  
                        ),  
                        ft.ListTile(  
                            title=ft.Text("Description 2"),  
                        ),  
                        ft.ListTile(  
                            title=ft.Text("Description 3"),  
                        ),  
                    ]  
                ),  
            ],  
        ),  
        ft.ExpansionTile(  
            title=ft.Text("Education"),  
            controls=[  
                ft.ListTile(  
                    ft.Text("School"),  
                    ft.Text("Start Date"),  
                    ft.Text("Finish Date"),  
                    ft.Text("Degree"),  
                )  
            ],  
        ),  
        ft.ExpansionTile(  
            title=ft.Text("Skills"),  
            controls=[  
                ft.ListTile(  
                    title=ft.Text("Skills"),  
                )  
            ],  
        ),  
    ])  

if __name__ == "__main__":  

    main()  