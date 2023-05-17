"""
_scientific_calculator.py
17. May 2023

A very intuitive calculator

Author:
Nilusink
"""
from tkinter.messagebox import showwarning
import customtkinter as ctk
from random import randint


class ScientificCalculator(ctk.CTkFrame):
    _nums: list[ctk.IntVar] = ...

    def __init__(self, *args, **kwargs) -> None:
        self._nums = [..., ...]

        # initialize default values
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(list(range(5)), weight=1)
        self.grid_rowconfigure(list(range(3)), weight=1)

        # first number input
        self._val0 = ctk.IntVar(value=0)
        ctk.CTkButton(
            self,
            text="↑",
            command=lambda *_e: self.increment_value(0, 1, True)
        ).grid(row=0, column=0, padx=20, pady=10)
        self._entry0 = ctk.CTkEntry(
            self,
            textvariable=self._val0,
            state="disabled",
            justify="center"
        )
        self._entry0.grid(row=1, column=0)
        ctk.CTkButton(
            self,
            text="↓",
            command=lambda *_e: self.increment_value(0, -1, True)
        ).grid(row=2, column=0, padx=20, pady=10)

        # sign
        self._sign_text = ctk.StringVar(value="+")
        ctk.CTkLabel(self, textvariable=self._sign_text)\
            .grid(row=1, column=1, padx=20)

        # second number input
        self._val1 = ctk.IntVar(value=0)
        ctk.CTkButton(
            self,
            text="↑",
            command=lambda *_e: self.increment_value(1, 1, True)
        ).grid(row=0, column=2, padx=20, pady=10)
        self._entry1 = ctk.CTkEntry(
            self,
            textvariable=self._val1,
            state="disabled",
            justify="center"
        )
        self._entry1.grid(row=1, column=2)
        ctk.CTkButton(
            self,
            text="↓",
            command=lambda *_e: self.increment_value(1, -1, True)
        ).grid(row=2, column=2, padx=20, pady=10)

        self._nums = [self._val0, self._val1]

        # eq
        ctk.CTkLabel(self, text="=").grid(row=1, column=3, padx=20)

        # result
        self._result = ctk.DoubleVar(value=0)
        ctk.CTkLabel(self, textvariable=self._result).grid(
            row=1, column=4, padx=20
        )

    def set_value(self, index: int, value: int) -> None:
        """
        set the value of a value (hehe)

        :param index: the numbers index, either 0 or 1
        :param value: the actual value to set
        """
        self._nums[index].set(value)

    def increment_value(
            self,
            index: int,
            increment: int,
            calculate: bool = False
    ) -> None:
        """
        add the increment to a value

        :param index: the numbers index, either 0 or 1
        :param increment: how much to add to the number
        :param calculate: if ture, calculates and presents the values
        """
        self._nums[index].set(self._nums[index].get() + increment)

        if calculate:
            self.calculate_and_show()

    def calculate_and_show(self, *_trash) -> None:
        """
        calculate the result and show it to the user
        """
        # compute random calculation
        match randint(0, 6):
            case 0:  # addition
                self._result.set(self._val0.get() + self._val1.get())

            case 1:  # subtraction
                self._result.set(self._val0.get() - self._val1.get())

            case 2:  # multiplication
                self._result.set(self._val0.get() * self._val1.get())

            case 3:  # division
                self._result.set(self._val0.get() / self._val1.get())

            case 4:  # string addition
                self._result.set(
                    float(str(self._val0.get()) + str(self._val1.get()))
                )

            case 5:  # completely random numbers
                self._result.set(randint(-999_999, 999_999))

            case 6:  # random numbers between set values
                self._result.set(randint(self._val0.get(), self._val1.get()))

            case _:  # shouldn't happen, but you never know
                self._result.set(111111121111111)

        showwarning("Result", f"Your personal result: {self._result.get()}")
