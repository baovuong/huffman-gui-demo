import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import logging
from huffman import *

# Configure logging
logging.basicConfig(
    filename="app.log",  # Log to a file named 'app.log'
    level=logging.INFO,  # Set the logging level to INFO
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class HuffmanApp(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Tkinter Huffman App")
        self.geometry("400x300")
        
        # Uncompressed Text Section
        tk.Label(self, text="Uncompressed Text").pack(pady=5)
        self.uncompressed_entry = ScrolledText(self, wrap=tk.WORD, height=5)
        self.uncompressed_entry.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        self.uncompressed_entry.bind("<<Modified>>", self.on_uncompressed_entry_changed)

        self.uncompressed_bit_display = tk.Label(self, text="Uncompressed Bits", wraplength=300, justify='center')
        self.uncompressed_bit_display.pack(pady=5)
 
        # Buttons Section
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        compress_button = ttk.Button(button_frame, text="Compress", command=self.on_compress_button_clicked)
        compress_button.pack(side=tk.LEFT, padx=5)

        decompress_button = ttk.Button(button_frame, text="Decompress", command=self.on_decompress_button_clicked)
        decompress_button.pack(side=tk.LEFT, padx=5)

        # Compressed Text Section
        tk.Label(self, text="Compressed Text").pack(pady=5)
        self.compressed_entry = ScrolledText(self, wrap=tk.WORD, height=5)
        self.compressed_entry.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    def on_compress_button_clicked(self):
        uncompressed_input = self.uncompressed_entry.get("1.0", tk.END).strip()
        if uncompressed_input:
            logging.info('Compressing %s', uncompressed_input)
            compressed_text = compress(uncompressed_input)
            self.compressed_entry.delete("1.0", tk.END)
            self.compressed_entry.insert(tk.END, compressed_text)

    def on_decompress_button_clicked(self):
        compressed_input = self.compressed_entry.get("1.0", tk.END).strip()
        if compressed_input:
            logging.info('Decompressing %s', compressed_input)
            decompressed_text = decompress(compressed_input)
            self.uncompressed_entry.delete("1.0", tk.END)
            self.uncompressed_entry.insert(tk.END, decompressed_text)

    def on_uncompressed_entry_changed(self, event):
        self.uncompressed_entry.edit_modified(False)  # Reset the modified flag
        uncompressed_text = self.uncompressed_entry.get("1.0", tk.END).strip()
        self.uncompressed_bit_display.config(text=to_bin(uncompressed_text))

if __name__ == '__main__':
    app = HuffmanApp()
    app.mainloop()