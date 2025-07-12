

#========================code 1=========================
# "mencari data transaksi penjualan berdasarkan harga produk"
# #mengunakan metode searching
# def linear_search(nama_produk, harga_produk, search_produk):
#     """Mencari harga produk berdasarkan nama produk"""
#     for i in range(len(nama_produk)):
#         if nama_produk[i] == search_produk:
#             return harga_produk[i]
        
#     return None  # jika tidak ditemukan

#  #contoh hasil pengurutan/pengunaan
# produk_list =["buku"]
# harga_list =[5000,2000,3500,4000,50.000]

# search_produk ="pensil"
# result= linear_search(produk_list,harga_list,search_produk="pensil")
# if result is None:
#     print(f"produk {search_produk}tidak ditemukan")
# else:
#     print(f"harga produk{search_produk}:{result}")

#=====================CODE 2========================
# Mencari harga produk berdasarkan nama produk
# Menggunakan metode searching (linear search)

def linear_search(nama_produk, harga_produk, search_produk):
    """Mencari harga produk berdasarkan nama produk"""
    for i in range(len(nama_produk)):
        if nama_produk[i] == search_produk:
            return harga_produk[i]#apa bila kondisinya true/ ditemukan
    return None  # jika tidak ditemukan/false

# Data transaksi (nama produk dan harga)
produk_list = ["buku", "pensil", "pulpen", "tas","kertas","bakso","cocacola"]
harga_list = [ 2000, 3500, 4000,65.000,10000,50.000,6000]

# Contoh penggunaan searching
daftar_cari =["pensil","buku","pulpen","tas","kertas","bakso","cocacola"]
# search_produk = "kertas"   #tanpa koma
for search_produk in daftar_cari:
   result = linear_search(produk_list, harga_list, search_produk)
   if result is None:
                print(f"produk {search_produk} tidak ditemukan")
   else:
                print(f"harga produk {search_produk}: {result}")