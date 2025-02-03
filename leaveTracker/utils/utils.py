import json
import os
from datetime import datetime


class Utils:

    @staticmethod
    def calculate_leave_balance():
        leave_per_month = 15 / 12
        current_date = datetime.now()

        if current_date.day <= 7:
            leave_balance = (12 - current_date.month + 1) * leave_per_month
        else:
            leave_balance = (12 - current_date.month) * leave_per_month

        return int(leave_balance + 0.5)

    @staticmethod
    def read_json(filepath: str) -> dict:
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            full_path = os.path.join(current_dir, "..", "static", filepath)
            full_path = os.path.normpath(full_path)

            with open(full_path) as f:
                _data = json.load(f)
                return _data
        except Exception as E:
            print(E)
            