import cdsapi
import pandas as pd
import numpy as np
import multiprocessing as mp
import time
import sys


# params = '129/130/131/132/133'
def get_ml_era5(date=None, time=None, params=None):
    output_filename = 'ea.oper.an.ml.' + date + time
    c = cdsapi.Client()
    c.retrieve('reanalysis-era5-complete', {
        'class': 'ea',
        'date': date,
        'expver': '1',
        'levelist': '1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26/27/28/29/30/31/32/33/34/35/36/37/38/39/40/41/42/43/44/45/46/47/48/49/50/51/52/53/54/55/56/57/58/59/60/61/62/63/64/65/66/67/68/69/70/71/72/73/74/75/76/77/78/79/80/81/82/83/84/85/86/87/88/89/90/91/92/93/94/95/96/97/98/99/100/101/102/103/104/105/106/107/108/109/110/111/112/113/114/115/116/117/118/119/120/121/122/123/124/125/126/127/128/129/130/131/132/133/134/135/136/137',
        'levtype': 'ml',
        'param': params,
        'stream': 'oper',
        'time': time,
        'type': 'an',
    }, output_filename)


def get_sfc_era5(date=None, time=None, params=None):
    # TODO: modify this function to get the correct surface era5 data
    output_filename = 'ea.oper.an.sfc.' + date + time
    c = cdsapi.Client()
    c.retrieve('reanalysis-era5-complete', {
        'class': 'ea',
        'date': date,
        'expver': '1',
        'levelist': '1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26/27/28/29/30/31/32/33/34/35/36/37/38/39/40/41/42/43/44/45/46/47/48/49/50/51/52/53/54/55/56/57/58/59/60/61/62/63/64/65/66/67/68/69/70/71/72/73/74/75/76/77/78/79/80/81/82/83/84/85/86/87/88/89/90/91/92/93/94/95/96/97/98/99/100/101/102/103/104/105/106/107/108/109/110/111/112/113/114/115/116/117/118/119/120/121/122/123/124/125/126/127/128/129/130/131/132/133/134/135/136/137',
        'levtype': 'sfc',
        'param': params,
        'stream': 'oper',
        'time': time,
        'type': 'an',
    }, output_filename)


if __name__ == '__main__':

    scratch_dir = '/glade/scratch/gbromley/'

    start_year = int(sys.argv[1])
    end_year = int(sys.argv[2])

    if (end_year <= start_year):
        print("invalid years")
        sys.exit()

    if (start_year < 1979 or end_year >= 2018 or start_year >= 2017 or end_year <= 1979):
        print("invalid range of years")
        sys.exit()

    start_year = 2011
    end_year = 2012
    num_years = end_year - start_year
    months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18',
            '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    times_utc = ['00', '03', '06', '09', '12', '15', '18', '21']
    num_days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    num_times = 8
    print("grabbing " + str(start_year) + " to " + str(end_year))
    current_year = start_year

    # output_filename = 'ea.oper.an.sfc'

    # date = ''
    # pool = mp.Pool(processes=1)
    for year in np.arange(0, num_years + 1, 1):
        for month in np.arange(0, 12, 1):
            for day in np.arange(0, num_days_month[month], 1):
                for time in np.arange(0, num_times, 1):
                    date = str(start_year + year) + months[month] + days[day]
                    print(date)
                    e5_time = times_utc[time]
                    print(e5_time)
                    params = '129/130/131/132/133'
# TODO: Confirm that this loop spawns the cdsapi properly.

# pool.apply_async(get_ml_era5, args=(date,e5_time,params))


# pool.close()
# pool.join()
