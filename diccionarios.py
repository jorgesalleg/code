# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 14:26:10 2024

@author: jorge
"""
"""
PERSONA
Llaves:nombre, edad, direccion, altura, peso
Valores: Juan, 33, Reforma 333, 1,70, 80
"""
persona = { "nombre":"Juan", "edad":33, "direccion":"Reforma 333"}

print(persona["edad"])
print(persona.get("edad"))

for valor in persona.values():
    print(valor)
    
for llave in persona.keys():
    print(llave)    
    
for elemento in persona.items():
    print(elemento)

for llave, valor in persona.items():
    print(llave, valor)
    
persona["direccion"] = "Reforma 300"

persona.update({"direccion":"Reforma 200", "altura":1.70})

persona["peso"] = 80

persona.pop("peso")

"""
Contar palabras en un texto
"""
texto = "Organización, Nivel académico , Unión entre colaboradores. , Ambiente familiar., Preparación constante al docente en todas las áreas del saber., La comunicación., Protector, Amable y empático., Una sola voz, es decir que la directrices sea una sola y no tan cambiante. , Orientación por parte de los directivos , Comunicación permanente con los compañeros de trabajo, Comportamiento de algunos alumnos (Vocabulario), Organizado, Eficiente, Trabajo operativo, organización en los diferentes procesos. , Exigencia, Tener mayor iniciativa con el ser, de manera general. Trabajadores y estudiantes., Oportunidad laboral. , Organización empresarial. , Integración y mayor comunicación. , Organización, Disciplina, La comunicación oportuna. , Horario de trabajo, Organización, Espacios deportivos, Trabajo en equipo y empatía , Excelencia , Mayor Autonomía para el cuerpo docente., Preparación y capacitación constante a los colaboradores. , Trabajo en equipo. , Desde el área de matemáticas, una oportunidad de mejora sería implementar una aula virtual para los laboratorios de matemáticas , Procesos Académicos, Estabilidad Laboral, Tener en cuenta opinión de los docentes para la toma de decisiones académicas., Enfoque integral educativo y social , Lider y formador de líderes., Más cercanía por parte de la administración hacia todos los docentes, buscar tener docentes felices para que hagan un trabajo por amor , Apoyo., Capacidad de escucha., Enfocarse también en lo que sienten y piensan los docentes, no sólo en los estudiantes., Organización y orden. , Posicionamiento y reconocimiento como una excelente institución , Estructurar y realizar un procedimiento correcto en el requisito legal de Inclusión. , organizacion , Planta fisica y equipo de trabajo, Comunicacion general, La excelencia, Trabajo en equipo., Mayor autonomía para los docentes, Organización , Disciplina , Trabajo emocional con los colaboradores , 1. Capacidad de adaptación a los cambios en procesos formación., 2. Capacidad de formar pedagógicamente y de alta calidad., 1. Crear hábitos en estudiantes para el estudio., Organización , Nivel de Inglés, Mayor autonomía al docente, Organización: La forma en como cada segmento, cada recurso y cada factor institucional está dividido. , La cultura de Respeto: todos los miembros  y colaboradores de la institución manejan un buen nivel profesional y de respeto. , Gestionar de forma minuciosa las tareas, trabajos y actividades que dejamos a los estudiantes, a veces se sienten cargados con muchos ejercicios para la casa y eso los agota y desmotiva. , Que los docentes somos unidos en cuanto a los procesos educativos., los equipos tecnológicos de cada aula que ayudan al desarrollo de cada una de las clases., los salones de música y canto no parecen salones de música, ya que hace falta embellecer el entorno, con cuadros, con instrumentos (pianos, guitarras)., Se preocupan genuinamente por el colaborador abriendo espacios para el diálogo. , Los líderes directivos forman desde el ser y el ejemplo. Empoderan a los coordinadores y ayudan a desarrollar sus talentos aún con inseguridades, siempre apelan a que las personas demostremos todo nuestro potencial. , Se debe fomentar una cultura más íntegra y educar a los docentes a evitar la crítica destructiva o comentarios que puedan generar malestar. , Trabajo en equipo., La excelente formación que se adquiere durante el proceso como docente. , La sala de profesores ya que, en las primeras horas de clase es difícil el trabajo por el calor generado por la falta de ventiladores. , Organización, Responsabilidad y cumplimiento, Brindar mayor autonomía al docente., La organización que maneja., Es un colegio muy enfocado a lo familiar y siempre busca y fomenta a que se integren las famílias buscando un entorno agradable entre ellas., La sala de profesores no debería ser solo un espacio de trabajo, debería ser un poco más abierta y dispuesta al bienestar integral, permitiendo a los docentes librar cargas emocionales y de estrés, facilitando áreas de descanso, recursos para la gestión del estrés y espacios para la relajación y el esparcimiento., Responsabilidad, Organización , Mayor flexibilidad  con los docentes , Trabajo en equipo. , Honestidad. , Mejor comunicación. , Es una organización estructura, que lleva procesos de manera secuencial y dan frutos lo que se traza., Es una institución que se preocupa por el estudiantado en sus  aspectos académicos, disciplinarios  y socioafectivos., Emplear mas insumos físicos y tecnológicos en las aulas de artes y deportes, mejorando las instalaciones en su ambientación y horarios para el desarrollo de clases y conformación de grupos artísticos.  , El Gimsaber tiene como fortaleza la organización en cada uno de los procesos académicos., El Gimsaber tiene como fortaleza la unión entre todos los participantes en la institución., Brindar mayor autonomía al docente en los procesos académicos., Creo que la institución siempre busca la manera de mejorar en cualquier aspecto. Cuando se presenta una falla, se busca rápidamente la mejor opción solución para todos., La institución cuenta con todas las herramientas necesarias para nuestro trabajo, desde los recursos físicos hasta el material humano., Creo que una oportunidad de mejora sería la comunicación entre las diferentes áreas de trabajo, esto sería importante para llevar de manera alineada el proceso académico del estudiante., Ambiente familiar, Capacitación al personal docente., Unificación de criterios en la comunicación., Formación en valores, calidad educativa en competencias de formación en sus estudiantes , Mejorar en los presaber, con el objetivo de estar en el top 10 de las mejores pruebas saber 11 en Valledupar., Calidad acádemica , Planeamiento  y ejecución , Realizar con frecuencia actividades con los padres de familia y estudiantes , Somos una familia, es un grupo de trabajo eficiente, Pago puntual, Reducir la operatividad, La importancia de DIOS en todo momento., El ímpetu de siempre mejorar, innovar y brindar lo mejor a estudiantes, padres de familia y docentes. , La comunicación entre docentes y directivos., Equipo de trabajo. , Horario laboral. , Canales de comunicación , TRABAJO EN EQUIPO, BUEN CLIMA LABORAL, HACER REAJUSTES CURRICULARES PARA OBTENER RESULTADOS MEJORES Y MÁS REALES, Una de las fortalezas que encuentro en esta institución es su preocupación por sus colaboradores, nos nutre y nos reconforta saber que de una u otra forma los directivos y líderes están al tanto de nuestro bienestar, Otra fortaleza que he identifico es la exigencia en los procesos, esta nos ayuda a ser mejor como profesionales., En cuanto a la formación de nuestros estudiantes  se pueden fortalecer los valores mediante más charlas y actividades, dirigidas en especial a grados de primaria que estén presentando dificultades convivenciales. En estas pueden participar directivos y departamentos de psicología e inclusive padres de familia., COMUNICACÍON, UNIÓN , Conocerse mas con todos los compañeros. , Recursos, Respeto, Canales de comunicación, siendo más claros con la información que se brinda., comprensión ante situaciones adversas. , recursos para el desarrollo de actividades en el aula, apoyo en el manejo del estrés , Calidad humana, Crecimiento, Número de asignaciones dentro y fuera del aula. , Liderazgo, Organización, Programas de bienestar y salud mental, que permitan adquirir herramienta para el manejo emocional y manetener un equilibrio emocional saludable a nivel integral., Calidad humana., Respeto, comprensión, tolerancia. , Disminuir trabajo operativo., Calidad, Orden en todos los aspectos. , Tomar acciones de autoevaluación continua. , Infraestructura., Recursos., Apoyo en la gestión del estrés., Programa académico., Los docentes., El ser en los docentes., Velan por el bienestar de la comunidad educativa., Buen trato y capacidad de escuchar., Mejorar los canales de comunicación., Instalaciones y equipamiento., Pago puntual, trabajo en equipo, trato adecuado por los directivo y coordinadores., Gestión y manejo del estrés. , unión, competencia, funcionamiento de actividades en los recreos donde se integren las diversas edades y se le permita al estudiante tener un ambiente especial, Calidad acádemica , Compromiso , Implementar más actividades recreativas con los padres de familia, Talento humano, Innovación , Tener en cuenta que somos formadores de estudiantes reflexivos, críticos y participativos., El ambiente laboral es cómodo y agradable, los compañeros y directivos siempre están prestos a apoyarnos siempre que los necesitamos. En su gran mayoría son muy empáticos y carismáticos., Se maneja respeto entre todos los colaboradores, incluyendo respeto hacia orientación sexual credo y costumbres personales. Sobre todo sus opiniones y aportes sobre diferentes temas., Cantidad de horas (carga docente), en algunos momentos del año (periodos se hace un poco pesada la carga)., El trato humano. , Apoyo entre compañeros. , Más salidas pedagógicas a lugares donde se evidencie la aplicación del conocimiento. , La organización. Todo está correctamente sistematizado y muy ordenado, eso hace que el trabajo sea sencillo., La empatía. Es un colegio muy empático con sus estudiantes y colaboradores, realmente re preocupa por el bienestar de su comunidad., Crear más espacios verdes dentro de la institución. Eso incentivaría un interés más grande, de nuestros estudiantes, hacia el medio ambiente., cuenta con un excelente grupo administrativo y docente., es una institucion que cuenta con buenos espacios y sobre todo con un  buen metodo de desarrollo educativo., tipo de piso en la cancha., Organizada, De puertas abiertas, Comunicación clara"
texto = texto.upper()
simbolos_a_quitar = (",", ".", "(", ")","EL ","EN ", "LA ", "LAS ","DE ","POR ", "CON ", "LOS ", "LO ", "SE ","QUE ", "UNA ", "UN ","COMO ", "AL ", "Y ", "EL ","SU ",)

for simbolo in simbolos_a_quitar:
    texto = texto.replace(simbolo," ")

vocablos = texto.split()
palabras = {}
for vocablo in vocablos:
    if vocablo in palabras.keys():
        palabras[vocablo] = palabras[vocablo] + 1
    else:
        palabras[vocablo] = 1

lista = list(palabras.items())

lista.sort(key = lambda palabra : palabra[1])
print(lista)



