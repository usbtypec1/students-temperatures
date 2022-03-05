from datetime import date

from openpyxl.cell import Cell, WriteOnlyCell
from openpyxl.styles import Font, PatternFill, Border, Side
from openpyxl.worksheet.worksheet import Worksheet

__all__ = (
    'DateCell',
    'SuspiciousTemperatureCell',
    'StudentNameCell',
)


class SuspiciousTemperatureCell:
    fg_color = 'ff0000'
    pattern_type = 'solid'
    bold = True

    def __new__(cls, worksheet: Worksheet, value: float) -> Cell:
        cell = WriteOnlyCell(worksheet, value)
        cell.font = Font(bold=cls.bold)
        cell.fill = PatternFill(patternType=cls.pattern_type, fgColor=cls.fg_color)
        return cell


class DateCell:
    date_format = r'%d.%m.%Y'

    def __new__(cls, worksheet: Worksheet, value: date):
        value = value.strftime(cls.date_format)
        cell = WriteOnlyCell(worksheet, value)
        return cell


class StudentNameCell:
    border_color = '000000'
    border_style = 'thin'
    bold = True

    def __new__(cls, worksheet: Worksheet, value: str) -> Cell:
        cell = WriteOnlyCell(worksheet, value)
        cell.font = Font(bold=cls.bold)
        cell.border = Border(bottom=Side(color=cls.border_color, border_style=cls.border_style))
        return cell
