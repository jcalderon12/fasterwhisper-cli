import argparse
import logging


from .utils.file_utils import is_media_file 
from .utils.logger import configure_logger 
from .utils.whisper import transcribe_audio 

def main():

    logger = configure_logger()

    parser = argparse.ArgumentParser(description="Transcribe audio using faster-whisper")
    parser.add_argument("file_path", help="Path to the audio file. Must be a valid audio or video file")
    parser.add_argument("-o", "--output", required=False, help="Output file to store the transcribed text")
    parser.add_argument("--model_size", required=False, choices=["tiny", "small"], default="tiny", help="Model size of whisper")

    args = parser.parse_args()

    try:
        is_media_file(args.file_path)

    except TypeError:
        logger.error("The selected file is a directory")
    except ValueError:
        logger.error("The selected file is not a video/audio file or is not in a compatible format")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")

    transcribed_text = transcribe_audio(args.file_path, args.model_size)
    logger.info("Using %s size for the model", args.model_size)

    
    if args.output:
        try:
            with open(args.output, 'w') as output_file:
                for segment in transcribed_text:
                    output_file.write("[%.2fs -> %.2fs] %s \n" % (segment.start, segment.end, segment.text))
                logger.info("Text saved successfully")
        except FileNotFoundError:
            logger.error(f"Error: The output route entered is wrong: {args.output}")
        except OSError:
            logger.error("Error: There was a problem writing to the file")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
    else:
        logger.info("The transcription of the file is as follows:")
        for segment in transcribed_text:
            logger.info("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
    

if __name__ == "__main__":
    main()