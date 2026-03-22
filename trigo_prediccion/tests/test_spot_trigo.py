import csv
import tempfile
import unittest
from datetime import datetime
from pathlib import Path

from trigo_prediccion.spot_trigo.generate_report import build_svg
from trigo_prediccion.spot_trigo.normalize_cac_excel import normalize_rows, parse_excel_date, parse_price
from trigo_prediccion.spot_trigo.update_master import merge_rows, read_rows


class NormalizeHelpersTest(unittest.TestCase):
    def test_parse_excel_date_accepts_datetime_and_strings(self) -> None:
        self.assertEqual(parse_excel_date(datetime(2026, 3, 21, 10, 30)), "2026-03-21")
        self.assertEqual(parse_excel_date("21/03/2026 10:30:00"), "2026-03-21")

    def test_parse_price_handles_localized_and_numeric_values(self) -> None:
        self.assertEqual(parse_price("12.345,67"), "12345.67")
        self.assertEqual(parse_price(12345.67), "12345.67")

    def test_normalize_rows_detects_header_after_intro_rows(self) -> None:
        rows = [
            ("Mercado", None),
            ("Reporte semanal", None),
            ("Fecha", "Precio Pizarra"),
            ("21/03/2026", "12.345,67"),
        ]

        normalized = normalize_rows(rows)

        self.assertEqual(
            normalized,
            [
                {
                    "date": "2026-03-21",
                    "price_ars_tn": "12345.67",
                    "source": "CAC BCR",
                    "price_kind": "Precio Pizarra y Estimativo",
                    "product": "Trigo",
                }
            ],
        )


class MasterMergeTest(unittest.TestCase):
    def test_merge_rows_replaces_existing_date_and_sorts(self) -> None:
        existing = [
            {"date": "2026-03-21", "price_ars_tn": "100.00", "source": "A", "price_kind": "X", "product": "Trigo"},
            {"date": "2026-03-28", "price_ars_tn": "110.00", "source": "A", "price_kind": "X", "product": "Trigo"},
        ]
        new_rows = [
            {"date": "2026-03-28", "price_ars_tn": "111.00", "source": "B", "price_kind": "Y", "product": "Trigo"},
            {"date": "2026-04-04", "price_ars_tn": "120.00", "source": "B", "price_kind": "Y", "product": "Trigo"},
        ]

        merged = merge_rows(existing, new_rows)

        self.assertEqual([row["date"] for row in merged], ["2026-03-21", "2026-03-28", "2026-04-04"])
        self.assertEqual(merged[1]["price_ars_tn"], "111.00")

    def test_read_rows_validates_header_even_if_file_has_no_data_rows(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "master.csv"
            with path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.writer(handle)
                writer.writerow(["date", "price_ars_tn", "source"])

            with self.assertRaises(ValueError):
                read_rows(path)


class ReportTest(unittest.TestCase):
    def test_build_svg_returns_polyline_when_values_exist(self) -> None:
        svg = build_svg([100.0, 105.0, 103.0])
        self.assertIn("polyline", svg)
        self.assertIn("viewBox", svg)


if __name__ == "__main__":
    unittest.main()
