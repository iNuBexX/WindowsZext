import zstandard as zstd

def decompress_zst(input_path, output_path):
    with open(input_path, "rb") as compressed:
        dctx = zstd.ZstdDecompressor()
        with open(output_path, "wb") as decompressed:
            dctx.copy_stream(compressed, decompressed)

if __name__ == "__main__":
    decompress_zst("file.zst", "file.dem")