from faster_whisper import WhisperModel


def transcribe_audio(file_path: str, model_size: str = "tiny") -> str:
    """
    Transcribe audio using the FasterWhisper package.

    Args:
        file_path(string): the path of the audio/video file.

        model_size(string): Size of the model to use (tiny, tiny.en, base, base.en,
            small, small.en, distil-small.en, medium, medium.en, distil-medium.en, large-v1,
            large-v2, large-v3, large, distil-large-v2 or distil-large-v3)
        
    Return:
        string: The transciption of the file 
    """

    model = WhisperModel(model_size, device="cpu", compute_type="int8")

    transcription, _ = model.transcribe(file_path, beam_size=5)
    
    return transcription
