# RigelSirius

### Métodos Numéricos - Semestre 2025-B

En este repositorio se trabajará durante el transcurso del proyecto del semestre **2025-B** de la asignatura **Métodos Numéricos**.  

**Descripción del proyecto**:
El proyecto busca analizar numéricamente características clínicas de las lesiones cutáneas, usando variables que se encuentran en el dataset ISIC 2024 para construir una función que permita detectar o clasificar lesiones cutáneas que podrían corresponder a un melanoma. Para lo cual se usarán variables relacionadas con el estándar dermatológico ABCD (Asimetría, Bordes, Color y Diámetro).

**Descripcion del Dataset**
El dataset utilizado corresponde al ISIC 2024 - Skin Cancer Detection Challen-
ge, disponible púbicamente en la plataforma Kaggle, uno de los repositorios más
completos para el estudio cuantitativo de lesiones cutáneas. Este dataset incluye imáge-
nes clínico-dermatoscópicas de lunares y lesiones de piel, junto con un conjunto extenso de
variables tabulares generadas mediante análisis geométricos, cromáticos y estadísticos
realizados por la International Skin Imaging Collaborating (ISIC).
Las variables tabulares provienen de procesamientos numéricos sobre las imáge-
nes, tales como el cálculo de área, perímetro, ejes principales, excentricidad, métricas
de borde, desviaciones estándar de color y variaciones de pigmentación. Estas medicio-
nes constituyen representaciones cuantitativas de factores clínicos asociados al estándar
ABCD (Asimetría, Borde, Color, Diámetro), ampliamente utilizado para la evaluación
inicial de lesiones cutáneas

## Etapa 0 – Selección y filtrado del dataset

Para el desarrollo tentativo de este proyecto, primero se realiza la identificación y selección de las variables del *dataset*, con el fin de llevar a cabo un filtrado adecuado de la información. Se propone conservar únicamente las variables relacionadas con los parámetros clínicos del estándar dermatológico **ABCD**, debido a que este criterio es ampliamente utilizado para la detección temprana del melanoma y ha demostrado ser un método fiable, fácil de aplicar y consistente con el diagnóstico de un experto [5].

Por otro lado, se emplean datos provenientes de imágenes del tipo **3D "XP"**, ya que este tipo de imágenes reduce el efecto de la iluminación, sombras y variaciones superficiales, permitiendo una mejor visualización de la lesión. Esto contribuye a que la información de las variables sea más clara y representativa.

Como parte del proceso de filtrado, también es fundamental eliminar datos nulos, incompletos o inconsistentes, dado que estos pueden generar sesgos que afecten negativamente la aplicación de los métodos numéricos.

---

## Etapa 1 – Normalización de las variables seleccionadas

Una vez seleccionadas las variables y obtenido el *dataset* filtrado, es necesario aplicar un proceso de normalización. Esto se debe a que cada variable puede presentar unidades y rangos muy diferentes entre sí, lo cual podría generar desequilibrios en el análisis. Para evitar que una variable influya más que otra únicamente por manejar valores de mayor magnitud, se normalizan todas las variables a una misma escala.


Se sugiere utilizar la normalización **Min–Max**, ya que permite conservar la forma y distribución original de los datos, además de llevar todas las variables a un rango común.

---

## Etapa 2 – Obtención de índices relacionados con el estándar ABCD

Se propone calcular índices individuales para cada parámetro del estándar **ABCD**, debido a que las variables seleccionadas del *dataset* se asocian directamente a cada uno de estos parámetros. Por esta razón, no deben tratarse como variables independientes ni asignarse el mismo peso a todas.

Dada la cantidad de variables obtenidas por cada parámetro, se plantea calcular estos índices mediante un método que permita identificar cuáles variables presentan una mayor relación con el objetivo (*target*). Esto evita el uso de pesos equitativos o promedios simples, los cuales podrían ocultar la importancia relativa de cada variable.

---

## Etapa 3 – Ajuste de curvas multivariables

Una vez obtenidos los índices correspondientes a cada parámetro, se propone construir una función que describa la relación existente entre ellos. Para este propósito, se utilizará el método de **mínimos cuadrados multivariable lineal**, ya que la alta cantidad de registros del *dataset* permite obtener una función que se ajuste de forma adecuada, minimizando las diferencias entre los valores calculados y los observados.

Se selecciona un modelo de grado lineal debido a que no se dispone de la cantidad de variables ni de la estructura necesaria para aplicar un modelo cuadrático. Además, el uso de interpolaciones o ajustes de grado superior podría generar oscilaciones indeseadas y conducir a un sobreajuste del modelo.

---

## Etapa 4 – Clasificación

Una vez obtenidos los pesos asociados a cada parámetro dentro de la función final, es necesario establecer un valor límite que permita decidir si el caso analizado es positivo o negativo (*target*). Este valor, conocido como **umbral**, es fundamental, ya que define la interpretación de la salida del modelo.

Dado que en este tipo de problemas siempre existirán errores de clasificación, el umbral no puede elegirse de forma arbitraria. Por esta razón, se propone emplear un criterio que considere las diferencias entre los posibles tipos de error, de modo que el funcionamiento del sistema sea coherente con el problema clínico analizado.

Para definir el umbral, se prueban diferentes valores dentro del rango permitido y se comparan sus errores asociados, con el objetivo de encontrar aquel que resulte más adecuado para el contexto clínico. El resultado será el umbral que mejor se ajuste al propósito del problema planteado.


## Integrantes
- Cristhian Carrillo
- Jumbo Frank  
- Andy Rengifo
