import argparse
import subprocess
import sys
from pathlib import Path

EXCEL_EXTENSIONS = {".xlsx", ".xlsm", ".xltx", ".xltm"}
DEFAULT_NORMALIZED = Path("trigo_prediccion/spot_trigo/normalized/precio_spot_trigo_normalizado.csv")
DEFAULT_MASTER = Path("trigo_prediccion/spot_trigo/master/precio_spot_trigo_master.csv")
DEFAULT_REPORT = Path("trigo_prediccion/spot_trigo/reports/precio_spot_trigo_report.html")


def run_command(args: list[str]) -> None:
    subprocess.run(args, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Ejecuta el flujo completo del precio spot del trigo. "
            "Acepta como entrada un Excel descargado desde CAC/BCR o un CSV ya normalizado."
        )
    )
    parser.add_argument(
        "--input",
        type=Path,
        required=True,
        help="Ruta al Excel descargado o al CSV normalizado que querés incorporar",
    )
    parser.add_argument(
        "--normalized-output",
        type=Path,
        default=DEFAULT_NORMALIZED,
        help="Ruta del CSV normalizado intermedio cuando la entrada es un Excel",
    )
    parser.add_argument(
        "--master",
        type=Path,
        default=DEFAULT_MASTER,
        help="Ruta de la base maestra consolidada",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_REPORT,
        help="Ruta del reporte HTML final",
    )
    args = parser.parse_args()

    if not args.input.exists():
        raise FileNotFoundError(f"No encontré el archivo de entrada: {args.input}")

    normalized_input = args.input
    if args.input.suffix.lower() in EXCEL_EXTENSIONS:
        normalized_input = args.normalized_output
        run_command(
            [
                sys.executable,
                "trigo_prediccion/spot_trigo/normalize_cac_excel.py",
                "--input",
                str(args.input),
                "--output",
                str(normalized_input),
            ]
        )

    run_command(
        [
            sys.executable,
            "trigo_prediccion/spot_trigo/update_master.py",
            "--input",
            str(normalized_input),
            "--master",
            str(args.master),
        ]
    )
    run_command(
        [
            sys.executable,
            "trigo_prediccion/spot_trigo/generate_report.py",
            "--master",
            str(args.master),
            "--output",
            str(args.output),
        ]
    )
    print("Flujo completo ejecutado correctamente.")


if __name__ == "__main__":
    main()
