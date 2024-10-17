import argparse
import logging


from utils import file_utils as fu # import 
from utils import logger as lg # import 
from utils import whisper as wp # import   

def main():

    logger = lg.configure_logger()

    parser = argparse.ArgumentParser(description="Transcribe audio using faster-whisper")
    parser.add_argument("file_path", help="Path to the audio file. Must be a valid audio or video file")
    parser.add_argument("-o", "--output", required=False, help="Output file to store the transcribed text")
    parser.add_argument("--model_size", required=False, choices=["tiny", "small"], default="tiny", help="Model size of whisper")

    args = parser.parse_args()

    try:
        fu.is_media_file(args.file_path)

    except TypeError:
        logger.error("The selected file is a directory")
    except ValueError:
        logger.error("The selected file is not a video/audio file or is not in a compatible format")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")

    if args.model_size:
        transcribed_text = wp.transcribe_audio(args.file_path, args.model_size)
        logger.info(f"Using {args.model_size} size for the model")
    else:
        transcribed_text = wp.transcribe_audio(args.file_path)
        logger.info("Using tiny size for the model")
    
    if args.output:
        try:
            with open(args.output, 'w') as output_file:
                output_file.write(transcribed_text)
                logger.info("Text saved successfully")
        except FileNotFoundError:
            logger.error(f"Error: The output route entered is wrong: {args.output}")
        except IOError:
            logger.error("Error: There was a problem writing to the file")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
    else:
        logger.info("The transcription of the file is as follows:\n", transcribed_text)
    

if __name__ == "__main__":
    main()