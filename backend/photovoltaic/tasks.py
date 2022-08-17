from celery import shared_task
from celery.execute import send_task

from datetime import datetime

from .util import read_dat_file

from photovoltaic.models import PVData, PVString, PowerForecast, YieldDay, YieldMonth

# def createNotification(self, exc, task_id, args, kwargs, einfo):
#     notification = Notification.create(title="Erro em tarefa de background.", message="Erro na execução da tarefa {task}: {einfo}".format(task=task_id, einfo=einfo), link='/nlp/admin/logs/')
#     notification.save()

@shared_task(bind=True)
def simulate_input(self):
    print("Test")

    df = read_dat_file("./photovoltaic/fixtures/test_day.dat")

    datetime_now = datetime.now()

    index = datetime_now.hour*60 + datetime_now.minute

    df_row = df.iloc[[index]]

    s1 = PVString.objects.create(name="S1 " + str(datetime_now), 
                                timestamp=datetime_now,
                                voltage=df_row['Tensao_S1_Avg'],
                                current=df_row['Corrente_S1_Avg'],
                                power=df_row['Potencia_S1_Avg'])
    s2 = PVString.objects.create(name="S2 " + str(datetime_now),
                                timestamp=datetime_now,
                                voltage=df_row['Tensao_S2_Avg'],
                                current=df_row['Corrente_S2_Avg'],
                                power=df_row['Potencia_S2_Avg'])
    data = PVData.objects.create(timestamp=datetime.now(),
                                irradiation=df_row['Radiacao_Avg'],
                                temperature_pv=df_row['Temp_Cel_Avg'],
                                temperature_amb=df_row['Temp_Amb_Avg'],
                                power_avg=df_row['Potencia_FV_Avg'])

    data.strings.set([s1, s2])

    energy = df_row['Potencia_FV_Avg']*(1/60)/1000

    day = datetime_now.replace(hour=0, minute=0, second=0, microsecond=0)
    yield_day, created = YieldDay.objects.get_or_create(timestamp=day)
    yield_day.yield_day = yield_day.yield_day + energy #kWh
    yield_day.save()

    month = day.replace(day=1)
    yield_month, created = YieldMonth.objects.get_or_create(timestamp=month)
    yield_month.yield_month = yield_month.yield_month + energy #kWh
    yield_month.save()

    # year = month.replace(month==1)
    # yield_year, created = YieldYear.objects.get_or_create(timestamp=year)
    # yield_year.yield_year = yield_year.yield_year + (energy/1000) #MWh
    # yield_year.save()

