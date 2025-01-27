from datetime import datetime

class Utils:
    
    @staticmethod
    def calculate_leave_balance():
        leave_per_month = 15 / 12
        current_date = datetime.now()

        if current_date.day  <= 7:
            leave_balance = (12 - current_date.month + 1) * leave_per_month
        else:
            leave_balance = (12 - current_date.month) * leave_per_month

        return int(leave_balance + 0.5)
