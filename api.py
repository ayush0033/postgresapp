from app import PostgreSQL
app = PostgreSQL()

@app.action("Run SQL Query")
def run_query(params):
    return app.run_query(
        params["host"],
        params["port"],
        params["dbname"],
        params["user"],
        params["password"],
        params["query"]
    )
