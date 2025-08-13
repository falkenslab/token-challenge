# token-challenge

Pequeño experimento para comprobar el uso de tokens de los modelos de OpenAI en diferentes idiomas, midiendo la cantidad de tokens necesarios para representar un texto dado en cada uno.

> ⚠️ Se trata de un pequeño experimento que no pretende ser exhaustivo ni definitivo en sus conclusiones.

## Resultados

En los resultados se observa que en general, los textos en inglés tienden a requerir menos tokens en comparación con otros idiomas, como el español o el francés.

Una explicación para esto puede ser que el modelo ha sido entrenado principalmente con datos en inglés, lo que le permite manejar mejor la tokenización y la representación de los textos en ese idioma, así como que el inglés no marca tanto el género y el número, como ocurre en otros idiomas en sustantivos, adjetivos, artículos, etc.

Se puede concluir que el inglés es el idioma más eficiente en términos de uso de tokens, por lo que utilizarlo (en este caso con los modelos LLM de OpenAI) puede ser más ventajoso en términos de coste (ya que el uso de tokens es más bajo) y eficiencia de procesamiento (ya que se requieren menos tokens para representar la misma información y para generar respuestas por parte del modelo).

## Instalación

Clonamos el repositorio y nos movemos al directorio del proyecto:

```bash
git clone https://github.com/falkenslab/token-challenge.git
cd token-challenge
```

Crearemos un entorno virtual para instalar las dependencias:
```bash
python -m venv venv
venv\Scripts\activate  # En Windows
# o
source venv/bin/activate  # En Linux o macOS
```

Instalamos las dependencias necesarias:

```bash
pip install -e .
```

Crearemos un entorno virtual para instalar las dependencias:

```bash
python -m venv venv
venv\Scripts\activate  # En Windows
# o
source venv/bin/activate  # En Linux o macOS
```

Instalamos las dependencias necesarias:

```bash
pip install -e .
```

## Uso

Para ejecutar el script de prueba, simplemente ejecutamos:

```bash
challenge
```