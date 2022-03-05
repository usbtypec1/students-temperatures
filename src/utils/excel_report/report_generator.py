from typing import Iterable, Union

import openpyxl
from openpyxl.cell import Cell

import db
from utils.excel_report.cell_types import SuspiciousTemperatureCell, DateCell, StudentNameCell
from utils.temperature_utils import is_student_temperature_suspicious, filter_and_sort_unique_dates

__all__ = (
    'TemperaturesReportGenerator',
)


class TemperaturesReportGenerator:
    """Collect all student's temperatures in one Excel file."""

    def __init__(self, file_path: str):
        self._wb = openpyxl.Workbook(write_only=True)
        self._ws = self._wb.create_sheet('Отчёт')
        self._file_path = file_path

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._wb.close()

    def get_stylized_temperature_cell(self, temperature: float) -> Union[Cell, float]:
        """Apply for some cell's styles.

        Args:
            temperature: Student's temperature.

        Returns:
            Cell object or raw temperature value.
        """
        if is_student_temperature_suspicious(temperature):
            return SuspiciousTemperatureCell(self._ws, temperature)
        return temperature

    def write_student_first_names(self, users: Iterable[db.User]) -> None:
        """Add row that contains student's names.
        Use it only once at the beginning of the sheet.

        Args:
            users: Collection of students.

        Returns:
            Modifies the worksheet.
        """
        student_first_name_cells = [StudentNameCell(self._ws, user.first_name) for user in users]
        student_first_names_row = [StudentNameCell(self._ws, 'Дата')] + student_first_name_cells
        self._ws.append(student_first_names_row)

    def write_temperature_records(self, users: Iterable[db.TemperatureRecord],
                                  temperature_records: Iterable[db.TemperatureRecord]) -> None:
        """Add temperature records to sheet.
        Each row marked by date when temperatures were marked.

        Args:
            users: Collection of students.
            temperature_records: Collection of all temperature records.

        Returns:
            Modifies the worksheet.
        """
        for unique_date in filter_and_sort_unique_dates(temperature_records):
            student_first_name_to_temperature_record = {
                record.student.first_name: record for record in temperature_records
                if record.recorded_at_date == unique_date}
            row = [DateCell(self._ws, unique_date)]
            for user in users:
                temperature_record = student_first_name_to_temperature_record.get(user.first_name)
                temperature = None
                if temperature_record is not None:
                    temperature = self.get_stylized_temperature_cell(
                        temperature_record.temperature_value)
                row.append(temperature)
            self._ws.append(row)

    def write_report(self, users: Iterable[db.User],
                     temperature_records: Iterable[db.TemperatureRecord]):
        """Fill the worksheet with data and write it in the tmp directory.

        Args:
            users: Collection of students.
            temperature_records: Collection of all temperature records.

        Returns:
            Writes ready xlsx file in the tmp directory.
        """
        self.write_student_first_names(users)
        self.write_temperature_records(users, temperature_records)
        self._wb.save(self._file_path)
