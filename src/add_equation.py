# SPDX-License-Identifier: GPL-3.0-or-later
from gi.repository import Adw, Gtk

from graphs import graphs, plotting_tools, utilities
from graphs.data import Data

import numpy
from numpy import *


def on_accept(_widget, self, window):
    """Launched when the accept button is pressed on the equation window"""
    x_start = window.x_start_entry.get_text()
    x_stop = window.x_stop_entry.get_text()
    step_size = window.step_size_entry.get_text()
    equation = str(window.equation_entry.get_text())
    dataset = create_dataset(x_start, x_stop, equation, step_size,
                             str(window.name_entry.get_text()))
    try:
        new_file = Data(self, dataset["xdata"], dataset["ydata"])
        new_file.filename = dataset["name"]
    except Exception as exception:
        exception_type = exception.__class__.__name__
        toast = f"{exception_type} - Unable to add data from equation"
        window.toast_overlay.add_toast(Adw.Toast(title=toast))
        return

    # Choose how to handle duplicates filenames. Add them,
    # ignore them, overide them, Or rename the file
    handle_duplicates = self.preferences.config["handle_duplicates"]
    if not handle_duplicates == "Add duplicates":
        for key, item in self.datadict.items():
            if new_file.filename in item.filename:
                if handle_duplicates == "Auto-rename duplicates":
                    new_file.filename = utilities.get_duplicate_filename(
                        self, new_file.filename)
                elif handle_duplicates == "Ignore duplicates":
                    toast = "Item with this name already exists"
                    window.toast_overlay.add_toast(Adw.Toast(title=toast))
                    return
                elif handle_duplicates == "Override existing items":
                    new_file.xdata_clipboard = [new_file.xdata.copy()]
                    new_file.ydata_clipboard = [new_file.ydata.copy()]
                    new_file.clipboard_pos = -1
                    self.datadict[key] = new_file
                    plotting_tools.refresh_plot(self)
                    window.destroy()
                    return

    new_file.xdata_clipboard = [new_file.xdata.copy()]
    new_file.ydata_clipboard = [new_file.ydata.copy()]
    new_file.clipboard_pos = -1
    color = plotting_tools.get_next_color(self)
    self.datadict[new_file.key] = new_file
    graphs.add_sample_to_menu(self, new_file.filename,
                              color, new_file.key, True)
    plotting_tools.refresh_plot(self)
    window.destroy()


def create_dataset(x_start, x_stop, equation, step_size, name):
    """
    Create all data set parameters that are required
    to create a new data object
    """
    dataset = {}
    if name == "":
        name = f"Y = {str(equation)}"
    dataset["name"] = name
    datapoints = int(abs(eval(x_start) - eval(x_stop)) / eval(step_size))
    xdata = numpy.linspace(eval(x_start), eval(x_stop), datapoints)
    equation = equation.replace("X", "xdata")
    equation = str(equation.replace("^", "**"))
    equation += " + xdata*0"
    dataset["ydata"] = eval(equation)
    dataset["xdata"] = numpy.ndarray.tolist(xdata)
    return dataset


@Gtk.Template(resource_path="/se/sjoerd/Graphs/ui/add_equation_window.ui")
class AddEquationWindow(Adw.Window):
    __gtype_name__ = "AddEquationWindow"
    add_equation_confirm_button = Gtk.Template.Child()
    step_size_entry = Gtk.Template.Child()
    x_stop_entry = Gtk.Template.Child()
    x_start_entry = Gtk.Template.Child()
    equation_entry = Gtk.Template.Child()
    name_entry = Gtk.Template.Child()
    toast_overlay = Gtk.Template.Child()

    def __init__(self, parent):
        super().__init__()
        self.step_size_entry.set_text(
            parent.preferences.config["addequation_step_size"])
        self.x_start_entry.set_text(
            parent.preferences.config["addequation_X_start"])
        self.x_stop_entry.set_text(
            parent.preferences.config["addequation_X_stop"])
        self.equation_entry.set_text(
            parent.preferences.config["addequation_equation"])

        style_context = self.add_equation_confirm_button.get_style_context()
        style_context.add_class("suggested-action")
        self.add_equation_confirm_button.connect("clicked", on_accept,
                                                 parent, self)
        self.set_transient_for(parent.main_window)
        self.set_modal(True)
