# # Ek warehouse scanner packages ke IDs is order mein record karta hai:
# Scanner team ko pehla aisa package ID chahiye jo poori list mein sirf ek baar aaya ho.
# Is example mein answer 56 hai, kyunki 56 sirf ek baar aaya hai aur 90 bhi ek baar aane ke bawajood uske baad aata hai.
# ids = [41, 23, 41, 17, 23, 56, 17, 90]


#first appraoch
def first_unique_id(ids):
    n = len(ids)
    for i in range(n):
        count = 0
        for j in range(n):
            if ids[i] == ids[j]:
                count += 1             
        if count == 1:
            return ids[i]
ids = [41, 23, 41, 17, 23, 56, 17, 90]

print(first_unique_id(ids))
# def first_unique_id(ids):
#     pass