"""
_selection_frame.py
16. May 2023

The Selection Screen

Author:
Nilusink
"""
import customtkinter as ctk
import typing as tp


class SelectionFrame(ctk.CTkFrame):
    _selection_callback: tp.Callable[[int, tp.Optional[bool]], None]

    def __init__(
            self,
            *args,
            selection_callback: tp.Callable[[int, tp.Optional[bool]], None],
            **kwargs
    ) -> None:
        self._selection_callback = selection_callback

        # initialize parent
        super().__init__(*args, **kwargs)

        # configure grid
        self.grid_rowconfigure(list(range(3)), weight=1)
        self.grid_columnconfigure(0, weight=1)

        # create buttons
        self.scientific_calculator_button = ctk.CTkButton(
            self,
            text="Scientific",
            command=lambda *_trash: self._selection_callback(1, True)
        )
        self.scientific_calculator_button.grid(
            row=0,
            column=0,
            padx=20,
            pady=20
        )

        self.age_calculator_button = ctk.CTkButton(
            self,
            text="Age",
            command=lambda *_trash: self._selection_callback(2, True)
        )
        self.age_calculator_button.grid(
            row=1,
            column=0,
            padx=20,
            pady=20
        )

        self.ohms_calculator_button = ctk.CTkButton(
            self,
            text="Ohm",
            command=lambda *_trash: self._selection_callback(3, True)
        )
        self.ohms_calculator_button.grid(
            row=2,
            column=0,
            padx=20,
            pady=20
        )
