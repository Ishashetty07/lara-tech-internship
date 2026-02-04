import pandas as pd

from ai_triage import triage_with_ai
from rule_triage import rule_based_triage
from evaluator import compare


def main():

    df = pd.read_csv("sample_feedback.csv")

    for _, row in df.iterrows():

        feedback = row["feedback"]

        print("\n----------------------------------")
        print("Feedback:", feedback)

        ai_result = triage_with_ai(feedback)
        rule_result = rule_based_triage(feedback)
        evaluation = compare(ai_result, rule_result)

        print("\nAI Decision:")
        print(ai_result)

        print("\nRule Decision:")
        print(rule_result)

        print("\nComparison:")
        print(evaluation)


if __name__ == "__main__":
    main()
