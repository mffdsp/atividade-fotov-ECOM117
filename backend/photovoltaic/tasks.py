from celery import shared_task
from celery.execute import send_task

from datetime import datetime
from pytz import timezone
import numpy as np
import random

from .util import read_dat_file

from photovoltaic.models import PVData, PVString, PowerForecast, YieldDay, YieldMonth, YieldYear, YieldMinute

@shared_task(bind=True, max_retries=3)
def simulate_input(self):
    df = read_dat_file("./photovoltaic/fixtures/test_day.dat")

    tz = timezone('America/Sao_Paulo')
    datetime_now = tz.localize(datetime.now())

    index = datetime_now.hour*60 + datetime_now.minute

    df_row = df.iloc[[index]]

    s1 = PVString.objects.create(name="S1 " + str(datetime_now), 
                                timestamp=datetime_now,
                                voltage=df_row['Tensao_S1_Avg'],
                                current=df_row['Corrente_S1_Avg'],
                                power=df_row['Potencia_S1_Avg'],
                                voltage_alert=np.random.choice(['NM', 'WA', 'FT'], p=[0.88, 0.10, 0.02]),
                                current_alert=np.random.choice(['NM', 'WA', 'FT'], p=[0.88, 0.10, 0.02]),
                                string_number=1)
    
    s2 = PVString.objects.create(name="S2 " + str(datetime_now),
                                timestamp=datetime_now,
                                voltage=df_row['Tensao_S2_Avg'],
                                current=df_row['Corrente_S2_Avg'],
                                power=df_row['Potencia_S2_Avg'],
                                voltage_alert=np.random.choice(['NM', 'WA', 'FT'], p=[0.83, 0.15, 0.02]),
                                current_alert=np.random.choice(['NM', 'WA', 'FT'], p=[0.83, 0.15, 0.02]),
                                string_number=2)

    data = PVData.objects.create(timestamp=datetime_now,
                                irradiation=df_row['Radiacao_Avg'],
                                temperature_pv=df_row['Temp_Cel_Avg'],
                                temperature_amb=df_row['Temp_Amb_Avg'],
                                power_avg=df_row['Potencia_FV_Avg'])

    data.strings.set([s1, s2])

    energy = df_row['Potencia_FV_Avg']*(1/60)/1000

    day = datetime_now.replace(hour=0, minute=0, second=0, microsecond=0)
    yield_day, created = YieldDay.objects.get_or_create(timestamp=day)
    yield_day.yield_day = yield_day.yield_day + energy #kWh
    yield_day.yield_day_forecaste = 30
    yield_day.save()

    yield_minute, created = YieldMinute.objects.get_or_create(timestamp=datetime_now)
    yield_minute.yield_minute = yield_day.yield_day #kWh
    yield_minute.yield_day_forecaste = 30
    yield_minute.save()

    month = day.replace(day=1)
    yield_month, created = YieldMonth.objects.get_or_create(timestamp=month)
    yield_month.yield_month = yield_month.yield_month + energy #kWh
    yield_month.save()

    year = month.replace(month=1)
    yield_year, created = YieldYear.objects.get_or_create(timestamp=year)
    yield_year.yield_year = yield_year.yield_year + (energy/1000) #MWh
    yield_year.save()

    power1 = float(df.iloc[[index+1]]['Potencia_FV_Avg'])
    power2 = float(df.iloc[[index+2]]['Potencia_FV_Avg'])
    power3 = float(df.iloc[[index+3]]['Potencia_FV_Avg'])
    power4 = float(df.iloc[[index+4]]['Potencia_FV_Avg'])
    power5 = float(df.iloc[[index+5]]['Potencia_FV_Avg'])

    simulate_model.apply_async(args=[datetime_now, power1, power2, power3, power4, power5], kwargs={}, queue='model')

@shared_task(bind=True, max_retries=3)
def simulate_model(self, datetime_now, power1, power2, power3, power4, power5):
    pf = PowerForecast.objects.create(timestamp=datetime_now,
                                    t1=power1 + random.uniform(0, 1.0),
                                    t2=power2 + random.uniform(0.3, 1.3),
                                    t3=power3 + random.uniform(0.6, 1.6),
                                    t4=power4 + random.uniform(0.9, 1.9),
                                    t5=power5 + random.uniform(1.2, 2.2))


# @shared_task(bind=True, max_retries=3)
# def calculate_alerts_tresholds(self):
#     pass
