import math
from collections import Counter

class DecisionTreeClassifier:
    def __init__(self, max_depth=None, min_samples_split=2, criterion='entropy'):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.criterion = criterion
        self.tree = None

    # Public API
    def fit(self, X, y):
        data = [x + [label] for x, label in zip(X, y)]
        self.n_features = len(X[0])
        self.tree = self._build_tree(data, depth=0)
        return self

    def predict(self, X):
        return [self._predict_one(row, self.tree) for row in X]

    # Internal helpers
    def _predict_one(self, row, node):
        if 'value' in node:
            return node['value']
        feature = node['feature']
        threshold = node['threshold']
        if row[feature] <= threshold:
            return self._predict_one(row, node['left'])
        else:
            return self._predict_one(row, node['right'])

    def _build_tree(self, data, depth):
        labels = [row[-1] for row in data]
        num_samples = len(labels)
        num_labels = len(set(labels))

        # stopping criteria
        if (self.max_depth is not None and depth >= self.max_depth) or \
           num_labels == 1 or \
           num_samples < self.min_samples_split:
            return {'value': self._majority_class(labels)}

        best = self._best_split(data)
        if best['gain'] == 0:
            return {'value': self._majority_class(labels)}

        left = self._build_tree(best['left'], depth + 1)
        right = self._build_tree(best['right'], depth + 1)
        return {
            'feature': best['feature'],
            'threshold': best['threshold'],
            'left': left,
            'right': right
        }

    def _best_split(self, data):
        base_impurity = self._impurity([row[-1] for row in data])
        best = {'gain': 0, 'feature': None, 'threshold': None, 'left': None, 'right': None}
        n_features = self.n_features

        for feature in range(n_features):
            values = sorted(set(row[feature] for row in data))
            if len(values) == 1:
                continue
            # candidate thresholds: midpoints between consecutive unique values
            thresholds = [(values[i] + values[i+1]) / 2.0 for i in range(len(values)-1)]
            for thr in thresholds:
                left = [r for r in data if r[feature] <= thr]
                right = [r for r in data if r[feature] > thr]
                if not left or not right:
                    continue
                gain = base_impurity - (len(left)/len(data))*self._impurity([r[-1] for r in left]) \
                                      - (len(right)/len(data))*self._impurity([r[-1] for r in right])
                if gain > best['gain']:
                    best.update({'gain': gain, 'feature': feature, 'threshold': thr, 'left': left, 'right': right})
        return best

    def _impurity(self, labels):
        if self.criterion == 'gini':
            return self._gini(labels)
        return self._entropy(labels)

    def _entropy(self, labels):
        total = len(labels)
        counts = Counter(labels)
        ent = 0.0
        for cnt in counts.values():
            p = cnt / total
            ent -= p * math.log2(p) if p > 0 else 0
        return ent

    def _gini(self, labels):
        total = len(labels)
        counts = Counter(labels)
        g = 1.0
        for cnt in counts.values():
            p = cnt / total
            g -= p * p
        return g

    def _majority_class(self, labels):
        return Counter(labels).most_common(1)[0][0]


# Example usage:
# X = [[2.7, 2.5], [1.3, 3.1], [3.0, 4.0], [1.0, 1.0]]
# y = [0, 0, 1, 1]
# clf = DecisionTreeClassifier(max_depth=3)
# clf.fit(X, y)
# preds = clf.predict([[1.5,2.0], [3.1,3.9]])
# print(preds)