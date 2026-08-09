"""
Run the Silver Pipeline.
"""

from streaming.silver.silver_pipeline import SilverPipeline


def main() -> None:

    pipeline = SilverPipeline()

    pipeline.run()


if __name__ == "__main__":

    main()