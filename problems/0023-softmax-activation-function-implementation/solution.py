import math

def softmax(scores: list[float]) -> list[float]:
    max_val = max(scores)
    din = 0.0
    for s in scores:
        din = din + math.exp(s - max_val)

    scores_ = []
    for score in scores:
        scores_.append(round(math.exp(score - max_val)/din,4))
    return scores_