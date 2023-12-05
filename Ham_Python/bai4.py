
import bai3
import bai2

def kiem_tra_so(n):
    result = []
    
    if bai2.kiem_tra_so_nguyen_to(n):
        result.append("Số nguyên tố")
    
    if bai3.kiem_tra_so_fibonacci(n):
        result.append("Số Fibonacci")
    
    if sum([i for i in range(1, n) if n % i == 0]) == n:
        result.append("Số hoàn hảo")
    
    return result if result else "Không thuộc loại nào"


print(kiem_tra_so(5))