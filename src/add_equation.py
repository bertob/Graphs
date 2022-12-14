from gi.repository import Gtk, Adw, GObject, Gio
from numpy import *
from . import item_operations, plotting_tools, datman
from .data import Data

def open_add_equation_window(widget, _, self):
    win = AddEquationWindow(self)
    name = "transform_confirm"
    button = win.add_equation_confirm_button
    button.set_sensitive(True)
    button.connect("clicked", on_accept, self, win)
    win.present()

def on_accept(widget, self, window):
    x_start = float(window.X_start_entry.get_text())
    x_stop = float(window.X_stop_entry.get_text())
    step_size = float(window.step_size_entry.get_text())
    equation = str(window.equation_entry.get_text())
    name = str(window.name_entry.get_text())
    new_file = create_data(self, x_start, x_stop, equation, step_size, name)
    if name in self.datadict:
        loop = True
        i = 0
        while loop:
            i += 1
            new_name = f"{name} ({i})"
            if new_name not in self.datadict:
                loop = False
                new_file.filename = f"{name} ({i})"
    color = plotting_tools.get_next_color(self)
    datman.add_sample_to_menu(self, new_file.filename, color)
    self.datadict[new_file.filename] = new_file

    plotting_tools.refresh_plot(self)
    window.destroy()

def create_data(self, x_start, x_stop, equation, step_size, name):
    new_file = Data()
    if name == "":
        name = f"Y = {str(equation)}"
    datapoints = int(abs(x_start - x_stop)/step_size)
    new_file.xdata =  ndarray.tolist(linspace(x_start,x_stop,datapoints))    
    equation = equation.replace("X", "new_file.xdata")
    equation = equation.replace("^", "**")
    new_file.ydata = eval(equation)
    new_file.filename = name
    return new_file

@Gtk.Template(resource_path="/se/sjoerd/DatMan/add_equation_window.ui")
class AddEquationWindow(Adw.Window):
    __gtype_name__ = "AddEquationWindow"
    add_equation_confirm_button = Gtk.Template.Child()
    step_size_entry = Gtk.Template.Child()
    X_stop_entry = Gtk.Template.Child()
    X_start_entry = Gtk.Template.Child()
    equation_entry = Gtk.Template.Child()
    name_entry = Gtk.Template.Child()
    equation_info = Gtk.Template.Child()

    def __init__(self, parent):
        super().__init__()
        buffer = Gtk.TextBuffer()
        text1 = "Here you can add add a data by equation\n"
        text2 = "The equation field uses Numpy notation \n"
        text3 = "Make sure to use a capital letter for the X coordinate"
        buffer.set_text(text1 + text2 + text3)
        self.equation_info.set_buffer(buffer)



