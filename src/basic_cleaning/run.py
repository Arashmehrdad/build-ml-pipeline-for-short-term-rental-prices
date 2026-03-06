import argparse
import pandas as pd
import wandb


def go(args: argparse.Namespace) -> None:
    run = wandb.init(job_type="basic_cleaning")
    run.config.update(vars(args))

    local_path = run.use_artifact(args.input_artifact).file()
    df = pd.read_csv(local_path)

    # Filter out price outliers
    df = df[df["price"].between(args.min_price, args.max_price)].copy()

    # Convert last_review to datetime
    if "last_review" in df.columns:
        df["last_review"] = pd.to_datetime(df["last_review"], errors="coerce")

    df.to_csv("clean_sample.csv", index=False)

    artifact = wandb.Artifact(
        args.output_artifact,
        type=args.output_type,
        description=args.output_description,
    )
    artifact.add_file("clean_sample.csv")
    run.log_artifact(artifact)

    run.finish()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Basic cleaning")
    parser.add_argument("--input_artifact", type=str, required=True)
    parser.add_argument("--output_artifact", type=str, required=True)
    parser.add_argument("--output_type", type=str, required=True)
    parser.add_argument("--output_description", type=str, required=True)
    parser.add_argument("--min_price", type=float, required=True)
    parser.add_argument("--max_price", type=float, required=True)
    go(parser.parse_args())
