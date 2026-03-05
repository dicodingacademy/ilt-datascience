from prefect import task

@task
def export_to_csv(df, name):
    return df.to_csv(f"{name}.csv")