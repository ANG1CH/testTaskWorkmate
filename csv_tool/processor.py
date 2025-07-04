import csv

def load_csv(filepath):
    with open(filepath, encoding='utf-8') as f:
        return list(csv.DictReader(f))

def filter_data(data, condition):
    column, expr = condition.split('=', 1)
    op = expr[0]
    value = expr[1:]

    if op not in ('>', '<', '='):
        raise ValueError(f"Unsupported operator: {op}")

    def match(row):
        cell = row[column]
        try:
            val = float(value)
            cell_val = float(cell)
        except ValueError:
            val = value
            cell_val = cell

        if op == '>':
            return cell_val > val
        elif op == '<':
            return cell_val < val
        return cell_val == val

    return [row for row in data if match(row)]

def aggregate_data(data, agg):
    column, func = agg.split('=')
    values = [float(row[column]) for row in data]

    if func == 'avg':
        return f"AVG of {column}: {sum(values)/len(values):.2f}"
    elif func == 'min':
        return f"MIN of {column}: {min(values)}"
    elif func == 'max':
        return f"MAX of {column}: {max(values)}"
    else:
        raise ValueError("Invalid aggregation function")