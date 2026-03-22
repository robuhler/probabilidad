import argparse
import csv
from pathlib import Path


def read_master(path: Path) -> list[dict[str, str]]:
    with path.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def to_float(value: str) -> float:
    return float(value)


def build_svg(values: list[float], width: int = 900, height: int = 320) -> str:
    if not values:
        return "<svg width='900' height='320'></svg>"
    min_v = min(values)
    max_v = max(values)
    spread = max(max_v - min_v, 1.0)
    points = []
    for index, value in enumerate(values):
        x = 40 + (index * (width - 80) / max(len(values) - 1, 1))
        y = height - 40 - ((value - min_v) / spread) * (height - 80)
        points.append(f"{x:.2f},{y:.2f}")
    polyline = " ".join(points)
    return (
        f"<svg width='{width}' height='{height}' viewBox='0 0 {width} {height}' xmlns='http://www.w3.org/2000/svg'>"
        f"<rect x='0' y='0' width='{width}' height='{height}' fill='white' stroke='#ddd'/>"
        f"<polyline fill='none' stroke='#1f77b4' stroke-width='3' points='{polyline}'/>"
        f"</svg>"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Genera un informe HTML del precio spot del trigo.")
    parser.add_argument(
        "--master",
        type=Path,
        default=Path("trigo_prediccion/spot_trigo/master/precio_spot_trigo_master.csv"),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("trigo_prediccion/spot_trigo/reports/precio_spot_trigo_report.html"),
    )
    args = parser.parse_args()

    rows = read_master(args.master)
    if not rows:
        raise ValueError("La base maestra está vacía. Primero actualizá el master.")

    values = [to_float(row["price_ars_tn"]) for row in rows]
    latest = values[-1]
    first = values[0]
    max_value = max(values)
    min_value = min(values)
    change_pct = ((latest / first) - 1) * 100 if first else 0.0
    last_rows = rows[-8:]

    table_html = "".join(
        "<tr>"
        f"<td>{row['date']}</td>"
        f"<td>{row['price_ars_tn']}</td>"
        f"<td>{row['price_kind']}</td>"
        "</tr>"
        for row in last_rows
    )

    svg = build_svg(values)
    html = f"""
    <html>
      <head>
        <meta charset='utf-8'>
        <title>Reporte ejecutivo - Precio spot del trigo</title>
        <style>
          body {{ font-family: Arial, sans-serif; margin: 32px; color: #222; }}
          .cards {{ display: flex; gap: 16px; flex-wrap: wrap; margin-bottom: 24px; }}
          .card {{ border: 1px solid #ddd; border-radius: 8px; padding: 16px; min-width: 180px; }}
          table {{ border-collapse: collapse; width: 100%; margin-top: 20px; }}
          th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
          th {{ background: #f5f5f5; }}
        </style>
      </head>
      <body>
        <h1>Reporte ejecutivo - Precio spot del trigo</h1>
        <p>Serie consolidada de precio spot del trigo en ARS/tn.</p>
        <div class='cards'>
          <div class='card'><strong>Último precio</strong><br>{latest:.2f}</div>
          <div class='card'><strong>Variación acumulada</strong><br>{change_pct:.2f}%</div>
          <div class='card'><strong>Máximo</strong><br>{max_value:.2f}</div>
          <div class='card'><strong>Mínimo</strong><br>{min_value:.2f}</div>
        </div>
        <h2>Evolución</h2>
        {svg}
        <h2>Últimas observaciones</h2>
        <table>
          <thead><tr><th>Fecha</th><th>Precio ARS/tn</th><th>Tipo</th></tr></thead>
          <tbody>{table_html}</tbody>
        </table>
      </body>
    </html>
    """

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(html, encoding="utf-8")
    print(f"Reporte generado: {args.output}")


if __name__ == "__main__":
    main()
