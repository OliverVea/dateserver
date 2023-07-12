import datetime
import flask

DATE_FORMAT = '%Y-%m-%d'

def parse_date_string(s: str) -> datetime.date:
    year = int(s[:-4])
    month = int(s[-4:-2])
    day = int(s[-2:])

    return datetime.date(year, month, day)


def try_parse_date_string(s: str) -> str:
    try:
        date = parse_date_string(s)
        return date.strftime(DATE_FORMAT)
    except Exception as e:
        print(e)
        return s


app = flask.Flask(__name__)

@app.get('/prettify-date-string/<date>')
def prettify_date_string(date: str):
    return try_parse_date_string(date)

app.run()