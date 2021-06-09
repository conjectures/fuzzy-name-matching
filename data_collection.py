

from google.cloud import bigquery


def fetch_bq():

    client = bigquery.Client()
    sql = """
    SELECT
     names.name, names.gender, sum(names.number) as `total_count`
    FROM
        `bigquery-public-data..usa_names.usa_1910_2013` AS names
    GROUP BY
     names.name, names.gender
    ORDER BY
     sum(names.number) DESC
    LIMIT
        5000;
    """
    df = client.query(sql).to_dataframe()
    res = df.head(100)

    df.to_csv('usa_names_2010.csv', index=False)
