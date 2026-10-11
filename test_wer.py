import string
import time
from jiwer import wer
from stt import transcribe


def clean(text):
    text = text.lower()
    text = text.replace("'", "")
    for ch in string.punctuation:
        text = text.replace(ch, " ")
    return " ".join(text.split())


scores = []
start=time.time()
for n in range(1, 6):
    audio_path = f"Test/test{n}.wav"
    answer_path = f"Test/text{n}.txt"

    model_text = transcribe(audio_path)

    with open(answer_path, "r", encoding="utf-8") as f:
        answer = f.read()

    score = wer(clean(answer), clean(model_text))
    scores.append(score)

    print(f"--- Sentence {n} ---")
    print("answer :", clean(answer))
    print("model  :", clean(model_text))
    print(f"WER    : {score:.2f}")

print(f"Average WER: {sum(scores) / len(scores):.2f}")
print(time.time()-start)