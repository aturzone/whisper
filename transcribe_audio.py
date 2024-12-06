import whisper

# مسیر فایل صوتی
audio_path = "/home/aturzone/Desktop/audio_converted.wav"  # فایل صوتی که می‌خواهید تبدیل کنید
output_txt_path = "/home/aturzone/Desktop/transcription.txt"  # نام فایل متنی خروجی

# بارگذاری مدل Whisper
print("Loading Whisper model...")
model = whisper.load_model("base")

# تبدیل صوت به متن (با تنظیم زبان فارسی)
print("Transcribing audio (language: Persian)...")
result = model.transcribe(audio_path, language="fa")  # تنظیم زبان به فارسی

# ذخیره متن در فایل
print("Saving transcription to file...")
with open(output_txt_path, "w", encoding="utf-8") as f:
    f.write(result["text"])

print(f"Transcription saved to {output_txt_path}")
