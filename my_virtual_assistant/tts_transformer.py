from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
from datasets import load_dataset
import torch
import soundfile as sf

import time

device = "cuda" if torch.cuda.is_available() else "cpu"

# load the processor
processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
# load the model
model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts").to(device)
# load the vocoder, that is the voice encoder
vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan").to(device)
# we load this dataset to get the speaker embeddings
embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")

# speaker ids from the embeddings dataset
speakers = {
    'awb': 0,     # Scottish male
    'bdl': 1138,  # US male
    'clb': 2271,  # US female
    'jmk': 3403,  # Canadian male
    'ksp': 4535,  # Indian male
    'rms': 5667,  # US male
    'slt': 6799   # US female
}

def save_text_to_speech(text, speaker=None):
    # preprocess text
    inputs = processor(text=text, return_tensors="pt").to(device)
    if speaker is not None:
        # load xvector containing speaker's voice characteristics from a dataset
        speaker_embeddings = torch.tensor(embeddings_dataset[speaker]["xvector"]).unsqueeze(0).to(device)
    else:
        # random vector, meaning a random voice
        speaker_embeddings = torch.randn((1, 512)).to(device)
    # generate speech with the models
    speech = model.generate_speech(inputs["input_ids"], speaker_embeddings, vocoder=vocoder)
    
    output_filename = f"output-{time.time()}.wav"
    
    # save the generated speech to a file with 16KHz sampling rate
    sf.write(output_filename, speech.cpu().numpy(), samplerate=16000)
    # return the filename for reference
    return output_filename