# Experiment Report: Data Quality Impact on AI Agent

**Student ID:** AI20K-2A202600374  
**Name:** Lại Đức Anh  
**Date:** 15/04/2026
**Email:** laiducanh26112004@gmail.com

---

## 1. Ket qua thi nghiem

Chay `agent_simulation.py` voi 2 bo du lieu va ghi lai ket qua:

| Scenario | Agent Response | Accuracy (1-10) | Notes |
|----------|----------------|-----------------|-------|
| Clean Data (`processed_data.csv`) | Agent: Based on my data, the best choice is Laptop at $1200. | 9 | Du lieu da duoc lam sach, chi giu cac san pham hop le nen Agent dua ra lua chon hop ly |
| Garbage Data (`garbage_data.csv`) | Agent: Based on my data, the best choice is Nuclear Reactor at $999999. | 2 | Du lieu chua nhieu loi va gia tri bat thuong dan den viec Agent dua ra lua chon phi thuc te |

---

## 2. Phan tich & nhan xet

### Tai sao Agent tra loi sai khi dung Garbage Data?

Khi su dung Garbage Data, Agent bi anh huong nghiem trong boi cac van de chat luong du lieu. Cu the, du lieu co the chua cac gia tri khong hop ly nhu gia tri qua lon (outliers) nhu "Nuclear Reactor" voi muc gia 999999, lam sai lech hoan toan qua trinh danh gia va lua chon san pham. Ngoai ra, cac loi nhu gia tri am, category bi thieu hoac khong dong nhat cung lam Agent hieu sai ve tap du lieu. Khi khong co buoc lam sach du lieu, Agent se dua tren nhung thong tin sai lech nay de dua ra quyet dinh, dan den cac ket qua phi thuc te va khong dang tin cay.

---

## 3. Ket luan

**Quality Data > Quality Prompt?** Dong y.  

Ket qua thi nghiem cho thay ro rang rang chat luong du lieu anh huong truc tiep den do chinh xac cua Agent. Khi du lieu sach, Agent co the dua ra lua chon hop ly (Laptop). Nguoc lai, khi du lieu bi loi, Agent co the dua ra ket qua vo ly (Nuclear Reactor). Dieu nay chung minh rang du lieu chat luong cao quan trong hon viec toi uu prompt.