from .mbd import convert_to_mbd
from .api import upload

def print_rgb(img, host, zoom: float ):
  """_summary_
    Chuyển dữ liệu mảng 3 chiều [Cao x Rộng x 3] ra máy in mBrush
  Args:
      img (_type_): Mảng dữ liệu màu của từng pixel [Cao x Rộng x 3] cần in
      host (str, optional): Địa chỉ IP của máy in mBrush_.  Mặc định là '192.168.88.1'.
      zoom (float, optional): Tỉ lệ zoom ảnh để vừa khít với độ cao tối đa 1.44 cm. Giá trị phải <=1. Mặc định = 1.
  """
  data = convert_to_mbd(img, None, zoom)
  # Upload nội dung trọn vẹn của 1 file mdb lên máy mBrush
  upload(data, '0.mbd' ,host)
