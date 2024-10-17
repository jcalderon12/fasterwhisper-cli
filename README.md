# fasterwhisper-cli
Final assingment for Data Pre-processing 

`fasterwhisper-cli` is a command-line interface tool that allows users to transcribe audio files using the faster-whisper library. This project was created as a final assignment for Data Pre-processing subject.

## Installation

To install fasterwhisper-cli, you can use pip:

```bash
pip install -e .
```

NOTE: when using `-e` argument, there's no need to reinstall the library after making changes to it.

## Usage

After installation, you can use the CLI tool as follows:

```bash
fasterwhisper-cli <path_to_audio_file>
```

Replace `<path_to_audio_file>` with the path to your audio or video file.

## Supported File Formats

The tool supports various audio and video formats, including:

- Audio: .mp3, .wav, .ogg, .aac, .flac, .m4a, .wma
- Video: .mp4, .avi, .mov, .mkv, .flv, .wmv, .webm

# Preguntas para responder sobre la práctica:

1. ¿En qué casos has usado `logger.info` y qué casos has usado `logger.error`?

2. ¿Qué excepciones controlas en el caso de escribir en un archivo el resultado de la transcripción?

3. Según su docstring, ¿qué posibles valores hay para el parámetro `device` en la clase `WhisperModel`?

4. ¿Cómo se indica en Python el valor por defecto de un argumento en una **función**?

5. ¿Cuál es el valor por defecto de `device` en el constructor de `WhisperModel`?

6. ¿Cuáles son los valores obligatorios para la clase `WhisperModel`?

7. ¿Has usado un linter? ¿Cuál y cómo lo has ejecutado?

8. ¿Has usado tipado opcional? ¿Porqué si o porqué no?

9. ¿Cómo se añadiría un argumento nuevo usando `argparse`?

# Preguntas genéricas:

10. Cómo aplicarías tipado opcional a la siguiente función:

```python
def transcribe_audio(file_path, model_size = "tiny"):
```

11. ¿Cuál de las siguientes opciones se trata de importacion realtiva?

```python
from .utils.math_operations import sum #opcion 1
from utils.math_operations import sum #opcion 2
```

12. ¿Cómo puedo instalar la versión 2.1.0 de numpy?

13. ¿Porqué es importante especificar las versiones de un paquete en el requirements.txt?

14. ¿Y cómo puedo especificar que quiero instalar una versión de numpy menor a la 2.0.0?

15. ¿Para qué sirve modularizar código?

16. ¿Cómo le doy un alias a una librería?

17. ¿Cómo puedo obtener una lista de los paquetes instalados en mi entorno?

18. ¿Cómo puedo crear un nuevo entorno con conda? ¿Y porqué es recomendado usar entornos virtuales?
