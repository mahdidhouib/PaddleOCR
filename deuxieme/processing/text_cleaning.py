def group_lines_to_paragraphs(lines, max_vertical_gap=15):
    """
    lines: liste de dictionnaires [{"text":..., "bbox":..., "confidence":...}]
    max_vertical_gap: distance max entre lignes pour les regrouper
    """
    if not lines:
        return []

    # Trier les lignes par y_min (coordonnée verticale du bbox)
    lines = sorted(lines, key=lambda x: min([point[1] for point in x['bbox']]))

    paragraphs = []
    current_para = [lines[0]['text']]
    last_y = min([point[1] for point in lines[0]['bbox']])

    for line in lines[1:]:
        y = min([point[1] for point in line['bbox']])
        if y - last_y <= max_vertical_gap:
            current_para.append(line['text'])
        else:
            paragraphs.append(" ".join(current_para))
            current_para = [line['text']]
        last_y = y

    # Ajouter le dernier paragraphe
    paragraphs.append(" ".join(current_para))
    return paragraphs
