import os
# if file exists read and print
if os.path.exists('model_output.txt'):
    try:
        text = open('model_output.txt', encoding='utf-16le').read()
        with open('model_output_utf8.txt', 'w', encoding='utf-8') as f:
            f.write(text)
    except Exception as e:
        print("Error formatting:", e)
