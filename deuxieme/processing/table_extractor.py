# processing/table_extractor.py

# --- bbox helpers ---
def bbox_left(bbox):
    return min(p[0] for p in bbox)

def bbox_center_y(bbox):
    ys = [p[1] for p in bbox]
    return sum(ys) / len(ys)


# --- group OCR cells into TRUE rows ---
def group_by_rows(lines, row_threshold=10):
    """
    Group cells into real table rows using vertical center alignment
    """
    rows = []

    # trier par centre vertical
    lines = sorted(lines, key=lambda l: bbox_center_y(l["bbox"]))

    for line in lines:
        cy = bbox_center_y(line["bbox"])
        placed = False

        for row in rows:
            rcy = bbox_center_y(row[0]["bbox"])
            if abs(cy - rcy) <= row_threshold:
                row.append(line)
                placed = True
                break

        if not placed:
            rows.append([line])

    return rows


# --- sort row by column (X position) ---
def sort_row_by_columns(row):
    return sorted(row, key=lambda l: bbox_left(l["bbox"]))


# --- build final table ---
def build_table(lines):
    table = []

    rows = group_by_rows(lines)

    for row in rows:
        row = sort_row_by_columns(row)
        table.append([cell["text"] for cell in row])

    return table
