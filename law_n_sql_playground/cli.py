from __future__ import annotations
import argparse

from .playground import run_basic_demo


def main() -> None:
    parser = argparse.ArgumentParser(description="Law-N SQL Playground")
    parser.add_argument("--steps", type=int, default=5, help="Number of timesteps to simulate")
    parser.add_argument("--devices", type=int, default=5, help="Number of devices to simulate")
    parser.add_argument("--seed", type=int, default=None, help="Random seed for reproducible runs")
    args = parser.parse_args()

    run_basic_demo(steps=args.steps, devices=args.devices, seed=args.seed)


if __name__ == "__main__":
    main()
