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

class HuffmanApp(Gtk.Window):
    def __init__(self):
        super().__init__(title="PyGTK Huffman App")
        
        self.set_border_width(10)
        self.set_default_size(300, 200)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)

        self.uncompressed_entry = Gtk.Entry()
        vbox.pack_start(self.uncompressed_entry, False, False, 0)

        button_box = Gtk.Box(spacing=10)
        vbox.pack_start(button_box, True, True, 0)
        
        compressButton = Gtk.Button(label="Compress")
        compressButton.connect("clicked", self.on_compress_button_clicked)

        decompressButton = Gtk.Button(label="Decompress")
        decompressButton.connect("clicked", self.on_decompress_button_clicked)

        button_box.pack_start(compressButton, True, True, 0)
        button_box.pack_start(decompressButton, True, True, 0)

        self.compressed_entry = Gtk.Entry()
        vbox.pack_start(self.compressed_entry, False, False, 0)
        
    def on_compress_button_clicked(self, widget):

        uncompressed_input = self.uncompressed_entry.get_text()

        if uncompressed_input:
            logging.info("Compressing %s", uncompressed_input)
            self.compressed_entry.set_text(compress(uncompressed_input))

    def on_decompress_button_clicked(self, widget):

        compressed_input = self.compressed_entry.get_text()

        if compressed_input:
            logging.info("Decompressing %s", compressed_input)
            self.uncompressed_entry.set_text(decompress(compressed_input))

if __name__ == "__main__":
    app = HuffmanApp()
    app.connect("destroy", Gtk.main_quit)
    app.show_all()
    Gtk.main()
