#!/usr/bin/env python3

import sys


def ft_score_analytics(scores_str: list[str]) -> None:
    print("=== Player Score Analytics ===")
    count: int = len(scores_str)

    if count == 0:
        print("No scores provided.",
              "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return
    scores: list[int] = []
    invalids = 0
    for score in scores_str:
        try:
            scores.append(int(score.strip()))
        except ValueError:
            print(f"Error: Invalid score '{score}'skipped.",
                  "Scores must be numeric.")
            invalids += 1
    num_scores: int = len(scores)
    if num_scores == 0:
        print("Error: No valid scores given.")
        return
    sum_scores: int = sum(scores)
    average_score: float = sum_scores / num_scores
    high_score: int = max(scores)
    low_score: int = min(scores)
    score_range: int = high_score - low_score
    print(score)
    print("Scores processed:", scores)
    print("Total players:", num_scores,
          f"(invalid scores: {invalids})" if invalids else "")
    print("Total score:", sum_scores)
    print("Average score:", average_score)
    print("High score:", high_score)
    print("Low score:", low_score)
    print("Score range:", score_range)


if __name__ == "__main__":
    ft_score_analytics(sys.argv[1:])
