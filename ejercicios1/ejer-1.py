curso_tiempo_min = 2.5
curso_tiempo_max = 7
curso_tiempo_promedio = 4
curso_dalto = 1.5

diferencia_porcentaje_min = 100 - curso_dalto/curso_tiempo_min * 100
print(f'La diferencia de porcentaje entre el curso de dalto y el minimo es: {diferencia_porcentaje_min}%')

diferencia_porcentaje_max = 100 - curso_dalto*1000 // curso_tiempo_max/10
print(f'La diferencia de porcentaje entre el curso de dalto y el minimo es: {diferencia_porcentaje_max}%')

diferencia_porcentaje_prom = 100 - curso_dalto/curso_tiempo_promedio * 100
print(f'La diferencia de porcentaje entre el curso de dalto y el minimo es: {diferencia_porcentaje_prom}%')