def export_results(topology, output_file):
    with open(output_file, 'w') as file:
        for entry in topology:
            file.write(f"Part ID: {entry['part_id']}\n")
            file.write(f"Type: {entry['type']}\n")
            file.write("Nodes:\n")
            for node in entry['nodes']:
                file.write(f"  {node}\n")
            file.write("\n")