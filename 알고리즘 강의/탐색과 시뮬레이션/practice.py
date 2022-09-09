# # ### 1번 문제
# def getMaximumMex(arr, x):
#     # Write your code here
#     for i in arr:
#         arr.append(i+x)
    
#     arr.sort()
#     arr = list(set(arr))
#     missing = 1

#     for j in arr:
#         if j == missing:
#             missing += 1
#     return missing


# print(getMaximumMex([0,1,2,2,0,0,10], 3))
### 나와야 하는 아웃풋 7

### 2번문제
# def filter_vowels(self):
#         # Enter your code here
#         # Return a string
#         vowels = ['a', 'e', 'i', 'o', 'u']
#         letter = list(s)
#         for idx, x in enumerate(letter):
#             if x in vowels:
#                 letter.pop(idx)
#         result = ''.join(letter)
#         return result
                
#     def filter_consonants(self):
#         # Enter your code here
#         # Return a string
#         vowels = ['a', 'e', 'i', 'o', 'u']
#         letter = list(s)
#         for idx, x in enumerate(letter):
#             if x not in vowels:
#                 letter.pop(idx)
#         result = ''.join(letter)
#         return result

# print(filter_consonants('hackerrank'))


# 3번문제
# API 요청 문제...
# def getVoteCount(cityName, estimatedCost):
#     # Write your code here
#     response = requests.get("https://jsonmock.hackerrank.com/api/food_outlets?city=<cityName>&estimated_cost=<estimatedCost>")
#     result = response.json()



# 2번문제 최종
# def filter_consonants(s):
#         # Enter your code here
#         # Return a string
#         vowels = ['a', 'e', 'i', 'o', 'u']
#         result2 = []
#         letter = list(s)
#         for idx, x in enumerate(letter):
#             if x in vowels:
#                 letter.pop(idx)
#                 result2.append(x)
#         result = ''.join(letter)
#         result2 = ''.join(result2)
#         return result2

# print(filter_consonants('hackerrank'))

# 인풋
# uoiauuuuoxehlvalaodoyxeieuauueoiwiadxerusiqbaliwthxibmruokpniouuognahiguuzefuayksffcsuvqpkefiawhieihdtyulwiuzhrxuuipeesexiurixvmpaeapfzaobosiddhkwjriiosuuuquzkuoeiirwuooiuaoeoysgoqgygmuvwivabuileoabdcpjgyoenjitcefyvfzieietjithuxzrtkbajelaulneglhaxeuiiusiaukbveplxyaxieaauiydcmpiaomiioiiaeeznfphiauzoohewjhejepunijeavsoonekqzgtuqqaduruyjwegxaidikkoiuowdeyhikujgsujiafukzfulqihkeherazzbivixtamhnureieoohtdjyaotaawfaxkilaasubievuieudwtlicwcduuwyqxueukorlxluaakdbueoneackotoenaoakauwoeppeuahrixxagoiaswyzdhyhpdjvyavooytzdoiokuwatayxifpfqiuzhisgfaeapcraifebahtiufubxcgpafobuyahtrojukebeidilejpaueicfuigiuovogefeiemhuioriouiiriuqeefjiaihalpuuuumouazysberdoevsehepwreeugneqqoigfxoebumrccayuiajoyiisoodnkbioalkheijhioflaxdideqyufeaihyridbralnzifibhucguiievhivovuwbwmhwumjdxcgiuodiaeoonujeiiupurosqebeizuxlcakixabjowaftsairoemariseiaoypsjdyoouwuwnatmcacyuiboufzrxqjovpeiibaakixhoyzeexesugiyanoiipfdpciquiiaialhihoarimteajdaaiauneeaaeuaslkrruujquekueutlwvaeiifaxlauefibuxkifuquwaupbiduwhedgweauupuibosnfihsdunx

# 기대한 아웃풋
# xhlvldyxwdxrsqblwthxbmrkpngnhgzfyksffcsvqpkfwhhdtylwzhrxpsxrxvmppfzbsddhkwjrsqzkrwysgqgygmvwvblbdcpjgynjtcfyvfztjthxzrtkbjllnglhxskbvplxyxydcmpmznfphzhwjhjpnjvsnkqzgtqqdryjwgxdkkwdyhkjgsjfkzflqhkhrzzbvxtmhnrhtdjytwfxklsbvdwtlcwcdwyqxkrlxlkdbncktnkwpphrxxgswyzdhyhpdjvyvytzdkwtyxfpfqzhsgfpcrfbhtfbxcgpfbyhtrjkbdljpcfgvgfmhrrqfjhlpmzysbrdvshpwrgnqqgfxbmrccyjysdnkblkhjhflxddqyfhyrdbrlnzfbhcgvhvvwbwmhwmjdxcgdnjprsqbzxlckxbjwftsrmrsypsjdywwntmccybfzrxqjvpbkxhyzxsgynpfdpcqlhhrmtjdnslkrrjqktlwvfxlfbxkfqwpbdwhdgwpbsnfhsdnx
# uoiauuuuoeaaooeieuauueoiiaeuiaiiuoiouuoaiuueuaueiaieiuiuuuieeeiuiaeaaooiiiouuuuuoeiiuooiuaoeoouiauieoaoeieieieiuaeaueaeuiiuiaueaieaauiiaoiioiiaeeiauooeeeuieaooeuauueaiioiuoeiuuiauuieeaiiaueieooaoaaaiaauieuieuiuuueuouaaueoeaooeaoaauoeeuaiaoiaaoooiouaaiiuiaeaaieaiuuaouaoueeiieaueiuiiuooeeieuioiouiiiueeiaiauuuuouaeoeeeeeueoioeuauiaoiiooioaeiioaieueaiiaiiuuiieiouuiuoiaeooueiiuuoeeiuaiaoaaioeaieiaooouuaauiouoeiiaaioeeeuiaoiiiuiiaiaioaieaaaiaueeaaeuauuueueuaeiiaaueiuiuuauiueeauuuioiu



# def filter_consonants(self):
#         # Enter your code here
#         # Return a string
#         vowels = ['a', 'e', 'i', 'o', 'u']
#         result2 = []
#         letter = list(s)
#         for idx, x in enumerate(letter):
#             if x in vowels:
#                 result2.append(x)
#         result2 = ''.join(result2)
#         return result2

# print(filter_vowels('hackerrank'))


# 2번 다맞힘11


# 1번 문제 다시해보기
