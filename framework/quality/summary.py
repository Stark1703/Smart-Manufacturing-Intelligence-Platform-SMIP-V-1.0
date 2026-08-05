"""
SMIP Summary
"""

from framework.core.logger import banner


def print_summary(
    results,
):

    banner(
        "SMIP Execution Summary"
    )

    print(

        f"{'Dataset':<25}"

        f"{'Rows':<10}"

        f"{'Status'}"

    )

    print("-" * 60)

    for row in results:

        print(

            f"{row['Dataset']:<25}"

            f"{row['Rows']:<10}"

            f"{row['Status']}"

        )

    print("-" * 60)