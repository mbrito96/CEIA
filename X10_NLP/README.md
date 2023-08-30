# NLP - Procesamiento de Lenguaje Natural

En este repositorio se encuentran los trabajos prácticos realizados para la materia Procesamiento del Lenguaje Natural (NLP), que forman parte de la carrera de [Especializacion en IA de la UBA](https://lse.posgrados.fi.uba.ar/posgrados/especializaciones/inteligencia-artificial) (Universidad Nacional de Buenos Aires). 

A continuación se detalla el contenido de estos trabajos:

## Desafío 1: [Word2Vec](./1a&#32;-&#32;word2vec.ipynb) <a href="https://colab.research.google.com/github/mbrito96/CEIA/blob/main/X10_NLP/1a%20-%20word2vec.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" height=22.5></a>

Este trabajo tiene como objetivo introducir algunos conceptos y herramientas de procesamiento de lenguaje natural (NLP). Para ello, se utilizaron técnicas de vectorización de documentos, como OneHotEncoding o TF-IDF. Estas técnicas permiten representar a los documentos como una secuencia de vectores numéricos que son las palabras, lo que posibilita operar con ellos. Finalmente, se calculó la similitud entre documentos utilizando la similitud coseno, una medida que cuantifica la similitud entre dos vectores.

## Desafío 2: [IoT Chatbot (DNN + spaCy)](./Clase&#32;2/iot_bot_actions_v1.ipynb) <a href="https://colab.research.google.com/github/mbrito96/CEIA/blob/main/X10_NLP/Clase%202/iot_bot_actions_v1.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" height=22.5></a>

En este trabajo se desarrolló un chatbot utilizando redes neuronales densas (DNN) y la librería [spaCy](https://spacy.io/universe/project/spacy-stanza). Orientado a un contexto de IoT, el bot utiliza redes neuronales para analizar un comando escrito por el usuario y poder identificar la intención en ese texto (por ejemplo encender la luz, poner música o preguntar sobre el clima), para así clasificar el comando dentro de una categoría. Una vez identificada la categoría, el bot responde con respuestas predefinidas para notificar al usuario de la acción que se ejecutará.

## Desafío 3: [Custom embedding con Gesim](./Clase&#32;3/Custom&#32;embedding&#32;con&#32;Gensim.ipynb) <a href="https://colab.research.google.com/github/mbrito96/CEIA/blob/main/X10_NLP/Clase%203/Custom%20embedding%20con%20Gensim.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" height=22.5></a>

En este trabajo se generan embeddings de palabras basados un contexto específico, utilizando [Gensim](https://radimrehurek.com/gensim/). Como dataset, se utilizó el libro "[Sinceramente](https://es.wikipedia.org/wiki/Sinceramente)" de Cristina Fernandez de Kirchner. 

## Desafío 4: [Text Prediction](./Clase&#32;4/4d&#32;-&#32;predicción_palabra.ipynb) <a href="https://colab.research.google.com/github/mbrito96/CEIA/blob/main/X10_NLP/Clase%204/4d%20-%20predicci%C3%B3n_palabra.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" height=22.5></a>

El objetivo es utilizar documentos (corpus) para crear embeddings de palabras basado en ese contexto utilizando la layer Embedding de Keras. Se utilizará esos embeddings junto con layers LSTM para predecir la próxima palabra más probable a partir de un texto ingresado por el usuario. Se utilizó el mismo dataset del desafío anterior para entrenar los embeddings y el predictor.

## Desafío 5: [Sentiment analysis (Embeddings + LSTM)](./Clase&#32;5&#32;-&#32;Sentiment&#32;Analysis/5b_clothing_ecommerce_reviews_embd.ipynb) <a href="https://colab.research.google.com/github/mbrito96/CEIA/blob/main/X10_NLP/Clase%205%20-%20Sentiment%20Analysis/5a_clothing_ecommerce_reviews.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" height=22.5></a>


El objetivo es utilizar las críticas de compradores de ropa (eCommerce) para que el sistema determine la evaluación del comprador y su crítica (los cuales puntuaron a cada prenda con un puntaje de 1 a 5 estrellas). Se realizaron dos notebooks, la primera creando embeddings propios y la segunda utilizando embeddings de [FastText](https://fasttext.cc/). En la arquitectura del modelo, se utilizaron Embeddings y celdas de tipo LSTM.

## Desafío 6: [Q&A Chatbot (Embeddings + LSTM)](./Clase&#32;6/6_bot_qa.ipynb) <a href="https://colab.research.google.com/github/mbrito96/CEIA/blob/main/X10_NLP/Clase%206/6_bot_qa.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" height=22.5></a>

El objetivo de este desafío es utilizar datos disponibles del challenge ConvAI2 (Conversational Intelligence Challenge 2) de conversaciones en inglés. Se construirá un BOT para responder a preguntas del usuario (QA). El modelo propuesto tiene una arquitectura tipo encoder-decoder utilizando Embeddings y celdas tipo LSTM. Para el entrenamiento, la arquitectura propuesta fue la siguiente:

<p align="center" float="left" justify-content="center">
    <img src="./Clase&#32;6/arch.png" alt="model_enc-dec" class="center" width="820"/>
</p>

