def parse_dfn(file_path):
    fractures = {}
    with open(file_path, 'r') as file:
        for line in file.readlines()[1:]:
            parts = line.split()
            part_id = int(parts[0])
            x, y, z = map(float, parts[1:4])
            thickness, permeability = map(float, parts[4:6])
            if part_id not in fractures:
                fractures[part_id] = []
            fractures[part_id].append((x, y, z, thickness, permeability))
    return fractures