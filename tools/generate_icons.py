import struct, zlib, os

def create_icon(size, path):
    raw = b''
    for y in range(size):
        raw += b'\x00'
        for x in range(size):
            cx = x - size / 2
            cy = y - size / 2
            dist = (cx * cx + cy * cy) ** 0.5
            radius = size * 0.42
            if dist < radius:
                r = 255
                g = max(0, min(255, int(154 - (dist / radius) * 100)))
                b = 0
                a = 255
            else:
                r, g, b, a = 0, 0, 0, 0
            raw += struct.pack('BBBB', r, g, b, a)

    def chunk(ctype, data):
        c = ctype + data
        crc = struct.pack('>I', zlib.crc32(c) & 0xFFFFFFFF)
        return struct.pack('>I', len(data)) + c + crc

    with open(path, 'wb') as f:
        f.write(b'\x89PNG\r\n\x1a\n')
        f.write(chunk(b'IHDR', struct.pack('>IIBBBBB', size, size, 8, 6, 0, 0, 0)))
        f.write(chunk(b'IDAT', zlib.compress(raw)))
        f.write(chunk(b'IEND', b''))

icons_dir = os.path.join(os.path.dirname(__file__), '..', 'extension', 'icons')
os.makedirs(icons_dir, exist_ok=True)

for s in [16, 48, 128]:
    p = os.path.join(icons_dir, f'icon{s}.png')
    create_icon(s, p)
    print(f'Created {p}')
