import pandas as pd

def question_four(df: pd.Series):
    """Toma una serie y cuenta cuantos terminos diferentes hay"""
    economicos = 0
    recursos_humanos = 0
    politicas_ins, politicas_pu = 0, 0
    etico = 0
    juridico, factibilidad = 1, 1
    for i in df:
        i = i.replace(", ", ",")
        aspectos = i.split(",")
        if "Aspectos económicos" in aspectos:
            economicos += 1

        if "Recursos humanos" in aspectos:
            recursos_humanos += 1

        if "Políticas institucionales" in aspectos:
            politicas_ins += 1

        if "Políticas públicas" in aspectos:
            politicas_pu += 1

        if "Aspectos éticos" in aspectos:
            etico += 1
        
    return economicos, recursos_humanos, politicas_ins, politicas_pu, etico, juridico, factibilidad


def question_five(df: pd.Series):
    """Toma una serie y cuenta cuantos terminos diferentes hay"""
    mejoras_atención , mejora_procesos = 0, 0
    mejora_flujos_trabajo, satisfacción_usuarios = 0, 0
    mejora_percepción_de_usuarios, redistribución_trabajos = 1, 1
    for i in df:
        i = i.replace(", ", ",")
        impacto = i.split(",")
        if "Mejoras en la atención al usuario." in impacto:
            mejoras_atención += 1

        if "Mejora de procesos internos de las bibliotecas." in impacto:
            mejora_procesos += 1

        if "Mejoras en los flujos de trabajo." in impacto:
            mejora_flujos_trabajo += 1

        if "Satisfacción de los usuarios en los servicios." in impacto:
            satisfacción_usuarios += 1
    return mejoras_atención, mejora_procesos, mejora_flujos_trabajo, satisfacción_usuarios, mejora_percepción_de_usuarios, redistribución_trabajos


def question_six(df: pd.Series):
    """Toma una serie y cuenta cuantos terminos diferentes hay"""
    servicios_de_descubrimiento, robotica = 0, 0
    chatbots, autoprestamos_autoservicio = 0, 0
    catalogacion_automatizada, sistemas_de_recomendación = 0, 0
    servicios_descarte = 1

    for i in df:
        i = i.replace(", ", ",")
        tecnologia = i.split(",")
        if "Servicios de descubrimiento con asistentes inteligentes" in tecnologia:
            servicios_de_descubrimiento += 1

        if "Robótica" in tecnologia:
            robotica += 1

        if "Servicios de ayuda al estudiante vía chat. (chatbots)" in tecnologia:
            chatbots += 1

        if "Autopréstamos/autoservicio" in tecnologia:
            autoprestamos_autoservicio += 1
        
        if "Catalogación/clasificación automatizada" in tecnologia:
            catalogacion_automatizada += 1

        if "Sistemas de recomendación" in tecnologia:
            sistemas_de_recomendación += 1
    return servicios_de_descubrimiento, robotica, chatbots, autoprestamos_autoservicio, catalogacion_automatizada, sistemas_de_recomendación, servicios_descarte


def question_eight(df: pd.Series):
    """Toma una serie y cuenta cuantos terminos diferentes hay"""
    ia, reconocimiento_de_voz = 0, 0
    realidad_aumentada, mineria_datos = 0, 0
    autoprestamo, gamificacion = 0, 0
    chatbots, otro = 0, 0

    for i in df:
        i = i.replace(", ", ",")
        tecnologia = i.split(",")
        if "Reconocimiento de voz." in tecnologia:
            reconocimiento_de_voz += 1

        if "Minería de Datos" in tecnologia:
            mineria_datos += 1

        if "Auto-Préstamos de material bibliográfico." in tecnologia:
            autoprestamo += 1

        if "Chatbots" in tecnologia:
            chatbots += 1
        
        if "Aplicaciones de realidad aumentada." in tecnologia:
            realidad_aumentada += 1

        if "Inteligencia Artificial / Aprendizaje automático." in tecnologia:
            ia += 1

        if "Gamificación de la experiencia bibliotecaria." in tecnologia:
            gamificacion += 1
        
        if "Otros avances tecnológicos." in tecnologia:
            otro += 1
    return ia, reconocimiento_de_voz, realidad_aumentada, mineria_datos, autoprestamo, gamificacion, chatbots, otro