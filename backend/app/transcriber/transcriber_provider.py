from app.transcriber.whisper import WhisperTranscriber
print('实例化transcriber')
# TODO:后面需要加入逻辑选择
_transcriber = None

def get_transcriber(model_size="base", device="cuda"):
    global _transcriber
    if _transcriber is None:
        print('加载_transcriber')
        _transcriber = WhisperTranscriber(model_size=model_size, device=device)
    return _transcriber