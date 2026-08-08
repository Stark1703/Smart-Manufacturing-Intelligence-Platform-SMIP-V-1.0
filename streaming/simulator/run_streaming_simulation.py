"""
run_streaming_simulation.py

Entry point for the SMIP v2.0 Streaming Simulation.
"""

from streaming.pipeline import StreamingPipeline


def main() -> None:

    pipeline = StreamingPipeline()

    pipeline.run()


if __name__ == "__main__":

    main()