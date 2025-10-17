import flet as ft
from database_mgr import delete_row, get_all_rows, add_contact, add_summary, add_job_history, add_job_description, add_education, add_skill

def main():
    pass

def create_manage_page(page):
    def get_options():
        content_array = ["Contact", "Summary", "Job History", "Education", "Skills", "Projects"]
        options = []
        for item in content_array:
            options.append(
                ft.DropdownOption(
                    key=item,
                    content=ft.Text(item)
                )
            )
        return options

    # create shared controls first so handlers can reference them
    list_view = ft.ListView(expand=1, spacing=10, padding=10)
    list_view.controls.append(
        ft.ListTile(
            title=ft.Text("Select an option from the dropdown"),
            subtitle=ft.Text("No details available yet."),
            leading=ft.Icon(ft.Icons.INFO),
            visible=True,
        )
    )

    dropdown = ft.Dropdown(
        editable=True,
        label="Select an Option",
        options=get_options(),
        on_change=None,  # set later
    )

    # load_newwindow: opens a dialog with input fields depending on dropdown value
    def load_newwindow(e):
        value = dropdown.value
        if not value:
            alert = ft.AlertDialog(
                title=ft.Text("No option selected"),
                content=ft.Text("Please select an option from the dropdown first."),
                actions=[ft.TextButton("OK", on_click=lambda e: (setattr(alert, "open", False), page.update()))],
            )
            page.dialog = alert
            alert.open = True
            page.update()
            return

        # build controls for each type
        if value == "Contact":
            name = ft.TextField(label="Name")
            phone = ft.TextField(label="Phone")
            email = ft.TextField(label="Email")
            url = ft.TextField(label="URL")

            def on_save(e):
                add_contact(name.value or "", phone.value or None, email.value or None, url.value or None)
                setattr(dialog, "open", False)
                list_view.controls.append(
                    ft.ListTile(title=ft.Text(name.value or "New Contact"), subtitle=ft.Text("Added"))
                )
                page.update()

            controls = [name, phone, email, url]

        elif value == "Summary":
            summary = ft.TextField(label="Summary text", multiline=True, min_lines=3)

            def on_save(e):
                add_summary(summary.value or "")
                setattr(dialog, "open", False)
                list_view.controls.append(
                    ft.ListTile(title=ft.Text("New Summary"), subtitle=ft.Text((summary.value or "")[:100]))
                )
                page.update()

            controls = [summary]

        elif value == "Job History":
            company = ft.TextField(label="Company Name")
            start_date = ft.TextField(label="Start Date (YYYY-MM-DD)")
            finish_date = ft.TextField(label="Finish Date (YYYY-MM-DD, optional)")
            description = ft.TextField(label="Description", multiline=True, min_lines=3)

            def on_save(e):
                job_id = add_job_history(company.value or "", start_date.value or "", finish_date.value or None)
                if (description.value or "").strip():
                    add_job_description(job_id, description.value)
                setattr(dialog, "open", False)
                list_view.controls.append(
                    ft.ListTile(title=ft.Text(company.value or "New Job"), subtitle=ft.Text(start_date.value or ""))
                )
                page.update()

            controls = [company, start_date, finish_date, description]

        elif value == "Education":
            school = ft.TextField(label="School Name")
            sdate = ft.TextField(label="Start Date (YYYY-MM-DD)")
            gdate = ft.TextField(label="Graduation Date (YYYY-MM-DD, optional)")
            degree = ft.TextField(label="Degree")

            def on_save(e):
                add_education(school.value or "", sdate.value or "", degree.value or "", gdate.value or None)
                setattr(dialog, "open", False)
                list_view.controls.append(
                    ft.ListTile(title=ft.Text(school.value or "New Education"), subtitle=ft.Text(degree.value or ""))
                )
                page.update()

            controls = [school, sdate, gdate, degree]

        elif value == "Skills":
            skill = ft.TextField(label="Skill Name")

            def on_save(e):
                add_skill(skill.value or "")
                setattr(dialog, "open", False)
                list_view.controls.append(
                    ft.ListTile(title=ft.Text(skill.value or "New Skill"), subtitle=ft.Text("Added"))
                )
                page.update()

            controls = [skill]

        else:  # Projects or other -- simple entry
            proj = ft.TextField(label="Project Name")
            desc = ft.TextField(label="Description", multiline=True, min_lines=3)

            def on_save(e):
                setattr(dialog, "open", False)
                list_view.controls.append(
                    ft.ListTile(title=ft.Text(proj.value or "New Project"), subtitle=ft.Text((desc.value or "")[:100]))
                )
                page.update()

            controls = [proj, desc]

        # create and show dialog
        dialog = ft.AlertDialog(
            title=ft.Text(f"New {value}"),
            content=ft.Column(controls, tight=True),
            actions=[
                ft.TextButton("Cancel", on_click=lambda e: (setattr(dialog, "open", False), page.update())),
                ft.ElevatedButton("Save", on_click=on_save),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        page.dialog = dialog
        dialog.open = True
        page.update()

    def dropdown_changed(e):
        list_view.controls.clear()

        v = e.control.value
        if v == "Contact":
            my_data = ["Contact 1", "Contact 2", "Contact 3", "Contact 4"]
        elif v == "Summary":
            my_data = ["Summary 1", "Summary 2", "Summary 3"]
        elif v == "Job History":
            my_data = ["Job 1", "Job 2", "Job 3"]
        elif v == "Education":
            my_data = ["Education 1", "Certification 1"]
        elif v == "Skills":
            my_data = ["Skills 1", "Skills 2", "Skills 3", "Skills 4"]
        elif v == "Projects":
            my_data = ["Projects 1", "Projects 2"]
        else:
            my_data = []

        for item in my_data:
            list_view.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.NOTE),
                    title=ft.Text(f"Name of {item}"),
                    subtitle=ft.Text(f"Status of {item}."),
                    trailing=ft.PopupMenuButton(
                        icon=ft.Icons.MORE_VERT,
                        items=[
                            ft.PopupMenuItem(text="Modify", on_click=lambda e, it=item: print("Modify!", it)),
                            ft.PopupMenuItem(text="Delete", on_click=lambda e, it=item: print("Delete!", it)),
                        ],
                    ),
                )
            )
        page.update()

    # wire the dropdown change now that handler exists
    dropdown.on_change = dropdown_changed

    return ft.Column([
        ft.Row([
            ft.FilledTonalButton("New", icon=ft.Icons.ADD_OUTLINED, on_click=load_newwindow),
            ft.FilledTonalButton("Exit", icon=ft.Icons.EXIT_TO_APP, on_click=lambda _: page.window.close())
        ],
        alignment=ft.MainAxisAlignment.CENTER,),
        ft.Divider(),  
        dropdown,
        ft.Card(
            content=ft.Column(
                [
                    list_view
                ],
                spacing=0,
            ),
        )
    ])


if __name__ == "__main__":
    main()