"""
Crowd-Aware Transit Estimation (Toy Simulator)

This module simulates how crowd-derived signals
could influence confidence in a transit ETA.
"""

def analyze_crowd_signals(signals):
    score = 0

    if signals.get("complaints", 0) > 5:
        score -= 2

    if signals.get("confirmations", 0) > 5:
        score += 2

    if signals.get("waiting_crowd", 0) > 20:
        score -= 1

    if score >= 2:
        return "High confidence: vehicle likely on time"
    elif score <= -2:
        return "Low confidence: possible delay"
    else:
        return "Medium confidence: uncertain state"


if __name__ == "__main__":
    sample_signals = {
        "complaints": 7,
        "confirmations": 1,
        "waiting_crowd": 30
    }

    print(analyze_crowd_signals(sample_signals))


import json

def analyze_crowd_signals(signals):
    score = 0

    if signals.get("complaints", 0) > 5:
        score -= 2

    if signals.get("confirmations", 0) > 5:
        score += 2

    if signals.get("waiting_crowd", 0) > 20:
        score -= 1

    if score >= 2:
        return "High confidence: vehicle likely on time"
    elif score <= -2:
        return "Low confidence: possible delay"
    else:
        return "Medium confidence: uncertain state"


if __name__ == "__main__":
    with open("../data/sample_crowd_signals.json", "r") as f:
        signals = json.load(f)

    result = analyze_crowd_signals(signals)
    print("Crowd-based assessment:", result)

