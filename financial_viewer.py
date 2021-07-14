from sys import argv
import os
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates


def get_files_in_folder(path):
    result = []

    for a in os.walk(path, False):
        if len(a[2]) == 0:
            break
        for file in a[2]:
            result.append(os.path.join(a[0], file))

    return result


def read_money(money):
    try:
        return float(money.replace('$', ''))
    except:
        return money

def daily(tss):
    result = [0] * len(tss)
    for i in range(len(tss)):
        result[i] = tss[i].to_period('D').to_timestamp()

    return pd.DatetimeIndex(result)


if __name__ == '__main__':
    folder = "finances"
    if argv is not None and len(argv) > 1:
        folder = argv[1]

    files = get_files_in_folder(folder)

    df = pd.DataFrame()

    for f in files:
        df_read = pd.read_csv(f, header=0, converters={'Amount': read_money}, parse_dates=['Transaction Date'], index_col=0)
        df = pd.concat([df, df_read])

    spending = df[(df['Amount'] > 0)]

    # spending = spending.groupby(['Transaction Date'])['Amount'].sum()
    spending = spending.groupby(daily)['Amount'].sum()

    cumsum = spending.cumsum()

    fig, ax = plt.subplots(1)

    #zerothElementInIndex = [i[0] for i in cumsum.index]
    ax.plot(cumsum.index, cumsum, 'x-k')

    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
    # ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
    ax.xaxis_date()
    fig.autofmt_xdate()

    plt.show()


