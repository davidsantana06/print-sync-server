from datetime import date, datetime


TIME_PATTERN = '%H:%M'
DATE_PATTERN = '{day} de {month} de {year}'
MONTH = [
    'jan.', 'fev.', 'mar.', 'abr.', 'mai', 'jun.',
    'jul.', 'ago.', 'set.', 'out.', 'nov.', 'dez.'
]


def dt_now() -> datetime:
    return datetime.now()


def format_dt(dt: datetime, reference_date: date) -> str:
    formatted_dt = ''

    if dt.date() == reference_date:
        formatted_dt = dt.strftime(TIME_PATTERN)
    else:
        month_idx = dt.month - 1
        formatted_dt = DATE_PATTERN.format(
            month=MONTH[month_idx], day=dt.day, year=dt.year
        )

    return formatted_dt
