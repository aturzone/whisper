import whisper

# دریافت مسیر فایل صوتی از کاربر
audio_path = input("لطفاً مسیر فایل صوتی را وارد کنید: ")  # دریافت آدرس فایل صوتی از کاربر

# دریافت مسیر فایل متنی خروجی از کاربر
output_txt_path = input("لطفاً مسیر فایل متنی خروجی را وارد کنید: ")  # دریافت آدرس فایل متنی خروجی از کاربر

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
