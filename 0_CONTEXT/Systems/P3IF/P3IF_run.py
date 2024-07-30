"""
Example usage:

1. Generate synthetic data:
   python P3IF_run.py --generate

2. Visualize relationships:
   python P3IF_run.py --visualize

3. Analyze network:
   python P3IF_run.py --analyze

4. Export data to JSON:
   python P3IF_run.py --export

5. Import data from JSON file:
   python P3IF_run.py --import p3if_data.json

6. Hot-swap a dimension:
   python P3IF_run.py --swap old_dimension new_dimension

7. Multiplex with external framework:
   python P3IF_run.py --multiplex

8. Generate data and visualize:
   python P3IF_run.py --generate --visualize

9. Import data, analyze, and export:
   python P3IF_run.py --import input_data.json --analyze --export

10. Generate data, analyze, and hot-swap:
    python P3IF_run.py --generate --analyze --swap property1 property2

11. Import data, multiplex, and visualize:
    python P3IF_run.py --import external_data.json --multiplex --visualize

12. Full pipeline: generate, analyze, visualize, and export:
    python P3IF_run.py --generate --analyze --visualize --export
"""

import argparse
from P3IF import P3IF

def main():
    parser = argparse.ArgumentParser(description="Interact with the P3IF system")
    parser.add_argument('--generate', action='store_true', help='Generate synthetic data')
    parser.add_argument('--visualize', action='store_true', help='Visualize relationships')
    parser.add_argument('--analyze', action='store_true', help='Analyze network')
    parser.add_argument('--export', action='store_true', help='Export data to JSON')
    parser.add_argument('--import', dest='import_file', help='Import data from JSON file')
    parser.add_argument('--swap', nargs=2, metavar=('OLD', 'NEW'), help='Hot-swap a dimension')
    parser.add_argument('--multiplex', action='store_true', help='Multiplex with external framework')

    args = parser.parse_args()

    p3if = P3IF()

    if args.generate:
        p3if.generate_synthetic_data(num_properties=10, num_processes=10, num_perspectives=10, num_relationships=100)
        print("Synthetic data generated.")

    if args.visualize:
        p3if.visualize_relationships()
        print("Relationships visualized and saved to 'p3if_visualization.png'.")

    if args.analyze:
        analysis = p3if.analyze_network()
        print("Network Analysis:", analysis)

    if args.export:
        p3if.export_to_json()
        print("Data exported to 'p3if_export.json'.")

    if args.import_file:
        p3if.import_from_json(args.import_file)
        print(f"Data imported from {args.import_file}.")

    if args.swap:
        p3if.hot_swap_dimension(args.swap[0], args.swap[1])
        print(f"Dimension {args.swap[0]} swapped with {args.swap[1]}.")

    if args.multiplex:
        external_framework = {
            'properties': ['security', 'scalability'],
            'processes': ['authentication', 'data_processing'],
            'perspectives': ['user', 'developer']
        }
        p3if.multiplex_frameworks(external_framework)
        print("Multiplexed with external framework.")

    if not any(vars(args).values()):
        parser.print_help()

if __name__ == "__main__":
    main()
