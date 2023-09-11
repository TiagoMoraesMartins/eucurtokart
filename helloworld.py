from reactpy import component, html, run

@component
def PrintButton(display_text, message_text):
    def handle_event(event):
        print(message_text)
    
    return html.button({"on_click": handle_event}, display_text)

@component
def App():
    return html.div(
        PrintButton("Play","Playing"),
        PrintButton("Pause","Paused")
    )

@component
def Title(title):
    return html.h1(title)

@component
def Photo():
    return html.img({
        "src":"https://picsum.photos/id/152/500/300",
        "style":{"width":"30%"},
    })

@component
def PhotographerName(caption):
    return html.h4(caption)

@component
def PhotoViewer():
    return html.section(
        Title("Photo of the day"),
        Photo(),
        PhotographerName("Steven Spassov")
    )

@component
def HelloWorld():
    return html.h1("Hello, world!")

#run(HelloWorld)   
#run(PhotoViewer)    
run(App)