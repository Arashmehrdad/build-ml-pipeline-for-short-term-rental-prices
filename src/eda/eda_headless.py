import pandas as pd
import wandb
from ydata_profiling import ProfileReport

MIN_PRICE = 10
MAX_PRICE = 350

run = wandb.init(project="nyc_airbnb", group="eda", job_type="eda_headless", save_code=True)
local_path = wandb.use_artifact("sample.csv:latest").file()
df = pd.read_csv(local_path)

ProfileReport(df, title="EDA raw", minimal=True).to_file("eda_raw.html")

df = df[df["price"].between(MIN_PRICE, MAX_PRICE)].copy()
df["last_review"] = pd.to_datetime(df["last_review"])

ProfileReport(df, title="EDA cleaned", minimal=True).to_file("eda_cleaned.html")

art = wandb.Artifact("eda_reports", type="eda", description="Profiling reports before/after basic fixes")
art.add_file("eda_raw.html")
art.add_file("eda_cleaned.html")
run.log_artifact(art)

run.finish()
print("Done: logged artifact eda_reports to W&B")
