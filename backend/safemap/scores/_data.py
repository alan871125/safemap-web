import os
import csv
import pickle
data_dir = f'{os.path.dirname(__file__)}/scores'

def load_score(score_type, data_type='csv'):
    if score_type not in ['light', 'monitor', 'safety']:
        raise KeyError("score type should be one of ['light', 'monitor', 'safety']")
    if data_type == 'csv':
        return _load_csv(score_type)
    if data_type == 'pickle':
        return _load_pickle(score_type)

def _load_pickle(score_type):
    with open (f'{data_dir}/edge_{score_type}_scores.pickle', 'rb') as f:
        scores = pickle.load(f)
    return scores

def _save_csv(scores, score_type):
    if score_type not in ['light', 'monitor', 'safety']:
        raise KeyError("score type should be one of ['light', 'monitor', 'safety']")
    if not scores:
        raise ValueError("scores cannot be empty")
    
    # score_type = next(iter(scores.values()))['score_type']
    csv_file = f'{data_dir}/edge_{score_type}_scores.csv'
    
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['node1', 'node2', 'score'])
        for (node1, node2), score in scores.items():
            writer.writerow([node1, node2, score])
            
def _load_csv(score_type: str) -> dict[tuple[int, int], float]:
    csv_file = f'{data_dir}/edge_{score_type}_scores.csv'
    
    if not os.path.exists(csv_file):
        raise FileNotFoundError(f"{csv_file} does not exist")
    
    scores = {}
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            node1, node2, score = int(row[0]), int(row[1]), float(row[2])
            scores[(node1, node2)] = score
    return scores