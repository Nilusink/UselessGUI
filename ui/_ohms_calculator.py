"""
_ohms_calculator.py
16. May 2023

Doesn't calculate resistor stuff

Author:
Nilusink
"""
import customtkinter as ctk
from random import randint
from PIL import Image
from os import path
import typing as tp


VOLTAGE_DIVIDER = ctk.CTkImage(
    dark_image=Image.open(
        path.dirname(__file__) + "/assets/Spannungsteiler.png"
    ),
    size=(216, 384)
)


class OhmsCalculator(ctk.CTkFrame):
    _selection_callback: tp.Callable[[int], None]
    _curr_y: int = 0
    _curr_x: int = 0

    def __init__(
            self,
            *args,
            selection_callback: tp.Callable[[int], None],
            **kwargs
    ) -> None:
        # save parameters
        self._selection_callback = selection_callback

        super().__init__(*args, **kwargs)

        # configure grid
        self.grid_rowconfigure(list(range(9)), weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        # side image
        img = ctk.CTkLabel(self, image=VOLTAGE_DIVIDER, text="")
        img.grid(row=0, column=2, rowspan=9, padx=20, pady=20)

        # Current
        ctk.CTkLabel(self, text="I").grid(row=0, column=0)
        ctk.CTkEntry(self).grid(row=0, column=1, padx=20, pady=20)

        # Seperator
        ctk.CTkFrame(self, height=1, bg_color="#666").grid(
            row=1,
            column=0,
            columnspan=2,
            padx=15,
            pady=20,
            sticky="ew"
        )

        # Voltages
        ctk.CTkLabel(self, text="U1").grid(row=2, column=0)
        ctk.CTkEntry(self).grid(row=2, column=1, padx=20, pady=10)
        ctk.CTkLabel(self, text="U2").grid(row=3, column=0)
        ctk.CTkEntry(self).grid(row=3, column=1, padx=20, pady=10)

        # Seperator
        ctk.CTkFrame(self, height=1, bg_color="#666").grid(
            row=4,
            column=0,
            columnspan=2,
            padx=15,
            pady=20,
            sticky="ew"
        )

        # Resistors
        ctk.CTkLabel(self, text="R1").grid(row=5, column=0)
        ctk.CTkEntry(self).grid(row=5, column=1, padx=20, pady=10)
        ctk.CTkLabel(self, text="R2").grid(row=6, column=0)
        ctk.CTkEntry(self).grid(row=6, column=1, padx=20, pady=10)

        # Seperator
        ctk.CTkFrame(self, height=1, bg_color="#666").grid(
            row=7,
            column=0,
            columnspan=2,
            padx=15,
            pady=20,
            sticky="ew"
        )

        # Calculaten't button
        bg = self.cget("fg_color")
        btn_frame = ctk.CTkFrame(
            self,
            fg_color=bg
        )
        btn_frame.grid(
            row=8,
            column=0,
            columnspan=2,
            padx=20,
            pady=20,
            sticky="ew"
        )

        btn_frame.grid_columnconfigure((0, 1), weight=1, minsize=150)
        btn_frame.grid_rowconfigure((0, 1), weight=1, minsize=40)

        self._btn = ctk.CTkButton(
            btn_frame,
            text="Calculate",
            command=lambda *_t: self._selection_callback(0)
        )
        self._btn.grid(row=0, column=0)
        self._btn.bind("<Enter>", self._on_hover)

    def _on_hover(self, *_trash) -> None:
        has_changed = False

        if randint(0, 1):
            self._curr_x = int(not self._curr_x)
            has_changed = True

        if randint(0, 1) or not has_changed:
            self._curr_y = int(not self._curr_y)

        self._btn.grid_configure(column=self._curr_x, row=self._curr_y)
