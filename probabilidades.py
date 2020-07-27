import random

from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

def graph(values, name):


    output_file("colormapped_bars.html")

    times = ['100', '1000', '10000', '100000']
    counts = [5, 3, 4, 2, 4, 6]

    source = ColumnDataSource(data=dict(times=times, values=values))

    p = figure(x_range=times, plot_height=1000, toolbar_location=None, title=name)
    p.vbar(x='times', top='values', width=0.9, source=source, legend_field="times", line_color='white', fill_color=factor_cmap('times', palette=Spectral6, factors=times))
    p.y_range.start = 0
    p.y_range.end = 1
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"

    show(p)


def tirar_dado(numero_de_tiros):
    secuencia_de_tiros = []

    for i in range(numero_de_tiros):
        tiro = random.randint(2, 12)
       
        secuencia_de_tiros.append(tiro)
    return secuencia_de_tiros


def main(numero_de_tiros, numero_de_intentos, numero_persona):
    tiros = []

    for _ in range(numero_de_intentos):
        secuencia_de_tiros = tirar_dado(numero_de_tiros)
        tiros.append(secuencia_de_tiros)

    tiros_acertados = 0
    tiros_no_acertados = 0
    for tiro in tiros:
        if numero_persona in tiro:
            tiros_acertados += 1
        else: 
            tiros_no_acertados += 1
    
    probabilidad_de_tiros_acertados = tiros_acertados / numero_de_intentos
    probabilidad_de_tiros_no_acertados = tiros_no_acertados /numero_de_intentos
    # print(f"La probabilad de obtener por lo menos un 1 en un numero de intentos de {numero_de_intentos} es de {probabilidad_tiros_con_1}")
    print(f"La probabilad de obtener por lo menos un {numero_persona} en {numero_de_tiros} tiros\nSimulando este proceso {numero_de_intentos} veces es de {probabilidad_de_tiros_acertados}")
    print(f"La probabilad de NO obtener por lo menos un {numero_persona} en {numero_de_tiros} tiros\nSimulando este proceso {numero_de_intentos} veces es de {probabilidad_de_tiros_no_acertados}")
    print("=================================================================")
    return (probabilidad_de_tiros_acertados, probabilidad_de_tiros_no_acertados)


if __name__ == "__main__":
    all_prob_acert = []
    all_prob_no_acert = []

    numero_de_tiros = int(input("Cuantos veces quieres tirar los dos dados: "))
    numero_persona = int(input("A que numero le apuestas: "))
    while numero_persona > 12 or numero_persona < 2:
        numero_persona = int(input("El numero maximo con dos dados en 12 y el minimo es 2\n A que numero le apuestas:  "))
    numero_de_intentos = [100, 1000, 10000, 100000]

    for interval in numero_de_intentos:
        prob_acert, prob_no_acert = main(numero_de_tiros, interval, numero_persona)
        all_prob_acert.append(prob_acert)
        all_prob_no_acert.append(prob_no_acert)
    
    print("Graficando las probabilidades: ")
    print(f"Acertado: {all_prob_acert}")
    print(f"No Acertado: {all_prob_no_acert}")

    graph( all_prob_no_acert, f"Probabilidades no acertar con {numero_de_tiros} tiros" )
    graph( all_prob_acert, f"Probabilidades acertar con {numero_de_tiros} tiros" )

    print("=================================================================")

