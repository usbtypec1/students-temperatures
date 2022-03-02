from typing import Iterable

import openpyxl

import db


class ReportFile:

    def __init__(self):
        self._wb = openpyxl.Workbook(write_only=True)
        self._ws = self._wb.create_sheet('Отчёт')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._wb.save('./result.xlsx')
        self._wb.close()

    def write_report(self,
                     users: Iterable[db.User],
                     temperature_records: Iterable[db.TemperatureRecord]
                     ):
        # for i, user in enumerate(users, start=1):
        #     self._ws[f'A{i}'].value = user.first_name.title()
        dates = {record.recorded_at_date for record in temperature_records}

        for date in dates:
            records = {record.student.first_name: record.temperature_value
                       for record in temperature_records if record.recorded_at_date == date}
            insertable_data = []
            for user in users:
                try:
                    insertable_data.append(records[user.first_name])
                except KeyError:
                    insertable_data.append(None)
            self._ws.append(insertable_data)


with ReportFile() as file:
    file.write_report(db.User.select(), db.TemperatureRecord.select())
