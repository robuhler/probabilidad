import argparse
import csv
from pathlib import Path

REQUIRED_COLUMNS = ("date", "price_ars_tn", "source", "price_kind", "product")
DEFAULT_INPUT = Path("trigo_prediccion/spot_trigo/normalized/precio_spot_trigo_normalizado.csv")
DEFAULT_MASTER = Path("trigo_prediccion/spot_trigo/master/precio_spot_trigo_master.csv")


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            return []
        missing = [column for column in REQUIRED_COLUMNS if column not in reader.fieldnames]
        if missing:
            raise ValueError(f"Faltan columnas requeridas en {path}: {', '.join(missing)}")
        return list(reader)


def write_rows(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(REQUIRED_COLUMNS))
        writer.writeheader()
        writer.writerows(rows)


def merge_rows(existing: list[dict[str, str]], new_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    merged: dict[str, dict[str, str]] = {row["date"]: row for row in existing}
    for row in new_rows:
        merged[row["date"]] = row
    return [merged[key] for key in sorted(merged)]


def main() -> None:
    parser = argparse.ArgumentParser(description="Actualiza la base maestra del precio spot del trigo.")
    parser.add_argument("--input", type=Path, required=False, default=DEFAULT_INPUT, help="CSV nuevo para incorporar")
    parser.add_argument("--master", type=Path, default=DEFAULT_MASTER, help="CSV maestro consolidado")
    args = parser.parse_args()

    if not args.input.exists():
        raise FileNotFoundError(
            f"No encontré el CSV normalizado en {args.input}. Primero ejecutá normalize_cac_excel.py."
        )

    new_rows = read_rows(args.input)
    existing = read_rows(args.master) if args.master.exists() else []
    merged = merge_rows(existing, new_rows)
    write_rows(args.master, merged)
    print(f"Base maestra actualizada: {args.master} ({len(merged)} filas)")


if __name__ == "__main__":
    main()
