import concurrent.futures
import os
import time
import math

data_angka = list(range(1, 41))

def proses_chunk(chunk, chunk_id):
    """
    SImulasi pemrosesan CHUNK data.
    chunk      : list bilangan yang diproses
    chunk_id   : nomor identitas chunk
    """
    pid = os.getpid()
    print(f"[Chunk {chunk_id}] Proses PID {pid} mulai memproses data: {chunk}")
    hasil = []
    for num in chunk:
        time.sleep(0.05)
        hasil.append(math.factorial(num) if num <= 10 else num**2)
    print(f"[Chunk {chunk_id}] Proses PID {pid} selesai. Hasil: {hasil}")
    return hasil

def main():
    jumlah_pekerja = os.cpu_count() or 4
    print(f"Jumlah core CPU: {jumlah_pekerja}")
    print(f"Total data: {data_angka}")

    ukuran_chunk = math.ceil(len(data_angka) / jumlah_pekerja)
    chunks = []
    for i in range(0, len(data_angka), ukuran_chunk):
        chunks.append((data_angka[i:i+ukuran_chunk], len(chunks)+1))

    print(f"\nData dibagi menjadi {len(chunks)} chunk untuk diproses paralel:\n")
    for ch, cid in chunks:
        print(f"Chunk {cid}: {ch}")

    print("\nEksekusi Paralel Dimulai")
    start = time.time()

    with concurrent.futures.ProcessPoolExecutor(max_workers=jumlah_pekerja) as executor:
        futures = [executor.submit(proses_chunk, ch, cid) for ch, cid in chunks]

        for future in concurrent.futures.as_completed(futures):            
            _ = future.result()

    elapsed = time.time() - start
    print(f"Semua chunk selesai diproses dalam {elapsed:.2f} detik")

if __name__ == "__main__":
    main()