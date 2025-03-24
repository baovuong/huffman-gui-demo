import gi
import logging

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from huffman import * 

# Configure logging
logging.basicConfig(
    filename="app.log",  # Log to a file named 'app.log'
    level=logging.INFO,  # Set the logging level to INFO
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_text_from_textbuffer(textbuffer):
    start, end = textbuffer.get_bounds()
    return textbuffer.get_text(start, end, True)

def set_text_to_textview(textview, text):
    buffer = textview.get_buffer()
    buffer.set_text(text)

class HuffmanApp(Gtk.Window):
    def __init__(self):
        super().__init__(title='PyGTK Huffman App')
        
        self.set_border_width(10)
        self.set_default_size(300, 200)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)

        self.uncompressed_entry = Gtk.TextView()
        self.uncompressed_entry.set_wrap_mode(Gtk.WrapMode.WORD)  # Optional: Wrap text at word boundaries
        self.uncompressed_entry.get_buffer().connect('changed', self.on_uncompressed_entry_changed)
        vbox.pack_start(self.uncompressed_entry, True, True, 0)

        self.uncompressed_bit_display = Gtk.Label(label='Uncompressed Text')
        vbox.pack_start(self.uncompressed_bit_display, False, False, 0)

        button_box = Gtk.Box(spacing=10)
        vbox.pack_start(button_box, True, True, 0)
        
        compressButton = Gtk.Button(label='Compress')
        compressButton.connect('clicked', self.on_compress_button_clicked)

        decompressButton = Gtk.Button(label='Decompress')
        decompressButton.connect('clicked', self.on_decompress_button_clicked)

        button_box.pack_start(compressButton, True, True, 50)
        button_box.pack_start(decompressButton, True, True, 50)

        self.compressed_entry = Gtk.TextView()
        self.compressed_entry.set_wrap_mode(Gtk.WrapMode.WORD)  # Optional: Wrap text at word boundaries
        vbox.pack_start(self.compressed_entry, True, True, 0)
        
    def on_compress_button_clicked(self, widget):

        uncompressed_input = get_text_from_textbuffer(self.uncompressed_entry)

        if uncompressed_input:
            logging.info('Compressing %s', uncompressed_input)
            set_text_to_textview(self.compressed_entry, compress(uncompressed_input))

    def on_decompress_button_clicked(self, widget):

        compressed_input = get_text_from_textbuffer(self.compressed_entry)

        if compressed_input:
            logging.info('Decompressing %s', compressed_input)
            set_text_to_textview(self.uncompressed_entry, decompress(compressed_input))

    def on_uncompressed_entry_changed(self, widget):
        self.uncompressed_bit_display.set_text(to_bin(get_text_from_textbuffer(widget)))

if __name__ == '__main__':
    app = HuffmanApp()
    app.connect("destroy", Gtk.main_quit)
    app.show_all()
    Gtk.main()
