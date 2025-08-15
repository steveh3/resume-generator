import flet as ft  
from database_mgr import delete_row, get_all_rows
from file_mgr import ResumeFile

def main():  
    pass  

def create_main_page(page):  
    def get_listtile_options():  

        # Get DATA here  
        my_data = ["Item 1", "Item 2", "Item 3","Item 4"]  
        list_view = ft.ListView(expand=1, spacing=10, padding=20)  

        for item in my_data:  
            list_view.controls.append(  
                ft.ListTile(  
                    leading=ft.Icon(ft.Icons.NOTE),  
                    title=ft.Text(  
                        f"Name of {item}"  
                    ),  
                    subtitle=ft.Text(f"Status of {item}."),  
                    trailing=ft.PopupMenuButton(  
                        icon=ft.Icons.MORE_VERT,  
                        items=[  
                            ft.PopupMenuItem(  
                                text="Continue",  
                                on_click=print("Continue!")),  
                            ft.PopupMenuItem(  
                                text="Modify",  
                                on_click=print("Modify!")),  
                            ft.PopupMenuItem(  
                                text="Save",  
                                on_click=print("Save!")),  
                            ft.PopupMenuItem(  
                                text="Delete",  
                                on_click=print("Delete!")),  
                        ],  
                    ),  
                )  
            )  
        return list_view

    return ft.Column([
        ft.Text("Resumes"),
        ft.Card(  
            #content=ft.Container(  
            #width=500,  
            content=ft.Column(  
                [  
                    get_listtile_options()  
                ],  
                spacing=0,  
            ),  
            #padding=ft.padding.symmetric(vertical=10),  
            #)  
        )  
    ])   

if __name__ == "__main__":  
    main()  