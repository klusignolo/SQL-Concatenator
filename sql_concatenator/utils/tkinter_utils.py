import tkinter as tk

def update_widget_text(widget: tk.Widget, value):
    """Takes updates the widget's text to equal whatever Value is specified."""
    if isinstance(widget, tk.Entry):
        if widget.cget("state") == "disabled":
            widget.config(state="normal")
            widget.delete(0, tk.END)
            widget.insert(0, value)
            widget.config(state="disabled")
        else:
            widget.delete(0, tk.END)
            widget.insert(0, value)
    elif isinstance(widget, tk.Text):
        if widget.cget("state") == "disabled":
            widget.config(state="normal")
            widget.delete("1.0", tk.END)
            widget.insert("1.0", value)
            widget.config(state="disabled")
        else:
            widget.delete("1.0", tk.END)
            widget.insert("1.0", value)
    elif isinstance(widget, tk.Label) or isinstance(widget, tk.Button):
        widget.config(text=value)
        
def clip(main: tk.Tk, cliptext: str):
    """Append text to the clipboard"""
    tk.Tk.clipboard_clear(main)
    tk.Tk.clipboard_append(main, cliptext)