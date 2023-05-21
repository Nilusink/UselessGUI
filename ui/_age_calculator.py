
"""
_age_calculator.py
16. May 2023

Calculates your age based on your age + randomness

Author:
Nilusink
"""
from tkinter.messagebox import showwarning
from functools import reduce
import customtkinter as ctk
from random import randint


class AgeCalculator(ctk.CTkFrame):
    _progressbar: ctk.CTkProgressBar = ...
    _toplevel: ctk.CTkToplevel = ...
    _age: int = ...

    _current_progress: float = 0

    def __init__(self, *args, **kwargs) -> None:
        # initialize parent
        super().__init__(*args, **kwargs)

        # create age label
        self.label = ctk.CTkLabel(self, text="Enter your age: ")
        self.label.grid(row=0, column=0, pady=10, padx=10)

        # create entry
        self.age_var = ctk.StringVar()
        self.age_var.trace_add("write", self._on_age_change)
        self.age_entry = ctk.CTkEntry(
            self,
            placeholder_text="Your age here!",
            placeholder_text_color="#666",
            textvariable=self.age_var
        )
        self.age_entry.grid(row=1, column=0, padx=10, pady=10)

        # create button
        ctk.CTkButton(
            self,
            text="Calculate",
            command=self.calculate_age
        ).grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

    def _on_age_change(self, *_trash) -> None:
        """
        called if the age entry changes
        """
        val = self.age_var.get()

        if val:
            if val[-1].isdigit():
                self.age_var.set(val[:-1])

                # tell the user an invalid character has been entered
                showwarning("Attention", "You cannot enter numbers!")

    def _start_progress(self) -> None:
        """
        start the progress bar (results window)
        """
        self._toplevel = ctk.CTkToplevel(self)

        # configure the toplevel
        self._toplevel.title("Result")
        self._toplevel.geometry("300x50")
        self._toplevel.resizable(False, False)

        self._toplevel.grid_columnconfigure(0, weight=1)
        self._toplevel.grid_rowconfigure((0, 1), weight=1)

        # create widgets
        self._toplevel_label = ctk.CTkLabel(
            self._toplevel,
            text="Calculating ..."
        )
        self._toplevel_label.grid(row=0, column=0)

        self._progressbar = ctk.CTkProgressBar(self._toplevel)
        self._progressbar.grid(row=1, column=0)

        # start progress counter
        self.after(10, self._update_progress)

    def _update_progress(self, *_trash) -> None:
        """
        increment the progress
        """
        self._current_progress += .001
        self._progressbar.set(self._current_progress)

        if self._current_progress >= 1:
            self._current_progress = 0
            self._progressbar.grid_forget()

            self._toplevel_label.configure(text=f"Your Age: {self._age}")

            return

        self.after(10, self._update_progress)

    def calculate_age(self) -> None:
        """
        calculates the age
        """
        self._start_progress()

        # get the user age
        user_age = " " + self.age_var.get()

        # generate a random seed for better prediction
        seed = randint(12, 74823341)
        age_nums = [seed, randint(12, 984)] + [ord(c) for c in user_age]

        # calculate the flux age values
        age_avg = sum([ord(c) for c in user_age]) / (len(user_age) * 2)
        age_mul = reduce(lambda s, n: s * n, age_nums) / seed
        age_seed = reduce(lambda s, n: n - (s - seed**2), age_nums) / seed**2

        # save the age to be shown later
        self._age = round(
            (1e3 * age_avg * ((age_mul / seed) + age_seed)) % age_avg * 3,
            6
        )
