"""
_window.py
16. May 2023

Main program window

Author:
Nilusink
"""
from ._selection_frame import SelectionFrame
from ._ohms_calculator import OhmsCalculator
from ._age_calculator import AgeCalculator
import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class Window(ctk.CTk):
    _current_frame_id: int = 0
    frames: list[ctk.CTkFrame] = ...

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # configure window
        self.title("Calculators")
        # self.overrideredirect(True)  # no borders

        # configure the grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # initialize all frames
        self.frames = [
            SelectionFrame(self, selection_callback=self.set_current_frame_id),
            AgeCalculator(self),
            OhmsCalculator(self, selection_callback=self.set_current_frame_id),
        ]

        self.current_frame_id = 0

    @property
    def current_frame_id(self) -> int:
        return self._current_frame_id

    @current_frame_id.setter
    def current_frame_id(self, new_id: int) -> None:
        """
        change the frame id, while also "griding" the new one and
        "grid forgetting" the last one

        :param new_id: the new frame id
        :type new_id: int
        """
        self.frames[self.current_frame_id].grid_forget()
        self.frames[new_id].grid(row=0, column=0, sticky="nsew")

        self._current_frame_id = new_id

    def set_current_frame_id(self, new_id: int) -> None:
        """
        the exact same thing as setting  current_frame_id , but as
        a function, so it can be passed as a parameter

        :param new_id: the new frame id
        :type new_id: int
        """
        self.current_frame_id = new_id
