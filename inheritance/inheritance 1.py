class Report:
    def generate(self):
        return "Basic report"

class PDFReport(Report):
    def generate(self):
        base = super().generate()
        return f"{base} converted to PDF"

class ExcelReport(Report):
    def generate(self):
        base = super().generate()
        return f"{base} with Excel formatting"