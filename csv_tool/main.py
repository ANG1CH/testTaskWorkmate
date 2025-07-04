import argparse
from processor import load_csv, filter_data, aggregate_data
from tabulate import tabulate

def parse_args():
    parser = argparse.ArgumentParser(description='CSV Processor')
    parser.add_argument('file', help='Path to CSV file')
    parser.add_argument('--where', help='Filter: column=operator+value, e.g. price=>300')
    parser.add_argument('--aggregate', help='Aggregation: column=avg|min|max')
    return parser.parse_args()

def main():
    args = parse_args()
    data = load_csv(args.file)

    if args.where:
        data = filter_data(data, args.where)
        print(tabulate(data, headers="keys", tablefmt="pretty"))

    if args.aggregate:
        result = aggregate_data(data, args.aggregate)
        print(result)

if __name__ == '__main__':
    main()