import zstandard as zstd
import argparse

def decompress_zst(input_path, output_path):
    with open(input_path, "rb") as compressed:
        dctx = zstd.ZstdDecompressor()
        with open(output_path, "wb") as decompressed:
            dctx.copy_stream(compressed, decompressed)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Decompress a .zst file.")
    parser.add_argument("input_file", help="Path to the .zst file to decompress")
    parser.add_argument("output_file", help="Path to save the decompressed file")
    args = parser.parse_args()

    decompress_zst(args.input_file, args.output_file)
