promedio_crudo = 5
dalto_crudo = 3.5
curso_tiempo_promedio = 4
curso_dalto = 1.5

porcentaje_crudo_promedio = 100 - curso_tiempo_promedio/promedio_crudo*100
print(f'El porcentaje del material inservible del promedio es de: {porcentaje_crudo_promedio}%')


porcentaje_crudo_dalto = 100 - curso_dalto * 1000 // dalto_crudo/10
print(f'El porcentaje del material inservible del curso de dalto es de: {porcentaje_crudo_dalto}%')
