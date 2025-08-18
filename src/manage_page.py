import flet as ft  
from database_mgr import delete_row, get_all_rows  

def main():  
    pass       

def create_manage_page(page):  
    def get_options():  
        content_array = ["Contact", "Summary", "Job History","Education","Skills","Projects"]  
        options = []  
        for item in content_array:  
            options.append(  
                ft.DropdownOption(  
                    key=item,  
                    content=ft.Text(value=item)  
                )  
            )  
        return options  

    def dropdown_changed(e):  
        list_view.controls.clear()  

        if e.control.value == "Contact":  
            my_data = ["Contact 1", "Contact 2", "Contact 3","Contact 4"]  
        elif e.control.value == "Summary":  
            my_data = ["Summary 1", "Summary 2", "Summary 3"]  
        elif e.control.value == "Job History":  
            my_data = ["Job 1", "Job 2", "Job 3"]  
        elif e.control.value == "Education":  
            my_data = ["Education 1", "Certification 1"]  
        elif e.control.value == "Skills":    
            my_data = ["Skills 1", "Skills 2", "Skills 3","Skills 4"]  
        elif e.control.value == "Projects":    
            my_data = ["Projects 1", "Projects 2"]  
        else:  
            my_data = None  

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
                                text="Modify",  
                                on_click=print("Modify!")),  
                            ft.PopupMenuItem(  
                                text="Delete",  
                                on_click=print("Delete!")),  
                        ],  
                    ),  
                )  
            )  
        page.update()  

    list_view = ft.ListView()  
    list_view.controls.append(  
        ft.ListTile(  
            title=ft.Text("Select an option from the dropdown"),  
            subtitle=ft.Text("No details available yet."),  
            leading=ft.Icon(ft.Icons.INFO),  
            visible=True,  
        )  
    )  

    return ft.Column([  
        ft.Text("Manage Page Content"),  
        ft.Dropdown(  
                    editable=True,  
                    label="Select an Option",  
                    options=get_options(),  
                    on_change=dropdown_changed,  
        ),  
        ft.Card(  
            #content=ft.Container(  
            #width=500,  
            content=ft.Column(  
                [  
                    list_view  
                ],  
                spacing=0,  
            ),  
            #padding=ft.padding.symmetric(vertical=10),  
            #)  
        )  
    ])  

if __name__ == "__main__":  
    main()  